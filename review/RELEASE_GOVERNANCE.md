# HealthCalendar365 — Release Governance & Quality Assurance Standard

**Document Version:** 1.0.0  
**Effective Date:** October 16, 2026  
**Status:** ACTIVE — PRODUCTION HOLD MANDATORY  
**Repository Target:** `atuldhuvad-cmd/HealthCalendar365` (`D:\HealthCalendar365`)  
**Git Baseline Commit:** `e43caa77f5879a39e4b0d3d6d0678dc7716cc003`

---

## 1. Scope and Authority

This document defines the release governance, evidence standards, reviewer qualifications, approval vocabulary, change-control procedures, and authorization gates for **HealthCalendar365**. 

HealthCalendar365 is a public-facing, offline-first Progressive Web App (PWA) delivering bilingual (English and Gujarati) daily clinical health guidance to Indian doctors, healthcare professionals, and citizens. Because health guidance directly impacts patient decisions and disease prevention, **no asset, text string, or build may be promoted, deployed, or declared approved without satisfying the verifiable criteria defined herein**.

---

## 2. Reviewer Roles and Qualification Requirements

Every approved asset and copy string requires documented review by qualified, identifiable individuals. Anonymous, fabricated, synthetic, or unverified approvals are strictly invalid and void.

### 2.1 Clinical Medical Reviewer
- **Qualifications:** Registered medical professional (MBBS, MD, MS, BDS, or equivalent recognized qualification) or accredited public health specialist (MPH).
- **Competence Areas:**
  - Accuracy of medical claims against current peer-reviewed evidence and clinical guidelines (e.g., WHO, CDC, IOF, ICMR, MoHFW).
  - Validation that clinical polarity (positive action vs. negative avoidance) prevents patient harm.
  - Verification that recommended health actions are safe, clinically indicated, and free of unsupported causal claims.
  - Ensuring no promotion of unprescribed pharmaceuticals, extreme diets, or pseudo-scientific remedies.

### 2.2 Gujarati Language & Cultural Reviewer
- **Qualifications:** Native Gujarati speaker with proven fluency in formal written Gujarati and health communication experience, or a registered Gujarati-speaking clinician.
- **Competence Areas:**
  - Semantic agreement between English clinical guidance and Gujarati vernacular text.
  - Grammatical accuracy, formal honorifics, and appropriate medical terminology (e.g., distinguishing *ઓસ્ટીયોપોરોસીસ* [osteoporosis] from *ગલગંડ* [goiter]).
  - Typographic fidelity of complex Gujarati ligatures and conjuncts (*દ્વારા*, *શ્રવણ*, *શ્રી અન્ન*) to prevent rendering anomalies (such as dotted circles or broken vowel matras).
  - Cultural respectfulness and tone appropriate for diverse Gujarati households.

### 2.3 Visual Concordance & Production Reviewer
- **Qualifications:** Technical production engineer or visual design reviewer familiar with responsive canvas rendering and Indian cultural context.
- **Competence Areas:**
  - Visual concordance between the card’s clinical prompt and the rendered image.
  - Cultural authenticity: ensuring genuine Indian domestic, dietary, and clinical settings (e.g., stainless steel thalis, Indian non-slip grab bars, certified ISI helmets, authentic Indian senior citizens) rather than Western stock photography.
  - Strict absence of prohibited elements (commercial logos, watermarks, distorted hands/limbs, artificial text, graphic trauma).
  - Framing and safe cropping verification across both $1080\times1080$ px (square WhatsApp feed) and $1080\times1920$ px (vertical WhatsApp story) aspect ratios.

---

## 3. Required Evidence Fields for Every Review Decision

Every decision entered into the project's decision registers or approval ledgers must contain the following mandatory fields:

