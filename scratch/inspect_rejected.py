import json

data = json.load(open('scratch/cards_40_dump.json', encoding='utf-8'))
lines = []
for day in data:
    for c in day['cards']:
        m = c['manifest_entry']
        if m and m.get('status') == 'REJECTED_MISMATCH':
            lines.append("=" * 60)
            lines.append(f"REJECTED: Day {day['id']} Card {c['index']} [{c['type']}]")
            lines.append("=" * 60)
            lines.append(f"Day Title EN: {day['title_en']}")
            lines.append(f"Day Title GU: {day['title_gu']}")
            lines.append(f"Title EN: {c['title_en']}")
            lines.append(f"Title GU: {c['title_gu']}")
            lines.append(f"Desc EN: {c['desc_en']}")
            lines.append(f"Desc GU: {c['desc_gu']}")
            lines.append(f"Current Photo: {c['photo']}")
            lines.append(f"AI Prompt: {c['ai_prompt']}")
            lines.append(f"Manifest File Ref: {m.get('file_reference')}")
            lines.append(f"Findings: {m.get('clinical_review', {}).get('findings')}")
            lines.append(f"Visual Concordance: {m.get('clinical_review', {}).get('visual_concordance')}")
            lines.append(f"Cultural Authenticity: {m.get('clinical_review', {}).get('cultural_authenticity')}")
            lines.append(f"Polarity Match: {m.get('clinical_review', {}).get('polarity_match')}")
            lines.append(f"Safety Equipment: {m.get('clinical_review', {}).get('safety_equipment_check')}")
            lines.append(f"Spec Hash: {m.get('spec_hash')}")
            lines.append("")

with open('scratch/rejected_inspection.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"Wrote {len(lines)} lines to scratch/rejected_inspection.txt")
