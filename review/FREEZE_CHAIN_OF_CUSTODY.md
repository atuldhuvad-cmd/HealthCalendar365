# HealthCalendar365 — Freeze Chain of Custody & Identity Reconciliation Record


> **CURRENT-STATE NOTICE (2026-10-18):** This document contains historical checkpoint counts. The authoritative current state is `13 APPROVED / 27 PENDING / 0 REJECTED`; all 40 clinical copies are approved, while 27 records retain other human gates. See `review/approval_ledger_reconciliation_2026-10-18.json`.
**Date:** October 16, 2026  
**Status:** PRODUCTION HOLD ACTIVE — AUDIT & ACTIVATION GATE  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Authorized Expenditure:** USD 0.00 (Zero paid API calls, zero external spend)  
**Ledger State:** `0 APPROVED`, `31 PENDING_CLINICAL_SIGN_OFF`, `9 REJECTED_MISMATCH`  
**Candidate Identifier:** `CANDIDATE-HEALTH365-20261016-DECOUPLED`  
**Working Tree State:** `UNCOMMITTED_FREEZE_CANDIDATE`  
**Head Commit:** `e43caa77f5879a39e4b0d3d6d0678dc7716cc003`

---

## 1. Executive Summary

During activation of the Final Acceptance Phase, an automated integrity check detected an internal cryptographic discrepancy between the documented candidate freeze identity and the active working-tree manifest:

- **Documented Manifest SHA-256 (v1):** `4f8d29d772bfc2229c0ef244f615a5d12edf67453d94be08c4c4daf133fcc85e`  
- **Documented Candidate Size (v1):** 40,786,555 bytes  
- **Observed Manifest SHA-256 (v2):** `58a718fa92e29192012d5bf827cda46a324f7b368b199479c4a4a2241ece8034`  
- **Observed Candidate Size (v2):** 40,786,681 bytes  
- **Discrepancy:** +126 bytes

In accordance with mandatory governance rules, the Final Acceptance Phase was immediately **halted prior to recording any clinical, Gujarati, visual, or user acceptance decision**.

This document establishes the root cause of the discrepancy, formally supersedes both v1 and v2 identities, records the unrecoverable state of the overwritten v1 per-file records, and specifies the new decoupled, deterministic chain-of-custody architecture.

---

## 2. Chronology of Manifest Discrepancy & Root Cause Analysis

### 2.1 The Superseded Monolithic Freeze Identities (Historical Archive)

1. **Initial Monolithic Manifest (v1 - Revoked & Overwritten):**
   - **Original Path:** `review/final_acceptance_candidate_manifest.json` (overwritten on disk; not preserved in git)
   - **Documented SHA-256:** `4f8d29d772bfc2229c0ef244f615a5d12edf67453d94be08c4c4daf133fcc85e`
   - **Documented Candidate Size:** 40,786,555 bytes
   - **Tracked Files:** 147 files
   - **Historical Context:** Generated upon conclusion of the automated testing phase. The v1 file no longer exists and must not be reconstructed.

