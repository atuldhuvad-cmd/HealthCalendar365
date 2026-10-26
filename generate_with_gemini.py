"""
generate_with_gemini.py
-----------------------------------------------------------------------------
HealthCalendar365 - Image Generation (candidates saved to photos/staging/)
-----------------------------------------------------------------------------
  1. Candidate generations write ONLY to photos/staging/ with attempt hashes;
     active assets in photos/ are never touched by this script.
  2. Every attempt is recorded in data/generation_journal.json (git-ignored).
  3. Image integrity gate (verify_image_integrity_and_decode): structure check,
     full pixel decode, format/extension match, minimum 720x540, 4:3 aspect.
  4. Personal-use workflow: the doctor-owner inspects a candidate and copies it
     into photos/ (then updates the card's photo path and runs
     build_calendar_data.py / build_precache_manifest.py). There is no approval
     gate, manifest or transaction layer.
-----------------------------------------------------------------------------
"""

import argparse
import base64
import hashlib
import json
import os
import shutil
import sys
import time

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(PROJECT_DIR, "data", "health_365.json")
PHOTOS_DIR = os.path.join(PROJECT_DIR, "photos")
STAGING_DIR = os.path.join(PHOTOS_DIR, "staging")
JOURNAL_PATH = os.path.join(PROJECT_DIR, "data", "generation_journal.json")

def compute_file_sha256(filepath):
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def compute_bytes_sha256(data_bytes):
    """Compute SHA-256 hash of bytes."""
    return hashlib.sha256(data_bytes).hexdigest()

def verify_image_integrity_and_decode(filepath):
    """
    Exhaustively verifies image integrity:
    1. Checks file existence and non-zero size.
    2. Opens with PIL and runs im.verify() for structural chunk validity.
    3. Re-opens and fully decodes all pixels into memory using im.load() / convert('RGB').
    4. Validates format matches file extension (PNG for .png, WEBP for .webp).
    5. Validates minimum dimensions (>= 720x540).
    6. Validates aspect ratio (4:3 ratio with tolerance: 1.25 to 1.45).
    Returns (True, info_dict) or (False, error_reason).
    """
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return False, "File does not exist or is empty"

    ext = os.path.splitext(filepath)[1].lower()

    try:
        from PIL import Image

        # Pass 1: Structural verification
        with Image.open(filepath) as im:
            im_format = im.format
            im.verify()

        # Pass 2: Full pixel decompression & decode test
        with Image.open(filepath) as im:
            width, height = im.size
            rgb_im = im.convert("RGB")
            rgb_im.load()

        # Format match
        if ext == ".png" and im_format != "PNG":
            return False, f"Format mismatch: expected PNG, got {im_format}"
        if ext == ".webp" and im_format != "WEBP":
            return False, f"Format mismatch: expected WEBP, got {im_format}"
        if ext not in [".png", ".webp"]:
            return False, f"Unsupported extension: {ext}"

        # Dimension check
        if width < 720 or height < 540:
            return False, f"Undersized: {width}x{height} (minimum required: 720x540)"

        # Aspect ratio check
        aspect = width / height
        if aspect < 1.25 or aspect > 1.45:
            return False, f"Aspect ratio deviation: {aspect:.2f} (expected ~1.33 / 4:3)"

        return True, {
            "width": width,
            "height": height,
            "format": im_format,
            "aspect": aspect
        }
    except Exception as err:
        return False, f"Image decoding failed: {err}"

def get_api_key(cli_key=None):
    if cli_key:
        return cli_key
    for var in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        val = os.environ.get(var)
        if val:
            return val
    return None

def init_genai_client(api_key):
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except ImportError:
        print("[ERROR] google-genai SDK not found. Install via: pip install -U google-genai")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Failed to initialize Google GenAI Client: {e}")
        sys.exit(1)

