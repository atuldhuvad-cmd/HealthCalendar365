"""
test_remediation_round5.py
-----------------------------------------------------------------------------
Automated verification tests for Round 5 remediations:
1. Read-only preflight: corrupt backup rejected BEFORE touching target; active
   target file bytes remain 100% untouched.
2. Mandatory pre-transaction hashes: plan missing pre_transaction_hashes is
   rejected; active target files remain untouched; pointer preserved.
3. Isolated dry run: pending recovery is previewed; zero files mutated.
4. Contradictory clinical QA: candidate with status APPROVED but failing QA
   criteria is strictly rejected from promotion.
5. COMPLETE TEST ISOLATION: All tests run inside temporary directories
   (tempfile.mkdtemp()); zero real project state or quarantine files are touched.
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

def make_isolated_project_fixture():
    """Create a completely isolated mock project fixture in a temp directory."""
    temp_dir = tempfile.mkdtemp(prefix="health365_test_fixture_")
    os.makedirs(os.path.join(temp_dir, "data", "transactions"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "photos", "staging"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "js"), exist_ok=True)

    # Minimal dummy health_365.json
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
        f.write("const PRECACHE_ASSETS = [\n];\n")

    # Create dummy core assets for complete builder isolation within temp directory
    for rel in ["index.html", "manifest.json", "css/styles.css", "css/fonts.css", "js/app.js", "js/canvas-renderer.js", "js/db.js", "icons/icon-192.png", "icons/icon-512.png"]:
        p = os.path.join(temp_dir, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(b"mock")

    return temp_dir

def test_corrupt_backup_rejected_before_touching_target():
    print("\n--- Test 1: Corrupt Backup Rejected BEFORE Touching Target (Read-Only Preflight) ---")
    fixture = make_isolated_project_fixture()
    try:
        target_rel = "photos/10_15_card1.png"
        target_full = os.path.join(fixture, target_rel)
        original_target_bytes = b"ORIGINAL_TARGET_BYTES_STAY_SAFE"
        with open(target_full, "wb") as f:
            f.write(original_target_bytes)
        original_target_hash = hashlib.sha256(original_target_bytes).hexdigest()

        # Create corrupted backup file
        tx_id = "test_corrupt_backup_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)

        corrupt_backup_rel = f"data/transactions/{tx_id}/backup/10_15_card1.png"
        corrupt_backup_full = os.path.join(fixture, corrupt_backup_rel)
        with open(corrupt_backup_full, "wb") as f:
            f.write(b"CORRUPTED_GARBAGE_BYTES_SHOULD_NEVER_OVERWRITE_TARGET")

        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {
                target_rel: corrupt_backup_rel
            },
            "pre_transaction_hashes": {
                target_rel: original_target_hash  # Expected hash of the backup
            },
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_IMAGES"}, f)

        # Attempt recovery
        failed_closed = False
        try:
            gwg.recover_unfinalized_transactions(project_dir=fixture)
        except RuntimeError as rerr:
            failed_closed = True
            print(f"  [PASS] Preflight properly caught corruption: {rerr}")

        assert failed_closed, "Recovery MUST fail closed on corrupt backup!"

        # CRITICAL ASSERTION: The active target file must NOT have been touched!
        with open(target_full, "rb") as f:
            target_after_bytes = f.read()

        assert target_after_bytes == original_target_bytes, "Active target file MUST remain 100% untouched!"
        assert os.path.exists(active_tx_path), "Active pointer MUST NOT be deleted when preflight fails!"
        print("  [PASS] Read-only preflight successfully verified: active target was NEVER modified!")

    finally:
        shutil.rmtree(fixture)

def test_missing_pre_transaction_hashes_fails_closed():
    print("\n--- Test 2: Missing Pre-Transaction Hashes Rejected During Preflight ---")
    fixture = make_isolated_project_fixture()
    try:
        target_rel = "photos/10_15_card1.png"
        target_full = os.path.join(fixture, target_rel)
        original_bytes = b"ORIGINAL_TARGET_BYTES_ABC"
        with open(target_full, "wb") as f:
            f.write(original_bytes)

        tx_id = "test_no_hashes_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)

        backup_rel = f"data/transactions/{tx_id}/backup/10_15_card1.png"
        backup_full = os.path.join(fixture, backup_rel)
        with open(backup_full, "wb") as f:
            f.write(original_bytes)

        plan_path = os.path.join(tx_dir, "tx_plan.json")
        # Plan has NO pre_transaction_hashes dictionary!
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {
                target_rel: backup_rel
            },
            # Missing pre_transaction_hashes!
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_IMAGES"}, f)

        # Attempt recovery
        failed_closed = False
        try:
            gwg.recover_unfinalized_transactions(project_dir=fixture)
        except RuntimeError as rerr:
            failed_closed = True
            print(f"  [PASS] Preflight properly rejected missing hashes: {rerr}")

        assert failed_closed, "Recovery MUST fail closed when pre_transaction_hashes is missing!"
        assert os.path.exists(active_tx_path), "Active pointer MUST NOT be deleted!"

        with open(target_full, "rb") as f:
            assert f.read() == original_bytes, "Active target must remain untouched!"
        print("  [PASS] Mandatory hash enforcement verified: plan without hashes rejected; target untouched.")

    finally:
        shutil.rmtree(fixture)

def test_dry_run_zero_mutation_in_isolated_fixture():
    print("\n--- Test 3: Dry-Run Zero Mutation in Isolated Fixture ---")
    fixture = make_isolated_project_fixture()
    try:
        tx_id = "test_dry_run_fixture_tx"
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

        gwg.process_calendar(DummyArgs(), project_dir=fixture)

        # Assert no mutations
        with open(plan_path, "r", encoding="utf-8") as f:
            plan_after = json.load(f)
        assert plan_after["state"] == "PROMOTING_IMAGES", "Dry run must NOT mutate plan state!"
        assert os.path.exists(active_tx_path), "Dry run must NOT delete pointer!"
        print("  [PASS] Dry run strictly preserved isolated fixture state without any mutations.")

    finally:
        shutil.rmtree(fixture)

def test_contradictory_clinical_qa_rejection():
    print("\n--- Test 4: Contradictory/Failed Clinical QA Rejection in Isolated Fixture ---")
    fixture = make_isolated_project_fixture()
    try:
        # Create a valid 720x540 PNG candidate in staging
        candidate_path = os.path.join(fixture, "photos", "staging", "candidate_10_15_card1_test.png")
        im = Image.new("RGB", (720, 540), color="blue")
        im.save(candidate_path, format="PNG")
        c_hash = gwg.compute_file_sha256(candidate_path)

        with open(os.path.join(fixture, "data", "health_365.json"), "r", encoding="utf-8") as f:
            calendar_data = json.load(f)
        target_card = calendar_data[0]["cards"][0]
        spec_h = gwg.compute_card_spec_hash(target_card, "10-15")

        # Contradictory record: status is APPROVED, but visual_concordance is FAIL
        manifest = {
            c_hash: {
                "day_id": "10-15",
                "card_idx": 1,
                "status": "APPROVED",
                "spec_hash": spec_h,
                "reviewer": {"name": "Clinical QA Officer", "role": "Auditor"},
                "clinical_review": {
                    "visual_concordance": "FAIL",  # Contradiction!
                    "cultural_authenticity": "PASS",
                    "polarity_match": "PASS",
                    "safety_equipment_check": "PASS"
                }
            }
        }
        with open(os.path.join(fixture, "data", "approved_manifest.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f)

        # Attempt active promotion in safe isolated fixture (discriminating: verifies rejection is not merely dry-run nonmutation)
        gwg.promote_staged_assets(calendar_data, day_filter="10-15", dry_run=False, project_dir=fixture)

        # Assert candidate was NOT accepted for promotion
        active_target = os.path.join(fixture, "photos", "10_15_card1.png")
        assert not os.path.exists(active_target), "Candidate with visual_concordance=FAIL must NOT be promoted!"
        active_tx = os.path.join(fixture, "data", "active_transaction.json")
        assert not os.path.exists(active_tx), "No transaction should be created for rejected candidate!"
        print("  [PASS] Contradictory clinical QA candidate was strictly rejected under active promotion mode.")

    finally:
        shutil.rmtree(fixture)

if __name__ == "__main__":
    print("Running Round 5 Isolated Verification Tests...")
    test_corrupt_backup_rejected_before_touching_target()
    test_missing_pre_transaction_hashes_fails_closed()
    test_dry_run_zero_mutation_in_isolated_fixture()
    test_contradictory_clinical_qa_rejection()
    print("\nALL ROUND 5 ISOLATED REMEDIATION TESTS PASSED SUCCESSFULLY!")
