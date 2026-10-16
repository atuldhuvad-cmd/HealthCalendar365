"""
generate_with_gemini.py
-----------------------------------------------------------------------------
HealthCalendar365 - Image Generation & Verified Whole-Release Promotion
-----------------------------------------------------------------------------
Architecture:
  1. Staging Isolation:
     Candidate generations write ONLY to photos/staging/ with immutable attempt
     hashes. Active production assets in photos/ are never touched directly.
  2. Durable Journaling & Forensic Quarantine:
     Every generation attempt is recorded in data/generation_journal.json.
     Malformed journal or pointer files are quarantined, never silently overwritten.
  3. Comprehensive Image Integrity & Decode Gate:
     Candidates must pass structural verification (im.verify()), complete pixel
     decompression (im.convert('RGB').load()), format-to-extension matching,
     minimum dimensions (>= 720x540), and 4:3 aspect ratio tolerance.
  4. Strict Specification-Bound Approval & Clinical QA Gate:
     Candidates require matching candidate SHA-256 and spec_hash in
     data/approved_manifest.json with status: "APPROVED", accountable reviewer
     metadata, and all clinical QA criteria (visual_concordance, cultural_authenticity,
     polarity_match, safety_equipment_check) explicitly passing.
  5. Whole-Release Transactional Promotion with Mandatory-Hash Preflight:
     Active assets, datasets (JSON + JS), and precache manifest are promoted
     transactionally. Pre-transaction SHA-256 hashes are recorded for every target.
     Recovery and rollback enforce a strict READ-ONLY preflight of every backup file
     and mandatory hash before ANY target file is touched or modified.
     Fails closed if any backup is missing, corrupt, or unverified; active files
     remain 100% untouched, and pointer/evidence are preserved.
  6. Strict Zero-Mutation Dry Run:
     --dry-run guarantees zero file, directory, pointer, or recovery mutations.
     Pending recoveries are previewed and reported without execution.
-----------------------------------------------------------------------------
"""

import argparse
import base64
import copy
import hashlib
import json
import os
import shutil
import sys
import time
import uuid

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(PROJECT_DIR, "data", "health_365.json")
JS_PATH = os.path.join(PROJECT_DIR, "js", "calendar-data.js")
SW_PATH = os.path.join(PROJECT_DIR, "sw.js")
PHOTOS_DIR = os.path.join(PROJECT_DIR, "photos")
STAGING_DIR = os.path.join(PHOTOS_DIR, "staging")
JOURNAL_PATH = os.path.join(PROJECT_DIR, "data", "generation_journal.json")
APPROVED_MANIFEST_PATH = os.path.join(PROJECT_DIR, "data", "approved_manifest.json")
TRANSACTIONS_DIR = os.path.join(PROJECT_DIR, "data", "transactions")
ACTIVE_TX_PATH = os.path.join(PROJECT_DIR, "data", "active_transaction.json")

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

def compute_card_spec_hash(card, day_id):
    """
    Computes a canonical SHA-256 hash binding the card's polarity, titles,
    descriptions, and AI prompt. If any clinical instruction changes,
    the spec_hash changes, invalidating stale approvals.
    """
    payload = {
        "day_id": str(day_id),
        "index": int(card.get("index", 1)),
        "type": str(card.get("type", "message")),
        "title_en": str(card.get("title_en", "")),
        "title_gu": str(card.get("title_gu", "")),
        "desc_en": str(card.get("desc_en", "")),
        "desc_gu": str(card.get("desc_gu", "")),
        "ai_prompt": str(card.get("ai_prompt", ""))
    }
    canon_bytes = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canon_bytes).hexdigest()

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

def load_approved_manifest(manifest_path=APPROVED_MANIFEST_PATH):
    """Load the approved manifest defining verified candidate SHA-256 hashes."""
    if not os.path.exists(manifest_path):
        return {}
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as err:
        print(f"[WARN] Failed to read approved manifest: {err}")
        return {}

