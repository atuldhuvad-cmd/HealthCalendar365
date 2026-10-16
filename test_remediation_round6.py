"""
test_remediation_round6.py
-----------------------------------------------------------------------------
Automated verification tests for Round 6 remediations:
1. Builder explicit project root: build_manifest accepts project_dir and propagates
   it cleanly without touching D:\\HealthCalendar365.
2. Complete test isolation: Fixture operations (recovery, rollback, promotion)
   never read, write, or mutate the real service worker or live project state.
3. Builder failure handling: Manifest build failure (returning False or raising)
   blocks recovery/rollback, marks RECOVERY_BLOCKED_MANIFEST_FAILED, and
   PRESERVES active_transaction.json and transaction plan (fail-closed).
4. Stub call inspection: Builder receives explicit project_dir in call arguments.
-----------------------------------------------------------------------------
"""

import os
import shutil
import sys
import tempfile
import json
import hashlib
import inspect
from pathlib import Path
from PIL import Image

import generate_with_gemini as gwg
from build_precache_manifest import build_manifest, ManifestBuildError

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def make_fixture():
    temp_dir = tempfile.mkdtemp(prefix="health365_r6_fixture_")
    os.makedirs(os.path.join(temp_dir, "data", "transactions"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "photos", "staging"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "icons"), exist_ok=True)

    with open(os.path.join(temp_dir, "sw.js"), "w", encoding="utf-8") as f:
        f.write("const PRECACHE_ASSETS = [\n];\n")

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

    # Create dummy core assets in fixture
    for rel in ["index.html", "manifest.json", "css/styles.css", "css/fonts.css", "js/app.js", "js/canvas-renderer.js", "js/db.js", "icons/icon-192.png", "icons/icon-512.png", "photos/10_15_card1.png"]:
        p = os.path.join(temp_dir, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(b"mock_content")

    return temp_dir

def test_builder_signature_and_project_dir_isolation():
    print("\n--- Test 1: Builder Signature & Project Dir Isolation ---")
    sig = inspect.signature(build_manifest)
    assert "project_dir" in sig.parameters, "build_manifest must accept project_dir parameter!"
    print(f"  [PASS] build_manifest signature verified: {sig}")

    live_sw_path = os.path.join(PROJECT_DIR, "sw.js")
    with open(live_sw_path, "rb") as f:
        live_sw_before = f.read()

    fixture = make_fixture()
    try:
        ok = build_manifest(project_dir=fixture, raise_on_error=True)
        assert ok, "build_manifest must succeed inside isolated fixture"

        # Verify fixture sw.js was updated
        with open(os.path.join(fixture, "sw.js"), "r", encoding="utf-8") as f:
            fixture_sw = f.read()
        assert "./photos/10_15_card1.png" in fixture_sw, "Fixture sw.js must contain referenced photos"

        # Verify live sw.js was 100% UNTOUCHED
        with open(live_sw_path, "rb") as f:
            live_sw_after = f.read()
        assert live_sw_before == live_sw_after, "Live sw.js must NOT be touched by fixture operations!"
        print("  [PASS] Fixture sw.js updated successfully; live D:\\HealthCalendar365\\sw.js remained 100% untouched.")
    finally:
        shutil.rmtree(fixture)

def test_recovery_blocks_on_builder_failure_and_preserves_pointer():
    print("\n--- Test 2: Recovery Blocks on Builder Failure & Preserves Pointer ---")
    fixture = make_fixture()
    try:
        tx_id = "test_builder_failure_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)

        target_rel = "photos/card1.png"
        target_full = os.path.join(fixture, target_rel)
        with open(target_full, "wb") as f:
            f.write(b"CURRENT_ACTIVE_TARGET")

        backup_rel = f"data/transactions/{tx_id}/backup/card1.png"
        backup_full = os.path.join(fixture, backup_rel)
        backup_bytes = b"PRE_TRANSACTION_ORIGINAL_BACKUP"
        with open(backup_full, "wb") as f:
            f.write(backup_bytes)
        backup_hash = hashlib.sha256(backup_bytes).hexdigest()

        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_DATASETS",
            "backups": {target_rel: backup_rel},
            "pre_transaction_hashes": {target_rel: backup_hash},
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_DATASETS"}, f, indent=2)

        # Delete fixture sw.js so real build_manifest inside fixture fails
        os.remove(os.path.join(fixture, "sw.js"))

        failed_closed = False
        try:
            gwg.recover_unfinalized_transactions(project_dir=fixture)
        except RuntimeError as err:
            failed_closed = True
            print(f"  [PASS] Recovery correctly halted with RuntimeError: {err}")

        assert failed_closed, "Recovery MUST raise RuntimeError when manifest build fails!"
        assert os.path.exists(active_tx_path), "active_transaction.json MUST be preserved on manifest build failure!"

        with open(plan_path, "r", encoding="utf-8") as f:
            plan_after = json.load(f)
        assert plan_after["state"] == "RECOVERY_BLOCKED_MANIFEST_FAILED", f"Plan state must be RECOVERY_BLOCKED_MANIFEST_FAILED, got: {plan_after['state']}"
        assert "recovery_error" in plan_after, "Plan must record recovery_error"
        print("  [PASS] Recovery failed closed: pointer preserved, state recorded as RECOVERY_BLOCKED_MANIFEST_FAILED.")
    finally:
        shutil.rmtree(fixture)

def test_rollback_blocks_on_builder_failure_and_preserves_pointer():
    print("\n--- Test 3: Rollback Blocks on Builder Failure & Preserves Pointer ---")
    fixture = make_fixture()
    try:
        tx_id = "test_rollback_builder_fail_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)

        target_rel = "photos/card1.png"
        target_full = os.path.join(fixture, target_rel)
        with open(target_full, "wb") as f:
            f.write(b"CURRENT_ACTIVE_TARGET")

        backup_rel = f"data/transactions/{tx_id}/backup/card1.png"
        backup_full = os.path.join(fixture, backup_rel)
        backup_bytes = b"PRE_TRANSACTION_ORIGINAL_BACKUP"
        with open(backup_full, "wb") as f:
            f.write(backup_bytes)
        backup_hash = hashlib.sha256(backup_bytes).hexdigest()

        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {target_rel: backup_rel},
            "pre_transaction_hashes": {target_rel: backup_hash},
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_IMAGES"}, f, indent=2)

        # Corrupt sw.js in fixture to trigger ManifestBuildError
        with open(os.path.join(fixture, "sw.js"), "w", encoding="utf-8") as f:
            f.write("corrupted_sw_without_precache_pattern")

        ret = gwg.rollback_transaction(plan, plan_path, project_dir=fixture)
        assert ret is False, "rollback_transaction must return False when manifest build fails!"
        assert os.path.exists(active_tx_path), "active_transaction.json MUST be preserved on rollback builder failure!"

        with open(plan_path, "r", encoding="utf-8") as f:
            plan_after = json.load(f)
        assert plan_after["state"] == "ROLLBACK_BLOCKED_MANIFEST_FAILED", f"Plan state must be ROLLBACK_BLOCKED_MANIFEST_FAILED, got {plan_after['state']}"
        print("  [PASS] Rollback failed closed: pointer preserved, state recorded as ROLLBACK_BLOCKED_MANIFEST_FAILED.")
    finally:
        shutil.rmtree(fixture)

def test_builder_recording_stub_confirms_project_dir_propagation():
    print("\n--- Test 4: Recording Stub Confirms project_dir Propagation & State Retention ---")
    fixture = make_fixture()
    try:
        tx_id = "test_stub_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(backup_dir, exist_ok=True)

        target_rel = "photos/card1.png"
        target_full = os.path.join(fixture, target_rel)
        with open(target_full, "wb") as f:
            f.write(b"ACTIVE_DATA")

        backup_rel = f"data/transactions/{tx_id}/backup/card1.png"
        backup_full = os.path.join(fixture, backup_rel)
        backup_bytes = b"ORIGINAL_BACKUP_DATA"
        with open(backup_full, "wb") as f:
            f.write(backup_bytes)
        backup_hash = hashlib.sha256(backup_bytes).hexdigest()

        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PREPARED",
            "backups": {target_rel: backup_rel},
            "pre_transaction_hashes": {target_rel: backup_hash},
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)

        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PREPARED"}, f, indent=2)

        # Substitute recording stub exactly like independent reviewer check_round6.py
        import types
        calls = []
        stub = types.ModuleType("build_precache_manifest")
        def fake_build(*a, **kw):
            calls.append({"args": a, "kwargs": kw})
            return False  # Simulate builder failure
        stub.build_manifest = fake_build
        stub.ManifestBuildError = ManifestBuildError

        old_mod = sys.modules.get("build_precache_manifest")
        sys.modules["build_precache_manifest"] = stub
        try:
            failed_closed = False
            try:
                gwg.recover_unfinalized_transactions(project_dir=fixture)
            except RuntimeError:
                failed_closed = True

            assert failed_closed, "Must fail closed when builder returns False"
            assert len(calls) == 1, f"Expected 1 builder call, got {len(calls)}"
            call_kw = calls[0]["kwargs"]
            assert call_kw.get("project_dir") == fixture, f"Builder must receive project_dir={fixture}, got {call_kw}"

            with open(plan_path, "r", encoding="utf-8") as f:
                plan_after = json.load(f)
            assert plan_after["state"] == "RECOVERY_BLOCKED_MANIFEST_FAILED", "Must NOT be ROLLED_BACK when builder returns False!"
            assert os.path.exists(active_tx_path), "Pointer MUST be preserved!"
            print(f"  [PASS] Stub captured call with project_dir={fixture}; recovery blocked and preserved pointer.")
        finally:
            if old_mod:
                sys.modules["build_precache_manifest"] = old_mod
    finally:
        shutil.rmtree(fixture)

if __name__ == "__main__":
    print("Running Round 6 Remediation Verification Tests...")
    test_builder_signature_and_project_dir_isolation()
    test_recovery_blocks_on_builder_failure_and_preserves_pointer()
    test_rollback_blocks_on_builder_failure_and_preserves_pointer()
    test_builder_recording_stub_confirms_project_dir_propagation()
    print("\nALL ROUND 6 REMEDIATION TESTS PASSED SUCCESSFULLY!")