2. **Subsequent Monolithic Manifest (v2 - Revoked & Preserved):**
   - **Original Path:** `review/final_acceptance_candidate_manifest.json` (superseded active path)
   - **Preserved Archive Path:** [`review/superseded/final_acceptance_candidate_manifest_v2_58a718fa.json`](file:///d:/HealthCalendar365/review/superseded/final_acceptance_candidate_manifest_v2_58a718fa.json)
   - **Verified SHA-256:** `58a718fa92e29192012d5bf827cda46a324f7b368b199479c4a4a2241ece8034`
   - **Candidate Size:** 40,786,681 bytes
   - **Tracked Files:** 147 files
   - **Historical Context:** Generated during acceptance activation tooling execution; preserved unchanged in `review/superseded/` as historical audit evidence.

### 2.2 Root Cause: Architectural Circular Dependency

The discrepancy was caused by an architectural defect in the monolithic manifest design:
- The monolithic manifest included acceptance documentation ([`review/FINAL_ACCEPTANCE_PACKET.md`](file:///d:/HealthCalendar365/review/FINAL_ACCEPTANCE_PACKET.md) and [`review/FINAL_AUTOMATED_PHASE_REVIEW.md`](file:///d:/HealthCalendar365/review/FINAL_AUTOMATED_PHASE_REVIEW.md)) within its tracked candidate files.
- Concurrently, those acceptance documents attempted to cite the candidate manifest's own cryptographic digest and aggregate byte count.
- When the automated phase concluded, the documentation was edited to embed the v1 digest (`4f8d29d7...`) and size (`40,786,555 bytes`).
- These edits expanded the file sizes of the documents:
  - `review/FINAL_ACCEPTANCE_PACKET.md`: +82 bytes
  - `review/FINAL_AUTOMATED_PHASE_REVIEW.md`: +44 bytes
  - **Total Size Change:** $+82 + 44 = +126$ bytes.
- When `reconcile_and_freeze.py` was executed again during acceptance activation, it re-scanned all 147 files, detecting the expanded markdown files. The resulting candidate size shifted from 40,786,555 bytes to 40,786,681 bytes, altering the manifest SHA-256 to `58a718fa...`.
- Attempting to update the documents to reference `58a718fa...` would trigger another file change and another manifest invalidation, creating an unresolvable circular dependency.

### 2.3 Per-File Reconstruction Assessment

- When `reconcile_and_freeze.py` regenerated the manifest, the previous `review/final_acceptance_candidate_manifest.json` (v1) was overwritten in place on disk.
- Because v1 was an uncommitted file in the working tree, its exact per-file dictionary and file-level timestamp hashes were not archived in git history.
- **Custody Determination:** An exact byte-for-byte v1-to-v2 per-file comparison **cannot be reconstructed** from disk alone.
- However, forensic differential analysis verifies that the aggregate candidate size difference of exactly **126 bytes** is completely accounted for by the edits to the two documentation files noted above. Zero application runtime code, data, styles, fonts, or photographic assets were modified.

### 2.4 Formal Revocation & Supersession

Both earlier identities (`4f8d29d7...` and `58a718fa...`) are **formally revoked and superseded** due to structural invalidity. No release or acceptance decision may cite either digest.

---

## 3. Decoupled Chain-of-Custody Architecture

To eliminate circular dependencies and guarantee permanent mathematical determinism, the freeze design is decoupled into three independent components:

```
+-------------------------------------------------------------+
|               Runtime Application Payload                   |
|               (110 files | 38,588,400 bytes)                |
+-------------------------------------------------------------+
                              |
                              v
    |     review/candidate_payload_manifest.json        |
    |  (Stable Digest: 82b9e91823e983f263945dc7...)     |
    +---------------------------------------------------+
                              ^
                              | (Referenced by digest)
+-------------------------------------------------------------+
|              Acceptance & Verification Evidence             |
|              (40 files | Review, Audit, Tests)              |
+-------------------------------------------------------------+
                              |
                              v
    +---------------------------------------------------+
    |    review/acceptance_evidence_manifest.json       |
    |            (Excludes itself & checksums)          |
    +---------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|               review/freeze_checksums.sha256                |
|      (External checksums of both decoupled manifests)       |
+-------------------------------------------------------------+
```

### 3.1 Component 1: Candidate Payload Manifest
- **File:** [`review/candidate_payload_manifest.json`](file:///d:/HealthCalendar365/review/candidate_payload_manifest.json)
- **Scope:** Strictly the runtime files required to execute HealthCalendar365 in production.
- **Includes:**
  - Application shell: `index.html`, `manifest.json`, `sw.js`
  - Stylesheets: `css/styles.css`, `css/fonts.css`
  - JavaScript engine: `js/app.js`, `js/canvas-renderer.js`, `js/db.js`, `js/calendar-data.js`
  - Datasets: `data/health_365.json`, `data/approved_manifest.json`
  - PWA Icons: `icons/icon-192.png`, `icons/icon-512.png`
  - Bundled Fonts: 40 WOFF2 files in `fonts/`
  - Photographic Assets: 57 PNG files in `photos/`
- **Excludes:** All acceptance documents, audit reports, evidence JSONs, screenshots, scratch scripts, checksum files, and git metadata.
- **Metrics:**
  - **Total Runtime Files:** 110 files
  - **Total Runtime Payload Size:** 38,588,400 bytes (~36.80 MB)
  - **Payload Manifest SHA-256:** `82b9e91823e983f263945dc7f53fcdc64de66dde84b32ff1b5a9da64770193ce`
- **Invariance:** Because runtime code and assets are never modified during review, this digest is completely stable and invariant.

### 3.2 Component 2: Acceptance Evidence Manifest
- **File:** [`review/acceptance_evidence_manifest.json`](file:///d:/HealthCalendar365/review/acceptance_evidence_manifest.json)
- **Scope:** All review documents, audit reports, JSON test outputs, screenshots, and reconciliation/test scripts.
- **Includes:**
  - 23 Review & Governance Documents/JSONs in `review/`
  - 1 Preserved Historical Manifest in `review/superseded/` ([`review/superseded/final_acceptance_candidate_manifest_v2_58a718fa.json`](file:///d:/HealthCalendar365/review/superseded/final_acceptance_candidate_manifest_v2_58a718fa.json))
  - 9 Review Screenshots in `review/screenshots/`
  - 8 Verification & Reconciliation Scripts (`scratch/reconcile_and_freeze.py`, `scratch/test_*.cjs`, `test_remediation_round*.py`)
- **Excludes:**
  - `review/acceptance_evidence_manifest.json` (itself)
  - `review/candidate_payload_manifest.json` (tracked independently)
  - `review/freeze_checksums.sha256` (external binder)
  - Any file that would embed the evidence manifest's own digest.
- **Metrics:**
  - **Total Evidence Files:** 41 files
- **Reference Rule:** Acceptance documents ([`review/FINAL_ACCEPTANCE_PACKET.md`](file:///d:/HealthCalendar365/review/FINAL_ACCEPTANCE_PACKET.md) and [`review/FINAL_AUTOMATED_PHASE_REVIEW.md`](file:///d:/HealthCalendar365/review/FINAL_AUTOMATED_PHASE_REVIEW.md)) cite **only** the stable candidate payload manifest digest (`82b9e918...`). They do **not** cite the evidence manifest digest.

### 3.3 Component 3: External Checksums File
- **File:** [`review/freeze_checksums.sha256`](file:///d:/HealthCalendar365/review/freeze_checksums.sha256)
- **Scope:** External cryptographic binding file generated last.
- **Contents:**
  ```text
  82b9e91823e983f263945dc7f53fcdc64de66dde84b32ff1b5a9da64770193ce  review/candidate_payload_manifest.json
  [The current evidence-manifest digest is stored exclusively in review/freeze_checksums.sha256]  review/acceptance_evidence_manifest.json
  ```
- **Invariance:** Neither manifest includes `freeze_checksums.sha256`, preserving acyclicity. The current evidence-manifest digest is stored exclusively in [`review/freeze_checksums.sha256`](file:///d:/HealthCalendar365/review/freeze_checksums.sha256).

---

## 4. Verification Tooling & Safe Execution Model

The reconciliation script [`scratch/reconcile_and_freeze.py`](file:///d:/HealthCalendar365/scratch/reconcile_and_freeze.py) has been refactored with explicit command-line safeguards:

1. **`python scratch/reconcile_and_freeze.py --create`:**
   - Verifies the 110 runtime files, preserving `review/candidate_payload_manifest.json` content and timestamp unchanged when runtime files have not changed.
   - Constructs `review/acceptance_evidence_manifest.json` from the 41 evidence files.
   - Emits `review/freeze_checksums.sha256` with both digests.
   - Enforces pre-generation assertion checks preventing self-inclusion.

2. **`python scratch/reconcile_and_freeze.py --verify` (Read-Only Mode):**
   - Strictly read-only; modifies zero files and alters zero timestamps.
   - Validates that every entry in both manifests exists on disk with matching byte counts and SHA-256 digests.
   - Validates that aggregate byte sums and file counts match manifest headers.
   - Validates that both manifest digests match [`review/freeze_checksums.sha256`](file:///d:/HealthCalendar365/review/freeze_checksums.sha256).
   - Validates that no manifest includes itself or creates a circular dependency.
   - Validates that no runtime application file is omitted from the payload manifest.

3. **No-Argument Safety Guard:**
   - Invocation without `--create` or `--verify` prints usage instructions and exits with code `1`, making zero changes.

---

## 5. Governance, Spending, and Production Hold Invariants

1. **Production Hold Status:** **STRICTLY ACTIVE**.
   - No assets are promoted or released.
   - Ledger state remains `0 APPROVED`, `31 PENDING_CLINICAL_SIGN_OFF`, `9 REJECTED_MISMATCH`.
2. **Authorized Spending:** **USD 0.00**.
   - Zero external API calls were made or authorized.
3. **Clinical and Language Gate:**
   - Zero clinical medical decisions were recorded.
   - Zero Gujarati language decisions were recorded.
   - Zero user acceptance decisions were recorded.
   - All 10 human review domains remain cataloged as `DEFERRED_TO_FINAL_ACCEPTANCE`.
4. **Git Tree State:**
   - Zero commits, pushes, resets, cleans, or deployments were performed.
   - Working tree remains safely at `UNCOMMITTED_FREEZE_CANDIDATE` on branch `main` at commit `e43caa77f5879a39e4b0d3d6d0678dc7716cc003`.