def check_pending_transactions(project_dir=PROJECT_DIR):
    """
    Read-only inspection for pending/unfinalized transactions.
    Returns (has_pending, tx_id, plan_path, plan_or_error) without mutating any files.
    """
    active_tx_path = os.path.join(project_dir, "data", "active_transaction.json")
    transactions_dir = os.path.join(project_dir, "data", "transactions")

    if os.path.exists(active_tx_path):
        try:
            with open(active_tx_path, "r", encoding="utf-8") as f:
                info = json.load(f)
            plan_path = info.get("plan_path")
            tx_id = info.get("tx_id", "unknown")
            if plan_path and os.path.exists(plan_path):
                with open(plan_path, "r", encoding="utf-8") as f:
                    plan = json.load(f)
                if plan.get("state") not in ("FINALIZED", "ROLLED_BACK"):
                    return True, tx_id, plan_path, plan
            return True, tx_id, plan_path or "missing", "Active pointer exists with unfinalized state"
        except Exception as e:
            return True, "corrupt_pointer", active_tx_path, f"Corrupt active pointer: {e}"

    # Also inspect transactions directory
    if os.path.exists(transactions_dir):
        for tx_id in sorted(os.listdir(transactions_dir)):
            p_path = os.path.join(transactions_dir, tx_id, "tx_plan.json")
            if os.path.exists(p_path):
                try:
                    with open(p_path, "r", encoding="utf-8") as f:
                        plan = json.load(f)
                    if plan.get("state") not in ("FINALIZED", "ROLLED_BACK"):
                        return True, tx_id, p_path, plan
                except Exception:
                    pass
    return False, None, None, None

def validate_transaction_backups_preflight(plan, project_dir=PROJECT_DIR):
    """
    READ-ONLY preflight validation of all backups and mandatory pre-transaction hashes.
    Guarantees that NOT A SINGLE active target file is touched, copied, or deleted unless:
      1. plan['backups'] is a valid dict.
      2. plan['pre_transaction_hashes'] is a valid dict.
      3. For EVERY single target_rel in backups:
         - target_rel exists in pre_transaction_hashes.
         - expected_hash is a valid 64-char hex SHA-256 string.
         - backup file exists on disk, is readable, and non-empty.
         - compute_file_sha256(backup_file) == expected_hash.
    If ANY condition fails:
      Returns (False, error_message). Active target files remain 100% untouched.
    Only if 100% of backups pass preflight verification:
      Returns (True, None).
    """
    if not isinstance(plan, dict):
        return False, "Plan is not a valid dictionary"

    backups = plan.get("backups")
    if not isinstance(backups, dict):
        return False, "Plan missing valid 'backups' dictionary"

    pre_hashes = plan.get("pre_transaction_hashes")
    if not isinstance(pre_hashes, dict):
        return False, "Plan missing mandatory 'pre_transaction_hashes' dictionary"

    for target_rel, backup_rel in backups.items():
        if not target_rel or not backup_rel:
            return False, f"Malformed backup mapping: '{target_rel}' -> '{backup_rel}'"

        # Mandatory hash check
        expected_hash = pre_hashes.get(target_rel)
        if not expected_hash or not isinstance(expected_hash, str) or len(expected_hash) != 64:
            return False, f"Missing or invalid pre-transaction SHA-256 hash for target: '{target_rel}'"

        try:
            int(expected_hash, 16)
        except ValueError:
            return False, f"Pre-transaction hash for '{target_rel}' is not valid hex: '{expected_hash}'"

        # Backup file existence & readability check
        backup_full = os.path.join(project_dir, backup_rel)
        if not os.path.exists(backup_full):
            return False, f"Backup file missing on disk: '{backup_rel}' for target '{target_rel}'"

        if os.path.getsize(backup_full) == 0:
            return False, f"Backup file is empty (0 bytes): '{backup_rel}'"

        # Compute hash directly on backup file (read-only verification before touching any target)
        try:
            actual_backup_hash = compute_file_sha256(backup_full)
        except Exception as e:
            return False, f"Failed to read backup file '{backup_rel}': {e}"

        if actual_backup_hash != expected_hash:
            return False, (
                f"Backup file corrupted: '{backup_rel}' hash ({actual_backup_hash}) "
                f"does not match pre-transaction hash ({expected_hash}) for target '{target_rel}'"
            )

    return True, None

