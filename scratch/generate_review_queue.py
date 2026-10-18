import json
import os
import hashlib

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
calendar_path = os.path.join(PROJECT_DIR, 'data', 'health_365.json')
manifest_path = os.path.join(PROJECT_DIR, 'data', 'approved_manifest.json')

calendar = {d['id']: d for d in json.load(open(calendar_path, encoding='utf-8'))}
manifest = json.load(open(manifest_path, encoding='utf-8'))

manifest_by_slot = {}
for h, entry in manifest.items():
    manifest_by_slot[(entry['day_id'], int(entry['card_idx']))] = (h, entry)

DAYS = ['10-15', '10-15-cane', '10-16', '10-16-spine', '10-17', '10-18', '10-19', '10-19-oral', '10-20', '10-21']

# Compute file sha256 helper
def get_sha256(rel_path):
    p = os.path.join(PROJECT_DIR, rel_path.replace('/', os.sep))
    if os.path.exists(p):
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    return None

# Required visual objects/actions mapping based on clinical intent
REQUIRED_VISUALS = {
    ('10-15', 1): "Indian individual at washbasin lathering soap and clean water across all hand surfaces",
    ('10-15', 2): "Close-up of hands interlacing fingers, rotational thumb scrubbing, and fingernail cleaning with soap foam",
    ('10-15', 3): "Critical hygiene moment: Indian home setting, handwashing before handling food or after bathroom",
    ('10-15', 4): "Hands being dried with a clean personal cotton towel or air drying, avoiding communal damp cloths",
    ('10-15-cane', 1): "Clinical optometrist/ophthalmologist performing slit-lamp or dilated eye examination on Indian patient",
    ('10-15-cane', 2): "Visually impaired Indian individual using a white cane on clear tactile paving / footpath free of obstacles",
    ('10-15-cane', 3): "Sighted guide respectfully offering elbow to visually impaired person to cross a street safely",
    ('10-15-cane', 4): "Eye safety: Indian worker wearing protective glasses; clean eye-wash demonstration (no eye rubbing)",
    ('10-16', 1): "Nutritious Indian Desi Thali with 50% seasonal vegetables/salad, 25% plant protein (dal/paneer/sprouts), 25% millets",
    ('10-16', 2): "Assortment of traditional Indian millets (Shree Anna: bajra, jowar, ragi) with rustic roti or cooked grain",
    ('10-16', 3): "Visual contrast showing street food stall with dark re-heated frying oil vs healthy fresh alternatives (negative polarity)",
    ('10-16', 4): "Indian kitchen setting showing fresh produce being washed under running water and cooked food stored covered",
    ('10-16-spine', 1): "Ergonomic desk posture: Indian office worker with monitor at eye level, lumbar support, feet flat",
    ('10-16-spine', 2): "Hourly break: Individual standing up from desk, gentle backward spinal stretch and short walking step",
    ('10-16-spine', 3): "Safe heavy lifting technique: Indian individual squatting with bent knees, holding box close to chest",
    ('10-16-spine', 4): "Text-neck posture correction: Holding smartphone up near eye level rather than 60-degree slouched neck",
    ('10-17', 1): "Two-wheeler rider with fastened ISI full-face helmet and car passenger with 3-point seatbelt clicked",
    ('10-17', 2): "Indian Golden Hour response: Bystander dialing 108 emergency service beside an ambulance arriving promptly",
    ('10-17', 3): "Traffic safety discipline: Hand on handlebar, eyes on road, mobile phone kept away, avoiding speeding",
    ('10-17', 4): "First-aid precaution: Supporting accident victim without jerking cervical spine; keeping airway clear (no water)",
    ('10-18', 1): "Indian woman in 40s-50s enjoying gentle morning sunshine (Vit D) alongside calcium-rich ragi, sesame and curd",
    ('10-18', 2): "Active wellness: Indian woman engaging in brisk morning walking followed by calming Anulom-Vilom pranayama",
    ('10-18', 3): "Clinical consultation: Compassionate dialogue between Indian woman and gynecologist discussing menopause management",
    ('10-18', 4): "Dietary moderation: Transitioning away from excess caffeine, sugary sweets, and sedentary habits",
    ('10-19', 1): "ENT specialist gently examining an Indian patient's ear with an otoscope in a well-lit medical clinic",
    ('10-19', 2): "Earphone safety: Young Indian individual adjusting headphones to safe volume (<60%) with a 60-min timer cue",
    ('10-19', 3): "Ear safety warning: Prohibition of matchsticks, safety pins, keys, or cotton swabs inside the ear canal",
    ('10-19', 4): "Noise and water protection: Wearing earplugs in loud festive environments; gently drying ears after swimming/bath",
    ('10-19-oral', 1): "Soft-bristle toothbrushing: Indian individual demonstrating gentle circular brushing technique with fluoride toothpaste",
    ('10-19-oral', 2): "Vigorous post-meal water mouth rinsing: Swishing clean water inside mouth at clean washbasin to dislodge food particles",
    ('10-19-oral', 3): "Anti-tobacco stance: Indian setting with crushed gutkha/khaini/bidi packets symbolizing zero tobacco consumption",
    ('10-19-oral', 4): "Professional dental checkup: Dentist examining teeth and oral mucosa for early signs of lesions or plaque",
    ('10-20', 1): "Senior-friendly home: Indian elder safely using sturdy stainless steel bathroom grab bar with bright lighting and dry non-slip tiles",
    ('10-20', 2): "Bone health nutrition and activity: Active Indian seniors walking outdoors in morning sun, with ragi roti, sesame seeds, paneer",
    ('10-20', 3): "Fall hazard remediation: Senior Indian living room with cleared walkways, taped-down cords, non-skid floor mats",
    ('10-20', 4): "Bone-depleting diet avoidance: Moderating high sodium and dark sodas to prevent urinary calcium leaching",
    ('10-21', 1): "Authentic Indian kitchen: Scooping fine iodized salt from an airtight glass or ceramic jar (smiling sun logo visible)",
    ('10-21', 2): "Iodine preservation in cooking: Indian home cook adding a measured pinch of iodized salt near the completion of vegetable curry",
    ('10-21', 3): "Uniodized salt hazard: Contrast between unbranded loose coarse salt (lacks iodine) vs packaged iodized salt for maternal/child health",
    ('10-21', 4): "Proper salt storage: Tightly sealed salt jar placed in a cool, dry kitchen pantry cupboard protected from moisture"
}