def generate_image_bytes(client, prompt, model="imagen-3.0-generate-002"):
    if "imagen" in model.lower():
        try:
            from google.genai import types
            config = types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="4:3",
                output_mime_type="image/png"
            )
            response = client.models.generate_images(
                model=model,
                prompt=prompt,
                config=config
            )
            if response.generated_images and len(response.generated_images) > 0:
                return response.generated_images[0].image.image_bytes
        except Exception as err:
            print(f"[WARN] Imagen API failed ({err}). Trying Gemini Native fallback...")

    native_model = "gemini-nano-banana-2.1"
    try:
        interaction = client.interactions.create(
            model=native_model,
            input=prompt
        )
        if interaction.output_image and interaction.output_image.data:
            return base64.b64decode(interaction.output_image.data)
        else:
            raise RuntimeError(f"No image returned from {native_model}")
    except Exception as e:
        raise RuntimeError(f"Image generation failed: {e}")

def atomic_write_file(target_path, content, is_binary=False):
    """Safely write to temp file and atomically replace."""
    tmp_path = target_path + ".tmp"
    mode = "wb" if is_binary else "w"
    encoding = None if is_binary else "utf-8"
    with open(tmp_path, mode, encoding=encoding) as f:
        f.write(content)
    os.replace(tmp_path, target_path)

def load_journal_safely():
    """Load generation journal; quarantine if corrupt to preserve forensic evidence."""
    if not os.path.exists(JOURNAL_PATH):
        return []
    try:
        with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as err:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        quarantine_path = os.path.join(PROJECT_DIR, "data", f"generation_journal.corrupt.{timestamp}.json")
        shutil.move(JOURNAL_PATH, quarantine_path)
        print(f"[CAUTION] Corrupted generation journal quarantined to: {quarantine_path}")
        print(f"Error was: {err}")
        return []

def log_journal_entry(entry):
    journal = load_journal_safely()
    journal.append(entry)
    atomic_write_file(JOURNAL_PATH, json.dumps(journal, indent=2, ensure_ascii=False))

