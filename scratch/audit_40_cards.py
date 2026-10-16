import json
import os

calendar = {d['id']: d for d in json.load(open('data/health_365.json', encoding='utf-8'))}
manifest = json.load(open('data/approved_manifest.json', encoding='utf-8'))

manifest_map = {}
for h, entry in manifest.items():
    manifest_map[(entry['day_id'], int(entry['card_idx']))] = (h, entry)

days = ['10-15', '10-15-cane', '10-16', '10-16-spine', '10-17', '10-18', '10-19', '10-19-oral', '10-20', '10-21']

out = []
for d_id in days:
    day = calendar.get(d_id)
    if not day:
        print(f"MISSING DAY {d_id}")
        continue
    day_info = {
        "id": d_id,
        "date": day.get("date"),
        "title_en": day.get("title_en"),
        "title_gu": day.get("title_gu"),
        "org_en": day.get("org_en"),
        "org_gu": day.get("org_gu"),
        "theme_color": day.get("theme_color"),
        "cards": []
    }
    for card in day.get('cards', []):
        c_idx = int(card.get('index', 1))
        h, m_entry = manifest_map.get((d_id, c_idx), (None, None))
        card_data = {
            "index": c_idx,
            "type": card.get("type"),
            "title_en": card.get("title_en"),
            "title_gu": card.get("title_gu"),
            "desc_en": card.get("desc_en"),
            "desc_gu": card.get("desc_gu"),
            "photo": card.get("photo"),
            "ai_prompt": card.get("ai_prompt"),
            "manifest_hash": h,
            "manifest_entry": m_entry
        }
        day_info["cards"].append(card_data)
    out.append(day_info)

with open('scratch/cards_40_dump.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(out)} days and {sum(len(d['cards']) for d in out)} cards to scratch/cards_40_dump.json")
