#!/usr/bin/env python3
"""
HealthCalendar365 - Candidate Freeze & Evidence Reconciliation Tool
Chain-of-Custody Manifest Generator and Verification Tool

Modes:
  --create   Generates review/candidate_payload_manifest.json,
             review/acceptance_evidence_manifest.json, and
             review/freeze_checksums.sha256
  --verify   Performs strict read-only verification without modifying any files
"""

import os
import sys
import json
import hashlib
from collections import Counter
import subprocess

APP_ROOT = r"d:\HealthCalendar365"

PAYLOAD_MANIFEST_REL = os.path.join("review", "candidate_payload_manifest.json")
EVIDENCE_MANIFEST_REL = os.path.join("review", "acceptance_evidence_manifest.json")
CHECKSUMS_FILE_REL = os.path.join("review", "freeze_checksums.sha256")

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def normalize_relpath(p):
    return p.replace("\\", "/")

def get_payload_files():
    """Returns sorted list of relative paths for all runtime payload files."""
    core = [
        'index.html', 'manifest.json', 'sw.js',
        'css/styles.css', 'css/fonts.css',
        'js/app.js', 'js/canvas-renderer.js', 'js/db.js', 'js/calendar-data.js',
        'data/health_365.json', 'data/approved_manifest.json'
    ]
    icons_dir = os.path.join(APP_ROOT, 'icons')
    icons = [os.path.join('icons', f) for f in sorted(os.listdir(icons_dir))]

    fonts_dir = os.path.join(APP_ROOT, 'fonts')
    fonts = [os.path.join('fonts', f) for f in sorted(os.listdir(fonts_dir))]

    photos_dir = os.path.join(APP_ROOT, 'photos')
    photos = [os.path.join('photos', f) for f in sorted(os.listdir(photos_dir))
              if os.path.isfile(os.path.join(photos_dir, f))]

    all_files = sorted(core + icons + fonts + photos)
    return [normalize_relpath(f) for f in all_files]

def get_evidence_files():
    """Returns sorted list of relative paths for all acceptance and evidence files."""
    review_docs = [
        'review/AUTOMATED_BROWSER_PWA_TEST_REPORT.md',
        'review/automated_browser_pwa_test_results.json',
        'review/approval_ledger_reconciliation_2026-10-18.json',
        'review/ANTIGRAVITY_HANDOFF_2026-10-18.md',
        'review/candidate_generation_queue.json',
        'review/candidate_specifications_9_rejected.json',
        'review/CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.json',
        'review/CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.md',
        'review/CONTENT_RELEASE_ACCEPTANCE.md',
        'review/FINAL_ACCEPTANCE_PACKET.md',
        'review/FINAL_AUTOMATED_PHASE_REVIEW.md',
        'review/final_automated_phase_results.json',
        'review/FREEZE_CHAIN_OF_CUSTODY.md',
        'review/FULL_CALENDAR_AUDIT_REPORT.md',
        'review/full_calendar_audit.json',
        'review/human_decisions/clinical_dr_atul_2026-10-16.json',
        'review/human_decisions/clinical_dr_atul_2026-10-16_card_bindings.json',
        'review/human_decisions/clinical_decision_transition_2026-10-16.json',
        'review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json',
        'review/human_decisions/replacement_images_dr_atul_2026-10-16.json',
        'review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json',
        'review/MISSING_EVIDENCE_REGISTER.md',
        'review/NINE_CANDIDATE_PILOT_PLAN.json',
        'review/NINE_CANDIDATE_PILOT_PLAN.md',
        'review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md',
        'review/PILOT_SPENDING_AUTHORIZATION_SHEET.md',
        'review/PRODUCTION_HOSTING_EVALUATION.md',
        'review/proposed_copy_and_provenance_corrections.json',
        'review/REPLACEMENT_CANDIDATE_REVIEW.md',
        'review/replacement_candidate_generation_2026-10-16.json',
        'review/replacement-candidates.html',
        'review/REPLACEMENT_SPECIFICATION_AND_AUTHORIZATION_10_17_CARD1.md',
        'review/RELEASE_GOVERNANCE.md',
        'review/REVIEW_PACKET.md',
        'review/review_queue.json',
        'review/RUNTIME_OFFLINE_PWA_TEST_REPORT.md',
        'review/runtime_offline_pwa_test_results.json',
        'review/scoped-clinical-reapproval.html',
        'review/SCOPED_CLINICAL_REAPPROVAL_PACKET.md',
        'review/scoped_clinical_reapproval_packet.json',
        'review/superseded/final_acceptance_candidate_manifest_v2_58a718fa.json',
        'review/superseded/rejected_assets_10_17_card1_pre_replacement_2026-10-18.json',
        'review/superseded/rejected_assets_pre_replacement_2026-10-16.json'
    ]

    screenshots_dir = os.path.join(APP_ROOT, 'review', 'screenshots')
    screenshots = []
    if os.path.exists(screenshots_dir):
        screenshots = [os.path.join('review', 'screenshots', f) for f in sorted(os.listdir(screenshots_dir))]

    test_scripts = [
        'scratch/generate_stage1_md.py',
        'scratch/generate_stage1_register.py',
        'scratch/generate_acceptance_docs.py',
        'scratch/generate_review_queue.py',
        'scratch/inspect_reconcile_data.py',
        'scratch/reconcile_approval_ledger_2026_10_18.py',
        'scratch/reconcile_and_freeze.py',
        'scratch/update_current_acceptance_docs.py',
        'scratch/verify_phase_precheck.py',
        'scratch/verify_promotion_step5.py',
        'scratch/test_runtime_offline_pwa.cjs',
        'scratch/test_browser_pwa_lifecycle.cjs',
        'scratch/test_image_only_share.cjs',
        'scratch/test_all_widths.cjs',
        'test_remediation_round3.py',
        'test_remediation_round4.py',
        'test_remediation_round5.py',
        'test_remediation_round6.py'
    ]

    all_evidence = sorted(review_docs + screenshots + test_scripts)
    return [normalize_relpath(f) for f in all_evidence]

