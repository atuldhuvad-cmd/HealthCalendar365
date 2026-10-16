# 365-Day Health Poster Studio — Project Memory & Visual Integrity Ledger

## 1. System Overview
- **Project Directory:** `D:\HealthCalendar365`
- **Total Health Observance Posters:** 368 posters (365 calendar days + separated multi-observance dates).
- **Core Visual Style:** Indian Clinical Editorial Style (4-card modular HTML5 Canvas, 1080×1080 Square + 1080×1920 Vertical Portrait).
- **Typography:** Plus Jakarta Sans (English) + Noto Sans Gujarati (ગુજરાતી) bilingual layout.

---

## 2. Visual Discrepancy Registry & Resolution Log

### A. Spotlight Week (Oct 15 – Oct 21) Resolved Discrepancies
| Date & Observance | Card | Issue Identified by User | Root Cause | Status & Corrective Action Taken |
|---|---|---|---|---|
| **Oct 17: World Trauma Day** | Card 1 | No Indian couple; seatbelts/helmets not prominent. | Generic Caucasian stock models used. | **RESOLVED:** Cropped authentic Indian couple driving with 3-point seatbelts prominently buckled across chests with kids in back (`oct17_do1.png`). |
| **Oct 17: World Trauma Day** | Card 2 | Generic graphic. | Missing urgent trauma scene. | **RESOLVED:** Cropped urgent phone call to 108 ambulance next to road accident victim (`oct17_do2.png`). |
| **Oct 17: World Trauma Day** | Card 3 | Generic driver. | Helmet discipline missing. | **RESOLVED:** Cropped certified full-face motorcycle helmet with visor and fastened chin strap (`oct17_dont1.png`). |
| **Oct 17: World Trauma Day** | Card 4 | Traffic bystander. | Golden hour care missing. | **RESOLVED:** Cropped CPR chest compressions and safe limb stabilization on resuscitation dummy (`oct17_dont2.png`). |
| **Oct 18: World Menopause Day** | Card 3 | Elderly male walking on stairs for female menopause topic. | Elderly male fall prevention panel from `art-healthy-ageing` mistakenly assigned to bone care. | **RESOLVED:** Replaced with authentic woman squatting with weights, calcium-rich diet (milk, almonds, greens), and bone model (`oct18_dont1.png`). |
| **Oct 18: World Menopause Day** | Card 4 | Woman exercising on "Qualified Gynecologist Consultation" card. | Panel inversion from `art-women-health`. | **RESOLVED:** Replaced with female doctor holding anatomical uterus model consulting female patient (`oct18_dont2.png`). |
| **Oct 19: Ear & Hearing Care** | Card 1 | Tooth with toothbrush image on ENT Ear Care card. | Direct cross-topic swap with Oral Health. | **RESOLVED:** Replaced with female ENT doctor explaining ear anatomy and acoustic sound waves (`oct19_ear_card1.png`). |
| **Oct 19: Ear & Hearing Care** | Card 3 | Smoker lungs image on Ear Buds warning card. | Direct cross-topic swap with Tobacco. | **RESOLVED:** Replaced with woman inserting cotton bud with red 'X' danger symbol (`oct19_ear_card3.png`). |
| **Oct 19: Oral Health & Tobacco** | Card 1 | Ear anatomy diagram on tooth brushing card. | Direct cross-topic swap with Ear Care. | **RESOLVED:** Replaced with sparkling clean tooth model and toothbrush (`oct19_oral_card1.png`). |
| **Oct 19: Oral Health & Tobacco** | Card 3 | Cotton bud in ear on Gutkha/Mawa/Tobacco card. | Direct cross-topic swap with Ear Care. | **RESOLVED:** Replaced with smoker black lung vs healthy lung and broken cigarette (`oct19_oral_card3.png`). |
| **Oct 20: World Osteoporosis Day** | Cards 1-4 | Caucasian/Asian seniors and traffic worker in hi-vis vest. No Indian culture. | Cropped from legacy generic sheets (`art-healthy-ageing`, `art-first-aid`). | **FLAGGED FOR REPLACEMENT:** Needs dedicated Indian elderly models, bathroom grab bars, and ragi/sesame nutrition. |
| **Oct 21: World Iodine Deficiency Day** | Cards 1-4 | Fridge containers and vegetable shield. No iodized salt or thyroid. | Cropped from generic `art-food-safety` (refrigeration). | **FLAGGED FOR REPLACEMENT:** Needs dedicated Indian kitchen setting with airtight glass/ceramic salt jars, crystal salt, and smiling sun iodized logo. |

