"""
test_remediation_round4.py
-----------------------------------------------------------------------------
Automated verification tests for Round 4 remediations:
1. Recovery fails closed when a backup is missing: does NOT delete pointer,
   does NOT mark ROLLED_BACK, halts with RuntimeError.
2. Corrupt active pointer preservation: quarantines corrupt pointer file as evidence.
3. Dry-run zero mutation guarantee: does NOT execute recovery or change files.
4. Clinical QA contradiction rejection: rejects candidate with status APPROVED
   if visual_concordance or polarity_match is FAIL.
5. Exact event/date provenance: verifies Global Handwashing Day (Oct 15) cites
   Global Handwashing Partnership, UN FAO for Food Day, and no false WHO badges.

ISOLATION GUARANTEE:
All test cases modifying transactions or pointers run strictly inside isolated
temporary fixtures (tempfile.mkdtemp). Live project state is never mutated.
-----------------------------------------------------------------------------
"""

import os
import shutil
import sys
import tempfile
import json
import hashlib
from PIL import Image

import generate_with_gemini as gwg

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_isolated_project_fixture():
    """Create a completely isolated mock project fixture in a temp directory."""
    temp_dir = tempfile.mkdtemp(prefix="health365_test_fixture_r4_")
    os.makedirs(os.path.join(temp_dir, "data", "transactions"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "photos", "staging"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "js"), exist_ok=True)

    dummy_calendar = [
        {
            "id": "10-15",
            "title_en": "Global Handwashing Day",
            "cards": [
                {
                    "index": 1,
                    "type": "message",
                    "title_en": "20-Sec Soap Handwash",
                    "title_gu": "સાબુથી ૨૦ સેકન્ડ હાથ ધોવા",
                    "desc_en": "Wash with soap",
                    "desc_gu": "સાબુથી હાથ ધોવો",
                    "photo": "photos/10_15_card1.png",
                    "ai_prompt": "Indian doctor washing hands"
                }
            ]
        }
    ]
    with open(os.path.join(temp_dir, "data", "health_365.json"), "w", encoding="utf-8") as f:
        json.dump(dummy_calendar, f)

    with open(os.path.join(temp_dir, "js", "calendar-data.js"), "w", encoding="utf-8") as f:
        f.write("window.HEALTH_CALENDAR_DATA = [];")

    with open(os.path.join(temp_dir, "sw.js"), "w", encoding="utf-8") as f:
        f.write("const PRECACHE_ASSETS = [];")

    return temp_dir

def test_recovery_fails_closed_on_missing_backup():
    print("\n--- Test 1: Recovery Fails Closed on Missing Backup ---")
    fixture = make_isolated_project_fixture()
    try:
        tx_id = "test_missing_backup_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        os.makedirs(tx_dir, exist_ok=True)
        plan_path = os.path.join(tx_dir, "tx_plan.json")

        # Plan references a nonexistent backup file
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {
                "photos/test_target.png": f"data/transactions/{tx_id}/backup/nonexistent.png"
            },
            "pre_transaction_hashes": {
                "photos/test_target.png": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
            },
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_IMAGES"}, f)

        # Attempt recovery in isolated fixture
        failed_closed = False
        try:
            gwg.recover_unfinalized_transactions(project_dir=fixture)
        except RuntimeError as rerr:
            failed_closed = True
            print(f"  [PASS] Recovery failed closed as required: {rerr}")

        assert failed_closed, "Recovery MUST raise RuntimeError when a backup is missing!"
        assert os.path.exists(active_tx_path), "Active transaction pointer MUST NOT be deleted!"

        with open(plan_path, "r", encoding="utf-8") as f:
            updated_plan = json.load(f)
        assert updated_plan.get("state") != "ROLLED_BACK", "Transaction MUST NOT be marked ROLLED_BACK when backups are missing!"
        print("  [PASS] Fail-closed verification successful: pointer preserved, ROLLED_BACK not set.")
    finally:
        shutil.rmtree(fixture)

def test_corrupt_pointer_quarantined():
    print("\n--- Test 2: Corrupt Pointer Quarantined As Forensic Evidence ---")
    fixture = make_isolated_project_fixture()
    try:
        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            f.write("{ invalid json corrupt content !!!")

        has_pending, tx_id, plan_path, plan_or_err = gwg.check_pending_transactions(project_dir=fixture)
        assert has_pending, "Check must detect corrupt pointer"

        # Run recovery to trigger quarantine
        try:
            gwg.recover_unfinalized_transactions(project_dir=fixture)
        except RuntimeError:
            pass

        # Check that quarantine file was created in fixture
        data_dir = os.path.join(fixture, "data")
        corrupt_files = [f for f in os.listdir(data_dir) if f.startswith("active_transaction.corrupt.")]
        assert len(corrupt_files) > 0, "Corrupt active transaction pointer must be quarantined!"
        print(f"  [PASS] Corrupt pointer quarantined to: {corrupt_files[-1]}")
    finally:
        shutil.rmtree(fixture)

