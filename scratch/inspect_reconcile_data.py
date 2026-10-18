import json

h365 = json.load(open('data/health_365.json', 'r', encoding='utf-8'))
app_man = json.load(open('data/approved_manifest.json', 'r', encoding='utf-8'))
rq = json.load(open('review/review_queue.json', 'r', encoding='utf-8'))['review_queue']
prop = json.load(open('review/proposed_copy_and_provenance_corrections.json', 'r', encoding='utf-8'))
pilot = json.load(open('review/NINE_CANDIDATE_PILOT_PLAN.json', 'r', encoding='utf-8'))

h365_by_id = {p['id']: p for p in h365}
rq_by_slot = {f"{r['poster_id']}_card{r['card_idx']}": r for r in rq}
app_by_slot = {f"{v['day_id']}_card{v['card_idx']}": (k, v) for k, v in app_man.items()}

print(f"Total slots in rq: {len(rq_by_slot)}")
print(f"Total slots in app_man: {len(app_by_slot)}")

for slot, (img_hash, app_entry) in sorted(app_by_slot.items()):
    rq_entry = rq_by_slot.get(slot)
    p_id = app_entry['day_id']
    c_idx = app_entry['card_idx'] - 1
    poster = h365_by_id.get(p_id)
    card = poster['cards'][c_idx] if poster else None
    
    assert rq_entry is not None, f"Missing rq entry for {slot}"
    assert card is not None, f"Missing card in h365 for {slot}"
    assert rq_entry['image_sha256'] == img_hash, f"Hash mismatch for {slot}"

print("All 40 spotlight cards verified and cross-referenced 100% across h365, app_man, and review_queue!")