---

## 3. Full-Year Scope: Generic Placeholder Contamination Audit
- **Total Posters:** 368
- **Posters with Dedicated Photo Assets:** 10 posters (40 cards)
- **Posters Defaulting to Category Placeholders:** 358 posters (1,432 cards)
  - `photos/cat_cardio.png`: 280 cards
  - `photos/cat_infection.png`: 284 cards
  - `photos/cat_mental.png`: 292 cards
  - `photos/cat_nutrition.png`: 284 cards
  - `photos/cat_yoga.png`: 292 cards

### High-Priority National & Global Health Days Requiring Dedicated Assets
1. **World Diabetes Day (Nov 14):** Blood glucose glucometer, walking shoes, bitter gourd/methi seeds, foot inspection.
2. **World Cancer Day (Feb 04):** Early screening, clinical mammogram/biopsy, oncology consultation, healthy lifestyle.
3. **World Tuberculosis Day (Mar 24):** Sputum test container, DOTS treatment completion, mask wearing, nutrition.
4. **World Malaria Day (Apr 25):** Mosquito bed nets, blood smear test, mosquito repellent, drainage.
5. **National Vaccination Day (Mar 16):** Pediatric vaccination cold-chain, baby immunization card, smiling nurse.
6. **World Mental Health Day (Oct 10):** Clinical counseling session, stress journaling, mindful walking, family support.
7. **World Heart Day (Sep 29):** Digital BP monitor, echocardiogram, heart-healthy diet, stair climbing.

---

## 4. Mandatory Quality Gates for All Calendar Assets

Every poster and photo asset must strictly adhere to these 5 gates:

1. **Gender & Physiological Concordance Gate:**
   - Female-specific health topics (Menopause, Cervical Cancer, Breast Health, Maternal Care) must ONLY depict female subjects and female specialists.
   - Male-specific health topics (Prostate Health, Men's Mental Health) must ONLY depict male subjects.
2. **Direct Subject Correlation Gate:**
   - The primary action or medical object described in the card title MUST be visually prominent in the image (e.g. Ear Care must show ears/ENT, Oral Care must show teeth/gums, Tobacco must show tobacco/lungs, Iodine must show iodized salt packaging).
3. **Authentic Indian Context Gate:**
   - Visuals must reflect authentic Indian families, domestic Indian kitchens, Indian roads (certified ISI full-face helmets, fastened seatbelts), and Indian clinical environments. No Western stock imagery.
4. **Zero Cross-Card Duplication Gate:**
   - No single poster may share identical images across its 4 cards. Every card must feature an independent, distinct perspective.
5. **Zero Cross-Topic Swap Gate:**
   - Sourced assets must undergo strict manual validation to prevent sprite-sheet crop inversion (e.g., ear panels placed into oral cards).

---

## 5. Independent Technical Audit Remediation Ledger (Oct 15, 2026)

**CURRENT STATUS: PARTIAL REMEDIATION VERIFIED — PRODUCTION HOLD REMAINS STRICTLY ACTIVE.**
Bulk generation, public release, and unverified deployment remain halted.

### A. Verified PASS Items (from `REMEDIATION_REVIEW_2026-10-15.md`):
1. **Isolated Output Paths:** All 1,472 predicted card target paths are strictly unique; the shared-category overwrite defect is eliminated for the current dataset.
2. **Automatic Service Worker Registration:** Clean browser session successfully registered Service Worker `v1.1` with active controller.
3. **Sampled Offline Coverage:** Unvisited White Cane Card 1, Ear Care Card 1, and Oral Health Card 2 loaded successfully offline.
4. **WhatsApp Caption Polarity:** Actual White Cane poster generated all four messages without an erroneous `DON'Ts` header.
5. **Dataset Parity:** `data/health_365.json` and `js/calendar-data.js` match.

### B. Newly Resolved Code & Platform Hygiene Blockers:
1. **Enforced Candidate Staging & Approval Gate (`generate_with_gemini.py`):**
   - Generated bytes no longer write directly to active production assets or datasets.
   - Raw generations save to `photos/staging/candidate_{day_id}_card{idx}.png` with an attempt record logged in `data/generation_journal.json`.
   - Dedicated `--promote` command requires validation of staged candidate images before moving to `photos/`.
2. **Crash-Resilient Atomic Dataset Writes (`generate_with_gemini.py`):**
   - Dataset files are written to `.tmp` files first, then promoted via atomic `os.replace()` to prevent partial/corrupted dataset state on interruption.
3. **Preservation of Mixed Card Types in WhatsApp Captions (`js/app.js`):**
   - `buildWhatsAppText` renders `doCards`, `dontCards`, and `infoCards` (neutral `message` type) independently. No card is ever dropped in mixed-type posters.
4. **Origin-Scoped Cache Cleanup (`sw.js`):**
   - Service Worker activate handler strictly purges caches prefixed with `health-poster-`, preventing accidental deletion of unrelated origin caches.
5. **Removal of Unsafe CORS Canvas Tainting (`js/canvas-renderer.js`):**
   - Removed the fallback that retried failed anonymous loads without CORS. Failed image loads resolve safely to `null` with a warning, protecting `canvas.toBlob()` from security tainting.
6. **Automated Precache Manifest Maintenance (`build_precache_manifest.py`):**
   - Automatically synchronizes all active files in `photos/` into `sw.js`, eliminating manual precache list maintenance.

### C. Round 2 Technical Audit Remediations Verified:
1. **Strict Approval Gate Enforced (`generate_with_gemini.py`):**
   - Promotion requires matching SHA-256 candidate hash in `data/approved_manifest.json` with `status: "APPROVED"`.
   - Minimum dimensions check (>= 720×540) strictly rejects 1×1 test dummy images or unreadable files.
   - Mutation-free `--dry-run` guaranteed across all flags.
2. **Transactional Multi-File Promotion & Interruption Recovery (`generate_with_gemini.py`):**
   - Atomic replacement across candidate images, JSON dataset, and JS dataset with automated rollback to in-memory/disk backup if interrupted.
3. **Forensic Quarantine for Journal History (`generate_with_gemini.py`):**
   - Malformed journal files are never overwritten; quarantined to timestamped files (`generation_journal.corrupt.<timestamp>.json`). Candidate filenames include timestamp and hash to prevent clobbering previous attempts.
4. **Active Reference Precache Derivation (`build_precache_manifest.py`):**
   - Derives manifest strictly from active dataset references, excluding unused photos; automatically triggered by promotion. Supports PNG, WebP, and WOFF2.
5. **Authority Label Provenance Verified (`js/canvas-renderer.js`):**
   - Rotational daily guidance now displays `🛡️ દૈનિક આરોગ્ય માર્ગદર્શન` / `🛡️ Daily Health Guidance` instead of unverified WHO/MoHFW badges. Only verified official observance dates display official observance badges.
6. **Mandatory Card Image Failure Guard (`js/canvas-renderer.js` & `js/app.js`):**
   - `exportPoster()` halts poster generation and alerts user if any required card photo fails to load, preventing export of incomplete posters across single download, batch download, and WhatsApp sharing.
7. **Offline Font Bundling (`fonts/` & `css/fonts.css`):**
   - 40 WOFF2 files for Noto Sans Gujarati & Plus Jakarta Sans bundled locally (1.03 MB), eliminating external CDN network dependency. 97 total precached assets.

### D. Round 3 Technical Audit Remediations Verified:
1. **Preserved Evidence & Superseded Unsupported Approvals (`data/approved_manifest.json`):**
   - Preserved initial trace as `data/approved_manifest.round2_evidence.json`.
   - Superseded all unsupported records: 9 mismatched assets (`10-19-oral` Card 2, `10-20` Cards 1–4, `10-21` Cards 1–4) explicitly marked `REJECTED_MISMATCH` with accountable audit findings.
   - All manifest entries strictly bound to a 64-character canonical `spec_hash` representing the card's polarity, titles, descriptions, and AI prompt. Stale or tampered card specifications automatically invalidate approval.
2. **Exhaustive Image Integrity & Full Pixel Decompression Gate (`generate_with_gemini.py`):**
   - Replaced shallow `.size` check with `verify_image_integrity_and_decode()`:
     - Structural chunk validation with `Image.open().verify()`.
     - Full decompression of all image pixels into memory with `Image.open().convert("RGB").load()`, strictly rejecting truncated PNGs.
     - Format-to-extension validation (`PNG` for `.png`, `WEBP` for `.webp`).
     - Minimum dimensions check ($\ge 720\times540$).
     - 4:3 aspect ratio enforcement (tolerance $1.25$ to $1.45$).
3. **Whole-Release Transactional Rollback Restoring Active Artwork (`generate_with_gemini.py`):**
   - All destination artwork targets (`photos/...`), datasets, and `sw.js` are backed up to disk (`data/transactions/<tx_id>/backup/`) before any file modification.
   - Catches `BaseException` (including `SystemExit` and `KeyboardInterrupt`). On failure, completely restores original active artwork bytes, deletes partially created files, restores datasets, and resynchronizes the precache manifest.
4. **Durable Startup Crash Recovery (`generate_with_gemini.py`):**
   - `recover_unfinalized_transactions()` runs at script startup. If a process crash, kill signal, or power outage interrupts promotion, the on-disk plan (`data/active_transaction.json` and `tx_plan.json`) is automatically detected and rolled back, safely restoring the complete release.
5. **Sourced Authority Provenance Metadata (`data/health_365.json`, `js/calendar-data.js`, `js/canvas-renderer.js`):**
   - Completely eliminated hardcoded allowlists. Each day stores structured `provenance` metadata with authority (`WHO`, `MoHFW`, `WHO_FAO`, `WHO_IMS`, `GLOBAL_OBSERVANCE`, `DAILY_GUIDANCE`), verification status, official source name, and citation URL.
   - Rotational daily wellness days correctly render `🛡️ દૈનિક આરોગ્ય માર્ગદર્શન` / `🛡️ Daily Health Guidance`. World Trauma Day renders `🛡️ Global Trauma Prevention Day` rather than an unverified WHO badge.
6. **Zero External Font Requests (`index.html`):**
   - Removed redundant Google Fonts links and preconnects from `index.html`. Typography runs 100% on bundled local WOFF2 files via `css/fonts.css`.

### E. Round 4 Technical Audit Remediations Verified:
1. **Fail-Closed Crash Recovery & Pointer Preservation (`generate_with_gemini.py`):**
   - Recovery fails closed: if ANY planned backup file is missing or fails pre-transaction SHA-256 verification, recovery halts with `RuntimeError`, refuses to mark `ROLLED_BACK`, and preserves `data/active_transaction.json` and plan on disk for manual investigation.
   - Corrupt active pointer files are never silently deleted; quarantined as evidence to `data/active_transaction.corrupt.<timestamp>.json`.
2. **Strict Zero-Mutation Dry-Run Guarantee (`generate_with_gemini.py`):**
   - Dry-run mode (`--dry-run`) is checked before recovery. Pending recoveries are reported as previews without mutating any files, directories, pointers, or transaction plans.
3. **Clinical QA Contradiction Rejection & Removal of Invented Sign-Offs (`generate_with_gemini.py` & `data/approved_manifest.json`):**
   - Preserved evidence to `data/approved_manifest.round3_evidence.json`. All 31 unverified cards marked `PENDING_CLINICAL_SIGN_OFF`; invented committee names removed. Zero assets are approved until demonstrated clinical review occurs.
   - Promotion gate enforces all QA checks: candidate is strictly rejected if `visual_concordance`, `cultural_authenticity`, or `polarity_match` is `FAIL` or `UNKNOWN`, even if status was labeled `APPROVED`.
4. **Exact Sourced Event/Date Provenance Decoupling (`data/health_365.json` & `js/calendar-data.js`):**
   - October 15 Handwashing accurately cites Global Handwashing Partnership (`globalhandwashing.org/global-handwashing-day/`), correcting the erroneous citation of May 5 World Hand Hygiene Day.
   - Separate `observance_source_url` (public event page) and `clinical_source_url` (MoHFW/CDC guidelines) stored independently. Local `.local` URLs removed.
   - October 16 World Food Day accurately cites UN FAO; October 17 Trauma Day renders `World Trauma Prevention Day` without false WHO badge.

### F. Round 5 Technical Audit Remediations Verified:
1. **Read-Only Preflight Verification Before File Mutation (`generate_with_gemini.py`):**
   - Recovery and rollback now run `validate_transaction_backups_preflight()` across all planned backups *before* any destination file is opened, copied, or touched.
   - If ANY backup is missing, corrupt, empty, or mismatches the recorded hash, recovery halts immediately with `RuntimeError`. Zero target files are touched.
2. **Mandatory Pre-Transaction Hashes in Schema (`generate_with_gemini.py`):**
   - Plans without `pre_transaction_hashes` are strictly rejected during preflight. Hash verification cannot be bypassed.
3. **Atomic File Restoration & Verification (`generate_with_gemini.py`):**
   - Files are restored via atomic write (`.tmp` write followed by `os.replace`), and post-restoration file hashes are verified against expected pre-transaction hashes before finalizing recovery.
4. **Complete Test Suite Isolation Across All Test Rounds (`test_remediation_round3.py`, `test_remediation_round4.py`, `test_remediation_round5.py`):**
   - All tests run inside temporary fixture directories (`tempfile.mkdtemp()`).
   - Real transaction pointers (`data/active_transaction.json`), manifests (`data/approved_manifest.json`), datasets, and forensic evidence (`data/active_transaction.corrupt.*`) are NEVER modified, overwritten, or deleted by any test run.

---

### G. Active Release Blockers & Status:
1. **Production Hold Status:** STRICTLY ACTIVE. No bulk generation runs or public deployments without prior explicit verification and clinical approval.
2. **Clinical Imagery Gap (1,432 Placeholder Cards):** 358 posters still rely on 5 generic category placeholders.
3. **Spotlight Week Remaining Mismatches:**
   - Oct 19 Oral Health Card 2: Interdental flossing shown on "Rinse Mouth Vigorously After Meals" (recorded as `REJECTED_MISMATCH`).
   - Oct 20 Osteoporosis: Caucasian/Asian stock models & traffic worker lack authentic Indian elder fall-prevention imagery (all 4 cards recorded as `REJECTED_MISMATCH`).
   - Oct 21 Iodine Deficiency: Refrigerator & salad shield lack authentic Indian kitchen salt storage / iodized logo imagery (all 4 cards recorded as `REJECTED_MISMATCH`).
   - *Status:* Replacements must be generated, clinically verified, and approved with explicit `spec_hash` and reviewer metadata before promotion into active production.
4. **Pending Verification:** Live image API generation, physical Android behavior, and real WhatsApp sharing remain **NOT TESTED**.