def create_manifests():
    print("=== Creating Candidate Freeze & Evidence Manifests ===")

    payload_paths = get_payload_files()
    evidence_paths = get_evidence_files()

    # Pre-verification: Verify zero self-inclusion or cross-inclusion of generated manifests
    disallowed_in_payload = [
        normalize_relpath(PAYLOAD_MANIFEST_REL),
        normalize_relpath(EVIDENCE_MANIFEST_REL),
        normalize_relpath(CHECKSUMS_FILE_REL)
    ]
    for d in disallowed_in_payload:
        if d in payload_paths:
            raise ValueError(f"Self-reference violation: {d} must not be in payload files list!")

    disallowed_in_evidence = [
        normalize_relpath(EVIDENCE_MANIFEST_REL),
        normalize_relpath(PAYLOAD_MANIFEST_REL),
        normalize_relpath(CHECKSUMS_FILE_REL)
    ]
    for d in disallowed_in_evidence:
        if d in evidence_paths:
            raise ValueError(f"Self-reference violation: {d} must not be in evidence files list!")

    # 1. Build Payload Manifest
    payload_files_data = {}
    total_payload_bytes = 0
    for rel in payload_paths:
        full_p = os.path.join(APP_ROOT, rel.replace('/', os.sep))
        if not os.path.exists(full_p):
            raise FileNotFoundError(f"Missing payload file: {full_p}")
        b = os.path.getsize(full_p)
        h = sha256_file(full_p)
        total_payload_bytes += b
        payload_files_data[rel] = {
            'sha256': h,
            'bytes': b
        }

    with open(os.path.join(APP_ROOT, 'data', 'approved_manifest.json'), 'r', encoding='utf-8') as f:
        approval_ledger = json.load(f)
    approval_counts = Counter(entry.get('status', 'UNKNOWN') for entry in approval_ledger.values())
    with open(os.path.join(APP_ROOT, 'data', 'health_365.json'), 'r', encoding='utf-8') as f:
        health_calendar = json.load(f)
    photos_root = os.path.join(APP_ROOT, 'photos')
    active_photo_count = sum(1 for name in os.listdir(photos_root)
                             if os.path.isfile(os.path.join(photos_root, name)))

    git_probe = subprocess.run(['git', '-C', APP_ROOT, 'rev-parse', '--is-inside-work-tree'],
                               capture_output=True, text=True)
    if git_probe.returncode == 0 and git_probe.stdout.strip() == 'true':
        branch_result = subprocess.run(['git', '-C', APP_ROOT, 'branch', '--show-current'], capture_output=True, text=True)
        head_result = subprocess.run(['git', '-C', APP_ROOT, 'rev-parse', 'HEAD'], capture_output=True, text=True)
        status_result = subprocess.run(['git', '-C', APP_ROOT, 'status', '--porcelain'], capture_output=True, text=True)
        branch = branch_result.stdout.strip() or None
        head_commit = head_result.stdout.strip() or None
        working_tree_state = 'DIRTY' if status_result.stdout.strip() else 'CLEAN'
    else:
        branch = None
        head_commit = None
        working_tree_state = 'NO_GIT_METADATA_IN_PROJECT_ROOT'

    payload_manifest = {
        'manifest_type': 'candidate_payload_manifest',
        'manifest_version': '1.0.0',
        'created_at': '2026-10-18',
        'branch': branch,
        'head_commit': head_commit,
        'working_tree_state': working_tree_state,
        'hash_algorithm': 'SHA-256',
        'spending_status': 'USD 0.00',
        'production_hold_status': 'STRICTLY_ACTIVE',
        'invariants': {
            'posters_count': len(health_calendar),
            'total_card_slots': sum(len(day.get('cards', [])) for day in health_calendar),
            'dedicated_image_cards': len(approval_ledger),
            'category_placeholder_cards': sum(len(day.get('cards', [])) for day in health_calendar) - len(approval_ledger),
            'physical_photos_count': active_photo_count,
            'approval_counts': {
                'APPROVED': approval_counts.get('APPROVED', 0),
                'PENDING_CLINICAL_SIGN_OFF': approval_counts.get('PENDING_CLINICAL_SIGN_OFF', 0),
                'REJECTED_MISMATCH': approval_counts.get('REJECTED_MISMATCH', 0)
            }
        },
        'precache_breakdown': {
            'total_entries': 97,
            'root_and_application_shell': 5,
            'javascript': 4,
            'data': 1,
            'icons': 2,
            'fonts': 40,
            'photos': 45
        },
        'total_files': len(payload_paths),
        'total_bytes': total_payload_bytes,
        'files': payload_files_data
    }

    payload_manifest_path = os.path.join(APP_ROOT, PAYLOAD_MANIFEST_REL)
    new_payload_json = json.dumps(payload_manifest, indent=2)

    if os.path.exists(payload_manifest_path):
        with open(payload_manifest_path, 'r', encoding='utf-8') as f:
            existing_payload_json = f.read()
        if existing_payload_json == new_payload_json:
            print(f"Preserved unchanged: {PAYLOAD_MANIFEST_REL} (content, digest, and timestamp preserved)")
        else:
            with open(payload_manifest_path, 'w', encoding='utf-8') as f:
                f.write(new_payload_json)
            print(f"Updated: {PAYLOAD_MANIFEST_REL}")
    else:
        with open(payload_manifest_path, 'w', encoding='utf-8') as f:
            f.write(new_payload_json)
        print(f"Created: {PAYLOAD_MANIFEST_REL}")

    payload_manifest_hash = sha256_file(payload_manifest_path)
    print(f"  Files: {len(payload_paths)} | Bytes: {total_payload_bytes} | SHA-256: {payload_manifest_hash}")

    # 2. Build Acceptance Evidence Manifest
    evidence_files_data = {}
    total_evidence_bytes = 0
    for rel in evidence_paths:
        full_p = os.path.join(APP_ROOT, rel.replace('/', os.sep))
        if not os.path.exists(full_p):
            raise FileNotFoundError(f"Missing evidence file: {full_p}")
        b = os.path.getsize(full_p)
        h = sha256_file(full_p)
        total_evidence_bytes += b
        evidence_files_data[rel] = {
            'sha256': h,
            'bytes': b
        }

    evidence_manifest = {
        'manifest_type': 'acceptance_evidence_manifest',
        'manifest_version': '1.0.0',
        'created_at': '2026-10-18',
        'branch': branch,
        'head_commit': head_commit,
        'working_tree_state': working_tree_state,
        'hash_algorithm': 'SHA-256',
        'spending_status': 'USD 0.00',
        'production_hold_status': 'STRICTLY_ACTIVE',
        'reference_candidate_payload_manifest': {
            'path': normalize_relpath(PAYLOAD_MANIFEST_REL),
            'sha256': payload_manifest_hash,
            'total_payload_files': len(payload_paths),
            'total_payload_bytes': total_payload_bytes
        },
        'deferred_final_acceptance_register': [
            {'id': 'DEF-ACC-01', 'item': 'Physical Android-device testing', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-02', 'item': 'Manual PWA installation', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-03', 'item': 'WhatsApp export, sharing and compression review', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-04', 'item': 'Human visual inspection', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-05', 'item': 'User experience and usability testing', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-06', 'item': 'User acceptance testing', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-07', 'item': 'Clinical review and sign-off', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-08', 'item': 'Gujarati-language review and sign-off', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-09', 'item': 'Accessibility testing with actual users', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'},
            {'id': 'DEF-ACC-10', 'item': 'Human approval of images, messages and poster compositions', 'status': 'DEFERRED_TO_FINAL_ACCEPTANCE'}
        ],
        'total_files': len(evidence_paths),
        'total_bytes': total_evidence_bytes,
        'files': evidence_files_data
    }

    evidence_manifest_path = os.path.join(APP_ROOT, EVIDENCE_MANIFEST_REL)
    with open(evidence_manifest_path, 'w', encoding='utf-8') as f:
        json.dump(evidence_manifest, f, indent=2)

    evidence_manifest_hash = sha256_file(evidence_manifest_path)
    print(f"Created: {EVIDENCE_MANIFEST_REL}")
    print(f"  Files: {len(evidence_paths)} | Bytes: {total_evidence_bytes} | SHA-256: {evidence_manifest_hash}")

    # 3. Build External Checksums File
    checksums_path = os.path.join(APP_ROOT, CHECKSUMS_FILE_REL)
    checksum_lines = [
        f"{payload_manifest_hash}  {normalize_relpath(PAYLOAD_MANIFEST_REL)}\n",
        f"{evidence_manifest_hash}  {normalize_relpath(EVIDENCE_MANIFEST_REL)}\n"
    ]
    with open(checksums_path, 'w', encoding='utf-8') as f:
        f.writelines(checksum_lines)

    checksums_file_hash = sha256_file(checksums_path)
    print(f"Created: {CHECKSUMS_FILE_REL}")
    print(f"  SHA-256 of checksums file: {checksums_file_hash}")
    print(f"  Contents:\n    {checksum_lines[0].strip()}\n    {checksum_lines[1].strip()}")

    print("\n[SUCCESS] Deterministic chain-of-custody created without circular dependencies.")

def verify_manifests():
    print("=== Verifying Candidate Freeze & Evidence Chain of Custody (READ ONLY) ===")

    checksums_path = os.path.join(APP_ROOT, CHECKSUMS_FILE_REL)
    payload_path = os.path.join(APP_ROOT, PAYLOAD_MANIFEST_REL)
    evidence_path = os.path.join(APP_ROOT, EVIDENCE_MANIFEST_REL)

    errors = []

    # 1. Verify existence of manifests and checksums file
    for p, name in [(checksums_path, CHECKSUMS_FILE_REL), (payload_path, PAYLOAD_MANIFEST_REL), (evidence_path, EVIDENCE_MANIFEST_REL)]:
        if not os.path.exists(p):
            errors.append(f"Missing required manifest file: {name}")

    if errors:
        for e in errors:
            print(f"[FAIL] {e}")
        return False

    # 2. Verify external checksums file
    expected_hashes = {}
    with open(checksums_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(None, 1)
            if len(parts) == 2:
                expected_hashes[parts[1]] = parts[0]

    actual_payload_hash = sha256_file(payload_path)
    actual_evidence_hash = sha256_file(evidence_path)

    if expected_hashes.get(normalize_relpath(PAYLOAD_MANIFEST_REL)) != actual_payload_hash:
        errors.append(f"Checksum mismatch for {PAYLOAD_MANIFEST_REL}: expected {expected_hashes.get(normalize_relpath(PAYLOAD_MANIFEST_REL))} vs actual {actual_payload_hash}")
    else:
        print(f"[PASS] {PAYLOAD_MANIFEST_REL} matches freeze_checksums.sha256 ({actual_payload_hash})")

    if expected_hashes.get(normalize_relpath(EVIDENCE_MANIFEST_REL)) != actual_evidence_hash:
        errors.append(f"Checksum mismatch for {EVIDENCE_MANIFEST_REL}: expected {expected_hashes.get(normalize_relpath(EVIDENCE_MANIFEST_REL))} vs actual {actual_evidence_hash}")
    else:
        print(f"[PASS] {EVIDENCE_MANIFEST_REL} matches freeze_checksums.sha256 ({actual_evidence_hash})")

    # 3. Verify Payload Manifest Entries
    with open(payload_path, 'r', encoding='utf-8') as f:
        payload_data = json.load(f)

    p_files = payload_data.get('files', {})
    print(f"\n--- Checking Payload Manifest Entries ({len(p_files)} files) ---")
    p_bytes_sum = 0
    for rel, meta in p_files.items():
        if rel in [normalize_relpath(PAYLOAD_MANIFEST_REL), normalize_relpath(EVIDENCE_MANIFEST_REL), normalize_relpath(CHECKSUMS_FILE_REL)]:
            errors.append(f"Self-reference error: {rel} found inside payload manifest!")
        full_p = os.path.join(APP_ROOT, rel.replace('/', os.sep))
        if not os.path.exists(full_p):
            errors.append(f"Payload file missing on disk: {rel}")
            continue
        actual_bytes = os.path.getsize(full_p)
        actual_hash = sha256_file(full_p)
        p_bytes_sum += actual_bytes
        if actual_bytes != meta['bytes']:
            errors.append(f"Payload byte mismatch on {rel}: expected {meta['bytes']} vs actual {actual_bytes}")
        if actual_hash != meta['sha256']:
            errors.append(f"Payload hash mismatch on {rel}: expected {meta['sha256']} vs actual {actual_hash}")

    if p_bytes_sum != payload_data.get('total_bytes'):
        errors.append(f"Payload aggregate byte mismatch: manifest says {payload_data.get('total_bytes')}, sum is {p_bytes_sum}")
    else:
        print(f"[PASS] Payload aggregate bytes verified: {p_bytes_sum} bytes")

    if len(p_files) != payload_data.get('total_files'):
        errors.append(f"Payload aggregate file count mismatch: manifest says {payload_data.get('total_files')}, files dict has {len(p_files)}")
    else:
        print(f"[PASS] Payload aggregate file count verified: {len(p_files)} files")

    # 4. Verify Evidence Manifest Entries
    with open(evidence_path, 'r', encoding='utf-8') as f:
        evidence_data = json.load(f)

    e_files = evidence_data.get('files', {})
    print(f"\n--- Checking Evidence Manifest Entries ({len(e_files)} files) ---")
    e_bytes_sum = 0
    for rel, meta in e_files.items():
        if rel in [normalize_relpath(EVIDENCE_MANIFEST_REL), normalize_relpath(PAYLOAD_MANIFEST_REL), normalize_relpath(CHECKSUMS_FILE_REL)]:
            errors.append(f"Self-reference error: {rel} found inside evidence manifest!")
        full_p = os.path.join(APP_ROOT, rel.replace('/', os.sep))
        if not os.path.exists(full_p):
            errors.append(f"Evidence file missing on disk: {rel}")
            continue
        actual_bytes = os.path.getsize(full_p)
        actual_hash = sha256_file(full_p)
        e_bytes_sum += actual_bytes
        if actual_bytes != meta['bytes']:
            errors.append(f"Evidence byte mismatch on {rel}: expected {meta['bytes']} vs actual {actual_bytes}")
        if actual_hash != meta['sha256']:
            errors.append(f"Evidence hash mismatch on {rel}: expected {meta['sha256']} vs actual {actual_hash}")

    if e_bytes_sum != evidence_data.get('total_bytes'):
        errors.append(f"Evidence aggregate byte mismatch: manifest says {evidence_data.get('total_bytes')}, sum is {e_bytes_sum}")
    else:
        print(f"[PASS] Evidence aggregate bytes verified: {e_bytes_sum} bytes")

    if len(e_files) != evidence_data.get('total_files'):
        errors.append(f"Evidence aggregate file count mismatch: manifest says {evidence_data.get('total_files')}, files dict has {len(e_files)}")
    else:
        print(f"[PASS] Evidence aggregate file count verified: {len(e_files)} files")

    # 5. Check Circular Dependency and Exclusion
    print("\n--- Checking Self-Reference and Non-Circular Architecture ---")
    if normalize_relpath(PAYLOAD_MANIFEST_REL) in p_files:
        errors.append(f"Self-reference error: {PAYLOAD_MANIFEST_REL} is included inside payload manifest!")
    else:
        print(f"[PASS] {PAYLOAD_MANIFEST_REL} does not include itself.")

    if normalize_relpath(EVIDENCE_MANIFEST_REL) in e_files:
        errors.append(f"Self-reference error: {EVIDENCE_MANIFEST_REL} is included inside evidence manifest!")
    else:
        print(f"[PASS] {EVIDENCE_MANIFEST_REL} does not include itself.")

    if normalize_relpath(PAYLOAD_MANIFEST_REL) in e_files:
        errors.append(f"Circular dependency error: payload manifest is tracked inside evidence manifest!")
    else:
        print(f"[PASS] {PAYLOAD_MANIFEST_REL} is excluded from evidence manifest files list.")

    if normalize_relpath(EVIDENCE_MANIFEST_REL) in p_files:
        errors.append(f"Circular dependency error: evidence manifest is tracked inside payload manifest!")
    else:
        print(f"[PASS] {EVIDENCE_MANIFEST_REL} is excluded from payload manifest.")

    if normalize_relpath(CHECKSUMS_FILE_REL) in e_files or normalize_relpath(CHECKSUMS_FILE_REL) in p_files:
        errors.append(f"Circular dependency error: checksums file is tracked inside a manifest!")
    else:
        print(f"[PASS] {CHECKSUMS_FILE_REL} is strictly external to both manifests.")

    # Check that acceptance documents do not embed the evidence manifest hash
    for doc_rel in ['review/FINAL_ACCEPTANCE_PACKET.md', 'review/FINAL_AUTOMATED_PHASE_REVIEW.md']:
        doc_path = os.path.join(APP_ROOT, doc_rel.replace('/', os.sep))
        if os.path.exists(doc_path):
            with open(doc_path, 'r', encoding='utf-8') as df:
                content = df.read()
                if actual_evidence_hash in content:
                    errors.append(f"Circular dependency error: {doc_rel} embeds evidence manifest hash {actual_evidence_hash}!")
    if not any("Circular dependency error" in e for e in errors):
        print("[PASS] Acceptance documents do not embed evidence manifest digest (no circular dependency).")

    # 6. Check Unexpected Runtime File Omissions
    print("\n--- Checking Runtime File Completeness ---")
    expected_payload = set(get_payload_files())
    manifest_payload = set(p_files.keys())
    omitted_runtime = expected_payload - manifest_payload
    if omitted_runtime:
        errors.append(f"Unexpected runtime file omitted from payload manifest: {sorted(omitted_runtime)}")
    else:
        print(f"[PASS] All {len(expected_payload)} expected runtime files are present in payload manifest.")

    extra_payload = manifest_payload - expected_payload
    if extra_payload:
        errors.append(f"Unexpected extra file in payload manifest: {sorted(extra_payload)}")
    else:
        print("[PASS] No unexpected extra files found in payload manifest.")

    # 7. Overall result
    if not errors:
        print("\n[VERIFICATION PASS] Zero errors. All entries, bytes, and SHA-256 hashes strictly match.")
        print("Read-only verification succeeded. Zero files or timestamps were altered.")
        return True
    else:
        print(f"\n[VERIFICATION FAIL] Encountered {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return False

def print_usage():
    print("HealthCalendar365 - Freeze Manifest & Evidence Tool")
    print("Usage:")
    print("  python scratch/reconcile_and_freeze.py --create   Generate payload & evidence manifests + checksums")
    print("  python scratch/reconcile_and_freeze.py --verify   Verify all entries and checksums (read only)")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print_usage()
    arg = sys.argv[1].lower()
    if arg == '--create':
        create_manifests()
    elif arg == '--verify':
        ok = verify_manifests()
        sys.exit(0 if ok else 1)
    else:
        print_usage()

if __name__ == '__main__':
    main()
