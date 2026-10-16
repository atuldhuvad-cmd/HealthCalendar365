import json
import re
import os
from collections import Counter, defaultdict

def analyze():
    # 1. Read js/calendar-data.js
    with open('js/calendar-data.js', 'r', encoding='utf-8') as f:
        js_text = f.read()

    # Extract all calendar entries
    # The file defines window.CALENDAR_DATA = [ ... ];
    # Let's extract JSON or parse using regex
    pattern = re.compile(r'\{[^{}]*"id":\s*(\d+)[^{}]*"photo":\s*"([^"]+)"', re.DOTALL)
    
    # Let's parse with a more robust regex or direct JSON extraction
    m = re.search(r'window\.CALENDAR_DATA\s*=\s*(\[.*\]);?\s*$', js_text, re.DOTALL)
    if m:
        data = json.loads(m.group(1))
    else:
        # Fallback to json file if data matches
        with open('data/health_365.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

    print(f"Loaded {len(data)} posters from calendar data.")

    # Tally photos
    photo_usage = defaultdict(list) # photo_path -> list of (id, title_en, card_idx, card_title)
    poster_photos = []

    for entry in data:
        p_id = entry.get('id')
        m_num = entry.get('month')
        d_num = entry.get('day')
        title = entry.get('title_en', '')
        cards = entry.get('cards', [])
        
        c_photos = []
        for idx, card in enumerate(cards):
            p = card.get('photo') or card.get('image') or ''
            c_photos.append(p)
            card_title = card.get('title_en') or card.get('heading_en') or ''
            photo_usage[p].append((p_id, f"{m_num:02d}-{d_num:02d}", title, idx+1, card_title))
        
        poster_photos.append({
            'id': p_id,
            'date': f"{m_num:02d}-{d_num:02d}",
            'title': title,
            'photos': c_photos
        })

    # Summary of photo frequencies
    print(f"\nUnique photo paths referenced: {len(photo_usage)}")
    
    # Generic category placeholders
    category_placeholders = [p for p in photo_usage if p.startswith('photos/cat_') or 'placeholder' in p.lower()]
    print(f"\nCategory placeholder photos ({len(category_placeholders)} files):")
    cat_usage_total = 0
    for p in sorted(category_placeholders):
        count = len(photo_usage[p])
        cat_usage_total += count
        print(f"  {p}: used {count} times")
    print(f"Total cards using generic 'cat_' placeholders: {cat_usage_total} cards")

    # Specific photo paths (non-cat_)
    specific_photos = [p for p in photo_usage if not p.startswith('photos/cat_')]
    print(f"\nSpecific photos ({len(specific_photos)} files):")
    for p in sorted(specific_photos):
        count = len(photo_usage[p])
        print(f"  {p}: used {count} times across:")
        for u in photo_usage[p][:3]:
            print(f"     - [ID {u[0]} {u[1]} {u[2]}] Card {u[3]}: {u[4]}")
        if count > 3:
            print(f"     ... and {count-3} more")

    # Check for missing files on disk
    missing = []
    existing = []
    for p in photo_usage:
        if not p:
            continue
        full_path = os.path.join(os.getcwd(), p.replace('/', os.sep))
        if not os.path.exists(full_path):
            missing.append(p)
        else:
            existing.append(p)
    
    print(f"\nMissing files on disk: {len(missing)}")
    for m in missing:
        print(f"  MISSING: {m} (used {len(photo_usage[m])} times)")

if __name__ == '__main__':
    analyze()
