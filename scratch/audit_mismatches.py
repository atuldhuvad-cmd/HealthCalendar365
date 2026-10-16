"""
Comprehensive Audit of Image-to-Text Mismatches in HealthCalendar365
Finds:
1. Intra-poster duplicate images (cards in same poster sharing identical image content)
2. Semantic mismatches in October spotlight week
3. Generic category placeholder fallbacks across the 368 posters
"""

import json
import os
import hashlib
from collections import defaultdict

PROJECT_DIR = r"D:\HealthCalendar365"
JSON_PATH = os.path.join(PROJECT_DIR, "data", "health_365.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    cal = json.load(f)

print("=" * 80)
print("   HEALTHCALENDAR365: COMPREHENSIVE IMAGE-TO-TEXT MISMATCH AUDIT")
print("=" * 80)

def file_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# 1. Audit October 15-21 Spotlight Posters
print("\n--- SECTION 1: OCTOBER SPOTLIGHT WEEK POSTERS (OCT 15 - OCT 21) ---")
oct_posters = [d for d in cal if d.get("month") == 10 and 15 <= d.get("day", 0) <= 21]

for p in oct_posters:
    pid = p.get("id")
    p_title = p.get("title_en")
    cards = p.get("cards", [])
    
    # Check for duplicate hashes among cards
    hashes = {}
    dups = defaultdict(list)
    for c in cards:
        idx = c.get("index")
        photo_rel = c.get("photo", "")
        photo_full = os.path.join(PROJECT_DIR, photo_rel)
        h = file_hash(photo_full)
        if h:
            dups[h].append((idx, c.get("title_en"), photo_rel))
    
    has_dup = any(len(v) > 1 for v in dups.values())
    status = "[MISMATCH / DUPLICATE FOUND]" if has_dup else "[CLEAN - UNIQUE]"
    print(f"\n{status} {pid}: {p_title}")
    
    for c in cards:
        idx = c.get("index")
        photo_rel = c.get("photo", "")
        print(f"  Card #{idx}: '{c.get('title_en')}' -> {photo_rel}")
        
    if has_dup:
        print("  >> Duplicate Groups Detected:")
        for h, group in dups.items():
            if len(group) > 1:
                indices = [f"Card #{g[0]} ('{g[1]}')" for g in group]
                print(f"     * Same Image used for: {' AND '.join(indices)}")

# 2. Audit All 368 Posters for Duplicates & Placeholders
print("\n" + "=" * 80)
print("--- SECTION 2: GLOBAL 365-DAY CALENDAR MISMATCH SUMMARY ---")
total_posters = len(cal)
posters_with_dups = []
posters_with_placeholders = []

for p in cal:
    pid = p.get("id")
    p_title = p.get("title_en")
    cards = p.get("cards", [])
    
    card_photos = [c.get("photo", "") for c in cards]
    card_hashes = [file_hash(os.path.join(PROJECT_DIR, ph)) for ph in card_photos]
    
    # Check duplicates
    if len(set(card_hashes)) < len(card_hashes):
        posters_with_dups.append((pid, p_title))
        
    # Check generic placeholders (cat_*)
    if any("cat_" in ph for ph in card_photos):
        posters_with_placeholders.append((pid, p_title))

print(f"Total Posters Audited: {total_posters}")
print(f"Posters with duplicate images across cards: {len(posters_with_dups)}")
print(f"Posters using generic 'cat_*' placeholder images: {len(posters_with_placeholders)}")