1. **Reviewer Name:** Full legal or professional name of the reviewer.
2. **Reviewer Role & Qualifications:** Specific credential (e.g., `MBBS, MD (Medicine)`, `Clinical Linguist`).
3. **Organization / Affiliation:** Professional institution, clinic, hospital, or editorial body.
4. **Decision Date:** ISO 8601 timestamp (e.g., `2026-10-16T14:00:00Z`).
5. **Formal Decision:** Must be one of `ACCEPT`, `REJECT`, or `REVISION_REQUIRED`.
6. **Written Rationale:** Detailed justification explaining why the criteria were satisfied or failed.
7. **Bound Image SHA-256:** 64-character hexadecimal SHA-256 checksum of the exact image evaluated.
8. **Bound Card Specification SHA-256:** 64-character hexadecimal checksum of the canonical specification.
9. **Primary Source Evidence:** Authoritative reference URL, guideline document, or published study (where applicable).

Any record lacking any of these fields, or whose hashes do not match the current working tree, is classified as **`PENDING`** and cannot be used to promote assets.

---

## 4. Controlled Approval and Rejection Vocabulary

To prevent ambiguity, only the following status tokens may be used across the codebase, manifests, and documentation:

| Vocabulary Token | Meaning | Gate Effect |
| :--- | :--- | :--- |
| **`APPROVED`** | Verified, signed by qualified reviewers, bound to current hashes, and promoted to active database. | Release Eligible |
| **`PENDING_CLINICAL_SIGN_OFF`** | Generated or cropped asset exists, but lacks qualified human reviewer signature. | **BLOCKED** from release |
| **`REJECTED_MISMATCH`** | Asset evaluated and failed one or more clinical, visual, or cultural gates. | **BLOCKED** from release |
| **`READY_TO_REQUEST_AUTHORIZATION`** | Specifications, prompts, and safety rules are frozen and independent of copy changes; ready for spend authorization. | Awaiting User Sign-off |
| **`BLOCKED_PENDING_COPY_APPROVAL`** | Visual prompt depends on contested or revised clinical copy; image generation prohibited until copy is signed. | **BLOCKED** from generation |
| **`STRUCTURAL_RENDER_PASS`** | Automated render confirms canvas dimension conformance ($1080\times1080$, $1080\times1920$) and image decoding. | Visual/Clinical Review Pending |
| **`NOT TESTED`** | Verification requires physical target hardware or specific environmental conditions that have not been executed. | Explicitly Unverified |
| **`DEFERRED_TO_FINAL_ACCEPTANCE`** | Test requires physical device, target hardware, or qualified human review; explicitly deferred to final acceptance packet. | **BLOCKED** from release until signed |
| **`BLOCKED`** | Execution or promotion halted due to unsatisfied prerequisite or policy constraint. | **BLOCKED** from release |
| **`UNKNOWN`** | Status cannot be determined from available records. | Fail-Closed |

---

## 5. Image and Specification Hash-Binding Rules

Approval records are strictly cryptographically bound to prevent unauthorized or silent mutations:

1. **Image Hash:** `SHA256(image_bytes)` computed directly from the PNG file in `photos/`.
2. **Canonical Specification Hash:** `SHA256(canonical_json_bytes)` computed from the normalized card specification dictionary:
   ```json
   {
     "day_id": "10-15",
     "card_idx": 1,
     "title_en": "Use Soap & Clean Water",
     "title_gu": "સાબુ અને સ્વચ્છ પાણીનો ઉપયોગ કરો",
     "desc_en": "Lather all hand surfaces thoroughly including palms, between fingers, and under nails for at least 20 seconds.",
     "desc_gu": "હથેળી, આંગળીઓની વચ્ચે અને નખ સહિત ૨૦ સેકન્ડ સુધી સાબુથી ફીણ કરીને હાથ સારી રીતે ઘસો.",
     "polarity": "positive",
     "prompt": "Ultra-photorealistic 4:3 close-up photograph of...",
     "safety_rules": ["..."]
   }
   ```
3. **Invalidation Rule:** Any modification to English copy, Gujarati copy, clinical instructions, polarity, or image generation prompt **immediately invalidates the previous specification hash**.
4. **Re-Review Requirement:** If the specification hash changes, any previous clinical or visual approval is null and void; the card returns to `PENDING_CLINICAL_SIGN_OFF` and requires a new review cycle.

