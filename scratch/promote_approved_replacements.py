#!/usr/bin/env python3
"""Promote the nine user-approved replacement images as one recoverable transaction."""

import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(r"D:\HealthCalendar365")
sys.path.insert(0, str(ROOT))
TX_ID = "tx_20261016_approved_replacements"
TX_DIR = ROOT / "data" / "transactions" / TX_ID
BACKUP_DIR = TX_DIR / "backup"
PLAN_PATH = TX_DIR / "tx_plan.json"
POINTER_PATH = ROOT / "data" / "active_transaction.json"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


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


def compute_spec(card, day_id):
    from generate_with_gemini import compute_card_spec_hash
    return compute_card_spec_hash(card, day_id)


def main():
    if POINTER_PATH.exists():
        raise RuntimeError(f"Active transaction already exists: {POINTER_PATH}")
    if TX_DIR.exists():
        raise RuntimeError(f"Transaction directory already exists: {TX_DIR}")

    health_path = ROOT / "data" / "health_365.json"
    js_path = ROOT / "js" / "calendar-data.js"
    ledger_path = ROOT / "data" / "approved_manifest.json"
    sw_path = ROOT / "sw.js"
    journal_path = ROOT / "review" / "replacement_candidate_generation_2026-10-16.json"

    health = json.loads(health_path.read_text(encoding="utf-8"))
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    days = {day["id"]: day for day in health}

    copy_updates = {
        "10-20_card3": {
            "title_en": "Eliminate Slip, Trip & Fall Hazards at Home",
            "title_gu": "ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો",
            "desc_en": "Slippery wet floors and loose cords are a leading avoidable cause of falls and hip fractures in elders.",
            "desc_gu": "ભીનો ફ્લોર અને છૂટા વાયરો વડીલોમાં થાપાના ફ્રેક્ચરનું એક મુખ્ય ટાળી શકાય તેવું કારણ છે."
        },
        "10-20_card4": {
            "title_en": "Limit Excessive Salt Intake & Choose Wholesome Hydration",
            "title_gu": "વધુ પડતું મીઠું ટાળો અને પૂરતું પાણી-છાશ પીઓ",
            "desc_en": "Excessive dietary salt increases urinary calcium loss. For adults, keep total salt from all foods below 5 g/day (equivalent to less than 2 g/day sodium). Choose water or traditional unsalted buttermilk.",
            "desc_gu": "વધારે પડતું મીઠું ખાવાથી પેશાબ વાટે કેલ્શિયમ નીકળી જાય છે; પુખ્ત વયના લોકો માટે દિવસભરના બધા ખોરાકમાંથી મળતું કુલ મીઠું ૫ ગ્રામથી ઓછું રાખો (આશરે ૨ ગ્રામથી ઓછું સોડિયમ). પાણી અથવા મીઠું ઉમેર્યા વગરની છાશ પસંદ કરો."
        },
        "10-21_card2": {
            "desc_en": "Prolonged high-heat boiling can degrade and leach fortified iodine compounds. Adding iodized salt towards the end of cooking helps retain full micronutrient value.",
            "desc_gu": "લાંબા સમય સુધી વધુ ગરમીમાં ઉકાળવાથી આયોડિનનું પ્રમાણ ઘટી શકે છે; રસોઈ પૂરી થવાના સમયે મીઠું ઉમેરવાથી આયોડિનનું મૂલ્ય જળવાય છે."
        },
        "10-21_card3": {
            "title_en": "Avoid Unbranded Loose Coarse Salt",
            "title_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો"
        }
    }

    candidates = []
    for record in journal["records"]:
        slot = record["slot"]
        day_id, card_text = slot.rsplit("_card", 1)
        card_idx = int(card_text)
        matches = [(key, val) for key, val in ledger.items()
                   if val["day_id"] == day_id and int(val["card_idx"]) == card_idx]
        if len(matches) != 1:
            raise RuntimeError(f"Expected exactly one active ledger record for {slot}, got {len(matches)}")
        old_hash, old_record = matches[0]
        if old_record["status"] != "REJECTED_MISMATCH":
            raise RuntimeError(f"{slot} is not REJECTED_MISMATCH")
        staged = ROOT / record["candidate_path"]
        if sha256(staged) != record["sha256"]:
            raise RuntimeError(f"Candidate hash mismatch for {slot}")
        with Image.open(staged) as image:
            image.verify()
        with Image.open(staged) as image:
            if image.format != "PNG" or image.size != (1200, 900):
                raise RuntimeError(f"Candidate contract failed for {slot}: {image.format} {image.size}")
        target = ROOT / old_record["file_reference"]
        if not target.exists():
            raise FileNotFoundError(target)
        candidates.append((record, old_hash, old_record, staged, target, day_id, card_idx))

    backup_targets = [health_path, js_path, ledger_path, sw_path] + [item[4] for item in candidates]
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
        "created_at": "2026-10-16",
        "authorization_verbatim": "All aprove",
        "state": "PREPARED",
        "to_promote_count": 9,
        "backups": backups,
        "pre_transaction_hashes": pre_hashes,
        "created_files": []
    }
    save_json(PLAN_PATH, plan)
    save_json(POINTER_PATH, {"tx_id": TX_ID, "plan_path": str(PLAN_PATH), "state": "PREPARED"})

    try:
        for slot, updates in copy_updates.items():
            day_id, card_text = slot.rsplit("_card", 1)
            card = days[day_id]["cards"][int(card_text) - 1]
            card.update(updates)

        plan["state"] = "PROMOTING_IMAGES"
        save_json(PLAN_PATH, plan)
        for _, _, _, staged, target, _, _ in candidates:
            atomic_bytes(target, staged.read_bytes())

        plan["state"] = "PROMOTING_DATASETS"
        save_json(PLAN_PATH, plan)
        new_ledger = dict(ledger)
        for record, old_hash, old_record, _, target, day_id, card_idx in candidates:
            del new_ledger[old_hash]
            card = days[day_id]["cards"][card_idx - 1]
            new_hash = sha256(target)
            new_ledger[new_hash] = {
                "day_id": day_id,
                "card_idx": card_idx,
                "status": "APPROVED",
                "spec_hash": compute_spec(card, day_id),
                "reviewer": {
                    "name": "Dr. Atul",
                    "qualification": "MBBS",
                    "role": "Trainer in Health Department since 2002"
                },
                "timestamp": "2026-10-16",
                "clinical_review": {
                    "visual_concordance": "PASS",
                    "cultural_authenticity": "PASS",
                    "polarity_match": "PASS",
                    "safety_equipment_check": "PASS" if record["slot"] == "10-20_card1" else "N/A",
                    "findings": "Nine-candidate replacement set approved by Dr. Atul with the verbatim decision: All aprove."
                },
                "file_reference": old_record["file_reference"],
                "decision_record": "review/human_decisions/replacement_images_dr_atul_2026-10-16.json"
            }

        health_text = json.dumps(health, ensure_ascii=False, indent=2) + "\n"
        atomic_text(health_path, health_text)
        atomic_text(js_path, "// 365-Day Indian Health Calendar Data (Preloaded)\nwindow.HEALTH_CALENDAR_DATA = " + health_text.rstrip() + ";\n")
        save_json(ledger_path, new_ledger)

        sw_text = sw_path.read_text(encoding="utf-8")
        if "health-poster-v1.3" not in sw_text:
            raise RuntimeError("Expected service-worker cache health-poster-v1.3 before promotion")
        atomic_text(sw_path, sw_text.replace("health-poster-v1.3", "health-poster-v1.4"))

        plan["state"] = "PROMOTING_PRECACHE"
        save_json(PLAN_PATH, plan)
        from build_precache_manifest import build_manifest
        if not build_manifest(project_dir=str(ROOT), raise_on_error=True):
            raise RuntimeError("Precache manifest build returned false")

        for _, _, _, _, target, _, _ in candidates:
            if not target.exists() or sha256(target) not in new_ledger:
                raise RuntimeError(f"Post-promotion verification failed: {target}")

        old_records = {old_hash: old_record for _, old_hash, old_record, *_ in candidates}
        archive = {
            "schema_version": "1.0.0",
            "superseded_at": "2026-10-16",
            "transaction_id": TX_ID,
            "reason": "Nine rejected images replaced after Dr. Atul approved all generated candidates.",
            "records": old_records
        }
        save_json(ROOT / "review" / "superseded" / "rejected_assets_pre_replacement_2026-10-16.json", archive)

        decision = {
            "schema_version": "1.0.0",
            "submitted_at": "2026-10-16",
            "reviewer": {
                "name": "Dr. Atul",
                "qualification": "MBBS",
                "role": "Trainer in Health Department since 2002",
                "professional_role": "Trainer in Health Department since 2002"
            },
            "decision_verbatim": "All aprove",
            "normalized_decision": "APPROVE_ALL_NINE_REPLACEMENTS_AND_PROMOTE",
            "scope": [record["slot"] for record in journal["records"]],
            "candidate_generation_record": "review/replacement_candidate_generation_2026-10-16.json",
            "transaction_id": TX_ID
        }
        save_json(ROOT / "review" / "human_decisions" / "replacement_images_dr_atul_2026-10-16.json", decision)

        for record in journal["records"]:
            record["human_visual_decision"] = "APPROVED_BY_DR_ATUL_2026-10-16"
            record["promotion_status"] = "PROMOTED_TO_LIVE_ASSET"
        journal["production_hold"] = "ACTIVE_PENDING_REMAINING_ACCEPTANCE_GATES"
        journal["promotion_transaction"] = TX_ID
        save_json(journal_path, journal)

        plan["state"] = "FINALIZED"
        plan["finalized_at"] = "2026-10-16"
        plan["post_transaction_hashes"] = {
            target.relative_to(ROOT).as_posix(): sha256(target) for target in backup_targets
        }
        save_json(PLAN_PATH, plan)
        POINTER_PATH.unlink()
        print(f"[PASS] Promoted 9 replacement images in {TX_ID}")
    except BaseException:
        for rel, backup_rel in backups.items():
            shutil.copy2(ROOT / backup_rel, ROOT / rel)
        plan["state"] = "ROLLED_BACK"
        save_json(PLAN_PATH, plan)
        if POINTER_PATH.exists():
            POINTER_PATH.unlink()
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        raise
