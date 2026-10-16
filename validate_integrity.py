import json
import os
import sys

def main():
    print("Running 365-Day Health Poster Studio Integrity Check...")
    
    # 1. Validate data/health_365.json
    json_path = os.path.join("data", "health_365.json")
    if not os.path.exists(json_path):
        print("FAIL: health_365.json not found")
        sys.exit(1)
        
    with open(json_path, "r", encoding="utf-8") as f:
        cal = json.load(f)
        
    if len(cal) < 365:
        print(f"FAIL: Expected at least 365 posters, got {len(cal)}")
        sys.exit(1)
    print(f"  [PASS] {len(cal)} health observance posters loaded (full 365-day calendar + multi-observance dedicated posters).")
    
    # 2. Check Oct 15 - Oct 21 specifics
    oct_week = ["10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    found = {}
    
    for day in cal:
        day_id = day.get("id")
        if day_id in oct_week:
            found[day_id] = day
            cards = day.get("cards", [])
            if len(cards) != 4:
                print(f"FAIL: Day {day_id} has {len(cards)} cards instead of 4")
                sys.exit(1)
                
            for card in cards:
                photo = card.get("photo")
                if not photo or not os.path.exists(photo):
                    print(f"FAIL: Photo file missing on disk: {photo} for day {day_id}")
                    sys.exit(1)
                    
                prompt = card.get("ai_prompt", "")
                if len(prompt) < 20:
                    print(f"FAIL: AI photo prompt missing or too short for day {day_id}")
                    sys.exit(1)
                    
    if len(found) != 7:
        print(f"FAIL: Expected 7 days in Oct week, got {len(found)}")
        sys.exit(1)
    print("  [PASS] All 7 days (Oct 15 to Oct 21) have 4 cards, valid photo assets on disk, and rich AI prompts.")
    
    # 3. Check App Icons
    for icon in ["icons/icon-192.png", "icons/icon-512.png"]:
        if not os.path.exists(icon):
            print(f"FAIL: Missing icon: {icon}")
            sys.exit(1)
    print("  [PASS] PWA Icons 192x192 and 512x512 exist.")
    
    # 4. Check manifest.json and sw.js
    if not os.path.exists("manifest.json") or not os.path.exists("sw.js"):
        print("FAIL: PWA manifest or service worker missing.")
        sys.exit(1)
    print("  [PASS] PWA manifest.json and sw.js exist.")
    
    print("\nALL HEALTH POSTER INTEGRITY CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