---

## 6. Image-Generation Authorization and Spending Controls

External image generation via AI APIs involves financial expenditure, asset replacement, and computational execution. The following controls apply permanently:

1. **Zero-Spend Default:** The authorized spending baseline is **USD 0.00**.
2. **Pre-Flight Model and Pricing Verification:** Immediately before requesting authorization, the engineer must verify:
   - Official availability of the selected model ID.
   - Published API pricing per generation attempt on the provider's official pricing page.
3. **Spend Authorization Sheet:** An explicit authorization request must be submitted to the project owner specifying:
   - Target card slot IDs.
   - Provider name and exact model identifier.
   - Maximum allowed generation attempts per slot (default: 2 attempts).
   - Estimated cost per attempt and strict total budget cap (e.g., USD 0.40 for 4 pilot cards).
4. **Staging Directory Isolation:**
   - Generated assets must **never** be written directly into `photos/`.
   - All generated candidates must be saved exclusively to `photos/staging/` using an immutable naming convention: `photos/staging/candidate_{day_id}_{card_idx}_v{attempt}.png`.
5. **Generation Journaling:** Every API call, whether successful or failed, must be logged in `data/generation_journal.json` with timestamp, prompt, model, seed/request ID, response status, and SHA-256 of the output.
6. **No Automatic Retries:** If a generation attempt fails or produces a flawed image, the script must not automatically loop or burn budget; it must halt and record the result.

---

## 7. Promotion Authorization Procedure

Promoting candidate images from `photos/staging/` to active production in `photos/` must follow an atomic, fail-closed transaction protocol:

1. **Pre-Promotion Verification (Dry-Run):**
   - Candidate PNG decodes completely without corruption.
   - Dimensions meet or exceed $720\times540$ px with a $4:3$ aspect ratio ($1.33 \pm 0.05$).
   - Candidate has a verified `APPROVED` record signed by a qualified clinical reviewer.
   - Canonical specification hash matches the current copy in `data/health_365.json`.
2. **Atomic Transaction Execution:**
   - Pre-transaction SHA-256 hashes of all active targets are snapshotted.
   - Preflight verification ensures all existing targets are backed up in `data/transactions/{tx_id}/backup/`.
   - Backup files are hashed and verified against the live pre-transaction hashes *before* any file is touched.
   - Images are moved atomically into `photos/`.
   - `build_precache_manifest.py` is invoked with isolated `project_dir` parameter.
   - Manifest rebuild must succeed and return `True` before the transaction can be marked `FINALIZED`.
3. **Rollback Guarantee:**
   - If manifest building fails or any error occurs, the promotion engine automatically triggers `restore_from_backup()`, reverting all modified targets and retaining the transaction pointer in a `BLOCKED` state.
   - The transaction pointer is cleared only upon 100% verified success.

---

## 8. Git Branch, Review, Merge, and Release Procedure

The repository at `https://github.com/atuldhuvad-cmd/HealthCalendar365.git` is **PUBLIC**. Strict hygiene rules govern all version control actions:

### 8.1 Branching Strategy
- **`main`:** Protected release branch. Reflects tested, deployable, and approved production states only. Direct pushes to `main` are prohibited.
- **`batch/{name}`:** Work branches for specific batches or features (e.g., `batch/spotlight-pilot-4cards`, `batch/month-11-acceptance`).
- **Commits:** Atomic, descriptive commit messages documenting exact changes.

### 8.2 Privacy and Secrets Gate
Before any branch is pushed or merged, the working tree and commit diffs must be scanned:
- Zero API keys, passwords, or tokens.
- Zero local transaction logs (`data/transactions/`), candidate staging folders (`photos/staging/`), or temporary scratch files.
- Zero private reviewer contact details (e.g., personal phone numbers or email addresses).