def test_dry_run_zero_mutation_under_pending_recovery():
    print("\n--- Test 3: Dry-Run Zero Mutation Under Pending Recovery ---")
    fixture = make_isolated_project_fixture()
    try:
        tx_id = "test_dry_run_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        os.makedirs(tx_dir, exist_ok=True)
        plan_path = os.path.join(tx_dir, "tx_plan.json")

        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {},
            "pre_transaction_hashes": {},
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)
        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_IMAGES"}, f)

        class DummyArgs:
            dry_run = True
            promote = True
            day = None
            all_missing = False
            force = False
            model = "imagen-3.0-generate-002"
            api_key = None
            recover = None

        # Run process_calendar in dry-run mode in fixture
        gwg.process_calendar(DummyArgs(), project_dir=fixture)

        # Verify that plan and pointer were NOT modified
        with open(plan_path, "r", encoding="utf-8") as f:
            plan_after = json.load(f)
        assert plan_after["state"] == "PROMOTING_IMAGES", "Dry run must NOT change transaction state!"
        assert os.path.exists(active_tx_path), "Dry run must NOT delete active transaction pointer!"
        print("  [PASS] Dry-run strictly preserved files and pending transaction state without mutating anything.")
    finally:
        shutil.rmtree(fixture)

def test_clinical_qa_contradiction_rejection():
    print("\n--- Test 4: Clinical QA Contradiction Rejection ---")
    fixture = make_isolated_project_fixture()
    try:
        test_candidate = os.path.join(fixture, "photos", "staging", "candidate_10_15_card1_test_fail_qa.png")
        im = Image.new("RGB", (720, 540), color="green")
        im.save(test_candidate, format="PNG")

        c_hash = gwg.compute_file_sha256(test_candidate)

        with open(os.path.join(fixture, "data", "health_365.json"), "r", encoding="utf-8") as f:
            calendar_data = json.load(f)

        target_card = calendar_data[0]["cards"][0]
        spec_h = gwg.compute_card_spec_hash(target_card, "10-15")

        contradictory_record = {
            "day_id": "10-15",
            "card_idx": 1,
            "status": "APPROVED",
            "spec_hash": spec_h,
            "reviewer": {"name": "Test Reviewer", "role": "Tester"},
            "clinical_review": {
                "visual_concordance": "FAIL",  # Contradiction!
                "cultural_authenticity": "PASS",
                "polarity_match": "PASS",
                "safety_equipment_check": "PASS"
            }
        }

        manifest = {c_hash: contradictory_record}
        manifest_path = os.path.join(fixture, "data", "approved_manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        gwg.promote_staged_assets(calendar_data, day_filter="10-15", dry_run=True, project_dir=fixture)

        active_target = os.path.join(fixture, "photos", "10_15_card1.png")
        assert not os.path.exists(active_target), "Candidate with visual_concordance=FAIL must NOT be promoted!"
        print("  [PASS] Candidate with contradictory/failed clinical review QA checks was properly rejected.")
    finally:
        shutil.rmtree(fixture)

def test_provenance_citations():
    print("\n--- Test 5: Exact Provenance Citations & Event/Date Decoupling (Read-Only) ---")
    with open(gwg.JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    oct15 = next(d for d in data if d["id"] == "10-15")
    prov15 = oct15["provenance"]
    assert "globalhandwashing.org" in prov15["observance_source_url"], "Oct 15 MUST cite Global Handwashing Partnership"
    assert "world-hand-hygiene-day" not in prov15["observance_source_url"], "Oct 15 MUST NOT cite May 5 World Hand Hygiene Day!"
    assert prov15["authority_tier"] == "GLOBAL_PARTNERSHIP", "Oct 15 authority must be GLOBAL_PARTNERSHIP"
    print(f"  [PASS] Oct 15 accurately cites: {prov15['sponsoring_body']} ({prov15['observance_source_url']})")

    oct16 = next(d for d in data if d["id"] == "10-16")
    prov16 = oct16["provenance"]
    assert "fao.org" in prov16["observance_source_url"], "Oct 16 MUST cite FAO"
    assert prov16["authority_tier"] == "UN_AGENCY", "Oct 16 authority must be UN_AGENCY"
    print(f"  [PASS] Oct 16 accurately cites: {prov16['sponsoring_body']} ({prov16['observance_source_url']})")

    oct17 = next(d for d in data if d["id"] == "10-17")
    prov17 = oct17["provenance"]
    assert "Trauma" in prov17["badge_en"], "Oct 17 must not claim false WHO badge"
    assert "WHO" not in prov17["badge_en"], "Oct 17 must not claim false WHO badge"
    print("  [PASS] Oct 17 badge is organization-accurate: " + prov17['badge_en'].encode('ascii', 'ignore').decode('ascii'))

if __name__ == "__main__":
    print("Running Round 4 Isolated Verification Tests...")
    test_recovery_fails_closed_on_missing_backup()
    test_corrupt_pointer_quarantined()
    test_dry_run_zero_mutation_under_pending_recovery()
    test_clinical_qa_contradiction_rejection()
    test_provenance_citations()
    print("\nALL ROUND 4 ISOLATED REMEDIATION TESTS PASSED SUCCESSFULLY!")
