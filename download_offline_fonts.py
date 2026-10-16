"""
download_offline_fonts.py
-----------------------------------------------------------------------------
Downloads WOFF2 fonts for Noto Sans Gujarati and Plus Jakarta Sans from
Google Fonts and creates local css/fonts.css for full air-gapped offline support.
-----------------------------------------------------------------------------
"""

import os
import re
import urllib.request
import hashlib

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(PROJECT_DIR, "fonts")
CSS_DIR = os.path.join(PROJECT_DIR, "css")
FONTS_CSS_PATH = os.path.join(CSS_DIR, "fonts.css")

os.makedirs(FONTS_DIR, exist_ok=True)
os.makedirs(CSS_DIR, exist_ok=True)

GOOGLE_FONTS_URL = "https://fonts.googleapis.com/css2?family=Noto+Sans+Gujarati:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

print(f"Fetching Google Fonts CSS from: {GOOGLE_FONTS_URL}")
req = urllib.request.Request(GOOGLE_FONTS_URL, headers={"User-Agent": USER_AGENT})
with urllib.request.urlopen(req) as resp:
    css_content = resp.read().decode("utf-8")

blocks = css_content.split("@font-face")
new_blocks = [blocks[0]]

downloaded_count = 0

for b in blocks[1:]:
    m_sub = re.search(r"/\*\s*([^*]+)\s*\*/", b)
    sub = m_sub.group(1).strip() if m_sub else "all"
    
    m_family = re.search(r"font-family:\s*['\"]([^'\"]+)['\"]", b)
    family = m_family.group(1).replace(" ", "_").lower() if m_family else "font"
    
    m_weight = re.search(r"font-weight:\s*(\d+)", b)
    weight = m_weight.group(1) if m_weight else "400"
    
    m_url = re.search(r"url\((https://[^)]+\.woff2)\)", b)
    if not m_url:
        new_blocks.append(b)
        continue
    
    remote_url = m_url.group(1)
    url_hash = hashlib.md5(remote_url.encode("utf-8")).hexdigest()[:8]
    sub_clean = re.sub(r"[^a-zA-Z0-9]", "", sub)
    local_fname = f"{family}_{weight}_{sub_clean}_{url_hash}.woff2"
    local_path = os.path.join(FONTS_DIR, local_fname)
    
    if not os.path.exists(local_path):
        urllib.request.urlretrieve(remote_url, local_path)
        downloaded_count += 1
    
    new_b = b.replace(remote_url, f"../fonts/{local_fname}")
    new_blocks.append(new_b)

new_css = "@font-face".join(new_blocks)
with open(FONTS_CSS_PATH, "w", encoding="utf-8") as f:
    f.write("/* Bundled Offline Fonts for HealthCalendar365 (Air-Gapped PWA) */\n" + new_css)

total_fonts = len(os.listdir(FONTS_DIR))
print(f"Downloaded {downloaded_count} new files. Total fonts in fonts/: {total_fonts}")
print(f"Local fonts stylesheet saved to: {FONTS_CSS_PATH}")