### 8.3 Recommended GitHub Branch Protection Settings for `main`
To enforce release governance at the GitHub repository level, the following settings are established:

```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "automated-integrity-check",
      "remediation-regression-suites",
      "precache-manifest-validation"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": true
}
```

*Command to apply once authorized:*
```bash
gh api --method PUT repos/atuldhuvad-cmd/HealthCalendar365/branches/main/protection --input branch_protection.json
```

---

## 9. Deployment Authorization Procedure

Deployment to public production hosting (GitHub Pages / Cloudflare Pages) is governed by strict release gates:

1. **Preview Verification First:** Every release candidate must first be built and verified in a temporary preview deployment or isolated local HTTP environment.
2. **Immutable Commit Binding:** Production deployment requests must name the **exact Git commit SHA** and tag (e.g., `v1.0.0`).
3. **Cache-Busted Verification:** After deployment, the live URL must be tested with cache-busting query parameters to verify:
   - Root `index.html` loads cleanly.
   - `sw.js` registers and pre-caches the designated assets.
   - Web App Manifest (`manifest.json`) and high-resolution icons are accessible.
   - Offline fonts (`NotoSansGujarati.woff2`, `PlusJakartaSans.woff2`) load correctly.
   - Zero staging or test review files are exposed.
4. **Explicit Authorization:** Removal of the production hold and triggering public deployment requires explicit, written human authorization.

---

## 10. Rollback Ownership and Forensic Evidence Retention

In the event of an undetected clinical defect, rendering corruption, or deployment regression:

1. **Rollback Ownership:** The Technical Lead and Clinical Review Lead retain joint authority to execute immediate emergency rollbacks.
2. **Automated Rollback Tooling:** Rollback is executed using `python run_image_pipeline.py --rollback {transaction_id}`.
3. **Forensic Evidence Retention:**
   - Quarantined transaction files (`data/*.quarantine*`) and unfinalized transaction plans must never be deleted; they must be preserved offline for post-mortem analysis.
   - Corrupt files or failed candidate generations must be preserved in `scratch/forensics/` with their SHA-256 hashes recorded.
4. **Remediation Protocol:** Any post-release defect requires the full cycle: `AUDIT` → `BACKUP` → `SANITIZE` → `VERIFY` → `TEST` → `APPROVAL` → `RELEASE`.

---

## 11. Offline Runtime & Service Worker Verification Gate

Automated technical verification of the service worker, offline runtime, canvas rendering, and typography must be completed before advancing to human acceptance:

1. **Automated Runtime Standard:**
   - Real browser execution via headless Chromium loopback (`127.0.0.1`).
   - Verified active service worker registration and client control (`navigator.serviceWorker.controller`).
   - Cache Storage population verified with $\ge 90$ app-shell, font, and photo assets in `health-poster-*`.
   - Complete offline execution with network severed at browser level (`context.setOffline(true)`).
   - Dynamic canvas poster rendering in all six layout/language combinations with zero broken images.
   - Distinct webfont glyph metrics verifying offline Gujarati typography (`Noto Sans Gujarati`).
   - Cold launch verification from an empty in-memory browser tab while offline.
   - Safe scoped cache eviction verifying obsolete application caches are pruned while foreign/unrelated origin caches remain strictly intact.
   - Document `scrollWidth <= innerWidth` across mobile viewports (320px, 360px, 390px, 412px).
2. **Current Audit Status:**
   - Verified 26/26 checks passed in [`review/RUNTIME_OFFLINE_PWA_TEST_REPORT.md`](file:///d:/HealthCalendar365/review/RUNTIME_OFFLINE_PWA_TEST_REPORT.md).
3. **Strict Boundary with Human Acceptance:**
   - Automated mobile viewport emulation confirms technical CSS layout only; it does **not** constitute physical Android device sign-off.
   - All physical hardware, manual PWA installation, WhatsApp compression, clinical review, and Gujarati linguistic evaluations remain strictly categorized as **`DEFERRED_TO_FINAL_ACCEPTANCE`**.
