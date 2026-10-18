#!/usr/bin/env python3
"""
scratch/promote_10_17_card1.py
-----------------------------------------------------------------------------
Promotes the user-verified and Dr. Atul-approved replacement candidate for
10-17_card1 (World Trauma Day - Helmet & Seatbelt) as a strictly recoverable,
fail-closed atomic transaction.

Transaction ID: tx_20261018_approved_replacement_10_17_card1
-----------------------------------------------------------------------------
"""

import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(r"D:\HealthCalendar365")
sys.path.insert(0, str(ROOT))

TX_ID = "tx_20261018_approved_replacement_10_17_card1"
TX_DIR = ROOT / "data" / "transactions" / TX_ID
BACKUP_DIR = TX_DIR / "backup"
PLAN_PATH = TX_DIR / "tx_plan.json"
POINTER_PATH = ROOT / "data" / "active_transaction.json"

EXPECTED_CANDIDATE_PATH = ROOT / "photos" / "staging" / "candidate_10_17_card1_v1.png"
EXPECTED_CANDIDATE_SHA256 = "247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6"
EXPECTED_OLD_SHA256 = "4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e"
EXPECTED_SPEC_HASH = "122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1"
LIVE_TARGET_PATH = ROOT / "photos" / "oct17_do1.png"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def atomic_bytes(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_bytes(payload)
    os.replace(temp, path)

def atomic_text(path, payload):
    atomic_bytes(path, payload.encode("utf-8"))

def save_json(path, value):
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def main():
    print(f"=== Starting Transactional Promotion: {TX_ID} ===")

    # 1. Preflight safety checks
    if POINTER_PATH.exists():
        raise RuntimeError(f"Active transaction pointer already exists: {POINTER_PATH}")
    if TX_DIR.exists():
        raise RuntimeError(f"Transaction directory already exists: {TX_DIR}")

    # 2. Candidate verification
    if not EXPECTED_CANDIDATE_PATH.exists():
        raise FileNotFoundError(f"Candidate file missing: {EXPECTED_CANDIDATE_PATH}")
    cand_hash = sha256(EXPECTED_CANDIDATE_PATH)
    if cand_hash != EXPECTED_CANDIDATE_SHA256:
        raise ValueError(f"Candidate hash mismatch: {cand_hash} != expected {EXPECTED_CANDIDATE_SHA256}")
    
    with Image.open(EXPECTED_CANDIDATE_PATH) as img:
        img.verify()
    with Image.open(EXPECTED_CANDIDATE_PATH) as img:
        if img.format != "PNG" or img.size != (1200, 900) or img.mode != "RGB":
            raise ValueError(f"Candidate contract violation: format={img.format}, size={img.size}, mode={img.mode}")
        img.load()
    print("  [PASS] Candidate image verified: valid 1200x900 RGB PNG with matching SHA-256.")

    # 3. Target verification
    if not LIVE_TARGET_PATH.exists():
        raise FileNotFoundError(f"Live target missing: {LIVE_TARGET_PATH}")
    old_target_hash = sha256(LIVE_TARGET_PATH)
    if old_target_hash != EXPECTED_OLD_SHA256:
        raise ValueError(f"Live target hash mismatch: {old_target_hash} != expected {EXPECTED_OLD_SHA256}")

    # 4. Paths and active ledger verification
    health_path = ROOT / "data" / "health_365.json"
    js_path = ROOT / "js" / "calendar-data.js"
    ledger_path = ROOT / "data" / "approved_manifest.json"
    sw_path = ROOT / "sw.js"

    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    if EXPECTED_OLD_SHA256 not in ledger:
        raise KeyError(f"Expected old hash {EXPECTED_OLD_SHA256} not in active ledger!")
    old_ledger_rec = ledger[EXPECTED_OLD_SHA256]
    if old_ledger_rec.get("day_id") != "10-17" or old_ledger_rec.get("card_idx") != 1:
        raise ValueError(f"Unexpected ledger record for old hash: {old_ledger_rec}")
    if old_ledger_rec.get("spec_hash") != EXPECTED_SPEC_HASH:
        raise ValueError(f"Spec hash mismatch in ledger: {old_ledger_rec.get('spec_hash')} != {EXPECTED_SPEC_HASH}")

    # 5. Backup phase
    backup_targets = [LIVE_TARGET_PATH, health_path, js_path, ledger_path, sw_path]
    BACKUP_DIR.mkdir(parents=True)
    backups = {}
    pre_hashes = {}
    for target in backup_targets:
        rel = target.relative_to(ROOT).as_posix()
        backup = BACKUP_DIR / rel
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target, backup)
        backups[rel] = backup.relative_to(ROOT).as_posix()
        pre_hashes[rel] = sha256(target)

    plan = {
        "tx_id": TX_ID,
        "created_at": "2026-10-18T11:51:08-04:00",
        "authorization_verbatim": "Dr. Atul has explicitly APPROVED the replacement candidate for 10-17_card1.",
        "state": "PREPARED",
        "to_promote_count": 1,
        "backups": backups,
        "pre_transaction_hashes": pre_hashes,
        "created_files": []
    }
    save_json(PLAN_PATH, plan)
    save_json(POINTER_PATH, {"tx_id": TX_ID, "plan_path": str(PLAN_PATH), "state": "PREPARED"})
    print("  [PASS] Backup completed and transaction pointer established.")

    try:
        # Step A: Promote image
        plan["state"] = "PROMOTING_IMAGES"
        save_json(PLAN_PATH, plan)
        atomic_bytes(LIVE_TARGET_PATH, EXPECTED_CANDIDATE_PATH.read_bytes())
        print("  [PASS] Live image replaced with candidate.")

        # Step B: Promote ledger
        plan["state"] = "PROMOTING_DATASETS"
        save_json(PLAN_PATH, plan)
        new_ledger = dict(ledger)
        del new_ledger[EXPECTED_OLD_SHA256]

        decision_doc_rel = "review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json"
        new_ledger[EXPECTED_CANDIDATE_SHA256] = {
            "day_id": "10-17",
            "card_idx": 1,
            "status": "APPROVED",
            "spec_hash": EXPECTED_SPEC_HASH,
            "reviewer": {
                "name": "Dr. Atul",
                "qualification": "MBBS",
                "role": "Trainer in Health Department since 2002"
            },
            "timestamp": "2026-10-18T11:51:08-04:00",
            "clinical_review": {
                "visual_concordance": "PASS",
                "cultural_authenticity": "PASS",
                "polarity_match": "PASS",
                "safety_equipment_check": "PASS",
                "findings": "Replacement candidate for 10-17_card1 verified (1 RHD driver, 1 steering wheel, fastened 3-point seatbelts, no text/logos) and explicitly approved by Dr. Atul."
            },
            "file_reference": "photos/oct17_do1.png",
            "decision_record": decision_doc_rel
        }
        save_json(ledger_path, new_ledger)
        print("  [PASS] Active ledger updated with approved entry and old entry removed.")

        # Step C: Increment service worker cache version
        sw_text = sw_path.read_text(encoding="utf-8")
        if "health-poster-v1.4" not in sw_text:
            raise RuntimeError("Expected cache health-poster-v1.4 in sw.js before promotion!")
        sw_text_updated = sw_text.replace("health-poster-v1.4", "health-poster-v1.5")
        atomic_text(sw_path, sw_text_updated)
        print("  [PASS] Service worker cache incremented to health-poster-v1.5.")

        # Step D: Rebuild precache manifest
        plan["state"] = "PROMOTING_PRECACHE"
        save_json(PLAN_PATH, plan)
        from build_precache_manifest import build_manifest
        manifest_ok = build_manifest(project_dir=str(ROOT), raise_on_error=True)
        if not manifest_ok:
            raise RuntimeError("Precache manifest build failed or returned False!")
        print("  [PASS] Precache manifest rebuilt successfully.")

        # Step E: Post-promotion verification
        if not LIVE_TARGET_PATH.exists() or sha256(LIVE_TARGET_PATH) != EXPECTED_CANDIDATE_SHA256:
            raise RuntimeError(f"Post-promotion verification failed for {LIVE_TARGET_PATH}")
        if EXPECTED_CANDIDATE_SHA256 not in new_ledger or new_ledger[EXPECTED_CANDIDATE_SHA256]["status"] != "APPROVED":
            raise RuntimeError("Post-promotion verification failed for ledger entry")

        # Step F: Preserve historical rejection evidence in superseded archive
        superseded_path = ROOT / "review" / "superseded" / "rejected_assets_10_17_card1_pre_replacement_2026-10-18.json"
        archive = {
            "schema_version": "1.0.0",
            "superseded_at": "2026-10-18T11:51:08-04:00",
            "transaction_id": TX_ID,
            "reason": "10-17_card1 defective image (dual steering wheels AI defect) replaced after Dr. Atul approved candidate_10_17_card1_v1.png.",
            "record": {
                EXPECTED_OLD_SHA256: old_ledger_rec
            }
        }
        save_json(superseded_path, archive)
        plan["created_files"].append(str(superseded_path.relative_to(ROOT).as_posix()))
        print(f"  [PASS] Historical rejection preserved in {superseded_path.name}")

        # Step G: Finalize plan
        plan["state"] = "FINALIZED"
        plan["finalized_at"] = "2026-10-18T11:51:08-04:00"
        plan["post_transaction_hashes"] = {
            target.relative_to(ROOT).as_posix(): sha256(target) for target in backup_targets
        }
        save_json(PLAN_PATH, plan)
        POINTER_PATH.unlink()
        print(f"[TRANSACTION FINALIZED] Successfully promoted 10-17_card1 in {TX_ID}")

    except BaseException as exc:
        print(f"[ERROR] Transaction failed ({exc}). Initiating safe rollback...", file=sys.stderr)
        for rel, backup_rel in backups.items():
            shutil.copy2(ROOT / backup_rel, ROOT / rel)
        plan["state"] = "ROLLED_BACK"
        save_json(PLAN_PATH, plan)
        if POINTER_PATH.exists():
            POINTER_PATH.unlink()
        raise

if __name__ == "__main__":
    main()