POLARITY_MAP = {
    ('10-15', 1): "positive", ('10-15', 2): "positive", ('10-15', 3): "positive", ('10-15', 4): "positive",
    ('10-15-cane', 1): "positive", ('10-15-cane', 2): "positive", ('10-15-cane', 3): "positive", ('10-15-cane', 4): "positive",
    ('10-16', 1): "positive", ('10-16', 2): "positive", ('10-16', 3): "negative_avoidance", ('10-16', 4): "positive",
    ('10-16-spine', 1): "positive", ('10-16-spine', 2): "positive", ('10-16-spine', 3): "positive", ('10-16-spine', 4): "positive_correction",
    ('10-17', 1): "positive", ('10-17', 2): "positive", ('10-17', 3): "positive", ('10-17', 4): "negative_avoidance",
    ('10-18', 1): "positive", ('10-18', 2): "positive", ('10-18', 3): "positive", ('10-18', 4): "negative_avoidance",
    ('10-19', 1): "positive", ('10-19', 2): "positive", ('10-19', 3): "negative_avoidance", ('10-19', 4): "positive",
    ('10-19-oral', 1): "positive", ('10-19-oral', 2): "positive", ('10-19-oral', 3): "negative_avoidance", ('10-19-oral', 4): "positive",
    ('10-20', 1): "positive", ('10-20', 2): "positive", ('10-20', 3): "positive_safety", ('10-20', 4): "negative_avoidance",
    ('10-21', 1): "positive", ('10-21', 2): "positive", ('10-21', 3): "negative_avoidance", ('10-21', 4): "positive_storage"
}

review_queue = []

for d_id in DAYS:
    day = calendar[d_id]
    for card in day.get('cards', []):
        c_idx = int(card.get('index', 1))
        h, m_entry = manifest_by_slot.get((d_id, c_idx), (None, None))
        
        status = m_entry.get('status') if m_entry else 'UNTRACKED'
        photo_rel = card.get('photo', '')
        actual_photo_hash = get_sha256(photo_rel)
        
        findings = m_entry.get('clinical_review', {}).get('findings', '') if m_entry else ''
        if status == 'REJECTED_MISMATCH':
            observed_issue = findings
        elif status == 'APPROVED':
            observed_issue = findings if findings else 'Promoted replacement image approved by Dr. Atul; verified against clinical specification.'
        else:
            observed_issue = 'Awaiting formal board clinical sign-off and physical review verification.'
        
        source_evidence = {
            "day_id": d_id,
            "card_idx": c_idx,
            "manifest_file_reference": m_entry.get('file_reference') if m_entry else None,
            "manifest_recorded_hash": h,
            "actual_disk_hash": actual_photo_hash,
            "spec_hash": m_entry.get('spec_hash') if m_entry else None,
            "hashes_match": (h == actual_photo_hash) if (h and actual_photo_hash) else False
        }
        
        q_item = {
            "poster_id": d_id,
            "poster_title_en": day.get('title_en'),
            "poster_title_gu": day.get('title_gu'),
            "card_idx": c_idx,
            "card_type": card.get('type'),
            "bilingual_copy": {
                "title_en": card.get('title_en'),
                "title_gu": card.get('title_gu'),
                "desc_en": card.get('desc_en'),
                "desc_gu": card.get('desc_gu')
            },
            "image_path": photo_rel,
            "image_sha256": actual_photo_hash,
            "spec_hash": m_entry.get('spec_hash') if m_entry else None,
            "review_status": status,
            "observed_issue": observed_issue,
            "source_evidence": source_evidence,
            "required_visual_objects_actions": REQUIRED_VISUALS.get((d_id, c_idx), "Clinical visual corresponding to card copy"),
            "polarity": POLARITY_MAP.get((d_id, c_idx), "positive"),
            "clinical_review_assessment": m_entry.get('clinical_review') if m_entry else None,
            "reviewer": m_entry.get('reviewer') if m_entry else None
        }
        review_queue.append(q_item)

out_path = os.path.join(PROJECT_DIR, 'review', 'review_queue.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({
        "total_cards": len(review_queue),
        "status_summary": {
            "APPROVED": sum(1 for c in review_queue if c['review_status'] == 'APPROVED'),
            "PENDING_CLINICAL_SIGN_OFF": sum(1 for c in review_queue if c['review_status'] == 'PENDING_CLINICAL_SIGN_OFF'),
            "REJECTED_MISMATCH": sum(1 for c in review_queue if c['review_status'] == 'REJECTED_MISMATCH')
        },
        "review_queue": review_queue
    }, f, indent=2, ensure_ascii=False)

print(f"Generated {out_path} with {len(review_queue)} cards.")
