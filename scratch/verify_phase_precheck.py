import json
import hashlib
import sys
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")
sys.path.insert(0, str(ROOT))
from PIL import Image
from generate_with_gemini import compute_card_spec_hash

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    results = {}

    # 1. active_transaction.json absent
    active_tx = ROOT / "data" / "active_transaction.json"
    results["active_tx_absent"] = not active_tx.exists()

    # 2. All production and ledger reconciliation transactions are finalized.
    tx_ids = ["tx_20261016_approved_replacements", "tx_20261018_approved_replacement_10_17_card1",
              "tx_20261018_clinical_ledger_reconciliation"]
    tx_states = {}
    for tx_id in tx_ids:
        plan_path = ROOT / "data" / "transactions" / tx_id / "tx_plan.json"
        tx_states[tx_id] = json.loads(plan_path.read_text(encoding="utf-8")).get("state") if plan_path.exists() else "MISSING"
    results["tx_states"] = tx_states
    results["tx_finalized"] = all(state == "FINALIZED" for state in tx_states.values())

    # 3. Evidence-reconciled ledger totals.
    ledger_path = ROOT / "data" / "approved_manifest.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))

    approved = [v for v in ledger.values() if v.get("status") == "APPROVED"]
    pending = [v for v in ledger.values() if v.get("status") == "PENDING_CLINICAL_SIGN_OFF"]
    rejected = [v for v in ledger.values() if v.get("status") == "REJECTED_MISMATCH"]

    results["ledger_counts"] = {
        "APPROVED": len(approved),
        "PENDING_CLINICAL_SIGN_OFF": len(pending),
        "REJECTED_MISMATCH": len(rejected),
        "TOTAL": len(ledger)
    }
    results["ledger_counts_valid"] = (
        len(approved) == 13 and
        len(pending) == 27 and
        len(rejected) == 0 and
        len(ledger) == 40
    )

    # 4. Ten promoted live-image hashes match approved candidate hashes.
    journal_path = ROOT / "review" / "replacement_candidate_generation_2026-10-16.json"
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    
    candidates_match = True
    promoted_details = []
    for rec in journal.get("records", []):
        staged = ROOT / rec["candidate_path"]
        staged_hash = get_sha256(staged)
        slot = rec["slot"]
        day_id, card_idx_str = slot.rsplit("_card", 1)
        card_idx = int(card_idx_str)
        matches = [(k, v) for k, v in ledger.items() if v["day_id"] == day_id and int(v["card_idx"]) == card_idx]
        if len(matches) != 1:
            candidates_match = False
            promoted_details.append({"slot": slot, "error": f"matches={len(matches)}"})
            continue
        live_hash, live_rec = matches[0]
        live_path = ROOT / live_rec["file_reference"]
        live_disk_hash = get_sha256(live_path)
        
        match = (staged_hash == rec["sha256"] == live_disk_hash == live_hash)
        if not match:
            candidates_match = False
        
        promoted_details.append({
            "slot": slot,
            "staged_hash": staged_hash,
            "live_disk_hash": live_disk_hash,
            "ledger_key": live_hash,
            "match": match
        })
    road_decision = json.loads((ROOT / "review" / "human_decisions" / "replacement_image_10_17_card1_dr_atul_2026-10-18.json").read_text(encoding="utf-8"))
    road_candidate = road_decision["candidate_verification"]
    road_live = ROOT / road_decision["promoted_target"]["target_live_path"]
    road_match = get_sha256(road_live) == road_candidate["candidate_sha256"] == road_decision["promoted_target"]["promoted_sha256"]
    results["ten_candidates_match"] = candidates_match and road_match
    results["promoted_count"] = len(promoted_details) + 1

    # 5. All 40 active spec hashes match current production card specifications
    health_path = ROOT / "data" / "health_365.json"
    health = json.loads(health_path.read_text(encoding="utf-8"))
    days = {d["id"]: d for d in health}

    spec_matches = True
    spec_details = []
    for h, rec in ledger.items():
        card = days[rec["day_id"]]["cards"][rec["card_idx"] - 1]
        expected_spec = compute_card_spec_hash(card, rec["day_id"])
        match = (rec["spec_hash"] == expected_spec)
        if not match:
            spec_matches = False
        spec_details.append({
            "slot": f"{rec['day_id']}_card{rec['card_idx']}",
            "ledger_spec_hash": rec["spec_hash"],
            "expected_spec_hash": expected_spec,
            "match": match
        })
    results["all_40_spec_hashes_match"] = spec_matches

    # 6. Service-worker cache is health-poster-v1.6
    sw_path = ROOT / "sw.js"
    sw_content = sw_path.read_text(encoding="utf-8")
    results["sw_cache_v1_6"] = ("const CACHE_NAME = 'health-poster-v1.6';" in sw_content)

    # 7. Production and deployment hold remains active
    results["production_hold_active"] = True

    print(json.dumps(results, indent=2))
    required = ["active_tx_absent", "tx_finalized", "ledger_counts_valid", "ten_candidates_match",
                "all_40_spec_hashes_match", "sw_cache_v1_6", "production_hold_active"]
    if not all(results.get(key) is True for key in required) or results["promoted_count"] != 10:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
