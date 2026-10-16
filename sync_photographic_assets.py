"""
Downloads all 51 authentic photographic artwork sprite sheets from GitHub repository
into D:/Health-Message-/artwork/ and D:/HealthCalendar365/artwork/
"""

import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ARTWORK_FILES = [
    "art-alcohol-v1.png", "art-anaemia-v1.png", "art-blood-pressure-v1.png", "art-blood-v1.png", 
    "art-brain-v1.png", "art-cancer-v1.png", "art-child-health-v1.png", "art-diabetes-v1.png", 
    "art-eye-health-v1.png", "art-first-aid-v1.png", "art-food-safety-v1.png", "art-hand-hygiene-v1.png", 
    "art-healthy-ageing-v1.png", "art-hearing-v1.png", "art-heart-v1.png", "art-heat-health-v1.png", 
    "art-hepatitis-v1.png", "art-kidney-v1.png", "art-malaria-dengue-v1.png", "art-maternal-health-v1.png", 
    "art-men-health-v1.png", "art-mental-v1.png", "art-newborn-v1.png", "art-nutrition-v1.png", 
    "art-occupational-health-v1.png", "art-oral-health-v1.png", "art-organ-donation-v1.png", 
    "art-respiratory-health-v1.png", "art-road-safety-v1.png", "art-sanitation-v1.png", "art-sleep-v1.png", 
    "art-tobacco-v1.png", "art-tuberculosis-v1.png", "art-vaccination-v1.png", "art-water-v1.png", 
    "art-women-health-v1.png", "art-yoga-v1.png", "art-festival-diwali-v1.png", "art-festival-diwali-v2.png", 
    "art-festival-holi-v1.png", "art-festival-janmashtami-v1.png", "art-festival-navratri-v1.png", 
    "art-festival-navratri-v2.png", "art-gujarat-culture-v1.png", "art-gujarat-culture-v2.png",
    "art-gujarat-foundation-v1.png", "art-national-civic-v1.png", "art-women-leadership-v1.png", 
    "art-environment-stewardship-v1.png", "art-global-peace-v1.png", "art-epidemic-preparedness-v1.png"
]

BASE_URL = "https://raw.githubusercontent.com/atuldhuvad-cmd/Health-Message-/main/artwork/"

DEST_DIRS = [
    r"D:\Health-Message-\artwork",
    r"D:\HealthCalendar365\artwork"
]

for d in DEST_DIRS:
    os.makedirs(d, exist_ok=True)

def download_file(filename):
    url = BASE_URL + filename
    target1 = os.path.join(DEST_DIRS[0], filename)
    target2 = os.path.join(DEST_DIRS[1], filename)
    
    # Download to target1 if not present
    if not os.path.exists(target1) or os.path.getsize(target1) == 0:
        try:
            urllib.request.urlretrieve(url, target1)
        except Exception as e:
            return f"[ERROR] Failed {filename}: {e}"
            
    # Copy to target2 if not present
    if not os.path.exists(target2) or os.path.getsize(target2) == 0:
        try:
            with open(target1, 'rb') as f_in, open(target2, 'wb') as f_out:
                f_out.write(f_in.read())
        except Exception as e:
            return f"[ERROR] Copy {filename}: {e}"
            
    return f"[OK] {filename} ({os.path.getsize(target1)} bytes)"

print(f"Starting parallel download of {len(ARTWORK_FILES)} photographic artwork files...")
with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(download_file, ARTWORK_FILES))

for r in results:
    print(r)

print("\nAll photographic artwork successfully synchronized!")
