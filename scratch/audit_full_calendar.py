import os
import sys
import json
import hashlib
from collections import defaultdict
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

DATA_PATH = 'data/health_365.json'
APPROVED_MANIFEST_PATH = 'data/approved_manifest.json'

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    calendar_data = json.load(f)

with open(APPROVED_MANIFEST_PATH, 'r', encoding='utf-8') as f:
    approved_manifest = json.load(f)

print(f"Loaded {len(calendar_data)} posters from {DATA_PATH}")

audit_results = {
    "total_posters": len(calendar_data),
    "total_card_slots": 0,
    "calendar_dates_covered": set(),
    "multi_observance_dates": [],
    "month_distribution": defaultdict(int),
    "card_placeholder_distribution": defaultdict(int),
    "dedicated_card_slots": 0,
    "placeholder_card_slots": 0,
    "missing_photos": [],
    "corrupt_photos": [],
    "empty_text_fields": [],
    "cards_summary": []
}

photo_cache = {}

for poster in calendar_data:
    p_id = poster.get('id', '')
    month = poster.get('month')
    day = poster.get('day')
    audit_results["month_distribution"][month] += 1
    
    # date string e.g. "01-01"
    date_key = f"{int(month):02d}-{int(day):02d}"
    if date_key in audit_results["calendar_dates_covered"]:
        audit_results["multi_observance_dates"].append({
            "date": date_key,
            "poster_id": p_id,
            "title_en": poster.get('title_en'),
            "title_gu": poster.get('title_gu')
        })
    else:
        audit_results["calendar_dates_covered"].add(date_key)
        
    cards = poster.get('cards', [])
    for idx, card in enumerate(cards):
        audit_results["total_card_slots"] += 1
        card_idx = card.get('index', idx + 1)
        slot_id = f"{p_id}_card{card_idx}"
        photo_path = card.get('photo') or card.get('image') or ''
        
        # Verify text fields
        for field in ['title_en', 'title_gu', 'desc_en', 'desc_gu']:
            val = (card.get(field) or '').strip()
            if not val:
                audit_results["empty_text_fields"].append({
                    "slot": slot_id,
                    "field": field
                })
                
        # Check photo existence & decode
        if photo_path not in photo_cache:
            if not os.path.exists(photo_path):
                audit_results["missing_photos"].append((slot_id, photo_path))
                photo_cache[photo_path] = {"exists": False, "valid": False, "sha256": None}
            else:
                try:
                    with open(photo_path, 'rb') as pf:
                        p_bytes = pf.read()
                        p_sha256 = hashlib.sha256(p_bytes).hexdigest()
                    with Image.open(photo_path) as img:
                        img.verify()
                    with Image.open(photo_path) as img:
                        img.load()
                        w, h = img.size
                    photo_cache[photo_path] = {
                        "exists": True, 
                        "valid": True, 
                        "sha256": p_sha256,
                        "width": w,
                        "height": h
                    }
                except Exception as e:
                    audit_results["corrupt_photos"].append((photo_path, str(e)))
                    photo_cache[photo_path] = {"exists": True, "valid": False, "sha256": None, "error": str(e)}
                    
        p_info = photo_cache[photo_path]
        is_placeholder = "cat_" in photo_path
        if is_placeholder:
            audit_results["placeholder_card_slots"] += 1
            audit_results["card_placeholder_distribution"][photo_path] += 1
        else:
            audit_results["dedicated_card_slots"] += 1
            
        # Compute canonical spec hash
        spec_dict = {
            "day_id": p_id,
            "card_idx": card_idx,
            "title_en": card.get('title_en', ''),
            "title_gu": card.get('title_gu', ''),
            "desc_en": card.get('desc_en', ''),
            "desc_gu": card.get('desc_gu', ''),
            "polarity": "negative_avoidance" if (card_idx in [3, 4] and "Don't" in card.get('badge_en', '')) else "positive",
            "prompt": card.get('ai_prompt', ''),
            "safety_rules": []
        }
        spec_canonical = json.dumps(spec_dict, sort_keys=True, ensure_ascii=False)
        spec_hash = hashlib.sha256(spec_canonical.encode('utf-8')).hexdigest()
        
        audit_results["cards_summary"].append({
            "slot": slot_id,
            "poster_id": p_id,
            "card_idx": card_idx,
            "photo_path": photo_path,
            "is_placeholder": is_placeholder,
            "image_sha256": p_info["sha256"] if p_info.get("exists") else None,
            "spec_hash": spec_hash
        })

print(f"Total card slots audited: {audit_results['total_card_slots']}")
print(f"Total calendar dates covered: {len(audit_results['calendar_dates_covered'])} / 365")
print(f"Multi-observance dates: {len(audit_results['multi_observance_dates'])}")
print(f"Dedicated cards: {audit_results['dedicated_card_slots']}")
print(f"Placeholder cards: {audit_results['placeholder_card_slots']}")
print(f"Empty text fields: {len(audit_results['empty_text_fields'])}")
print(f"Missing photos: {len(audit_results['missing_photos'])}")
print(f"Corrupt photos: {len(audit_results['corrupt_photos'])}")

# Output summary to review/full_calendar_audit.json
output_json_path = 'review/full_calendar_audit.json'
with open(output_json_path, 'w', encoding='utf-8') as out_f:
    json.dump({
        "audit_timestamp": "2026-10-16T17:35:00Z",
        "total_posters": audit_results["total_posters"],
        "total_card_slots": audit_results["total_card_slots"],
        "dates_covered_count": len(audit_results["calendar_dates_covered"]),
        "multi_observance_count": len(audit_results["multi_observance_dates"]),
        "multi_observances": audit_results["multi_observance_dates"],
        "dedicated_card_slots": audit_results["dedicated_card_slots"],
        "placeholder_card_slots": audit_results["placeholder_card_slots"],
        "month_distribution": dict(audit_results["month_distribution"]),
        "placeholder_distribution": dict(audit_results["card_placeholder_distribution"]),
        "empty_text_field_count": len(audit_results["empty_text_fields"]),
        "missing_photo_count": len(audit_results["missing_photos"]),
        "corrupt_photo_count": len(audit_results["corrupt_photos"]),
        "cards_summary": audit_results["cards_summary"]
    }, out_f, indent=2, ensure_ascii=False)

print(f"Wrote audit summary to {output_json_path}")
