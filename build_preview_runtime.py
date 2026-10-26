"""
build_preview_runtime.py
-----------------------------------------------------------------------------
Deterministic preview runtime builder for HealthCalendar365.
Parses PRECACHE_ASSETS from sw.js and mirrors only what the app actually
serves into a clean target directory (default: build/preview-runtime).

Enforces:
1. Precache integrity: fails loudly and exits nonzero if any precache asset is missing.
2. Complete isolation: never copies .git, review/, scratch/, etc.
3. Cryptographic parity: verifies every copied destination file is byte-identical (SHA-256).
4. Idempotency: safe to re-run at any time.
-----------------------------------------------------------------------------
"""

import argparse
import hashlib
import os
import re
import shutil
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TARGET_DIR = os.path.join(PROJECT_DIR, "build", "preview-runtime")


def sha256_file(filepath):
    """Compute SHA-256 hexadecimal digest of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_asset_path(raw_asset):
    """
    Normalize an asset path string from sw.js.
    './' -> '.' (represents root directory)
    './index.html' -> 'index.html'
    'css/styles.css' -> 'css/styles.css'
    """
    cleaned = raw_asset.strip().strip("'\"").strip()
    if cleaned in (".", "./", ".\\"):
        return "."
    if cleaned.startswith("./") or cleaned.startswith(".\\"):
        cleaned = cleaned[2:]
    return os.path.normpath(cleaned).replace("\\", "/")


def parse_precache_assets(sw_path):
    """Extract PRECACHE_ASSETS array elements from sw.js."""
    if not os.path.isfile(sw_path):
        print(f"[FATAL ERROR] sw.js not found at: {sw_path}")
        sys.exit(1)

    with open(sw_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"const\s+PRECACHE_ASSETS\s*=\s*\[([\s\S]*?)\];", content)
    if not match:
        print(f"[FATAL ERROR] 'const PRECACHE_ASSETS = [...];' pattern not found in {sw_path}")
        sys.exit(1)

    raw_entries = match.group(1).split(",")
    assets = []
    for entry in raw_entries:
        cleaned = entry.strip().strip("'\"").strip()
        if cleaned:
            assets.append(cleaned)

    if not assets:
        print(f"[FATAL ERROR] PRECACHE_ASSETS array in {sw_path} is empty.")
        sys.exit(1)

    return assets


def build_runtime(source_dir=None, target_dir=None):
    source_dir = os.path.abspath(source_dir or PROJECT_DIR)
    target_dir = os.path.abspath(target_dir or DEFAULT_TARGET_DIR)

    sw_source_path = os.path.join(source_dir, "sw.js")

    print("=" * 65)
    print("   HealthCalendar365 - Build Preview Runtime")
    print("=" * 65)
    print(f"Source Directory: {source_dir}")
    print(f"Target Directory: {target_dir}\n")

    # 1. Parse PRECACHE_ASSETS from sw.js
    precache_assets = parse_precache_assets(sw_source_path)
    total_precache = len(precache_assets)
    print(f"[+] Parsed PRECACHE_ASSETS from sw.js: {total_precache} entries.")

    # 2. Check for missing assets in source
    missing = []
    file_assets_to_copy = []

    for raw_asset in precache_assets:
        norm = normalize_asset_path(raw_asset)
        if norm == ".":
            # Root directory representation
            if not os.path.isdir(source_dir):
                missing.append(raw_asset)
        else:
            src_file = os.path.join(source_dir, norm)
            if not os.path.isfile(src_file):
                missing.append(raw_asset)
            else:
                file_assets_to_copy.append(norm)

    if not os.path.isfile(sw_source_path):
        missing.append("sw.js")

    if missing:
        print(f"\n[FATAL ERROR] {len(missing)} precache asset(s) missing from source!")
        for m in missing:
            print(f"  [MISSING] {m}")
        print("\nAborting build: cache.addAll() is atomic. A single missing asset")
        print("causes service-worker installation to fail completely, breaking offline.")
        sys.exit(1)

    print(f"[+] Source verification: {total_precache} precache entries found (0 missing).")

    # 3. Prepare target directory
    os.makedirs(target_dir, exist_ok=True)

    # All expected relative files in target
    expected_rel_files = set(file_assets_to_copy)
    expected_rel_files.add("sw.js")

    # Copy sw.js
    shutil.copy2(sw_source_path, os.path.join(target_dir, "sw.js"))

    # Copy all precache file assets
    for rel_file in file_assets_to_copy:
        src_path = os.path.join(source_dir, rel_file)
        dst_path = os.path.join(target_dir, rel_file)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(src_path, dst_path)

    # Prune any extraneous files in target directory to prevent drift
    removed_count = 0
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, target_dir).replace("\\", "/")
            if rel_path not in expected_rel_files:
                os.remove(full_path)
                removed_count += 1
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

    if removed_count > 0:
        print(f"[+] Pruned {removed_count} extraneous file(s) from target mirror.")

    print(f"[+] Copied {len(expected_rel_files)} runtime files to {target_dir}.")

    # 4. Verify cryptographic SHA-256 parity between source and destination
    print("[+] Verifying destination SHA-256 checksums against source...")
    hash_matches = 0
    hash_mismatches = []

    for rel_file in sorted(expected_rel_files):
        src_file = os.path.join(source_dir, rel_file)
        dst_file = os.path.join(target_dir, rel_file)

        if not os.path.isfile(dst_file):
            hash_mismatches.append((rel_file, "Destination file missing"))
            continue

        src_hash = sha256_file(src_file)
        dst_hash = sha256_file(dst_file)

        if src_hash == dst_hash:
            hash_matches += 1
        else:
            hash_mismatches.append((rel_file, f"Hash mismatch: src={src_hash} dst={dst_hash}"))

    total_comparisons = len(expected_rel_files)

    print("-" * 65)
    print("Precache Verification Summary:")
    print(f"  - Precache entries parsed: {total_precache}")
    print(f"  - Missing source entries:  0")
    print(f"  - Files in preview mirror: {total_comparisons} ({len(file_assets_to_copy)} precache assets + sw.js)")
    print(f"  - SHA-256 comparisons:     {hash_matches}/{total_comparisons} PASS ({len(hash_mismatches)} failed)")
    print("-" * 65)

    if hash_mismatches:
        print("\n[FATAL ERROR] SHA-256 verification failed for the following file(s):")
        for f, err in hash_mismatches:
            print(f"  - {f}: {err}")
        sys.exit(1)

    print("[PASS] All precache entries verified and destination is byte-identical.")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Deterministic preview runtime builder for HealthCalendar365."
    )
    parser.add_argument(
        "--source",
        default=PROJECT_DIR,
        help="Source project directory (default: project root)"
    )
    parser.add_argument(
        "--target",
        "--dest",
        dest="target",
        default=DEFAULT_TARGET_DIR,
        help="Target preview runtime directory (default: build/preview-runtime)"
    )
    args = parser.parse_args()
    build_runtime(args.source, args.target)


if __name__ == "__main__":
    main()
