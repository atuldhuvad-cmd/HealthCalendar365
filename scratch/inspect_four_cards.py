import json
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")

health = json.loads((ROOT / "data" / "health_365.json").read_text(encoding="utf-8"))
days = {d["id"]: d for d in health}
ledger = json.loads((ROOT / "data" / "approved_manifest.json").read_text(encoding="utf-8"))

target_slots = [
    ("10-15", 2, "10-15_card2"),
    ("10-16-spine", 4, "10-16-spine_card4"),
    ("10-17", 1, "10-17_card1"),
    ("10-18", 4, "10-18_card4")
]

out = []
for day_id, card_idx, slot in target_slots:
    day = days.get(day_id)
    if not day:
        print(f"Error: {day_id} not found in health_365.json")
        continue
    card = day["cards"][card_idx - 1]
    
    # find in ledger
    ledger_entry = None
    ledger_hash = None
    for h, rec in ledger.items():
        if rec["day_id"] == day_id and rec["card_idx"] == card_idx:
            ledger_entry = rec
            ledger_hash = h
            break
            
    out.append({
        "slot": slot,
        "day_id": day_id,
        "card_idx": card_idx,
        "day_title_en": day.get("title", {}).get("en"),
        "day_title_gu": day.get("title", {}).get("gu"),
        "category": day.get("category"),
        "card": card,
        "ledger_hash": ledger_hash,
        "ledger_entry": ledger_entry
    })

(ROOT / "scratch" / "four_cards_info.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Successfully wrote {len(out)} cards to scratch/four_cards_info.json")