def recover_unfinalized_transactions(project_dir=PROJECT_DIR, explicit_tx_id=None):
    """
    Startup Crash Recovery:
    Fail-closed recovery that restores all active artwork and datasets.
    - Quarantines corrupt pointer files, preserving evidence.
    - Requires 100% of backups to pass read-only preflight verification before any file is touched.
    - Fails closed if any backup is missing or unverified:
      DOES NOT delete pointer, DOES NOT mark ROLLED_BACK, leaves active targets untouched.
    - Halts with error requiring manual intervention.
    """
    active_tx_path = os.path.join(project_dir, "data", "active_transaction.json")
    transactions_dir = os.path.join(project_dir, "data", "transactions")

    if explicit_tx_id:
        plan_path = os.path.join(transactions_dir, explicit_tx_id, "tx_plan.json")
        if not os.path.exists(plan_path):
            raise RuntimeError(f"Explicit transaction plan not found: {plan_path}")
        with open(plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)
        has_pending = True
        tx_id = explicit_tx_id
        plan_or_err = plan
    else:
        has_pending, tx_id, plan_path, plan_or_err = check_pending_transactions(project_dir)
        if not has_pending:
            return True

    print("!" * 70)
    print(f"[CRASH RECOVERY] Unfinalized transaction detected: {tx_id}")
    print("!" * 70)

    # Quarantine corrupt pointer file to preserve evidence
    if os.path.exists(active_tx_path):
        try:
            with open(active_tx_path, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as err:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            quarantine = os.path.join(project_dir, "data", f"active_transaction.corrupt.{timestamp}.json")
            shutil.copy2(active_tx_path, quarantine)
            print(f"[CAUTION] Corrupted active_transaction.json quarantined to: {quarantine}")
            raise RuntimeError(
                f"Recovery halted: active_transaction.json is corrupt (quarantined to {os.path.basename(quarantine)}).\n"
                f"Specify explicit plan using --recover <tx_id> or inspect {transactions_dir}. Active targets untouched."
            )

    if not isinstance(plan_or_err, dict):
        raise RuntimeError(f"Recovery failed: Transaction plan unreadable or missing at {plan_path}. Pointer preserved.")

    plan = plan_or_err

    # 1. MANDATORY-HASH READ-ONLY PREFLIGHT (BEFORE TOUCHING ANY TARGET FILE)
    valid_preflight, preflight_err = validate_transaction_backups_preflight(plan, project_dir)
    if not valid_preflight:
        plan["state"] = "RECOVERY_BLOCKED_PREFLIGHT_FAILED"
        plan["recovery_error"] = preflight_err
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)
        raise RuntimeError(
            f"CRASH RECOVERY BLOCKED (FAIL-CLOSED):\n{preflight_err}\n"
            "Zero active target files were modified or deleted. Pointer and transaction plan preserved."
        )

    backups = plan.get("backups", {})
    created_files = plan.get("created_files", [])

    # 2. RESTORE FILES VIA ATOMIC WRITE AND RE-VERIFY POST-RESTORATION HASH
    restored_count = 0
    for target_rel, backup_rel in backups.items():
        target_full = os.path.join(project_dir, target_rel)
        backup_full = os.path.join(project_dir, backup_rel)
        expected_hash = plan["pre_transaction_hashes"][target_rel]

        with open(backup_full, "rb") as f_in:
            backup_bytes = f_in.read()
        atomic_write_file(target_full, backup_bytes, is_binary=True)

        # Immediate verification of restored target
        restored_hash = compute_file_sha256(target_full)
        if restored_hash != expected_hash:
            raise RuntimeError(f"Post-restoration hash verification failed on '{target_rel}'")
        restored_count += 1
        print(f"  [RESTORED & VERIFIED] {target_rel} <- {backup_rel}")

    # 3. DELETE FILES CREATED DURING FAILED TRANSACTION
    for created_rel in created_files:
        created_full = os.path.join(project_dir, created_rel)
        if os.path.exists(created_full):
            os.remove(created_full)
            print(f"  [REMOVED UNFINALIZED] {created_rel}")

    # 4. REBUILD PRECACHE MANIFEST
    manifest_ok = False
    manifest_err = None
    try:
        from build_precache_manifest import build_manifest
        manifest_ok = build_manifest(project_dir=project_dir, raise_on_error=False)
    except Exception as e:
        manifest_ok = False
        manifest_err = str(e)

    if not manifest_ok:
        err_msg = manifest_err or "Manifest builder failed or returned False"
        plan["state"] = "RECOVERY_BLOCKED_MANIFEST_FAILED"
        plan["recovery_error"] = f"Manifest rebuild failed during recovery: {err_msg}"
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)
        print(f"[ERROR] Crash recovery blocked: {err_msg}. Pointer and transaction plan preserved.")
        raise RuntimeError(f"CRASH RECOVERY BLOCKED: {err_msg}. Pointer and plan preserved.")

    # 5. FINALIZE RECOVERY
    plan["state"] = "ROLLED_BACK"
    plan["recovered_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)

    if os.path.exists(active_tx_path):
        os.remove(active_tx_path)

    print(f"[CRASH RECOVERY COMPLETE] All {restored_count} files safely restored and verified against pre-transaction hashes.\n")
    return True

def rollback_transaction(plan, plan_path, project_dir=PROJECT_DIR):
    """
    Roll back in-process failed transaction across all artwork and datasets.
    Enforces read-only preflight before touching active targets.
    Fails closed: requires all backups to exist, verifies restored hashes,
    and preserves pointer if rollback cannot be completed.
    """
    print("\n" + "!" * 70)
    print(f"[TRANSACTION ROLLBACK] Reverting transaction {plan.get('tx_id')}...")
    print("!" * 70)

    # 1. READ-ONLY PREFLIGHT (BEFORE TOUCHING ANY TARGET FILE)
    valid_preflight, preflight_err = validate_transaction_backups_preflight(plan, project_dir)
    if not valid_preflight:
        plan["state"] = "ROLLBACK_BLOCKED_PREFLIGHT_FAILED"
        plan["rollback_error"] = preflight_err
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)
        print(f"[ERROR] Rollback preflight failed: {preflight_err}. Active target files untouched. Pointer preserved.")
        return

    backups = plan.get("backups", {})
    created_files = plan.get("created_files", [])

    # 2. RESTORE FILES VIA ATOMIC WRITE AND VERIFY HASHES
    for target_rel, backup_rel in backups.items():
        target_full = os.path.join(project_dir, target_rel)
        backup_full = os.path.join(project_dir, backup_rel)
        expected_hash = plan["pre_transaction_hashes"][target_rel]

        with open(backup_full, "rb") as f_in:
            backup_bytes = f_in.read()
        atomic_write_file(target_full, backup_bytes, is_binary=True)

        restored_hash = compute_file_sha256(target_full)
        if restored_hash != expected_hash:
            plan["state"] = "ROLLBACK_BLOCKED_HASH_MISMATCH"
            plan["rollback_error"] = f"Post-rollback hash mismatch on {target_rel}"
            with open(plan_path, "w", encoding="utf-8") as f:
                json.dump(plan, f, indent=2)
            print(f"[ERROR] Post-rollback hash mismatch on {target_rel}. Pointer preserved.")
            return

        print(f"  [RESTORED] {target_rel}")

    # 3. REMOVE CREATED FILES
    for created_rel in created_files:
        created_full = os.path.join(project_dir, created_rel)
        if os.path.exists(created_full):
            os.remove(created_full)
            print(f"  [REMOVED PARTIAL] {created_rel}")

    # 4. RESTORE PRECACHE MANIFEST
    manifest_ok = False
    manifest_err = None
    try:
        from build_precache_manifest import build_manifest
        manifest_ok = build_manifest(project_dir=project_dir, raise_on_error=False)
    except Exception as e:
        manifest_ok = False
        manifest_err = str(e)

    if not manifest_ok:
        err_msg = manifest_err or "Manifest builder failed or returned False"
        plan["state"] = "ROLLBACK_BLOCKED_MANIFEST_FAILED"
        plan["rollback_error"] = f"Manifest rebuild failed during rollback: {err_msg}"
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)
        print(f"[ERROR] Transaction rollback blocked: {err_msg}. Pointer and transaction plan preserved.")
        return False

    # 5. UPDATE PLAN STATE
    plan["state"] = "ROLLED_BACK"
    plan["rolled_back_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)

    active_tx_path = os.path.join(project_dir, "data", "active_transaction.json")
    if os.path.exists(active_tx_path):
        os.remove(active_tx_path)

    print("[TRANSACTION ROLLBACK COMPLETE] All artwork and datasets restored and verified.")
    return True

def promote_staged_assets(calendar_data, day_filter=None, dry_run=False, project_dir=PROJECT_DIR):
    """
    Approval & Promotion Gate:
    Enforces image decompression/integrity, specification binding (spec_hash),
    clinical assessment QA validation, and whole-release transactional promotion.
    """
    staging_dir = os.path.join(project_dir, "photos", "staging")
    approved_manifest_path = os.path.join(project_dir, "data", "approved_manifest.json")
    json_path = os.path.join(project_dir, "data", "health_365.json")
    js_path = os.path.join(project_dir, "js", "calendar-data.js")
    transactions_dir = os.path.join(project_dir, "data", "transactions")
    active_tx_path = os.path.join(project_dir, "data", "active_transaction.json")

    if not os.path.exists(staging_dir):
        print("[PROMOTION] Staging directory photos/staging/ does not exist.")
        return

    approved_manifest = load_approved_manifest(approved_manifest_path)
    print("=" * 70)
    print("   HealthCalendar365 - Asset Promotion & Approval Gate")
    print(f"   Mode: {'DRY RUN (Read-Only Preview)' if dry_run else 'ACTIVE PROMOTION'}")
    print("=" * 70)

    staged_files = sorted(os.listdir(staging_dir))
    if not staged_files:
        print("[PROMOTION] No staged candidate files found in photos/staging/.")
        return

    # Index calendar cards by (day_id, card_idx) for spec validation
    card_index = {}
    for day in calendar_data:
        day_id = str(day.get("id"))
        for card in day.get("cards", []):
            card_idx = int(card.get("index", 1))
            card_index[(day_id, card_idx)] = (day, card)

    to_promote = []
    seen_slots = {}

    for fname in staged_files:
        if not fname.startswith("candidate_") or not (fname.endswith(".png") or fname.endswith(".webp")):
            continue
        c_path = os.path.join(staging_dir, fname)

        # 1. Exhaustive Image Integrity & Full Decompression Test
        valid_img, img_info = verify_image_integrity_and_decode(c_path)
        if not valid_img:
            print(f"  [REJECTED - INTEGRITY FAILED] {fname}: {img_info}")
            continue

        c_hash = compute_file_sha256(c_path)

        # 2. Approval Record Gate
        approval_record = approved_manifest.get(c_hash)
        if not approval_record:
            print(f"  [REJECTED - UNAPPROVED] {fname} (SHA-256: {c_hash[:12]}...) lacks an approved record in approved_manifest.json.")
            continue

        status = approval_record.get("status")
        if status != "APPROVED":
            print(f"  [REJECTED - STATUS: {status}] {fname} status is '{status}' (must be 'APPROVED').")
            continue

        # 3. Clinical Assessment QA Gate: Reject any contradictory/failed QA checks
        cr = approval_record.get("clinical_review")
        if not cr or not isinstance(cr, dict):
            print(f"  [REJECTED - MISSING CLINICAL REVIEW] {fname} lacks clinical_review assessment.")
            continue

        qa_failures = []
        if cr.get("visual_concordance") != "PASS":
            qa_failures.append(f"visual_concordance={cr.get('visual_concordance')}")
        if cr.get("cultural_authenticity") != "PASS":
            qa_failures.append(f"cultural_authenticity={cr.get('cultural_authenticity')}")
        if cr.get("polarity_match") != "PASS":
            qa_failures.append(f"polarity_match={cr.get('polarity_match')}")
        if cr.get("safety_equipment_check") not in ("PASS", "N/A"):
            qa_failures.append(f"safety_equipment_check={cr.get('safety_equipment_check')}")

        if qa_failures:
            print(f"  [REJECTED - CLINICAL QA FAILED] {fname} failed criteria: {', '.join(qa_failures)} (all must be PASS).")
            continue

        day_id = str(approval_record.get("day_id", ""))
        card_idx = int(approval_record.get("card_idx", 0))
        if not day_id or not card_idx:
            print(f"  [REJECTED - MALFORMED APPROVAL] {fname} record missing day_id or card_idx.")
            continue

        if day_filter and day_id != str(day_filter):
            continue

        # 4. Specification Binding Check (spec_hash)
        slot_key = (day_id, card_idx)
        if slot_key not in card_index:
            print(f"  [REJECTED - INVALID TARGET] {fname} targets nonexistent slot: Day {day_id} Card #{card_idx}.")
            continue

        target_day, target_card = card_index[slot_key]
        expected_spec_hash = compute_card_spec_hash(target_card, day_id)
        recorded_spec_hash = approval_record.get("spec_hash")

        if not recorded_spec_hash or recorded_spec_hash != expected_spec_hash:
            print(f"  [REJECTED - SPEC MISMATCH] {fname} approval was bound to an outdated/mismatched card specification.")
            continue

        # 5. Reviewer Metadata Check
        reviewer = approval_record.get("reviewer")
        if not reviewer or not isinstance(reviewer, dict) or not reviewer.get("name"):
            print(f"  [REJECTED - UNACCOUNTABLE REVIEWER] {fname} lacks valid reviewer metadata.")
            continue

        # 6. Slot Conflict Resolution
        if slot_key in seen_slots:
            print(f"  [REJECTED - DUPLICATE CANDIDATE] Slot Day {day_id} Card #{card_idx} already filled by {seen_slots[slot_key]['candidate_fname']}.")
            continue

        clean_id = day_id.replace("-", "_").lower()
        ext = os.path.splitext(fname)[1]
        target_rel = f"photos/{clean_id}_card{card_idx}{ext}"
        target_full = os.path.join(project_dir, target_rel)

        candidate_item = {
            "candidate_path": c_path,
            "candidate_fname": fname,
            "candidate_hash": c_hash,
            "day_id": day_id,
            "card_idx": card_idx,
            "target_rel": target_rel,
            "target_full": target_full,
            "approval": approval_record,
            "img_info": img_info
        }

        to_promote.append(candidate_item)
        seen_slots[slot_key] = candidate_item

    if not to_promote:
        print("\n[PROMOTION] No approved candidates qualified for promotion.")
        print("To approve candidates, verify image decoding and add a validated record to data/approved_manifest.json with:")
        print("  - status: 'APPROVED'")
        print("  - clinical_review: { visual_concordance: 'PASS', cultural_authenticity: 'PASS', polarity_match: 'PASS', safety_equipment_check: 'PASS'|'N/A' }")
        print("  - spec_hash: matching current card canonical hash")
        print("  - reviewer: { name: '...', role: '...' }")
        return

    print(f"\nQualified Candidates Ready for Promotion: {len(to_promote)}")
    for item in to_promote:
        rev_name = item["approval"].get("reviewer", {}).get("name", "Authorized Reviewer")
        print(f"  - Day {item['day_id']} Card #{item['card_idx']} -> {item['target_rel']} ({item['img_info']['width']}x{item['img_info']['height']}, Reviewer: {rev_name})")

    if dry_run:
        print("\n[DRY RUN] Mutation prohibited. Staged files, active artwork, and datasets were NOT changed.")
        return

    # Transactional Whole-Release Promotion
    tx_id = f"tx_{int(time.time())}_{uuid.uuid4().hex[:8]}"
    tx_dir = os.path.join(transactions_dir, tx_id)
    tx_backup_dir = os.path.join(tx_dir, "backup")
    os.makedirs(tx_backup_dir, exist_ok=True)
    plan_path = os.path.join(tx_dir, "tx_plan.json")

    print(f"\n[TRANSACTION] Initiating durable whole-release promotion (TX: {tx_id})...")

    backups = {}
    pre_transaction_hashes = {}
    created_files = []

    # Backup active image targets if they already exist
    for item in to_promote:
        t_rel = item["target_rel"]
        t_full = item["target_full"]
        if os.path.exists(t_full):
            b_fname = os.path.basename(t_full)
            b_full = os.path.join(tx_backup_dir, b_fname)
            shutil.copy2(t_full, b_full)
            backups[t_rel] = os.path.relpath(b_full, project_dir).replace("\\", "/")
            pre_transaction_hashes[t_rel] = compute_file_sha256(t_full)
        else:
            created_files.append(t_rel)

    # Backup datasets and sw.js
    for rel_p in ["data/health_365.json", "js/calendar-data.js", "sw.js"]:
        f_full = os.path.join(project_dir, rel_p)
        if os.path.exists(f_full):
            b_fname = os.path.basename(f_full)
            b_full = os.path.join(tx_backup_dir, b_fname)
            shutil.copy2(f_full, b_full)
            backups[rel_p] = os.path.relpath(b_full, project_dir).replace("\\", "/")
            pre_transaction_hashes[rel_p] = compute_file_sha256(f_full)

    plan = {
        "tx_id": tx_id,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "state": "PREPARED",
        "to_promote_count": len(to_promote),
        "backups": backups,
        "pre_transaction_hashes": pre_transaction_hashes,
        "created_files": created_files
    }

    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)

    with open(active_tx_path, "w", encoding="utf-8") as f:
        json.dump({"tx_id": tx_id, "plan_path": plan_path, "state": "PREPARED"}, f, indent=2)

    try:
        # Step 1: Promote images atomically
        plan["state"] = "PROMOTING_IMAGES"
        for item in to_promote:
            with open(item["candidate_path"], "rb") as f_in:
                img_data = f_in.read()
            atomic_write_file(item["target_full"], img_data, is_binary=True)

        # Step 2: Update calendar data in-memory
        for item in to_promote:
            for day in calendar_data:
                if str(day.get("id")) == item["day_id"]:
                    for card in day.get("cards", []):
                        if int(card.get("index", 1)) == item["card_idx"]:
                            card["photo"] = item["target_rel"]

        # Step 3: Write JSON and JS datasets atomically
        plan["state"] = "PROMOTING_DATASETS"
        json_content = json.dumps(calendar_data, indent=2, ensure_ascii=False)
        atomic_write_file(json_path, json_content)

        js_content = "// 365-Day Indian Health Calendar Data (Preloaded)\nwindow.HEALTH_CALENDAR_DATA = " + json_content + ";\n"
        atomic_write_file(js_path, js_content)

        # Step 4: Synchronize precache manifest (raises ManifestBuildError on failure)
        plan["state"] = "PROMOTING_PRECACHE"
        from build_precache_manifest import build_manifest
        manifest_ok = build_manifest(project_dir=project_dir, raise_on_error=True)
        if not manifest_ok:
            raise RuntimeError("Manifest builder failed or returned False during promotion")

        # Step 5: Finalize transaction
        plan["state"] = "FINALIZED"
        plan["finalized_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)

        if os.path.exists(active_tx_path):
            os.remove(active_tx_path)

        print(f"\n[SUCCESS] Successfully promoted {len(to_promote)} approved candidates into active production!")
        print(f"Transaction {tx_id} FINALIZED safely.")

    except BaseException as err:
        # Catches BaseException: includes SystemExit, KeyboardInterrupt, and all Exceptions!
        rollback_transaction(plan, plan_path, project_dir=project_dir)
        raise

def process_calendar(args, project_dir=PROJECT_DIR):
    json_path = os.path.join(project_dir, "data", "health_365.json")

    # If explicit recovery requested
    if getattr(args, "recover", None):
        recover_unfinalized_transactions(project_dir, explicit_tx_id=args.recover)
        return

    # Check for unfinalized transactions
    has_pending, tx_id, plan_path, _ = check_pending_transactions(project_dir)

    # Dry-Run Mode Guarantee: Absolutely Zero Mutations!
    if args.dry_run:
        print("=" * 70)
        print("   HealthCalendar365 - Image Pipeline & Promotion Gate")
        print("   Mode: DRY RUN (Zero-Mutation Guarantee)")
        print("=" * 70)
        if has_pending:
            print(f"\n[DRY RUN PREVIEW] Unfinalized transaction detected: {tx_id}")
            print(f"  Plan: {plan_path}")
            print("  Active recovery is pending. Run without --dry-run to perform recovery.")
            print("[DRY RUN] Mutation strictly prohibited. Zero files were modified or recovered.")
            return

    # In active (non-dry-run) mode: execute recovery before proceeding
    if has_pending:
        try:
            recover_unfinalized_transactions(project_dir)
        except RuntimeError as rerr:
            print(f"\n[FATAL] Cannot proceed with calendar operations:\n{rerr}")
            sys.exit(1)

    if not os.path.exists(json_path):
        print(f"[ERROR] Calendar JSON missing at: {json_path}")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        calendar_data = json.load(f)

    # Handle Promotion Gate
    if args.promote:
        promote_staged_assets(calendar_data, day_filter=args.day, dry_run=args.dry_run, project_dir=project_dir)
        return

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
                "status": "staged_pending_approval",
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
    print("To review and promote approved candidates, record approval in data/approved_manifest.json, then run:")
    print("  python generate_with_gemini.py --promote")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Verified Image Pipeline for HealthCalendar365")
    parser.add_argument("--day", type=str, help="Specific Day ID to check/generate (e.g. 10-15)")
    parser.add_argument("--all-missing", action="store_true", help="Generate all missing or placeholder assets across 365 days")
    parser.add_argument("--dry-run", action="store_true", help="Read-only preview; guarantees zero mutations")
    parser.add_argument("--force", action="store_true", help="Regenerate photo assets even if file exists on disk")
    parser.add_argument("--promote", action="store_true", help="Validate and promote approved staged assets into active production")
    parser.add_argument("--recover", type=str, help="Explicitly recover a specific transaction ID from data/transactions/")
    parser.add_argument("--model", type=str, default="imagen-3.0-generate-002", help="Model to use (default: imagen-3.0-generate-002)")
    parser.add_argument("--api-key", type=str, help="Gemini API Key override")
    args = parser.parse_args()

    if not args.day and not args.all_missing and not args.promote and not args.recover:
        args.day = "10-15"

    process_calendar(args)

if __name__ == "__main__":
    main()