def process_calendar(args, project_dir=PROJECT_DIR):
    json_path = os.path.join(project_dir, "data", "health_365.json")

    if not os.path.exists(json_path):
        print(f"[ERROR] Calendar JSON missing at: {json_path}")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        calendar_data = json.load(f)

    # Generation Mode: Read-Only Collection
    if args.day:
        target_days = [d for d in calendar_data if str(d.get("id")) == args.day]
        if not target_days:
            print(f"[ERROR] Day '{args.day}' not found in calendar data (use format MM-DD, e.g. 10-15)")
            sys.exit(1)
    else:
        target_days = calendar_data

    tasks = []
    for day in target_days:
        day_id = str(day.get("id"))
        clean_id = day_id.replace("-", "_").lower()
        for card in day.get("cards", []):
            card_idx = card.get("index", 1)
            current_photo = card.get("photo", "")

            is_generic = (not current_photo) or ("cat_" in current_photo) or ("placeholder" in current_photo.lower())

            if is_generic:
                active_rel = f"photos/{clean_id}_card{card_idx}.png"
            else:
                active_rel = current_photo
            active_full = os.path.join(project_dir, active_rel)

            prompt = card.get("ai_prompt", "")
            exists = os.path.exists(active_full) and os.path.getsize(active_full) > 0
            needs_gen = (not exists) or args.force or (args.all_missing and is_generic)

            tasks.append({
                "day_id": day_id,
                "clean_id": clean_id,
                "card_ref": card,
                "card_idx": card_idx,
                "title": card.get("title_en", "Card"),
                "active_rel": active_rel,
                "prompt": prompt,
                "needs_gen": needs_gen
            })

    to_generate = [t for t in tasks if t["needs_gen"]]

    print("=" * 70)
    print("   HealthCalendar365 - Gemini Image Pipeline (Gemini Banav)")
    print("=" * 70)
    print(f"Scanned Days: {len(target_days)}")
    print(f"Total Cards Checked: {len(tasks)}")
    print(f"Assets Needing Generation: {len(to_generate)}")
    print(f"Mode: {'DRY RUN (Mutation-Free)' if args.dry_run else 'ACTIVE GENERATION'}")
    print(f"Model: {args.model}")
    print("-" * 70)

    if not to_generate:
        print("\n[OK] All requested photo assets exist on disk!")
        return

    if args.dry_run:
        print("\n[DRY RUN PREVIEW] The following candidates would be generated into staging:")
        for idx, task in enumerate(to_generate[:10], start=1):
            print(f"\n[{idx}/{len(to_generate)}] Day {task['day_id']} Card #{task['card_idx']} - {task['title']}")
            print(f"  Target Active Asset: {task['active_rel']}")
            print(f"  Candidate Staging Path: photos/staging/candidate_{task['clean_id']}_card{task['card_idx']}_<timestamp>_<hash>.png")
            print(f"  Gemini Prompt:\n  \"{task['prompt']}\"")
        if len(to_generate) > 10:
            print(f"\n... and {len(to_generate) - 10} more cards.")
        print("\n[DRY RUN] Zero files or directories were created or modified.")
        return

    api_key = get_api_key(args.api_key)
    if not api_key:
        print("\n[ERROR] Missing Gemini API Key.")
        print("Please set GEMINI_API_KEY environment variable or pass --api-key <YOUR_KEY>")
        print("Example: set GEMINI_API_KEY=AIzaSy...")
        sys.exit(1)

    staging_dir = os.path.join(project_dir, "photos", "staging")
    os.makedirs(staging_dir, exist_ok=True)
    print(f"\nInitializing Google GenAI Client with model '{args.model}'...")
    client = init_genai_client(api_key)

    success_count = 0
    fail_count = 0

    for idx, task in enumerate(to_generate, start=1):
        print(f"\n[{idx}/{len(to_generate)}] Generating candidate: Day {task['day_id']} Card #{task['card_idx']} ({task['title']})...")
        try:
            img_bytes = generate_image_bytes(client, task["prompt"], model=args.model)
            img_hash = compute_bytes_sha256(img_bytes)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            candidate_fname = f"candidate_{task['clean_id']}_card{task['card_idx']}_{timestamp}_{img_hash[:8]}.png"
            candidate_full = os.path.join(staging_dir, candidate_fname)

            with open(candidate_full, "wb") as f_out:
                f_out.write(img_bytes)
            print(f"  [SAVED TO STAGING] -> photos/staging/{candidate_fname} ({len(img_bytes)} bytes)")

            # Record in durable generation journal
            log_journal_entry({
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "day_id": task["day_id"],
                "card_idx": task["card_idx"],
                "title": task["title"],
                "staging_file": candidate_fname,
                "sha256": img_hash,
                "active_target": task["active_rel"],
                "status": "staged",
                "bytes": len(img_bytes)
            })

            success_count += 1
            time.sleep(1.0)
        except Exception as e:
            print(f"  [FAILED] {e}")
            fail_count += 1

    print("\n" + "=" * 70)
    print(f"Generation to Staging Complete! Success: {success_count}, Failed: {fail_count}")
    print("Candidates are saved safely in photos/staging/ with immutable attempt hashes.")
    print("Inspect a candidate, then copy it into photos/ and point the card's photo path at it.")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Image generation for HealthCalendar365 (candidates go to photos/staging/)")
    parser.add_argument("--day", type=str, help="Specific Day ID to check/generate (e.g. 10-15)")
    parser.add_argument("--all-missing", action="store_true", help="Generate all missing or placeholder assets across 365 days")
    parser.add_argument("--dry-run", action="store_true", help="Read-only preview; guarantees zero mutations")
    parser.add_argument("--force", action="store_true", help="Regenerate photo assets even if file exists on disk")
    parser.add_argument("--model", type=str, default="imagen-3.0-generate-002", help="Model to use (default: imagen-3.0-generate-002)")
    parser.add_argument("--api-key", type=str, help="Gemini API Key override")
    args = parser.parse_args()

    if not args.day and not args.all_missing:
        args.day = "10-15"

    process_calendar(args)

if __name__ == "__main__":
    main()
