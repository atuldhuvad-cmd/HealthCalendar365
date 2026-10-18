#!/usr/bin/env python3
"""Reconcile active ledger statuses against Dr. Atul's signed decisions.

This transaction promotes only the three scoped cards whose current clinical
copy and current visual were both explicitly approved. The 27 carried-forward
clinical approvals remain release-blocked because the bulk decision explicitly
excluded visual, Gujarati, provenance, and release approval.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generate_with_gemini import compute_card_spec_hash

TX_ID = "tx_20261018_clinical_ledger_reconciliation"
TX_DIR = ROOT / "data" / "transactions" / TX_ID
BACKUP_DIR = TX_DIR / "backup"
PLAN_PATH = TX_DIR / "tx_plan.json"
POINTER_PATH = ROOT / "data" / "active_transaction.json"
LEDGER_PATH = ROOT / "data" / "approved_manifest.json"
AUDIT_PATH = ROOT / "review" / "approval_ledger_reconciliation_2026-10-18.json"

SCOPED_PROMOTIONS = {"10-15_card2", "10-16-spine_card4", "10-18_card4"}
REVISED_SLOTS = SCOPED_PROMOTIONS | {"10-17_card1"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save_json_atomic(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slot_of(record: dict) -> str:
    return f"{record['day_id']}_card{int(record['card_idx'])}"


def main() -> None:
    if POINTER_PATH.exists():
        raise RuntimeError(f"Active transaction exists: {POINTER_PATH}")
    if TX_DIR.exists():
        raise RuntimeError(f"Transaction directory already exists: {TX_DIR}")

    ledger = load_json(LEDGER_PATH)
    health = load_json(ROOT / "data" / "health_365.json")
    days = {day["id"]: day for day in health}
    bulk = load_json(ROOT / "review" / "human_decisions" / "clinical_dr_atul_2026-10-16.json")
    transition = load_json(ROOT / "review" / "human_decisions" / "clinical_decision_transition_2026-10-16.json")
    scoped = load_json(ROOT / "review" / "human_decisions" / "scoped_reapproval_dr_atul_2026-10-16.json")
    nine = load_json(ROOT / "review" / "human_decisions" / "replacement_images_dr_atul_2026-10-16.json")
    road = load_json(ROOT / "review" / "human_decisions" / "replacement_image_10_17_card1_dr_atul_2026-10-18.json")

    bulk_scope = set(bulk["scope"])
    carried = set(transition["carried_forward_slots"])
    invalidated = set(transition["invalidated_slots"])
    scoped_decisions = scoped["card_decisions"]
    nine_scope = set(nine["scope"])

    assert bulk["decision"] == "APPROVE"
    assert len(bulk_scope) == 31
    assert bulk["explicitly_excluded"]["visual_accessibility_decisions"] is True
    assert bulk["explicitly_excluded"]["provenance_decisions"] is True
    assert bulk["explicitly_excluded"]["gujarati_linguistic_decisions"] is True
    assert bulk["explicitly_excluded"]["asset_promotion_or_release_authorization"] is True
    assert carried | invalidated == bulk_scope
    assert not (carried & invalidated)
    assert len(carried) == 27 and invalidated == REVISED_SLOTS
    assert set(scoped_decisions) == REVISED_SLOTS
    assert all(scoped_decisions[s]["clinical_copy_decision"] == "APPROVE" for s in REVISED_SLOTS)
    assert all(scoped_decisions[s]["visual_image_decision"] == "APPROVE" for s in SCOPED_PROMOTIONS)
    assert all(scoped_decisions[s]["production_approved"] is True for s in SCOPED_PROMOTIONS)
    assert scoped_decisions["10-17_card1"]["visual_image_decision"] == "REJECT"
    assert road["normalized_decision"] == "APPROVE_REPLACEMENT_AND_PROMOTE"
    assert road["scope"] == ["10-17_card1"]
    assert road["candidate_verification"]["slot"] == "10-17_card1"
    assert len(nine_scope) == 9

    by_slot = {slot_of(record): (image_hash, record) for image_hash, record in ledger.items()}
    assert len(by_slot) == len(ledger) == 40
    assert set(by_slot) == bulk_scope | nine_scope
    assert Counter(r["status"] for r in ledger.values()) == Counter({"PENDING_CLINICAL_SIGN_OFF": 30, "APPROVED": 10})

    for slot, (image_hash, record) in by_slot.items():
        path = ROOT / record["file_reference"]
        assert path.exists() and sha256(path) == image_hash
        card = days[record["day_id"]]["cards"][int(record["card_idx"]) - 1]
        assert compute_card_spec_hash(card, record["day_id"]) == record["spec_hash"]

    for slot in nine_scope | {"10-17_card1"}:
        assert by_slot[slot][1]["status"] == "APPROVED"
    for slot in SCOPED_PROMOTIONS:
        assert by_slot[slot][1]["status"] == "PENDING_CLINICAL_SIGN_OFF"
        decision = scoped_decisions[slot]
        image_hash, record = by_slot[slot]
        assert decision["image_sha256"] == image_hash
        assert decision["spec_hash"] == record["spec_hash"]

    BACKUP_DIR.mkdir(parents=True)
    backup = BACKUP_DIR / "data" / "approved_manifest.json"
    backup.parent.mkdir(parents=True)
    shutil.copy2(LEDGER_PATH, backup)
    pre_hash = sha256(LEDGER_PATH)
    plan = {
        "tx_id": TX_ID,
        "created_at": "2026-10-18",
        "state": "PREPARED",
        "scope": sorted(SCOPED_PROMOTIONS),
        "pre_transaction_hashes": {"data/approved_manifest.json": pre_hash},
        "backup": backup.relative_to(ROOT).as_posix(),
    }
    save_json_atomic(PLAN_PATH, plan)
    save_json_atomic(POINTER_PATH, {"tx_id": TX_ID, "plan_path": PLAN_PATH.relative_to(ROOT).as_posix(), "state": "PREPARED"})

    try:
        for slot in sorted(SCOPED_PROMOTIONS):
            image_hash, record = by_slot[slot]
            decision = scoped_decisions[slot]
            record.update({
                "status": "APPROVED",
                "reviewer": {
                    "name": scoped["reviewer"]["name"],
                    "qualification": scoped["reviewer"]["qualification"],
                    "role": scoped["reviewer"]["professional_role"],
                },
                "timestamp": scoped["submitted_at"],
                "clinical_review": {
                    "visual_concordance": "PASS",
                    "cultural_authenticity": "PASS",
                    "polarity_match": "PASS",
                    "safety_equipment_check": "N/A",
                    "findings": decision["notes"],
                },
                "decision_record": "review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json",
            })

        save_json_atomic(LEDGER_PATH, ledger)
        final_counts = Counter(r["status"] for r in ledger.values())
        assert final_counts == Counter({"PENDING_CLINICAL_SIGN_OFF": 27, "APPROVED": 13})

        audit_records = []
        for slot in sorted(by_slot):
            image_hash, record = by_slot[slot]
            if slot in nine_scope:
                basis = "approved_nine_replacement_set"
            elif slot == "10-17_card1":
                basis = "approved_scoped_copy_and_approved_replacement_image"
            elif slot in SCOPED_PROMOTIONS:
                basis = "approved_scoped_copy_and_existing_image"
            else:
                basis = "clinical_approval_carried_forward_other_human_gates_excluded"
            audit_records.append({
                "slot": slot,
                "status": record["status"],
                "decision_basis": basis,
                "image_sha256": image_hash,
                "spec_hash": record["spec_hash"],
                "decision_record": record.get("decision_record", "review/human_decisions/clinical_dr_atul_2026-10-16.json"),
            })

        audit = {
            "schema_version": "1.0.0",
            "created_at": "2026-10-18",
            "transaction_id": TX_ID,
            "result": "EVIDENCE_SUPPORTED_PARTIAL_RECONCILIATION",
            "active_ledger_counts": dict(final_counts),
            "clinical_copy_approved": 40,
            "release_eligible_approved": 13,
            "pending_overall_human_review": 27,
            "reason_27_remain_pending": "The original 31-card bulk decision explicitly excluded visual/accessibility, Gujarati linguistic, provenance, asset promotion, and release authorization. Clinical approval is preserved, but APPROVED is a release-eligible combined status under RELEASE_GOVERNANCE.md.",
            "records": audit_records,
        }
        save_json_atomic(AUDIT_PATH, audit)

        plan["state"] = "FINALIZED"
        plan["finalized_at"] = "2026-10-18"
        plan["post_transaction_hashes"] = {"data/approved_manifest.json": sha256(LEDGER_PATH)}
        plan["result_counts"] = dict(final_counts)
        save_json_atomic(PLAN_PATH, plan)
        POINTER_PATH.unlink()
        print("[PASS] Reconciled ledger to 13 APPROVED / 27 PENDING / 0 REJECTED")
    except BaseException:
        shutil.copy2(backup, LEDGER_PATH)
        plan["state"] = "ROLLED_BACK"
        save_json_atomic(PLAN_PATH, plan)
        if POINTER_PATH.exists():
            POINTER_PATH.unlink()
        raise


if __name__ == "__main__":
    main()
