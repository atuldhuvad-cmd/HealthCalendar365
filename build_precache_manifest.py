"""
build_precache_manifest.py
-----------------------------------------------------------------------------
Derives PRECACHE_ASSETS in sw.js strictly from active, validated references in
data/health_365.json, offline fonts, and core application files.
Supports PNG, WebP, and WOFF2 formats.
Raises ManifestBuildError on failure so callers can handle rollback cleanly.
-----------------------------------------------------------------------------
"""

import json
import os
import re
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SW_PATH = os.path.join(PROJECT_DIR, "sw.js")
JSON_PATH = os.path.join(PROJECT_DIR, "data", "health_365.json")
FONTS_DIR = os.path.join(PROJECT_DIR, "fonts")

CORE_ASSETS = [
    "./",
    "./index.html",
    "./manifest.json",
    "./css/styles.css",
    "./css/fonts.css",
    "./js/app.js",
    "./js/canvas-renderer.js",
    "./js/db.js",
    "./js/calendar-data.js",
    "./data/health_365.json",
    "./icons/icon-192.png",
    "./icons/icon-512.png"
]

class ManifestBuildError(RuntimeError):
    """Raised when precache manifest construction fails."""
    pass

def build_manifest(project_dir=None, raise_on_error=True):
    if isinstance(project_dir, bool):
        raise_on_error = project_dir
        project_dir = None
    if project_dir is None:
        project_dir = PROJECT_DIR

    sw_path = os.path.join(project_dir, "sw.js")
    json_path = os.path.join(project_dir, "data", "health_365.json")
    fonts_dir = os.path.join(project_dir, "fonts")

    if not os.path.exists(sw_path):
        msg = f"[ERROR] sw.js missing at: {sw_path}"
        if raise_on_error:
            raise ManifestBuildError(msg)
        print(msg)
        return False

    if not os.path.exists(json_path):
        msg = f"[ERROR] health_365.json missing at: {json_path}"
        if raise_on_error:
            raise ManifestBuildError(msg)
        print(msg)
        return False

    # 1. Verify core assets exist
    for ca in CORE_ASSETS:
        if ca == "./":
            continue
        rel_path = ca.lstrip("./").replace("/", os.sep)
        full_path = os.path.join(project_dir, rel_path)
        if not os.path.exists(full_path):
            msg = f"[ERROR] Required core asset missing: {ca}"
            if raise_on_error:
                raise ManifestBuildError(msg)
            print(msg)
            return False

    # 2. Add local offline font files (WOFF2) if present
    font_assets = []
    if os.path.exists(fonts_dir):
        for fname in sorted(os.listdir(fonts_dir)):
            if fname.endswith(".woff2"):
                font_assets.append(f"./fonts/{fname}")

    # 3. Extract active image references from dataset
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    referenced_photos = set()
    for day in data:
        for card in day.get("cards", []):
            photo = card.get("photo") or card.get("image")
            if photo:
                # Normalize to ./photos/...
                clean_photo = photo.replace("\\", "/").strip()
                if not clean_photo.startswith("./"):
                    clean_photo = "./" + clean_photo.lstrip("/")
                referenced_photos.add(clean_photo)

    # 4. Verify all active image references exist on disk and support png/webp
    missing = []
    valid_photos = []
    for p in sorted(referenced_photos):
        rel_path = p.lstrip("./").replace("/", os.sep)
        full_path = os.path.join(project_dir, rel_path)
        if not os.path.exists(full_path) or os.path.getsize(full_path) == 0:
            missing.append(p)
        else:
            valid_photos.append(p)

    if missing:
        msg = f"[ERROR] {len(missing)} referenced photo assets are missing on disk: {missing[:5]}"
        if raise_on_error:
            raise ManifestBuildError(msg)
        print(msg)
        return False

    # 5. Assemble final manifest
    all_assets = CORE_ASSETS + font_assets + valid_photos
    formatted_assets = ",\n".join(f"  '{a}'" for a in all_assets)

    with open(sw_path, "r", encoding="utf-8") as f:
        sw_content = f.read()

    pattern = re.compile(r"const PRECACHE_ASSETS = \[.*?\];", re.DOTALL)
    replacement = f"const PRECACHE_ASSETS = [\n{formatted_assets}\n];"

    if not pattern.search(sw_content):
        msg = "[ERROR] PRECACHE_ASSETS pattern not found in sw.js"
        if raise_on_error:
            raise ManifestBuildError(msg)
        print(msg)
        return False

    new_content = pattern.sub(replacement, sw_content)

    with open(sw_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[OK] Successfully built precache manifest:")
    print(f"  - Core Application Assets: {len(CORE_ASSETS)}")
    print(f"  - Local Offline Fonts (WOFF2): {len(font_assets)}")
    print(f"  - Active Referenced Photos: {len(valid_photos)}")
    print(f"  - Total Precached Assets: {len(all_assets)}")
    return True

if __name__ == "__main__":
    try:
        build_manifest(project_dir=PROJECT_DIR, raise_on_error=True)
    except ManifestBuildError as err:
        print(err)
        sys.exit(1)
