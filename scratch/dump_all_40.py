import json

data = json.load(open('scratch/cards_40_dump.json', encoding='utf-8'))
lines = []
for day in data:
    lines.append("=" * 70)
    lines.append(f"DAY ID: {day['id']} | Date: {day['date']}")
    lines.append(f"Title EN: {day['title_en']}")
    lines.append(f"Title GU: {day['title_gu']}")
    lines.append(f"Org EN:   {day['org_en']}")
    lines.append(f"Org GU:   {day['org_gu']}")
    lines.append("-" * 70)
    for c in day['cards']:
        m = c['manifest_entry']
        status = m.get('status') if m else 'NONE'
        lines.append(f"  Card {c['index']} [{c['type']}] - Status: {status}")
        lines.append(f"    Title EN: {c['title_en']}")
        lines.append(f"    Title GU: {c['title_gu']}")
        lines.append(f"    Desc EN:  {c['desc_en']}")
        lines.append(f"    Desc GU:  {c['desc_gu']}")
        lines.append(f"    Photo:    {c['photo']}")
        lines.append(f"    Hash:     {c.get('manifest_hash')}")
        lines.append(f"    SpecHash: {m.get('spec_hash') if m else 'N/A'}")
        if m and m.get('clinical_review'):
            cr = m['clinical_review']
            lines.append(f"    QA: VC={cr.get('visual_concordance')} CA={cr.get('cultural_authenticity')} PM={cr.get('polarity_match')} SEC={cr.get('safety_equipment_check')}")
            lines.append(f"    Findings: {cr.get('findings')}")
    lines.append("")

with open('scratch/all_40_cards_detail.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"Wrote {len(lines)} lines to scratch/all_40_cards_detail.txt")
