# Independent v1.28 handoff verification

**Follow-up verified:** the remaining data-cleanup and evidence qualifications below were subsequently addressed. See `FOLLOWUP_2026-10-27.md` and `followup_independent_verification.json`. Independent checks confirmed zero obsolete fields, unchanged card/source content and renderer, source/bundle parity, recomputed full-pixel comparison counts, and a fresh 2,190-render offline PASS. The new v1.28 scope/patch assertions also pass. The earlier findings below are retained as audit history.

Scope authorized by the owner: verify Claude's audit and reconcile staging with v1.28; no commit, push, deployment, further application fixes, or deletion. HEAD remains `5749793`. The index before reconciliation is preserved locally in `index_before_restage.backup`; this backup is not staged.

PASS: all 478 recovery archive records were independently read from `D:/HealthCalendar365_recovery/2026-10-27/HealthCalendar365_recovery_2026-10-27.zip` and matched recorded byte counts and SHA-256 hashes. All 183 deletion-manifest paths are absent. All 191 tracked deletions have corresponding archived originals. See `source_archive_verification.json`.

PASS: v1.28 has 264 runtime files and 264 precache entries. Every bundle file matches source, with no extra bundle files. An isolated rebuild reproduced `data/health_365.json` and `js/calendar-data.js` exactly.

PASS: fresh Chromium measurement of all 365 dates × two formats × three languages found zero measured heading/card overflow or truncated wrap calls, zero failed images, and zero page errors across 2,190 posters / 8,760 cards. This instruments actual rendered text calls and checks the current dataset; it is not a general proof against every possible future string. See `render_measurement.json`.

PASS: fresh offline browser verification loaded all 365 dates, fit a 390×844 viewport, supported search, installed all 264 cache entries, matched cached runtime-file hashes, preserved settings through offline reload, and rendered 2,190 poster combinations without browser exceptions. See `offline_verification.json`.

PASS: a fresh isolated v1.27→v1.28 upgrade removed the old cache, matched the updated runtime hashes, retained the exact uploaded-photo data URL and settings, and rendered 24 affected poster combinations offline. The archived test was copied locally with its report path redirected to this folder and its photo-retention check strengthened from presence to exact equality. See `upgrade_verification.json`.

PASS: fresh functional checks confirmed 365 unique dates / 1,460 cards, 208 decodable images, matching selected dates, English/Gujarati/date search, navigation wraparound, language/format state, 365 Reference detail panes, filter counts, Reference↔Studio synchronization, no approval controls, mobile width, and no browser errors. See `functional_verification.json`.

Download qualification: the original functional harness encountered canceled downloads using its default browser temporary location. A separate check of the unmodified app with `downloadsPath` explicitly inside this workspace saved valid 1080×1080 and 1080×1920 PNGs; no application fix was needed or applied. A test-only delayed-revocation comparison also passed and produced identical PNG sizes. See `download_verification.json`; canceled results remain in the raw functional report for transparency.

Visual scope: reviewed the six retained CPHC contact sheets covering all 140 square/vertical photo regions and inspected two before/after clipping examples. This is contact-sheet framing review, not clinical accuracy approval or physical-device testing.

## Qualifications and remedies

1. Approval-data cleanup is PARTIAL. `data/annual_review_2026.json` still contains 131 `governing_decision_id` fields and 131 `workflow_label` fields, including references to deleted DEC records. The active Reference code no longer reads these fields or exposes approval controls. Remedy: remove obsolete decision-link/workflow fields consistently from both JSON and its JS bundle while retaining useful source and change-history content, then rebuild and recheck parity. No such application edits were authorized or performed in this verification.
2. The claim that 1,763 outputs are byte-identical and all 427 changed outputs were previously flagged cannot be reproduced from the retained baseline evidence: `measure_before.json` contains no canvas hashes. The measurement script's current hash is a sampled 32-bit pixel hash, not byte-for-byte PNG comparison. Remedy: rerender preserved before/after builds and compare complete PNG bytes or full-image cryptographic hashes; report exact changed-key sets. Current overflow/truncation fixes independently pass.
3. `scratch/verify_all_cphc_framing.cjs` is a historical v1.27 test whose exact-renderer-scope assertion rejects the legitimate v1.28 typography changes. Other retained upgrade tests default to earlier releases. Remedy: label/version these tests clearly or add current tests without weakening their assertions. They have not been presented as v1.28 PASS checks.

Physical-device install/upgrade, real WhatsApp sharing/compression, and clinical accuracy remain NOT TESTED. No new cleanup decision was made for retained candidates, unique originals, artwork, or drafts.

## Staging scope

Re-stage current runtime/build inputs and audit-related documentation; include verified tracked deletions; remove staged-but-now-deleted approval files so a future commit cannot resurrect them. Preserve unrelated modified screenshots, older runtime-test outputs, and the pre-existing local-server change. Do not stage recovery archives, index backups, browser downloads, tool caches, image candidates, or unreferenced image sources. Stage selected independent verification records with these qualifications. Exact final paths and counts are recorded in `staging_summary.json` and `staged_files.txt` after reconciliation.

## Follow-up
See `FOLLOWUP_2026-10-27.md`: qualifications 1-3 above are resolved or restated there.
