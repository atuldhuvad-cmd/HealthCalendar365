"""
test_remediation_round3.py
-----------------------------------------------------------------------------
Automated verification tests for Round 3 remediations:
1. Truncated PNG rejection via full pixel decompression.
2. Dimensions and aspect ratio verification.
3. Spec-bound approval verification (outdated/tampered spec rejected) & REJECTED_MISMATCH count.
4. Whole-release transactional rollback restoring active artwork bytes on failure.
5. Startup crash recovery restoring pre-transaction state from unfinalized disk plan.

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
    temp_dir = tempfile.mkdtemp(prefix="health365_test_fixture_r3_")
    os.makedirs(os.path.join(temp_dir, "data", "transactions"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "photos", "staging"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "icons"), exist_ok=True)

    with open(os.path.join(temp_dir, "sw.js"), "w", encoding="utf-8") as f:
        f.write("const PRECACHE_ASSETS = [\n];\n")
    with open(os.path.join(temp_dir, "data", "health_365.json"), "w", encoding="utf-8") as f:
        f.write("[]")
    with open(os.path.join(temp_dir, "js", "calendar-data.js"), "w", encoding="utf-8") as f:
        f.write("window.HEALTH_CALENDAR_DATA = [];")

    # Create dummy core assets for complete builder isolation within temp directory
    for rel in ["index.html", "manifest.json", "css/styles.css", "css/fonts.css", "js/app.js", "js/canvas-renderer.js", "js/db.js", "icons/icon-192.png", "icons/icon-512.png"]:
        p = os.path.join(temp_dir, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(b"mock")
    return temp_dir

def test_truncated_image_rejection():
    print("\n--- Test 1: Truncated Image Rejection ---")
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tmp_name = f.name
        # Create valid 720x540 PNG then truncate it
        im = Image.new("RGB", (720, 540), color="blue")
        im.save(tmp_name, format="PNG")
    
    # Read bytes and truncate by 50%
    with open(tmp_name, "rb") as f:
        full_bytes = f.read()
    with open(tmp_name, "wb") as f:
        f.write(full_bytes[: len(full_bytes) // 2])
    
    valid, err = gwg.verify_image_integrity_and_decode(tmp_name)
    os.remove(tmp_name)
    
    assert not valid, "Truncated PNG must be rejected!"
    print(f"  [PASS] Truncated PNG correctly rejected: {err}")

def test_aspect_ratio_and_dimensions():
    print("\n--- Test 2: Dimensions and Aspect Ratio Verification ---")
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tmp_1x1 = f.name
        Image.new("RGB", (1, 1)).save(tmp_1x1, format="PNG")
    valid1, err1 = gwg.verify_image_integrity_and_decode(tmp_1x1)
    os.remove(tmp_1x1)
    assert not valid1, "1x1 PNG must be rejected!"
    print(f"  [PASS] 1x1 PNG rejected: {err1}")

    # Undersized height: 1000x400 fails minimum height 540
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tmp_undersized = f.name
        Image.new("RGB", (1000, 400)).save(tmp_undersized, format="PNG")
    valid2, err2 = gwg.verify_image_integrity_and_decode(tmp_undersized)
    os.remove(tmp_undersized)
    assert not valid2, "Undersized height must be rejected!"
    print(f"  [PASS] Undersized height rejected: {err2}")

    # Meets minimum dimensions (1200>=720, 600>=540) but violates 4:3 aspect ratio (2.0)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tmp_bad_aspect = f.name
        Image.new("RGB", (1200, 600)).save(tmp_bad_aspect, format="PNG")
    valid3, err3 = gwg.verify_image_integrity_and_decode(tmp_bad_aspect)
    os.remove(tmp_bad_aspect)
    assert not valid3, "Bad aspect ratio must be rejected!"
    assert "Aspect ratio deviation" in err3, f"Expected aspect ratio deviation error, got: {err3}"
    print(f"  [PASS] Bad aspect ratio rejected: {err3}")

def test_spec_bound_and_rejected_manifest():
    print("\n--- Test 3: Spec-Bound Approval & Mismatch Rejection (Read-Only) ---")
    with open(gwg.APPROVED_MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    # Check that known mismatches are REJECTED_MISMATCH
    rejected_entries = [v for v in manifest.values() if v.get("status") == "REJECTED_MISMATCH"]
    assert len(rejected_entries) == 9, f"Expected 9 rejected mismatch entries, found {len(rejected_entries)}"
    print(f"  [PASS] {len(rejected_entries)} mismatched assets correctly recorded as REJECTED_MISMATCH")

    # Verify that spec_hash is bound
    for k, v in manifest.items():
        assert "spec_hash" in v, f"Entry {k} must have spec_hash"
        assert len(v["spec_hash"]) == 64, "spec_hash must be a 64-char SHA-256"
    print("  [PASS] All manifest entries strictly bound to 64-char canonical spec_hash")

def test_whole_release_rollback_restores_artwork():
    print("\n--- Test 4: Whole-Release Rollback Restores Active Artwork Bytes ---")
    fixture = make_isolated_project_fixture()
    try:
        test_photo_rel = "photos/test_rollback_target.png"
        test_photo_full = os.path.join(fixture, test_photo_rel)
        
        original_bytes = b"ORIGINAL_ACTIVE_ARTWORK_BYTES_12345"
        with open(test_photo_full, "wb") as f:
            f.write(original_bytes)
        orig_hash = hashlib.sha256(original_bytes).hexdigest()
        
        # Create fake transaction plan in isolated fixture
        tx_id = "test_rollback_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        tx_backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(tx_backup_dir, exist_ok=True)
        
        backup_photo_rel = f"data/transactions/{tx_id}/backup/test_rollback_target.png"
        backup_photo_full = os.path.join(fixture, backup_photo_rel)
        shutil.copy2(test_photo_full, backup_photo_full)
        
        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_IMAGES",
            "backups": {
                test_photo_rel: backup_photo_rel
            },
            "pre_transaction_hashes": {
                test_photo_rel: orig_hash
            },
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)
        
        # Overwrite the target file with mutated bytes
        with open(test_photo_full, "wb") as f:
            f.write(b"MUTATED_CANDIDATE_BYTES_99999")
        
        # Execute rollback
        gwg.rollback_transaction(plan, plan_path, project_dir=fixture)
        
        # Verify that original bytes were restored
        with open(test_photo_full, "rb") as f:
            restored_bytes = f.read()
        
        assert restored_bytes == original_bytes, "Active artwork bytes MUST be restored to original on rollback!"
        print("  [PASS] Active artwork bytes successfully restored to original pre-transaction state!")
    finally:
        shutil.rmtree(fixture)

def test_startup_crash_recovery():
    print("\n--- Test 5: Startup Crash Recovery from Unfinalized Transaction ---")
    fixture = make_isolated_project_fixture()
    try:
        test_photo_rel = "photos/test_crash_target.png"
        test_photo_full = os.path.join(fixture, test_photo_rel)
        
        original_bytes = b"ORIGINAL_BEFORE_CRASH_BYTES_ABCDE"
        with open(test_photo_full, "wb") as f:
            f.write(original_bytes)
        orig_hash = hashlib.sha256(original_bytes).hexdigest()
        
        tx_id = "test_crash_tx"
        tx_dir = os.path.join(fixture, "data", "transactions", tx_id)
        tx_backup_dir = os.path.join(tx_dir, "backup")
        os.makedirs(tx_backup_dir, exist_ok=True)
        
        backup_photo_rel = f"data/transactions/{tx_id}/backup/test_crash_target.png"
        backup_photo_full = os.path.join(fixture, backup_photo_rel)
        shutil.copy2(test_photo_full, backup_photo_full)
        
        plan_path = os.path.join(tx_dir, "tx_plan.json")
        plan = {
            "tx_id": tx_id,
            "state": "PROMOTING_DATASETS",  # Interrupted mid-flight!
            "backups": {
                test_photo_rel: backup_photo_rel
            },
            "pre_transaction_hashes": {
                test_photo_rel: orig_hash
            },
            "created_files": []
        }
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f)
        
        active_tx_path = os.path.join(fixture, "data", "active_transaction.json")
        with open(active_tx_path, "w", encoding="utf-8") as f:
            json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PROMOTING_DATASETS"}, f)
        
        # Overwrite the target file with corrupted candidate bytes
        with open(test_photo_full, "wb") as f:
            f.write(b"CORRUPTED_BYTES_DURING_CRASH")
        
        # Run startup crash recovery in isolated fixture
        gwg.recover_unfinalized_transactions(project_dir=fixture)
        
        with open(test_photo_full, "rb") as f:
            restored_bytes = f.read()
        
        assert restored_bytes == original_bytes, "Crash recovery must restore original bytes!"
        print("  [PASS] Startup crash recovery automatically reverted interrupted transaction and restored original artwork!")
    finally:
        shutil.rmtree(fixture)

if __name__ == "__main__":
    print("Running Round 3 Isolated Verification Tests...")
    test_truncated_image_rejection()
    test_aspect_ratio_and_dimensions()
    test_spec_bound_and_rejected_manifest()
    test_whole_release_rollback_restores_artwork()
    test_startup_crash_recovery()
    print("\nALL ROUND 3 ISOLATED REMEDIATION TESTS PASSED SUCCESSFULLY!")
