# HealthCalendar365 — Real Browser Service-Worker & Offline-Runtime Verification Report


> **CURRENT-STATE NOTICE (2026-10-18):** This document contains historical checkpoint counts. The authoritative current state is `13 APPROVED / 27 PENDING / 0 REJECTED`; all 40 clinical copies are approved, while 27 records retain other human gates. See `review/approval_ledger_reconciliation_2026-10-18.json`.
**Date:** October 16, 2026  
**Document ID:** `REPORT-RUNTIME-OFFLINE-PWA-20261016`  
**Execution Environment:** Headless Chromium (Playwright / Node.js) on Local HTTP Loopback (`127.0.0.1`)  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Status:** ALL 26 AUTOMATED RUNTIME CHECKS PASSED (100%)  
**Production Hold:** STRICTLY ACTIVE (Authorized Spending: USD 0.00)

---

## 1. Executive Summary

An automated suite of real browser service-worker, offline-runtime, canvas rendering, typography, cold-launch, and cache-eviction tests was executed against `D:\HealthCalendar365` using headless Chromium controlled via Playwright.

All verification steps evaluated actual runtime execution in browser memory and Cache Storage rather than static source code inspection. Every automated runtime test passed with zero errors. All physical-device, manual PWA installation, WhatsApp compression, and human clinical/language evaluations are deferred to the final acceptance phase.

### Key Metrics:
- **Total Automated Runtime Checks:** 26
- **PASS:** 26 (100%)
- **FAIL:** 0
- **Browser Console Errors:** 0
- **Unhandled Page Exceptions:** 0
- **Financial Expenditure:** USD 0.00
- **Deferred Acceptance Items:** 10 (Cataloged as `DEFERRED_TO_FINAL_ACCEPTANCE`)

---

## 2. Test Execution Matrix

| Domain | Verification Item | Specification / Criteria | Result | Observed Evidence |
| :--- | :--- | :--- | :---: | :--- |
| **Online SW** | Root URL Loading | HTTP 200 via local HTTP loopback | **PASS** | HTTP Status: `200 OK` |
| **Online SW** | SW API Support | `navigator.serviceWorker` in browser context | **PASS** | Supported in Chromium runtime |
| **Online SW** | SW Registration | `navigator.serviceWorker.ready` resolves | **PASS** | `http://127.0.0.1:port/sw.js`, state: `activating` |
| **Online SW** | SW Page Controller | Worker controls active client after reload | **PASS** | `navigator.serviceWorker.controller` is active |
| **Cache Storage**| Application Cache Name | Scoped cache `health-poster-v1.1` created | **PASS** | `health-poster-v1.1` present in `caches.keys()` |
| **Cache Storage**| Precache Asset Volume | Complete app-shell, fonts, and photos cached | **PASS** | 97 assets cached on initial install |
| **Viewport** | Online Layout (360px) | `document.scrollWidth <= 360px` | **PASS** | `scrollWidth: 360px` matches `innerWidth: 360px` |
| **Viewport** | Online Layout (412px) | `document.scrollWidth <= 412px` | **PASS** | `scrollWidth: 412px` matches `innerWidth: 412px` |
| **Offline Switch**| Context Offline Toggle | `context.setOffline(true)` cuts network | **PASS** | Network disabled at browser layer |
| **Offline Reload**| Offline Root Reload | Document loads and renders from cache | **PASS** | Title loaded, 368 posters in memory, canvas initialized |
| **Viewport** | Offline Layout (360px) | `document.scrollWidth <= 360px` | **PASS** | `scrollWidth: 360px` matches `innerWidth: 360px` |
| **Viewport** | Offline Layout (412px) | `document.scrollWidth <= 412px` | **PASS** | `scrollWidth: 412px` matches `innerWidth: 412px` |
| **Offline Nav** | Date Stepping | Prev/Next navigation operates offline | **PASS** | `10-15` -> Prev (`10-14`) -> Next (`10-15-cane`) |
| **Canvas Export**| Offline Square English | $1080\times1080$ px canvas, valid PNG | **PASS** | Size $1080\times1080$, DataURL: 1.86 MB, 0 broken images |
| **Canvas Export**| Offline Square Gujarati | $1080\times1080$ px canvas, valid PNG | **PASS** | Size $1080\times1080$, DataURL: 1.89 MB, 0 broken images |
| **Canvas Export**| Offline Square Bilingual| $1080\times1080$ px canvas, valid PNG | **PASS** | Size $1080\times1080$, DataURL: 2.00 MB, 0 broken images |
| **Canvas Export**| Offline Vertical English| $1080\times1920$ px canvas, valid PNG | **PASS** | Size $1080\times1920$, DataURL: 2.89 MB, 0 broken images |
| **Canvas Export**| Offline Vertical Gujarati| $1080\times1920$ px canvas, valid PNG | **PASS** | Size $1080\times1920$, DataURL: 2.93 MB, 0 broken images |
| **Canvas Export**| Offline Vertical Bilingual| $1080\times1920$ px canvas, valid PNG | **PASS** | Size $1080\times1920$, DataURL: 3.05 MB, 0 broken images |
| **Offline Fonts**| Gujarati Font Cache | Noto Sans Gujarati loaded from cache | **PASS** | 6 active loaded faces, `check('bold 24px') === true` |
| **Offline Fonts**| Metric Distinction | Glyph width distinct from generic fallbacks | **PASS** | Noto: 385.4px vs Monospace: 477.7px vs Sans-Serif: 426.8px |
| **Cold Launch** | Cold Offline Start | Clean window launch without memory state | **PASS** | Brand new page in offline context loads 368 posters |
| **Recovery** | Online Network Restored | Seamless recovery upon restoring network | **PASS** | Zero console errors, full DOM reactivity |
| **SW Update** | Version Upgrade | New worker installs, activates, claims | **PASS** | `health-poster-v1.2` activated and controlling |
| **Cache Eviction**| Obsolete Cache Deletion| Stale `health-poster-*` caches pruned | **PASS** | `health-poster-v1.0` and `v1.1` removed |
| **Cache Eviction**| Foreign Cache Safety | Unrelated origin caches strictly preserved | **PASS** | `unrelated-third-party-cache-v1` preserved |

---

## 3. Detailed Runtime Verification Evidence

### 3.1 Service Worker Lifecycle & Page Control
- **Registration URL:** `http://127.0.0.1:port/sw.js`
- **Initial Active State:** `activating` transitioning to `activated` via `self.clients.claim()`
- **Controller Binding:** Confirmed active on subsequent requests (`navigator.serviceWorker.controller !== null`).

### 3.2 Cache Storage Contents (Initial State)
- **Primary Cache Name:** `health-poster-v1.1`
- **Total Precached Entries:** **97**
- **Corrected Precache Asset Breakdown:**
  - **Root & Application Shell (5):** `./`, `./index.html`, `./manifest.json`, `./css/styles.css`, `./css/fonts.css`
  - **JavaScript Logic (4):** `./js/app.js`, `./js/canvas-renderer.js`, `./js/db.js`, `./js/calendar-data.js`
  - **Clinical Data (1):** `./data/health_365.json`
  - **High-Resolution Icons (2):** `./icons/icon-192.png`, `./icons/icon-512.png`
  - **Bundled Fonts (40):** 20 `Noto Sans Gujarati` + 20 `Plus Jakarta Sans` WOFF2 files
  - **Active Photographic Assets (45):** 45 active card graphics in `./photos/`
- **Total Verification:** $5 + 4 + 1 + 2 + 40 + 45 = 97$ entries verified matching `sw.js`.

### 3.3 Offline Date Navigation & Poster Rendering
- Navigating previous day stepped from `10-15` (Global Handwashing Day) to `10-14`.
- Navigating next day stepped to `10-15-cane` (World White Cane Day) and loaded observance metadata seamlessly from browser memory.
- Dynamic HTML5 canvas poster generation was executed completely offline across all six layout/language pairs.
- In every execution, all four photo assets were decoded with `naturalWidth > 0` and zero broken image errors (`brokenImages: 0`).

### 3.4 Gujarati Offline Typography & Metric Distinction
To verify that Gujarati text was rendered with the intended cached web font rather than falling back to a system font:
1. `document.fonts.check('bold 24px "Noto Sans Gujarati"')` returned `true`.
2. Active FontFace instances for `Noto Sans Gujarati` registered with `status === 'loaded'`.
3. An offscreen 2D canvas rendered the Gujarati test phrase:
   `"આરોગ્ય કેલેન્ડર ૩૬૫ - વિશ્વ હાથ ધોવા દિવસ"`
   - **Noto Sans Gujarati Width:** **385.4 px**
   - **Monospace Fallback Width:** **477.7 px**
   - **Generic Sans-Serif Width:** **426.8 px**
4. The web font metric is distinct by over 92 px from monospace and 41 px from generic sans-serif, confirming genuine web font rasterization.

### 3.5 Cold Offline Launch
Fresh page opened in the same offline browser context after the original page was closed; page-level JavaScript memory was discarded while the origin’s service worker and Cache Storage remained available.
1. Active page and all in-memory JavaScript state were destroyed (`page.close()`).
2. Browser context remained strictly offline (`context.setOffline(true)`).
3. A fresh page (`context.newPage()`) in the same offline context was opened and navigated to `http://127.0.0.1:port/`.
4. Page shell loaded from Cache Storage via the service worker, initialized `window.HEALTH_CALENDAR_DATA` with all 368 records, and bound the interactive canvas.

### 3.6 Service Worker Update & Scoped Cache Eviction
To verify cache upgrade safety:
1. Two test caches were injected:
   - Obsolete application cache: `health-poster-v1.0`
   - Unrelated origin cache: `unrelated-third-party-cache-v1`
2. Service worker update simulation served `CACHE_NAME = 'health-poster-v1.2'`.
3. `navigator.serviceWorker.ready.then(reg => reg.update())` triggered the upgrade.
4. The updated worker installed, precached assets into `health-poster-v1.2`, called `self.skipWaiting()`, and activated.
5. Cache inspection after upgrade:
   - `health-poster-v1.2`: **PRESENT**
   - `health-poster-v1.1`: **EVICTED**
   - `health-poster-v1.0`: **EVICTED**
   - `unrelated-third-party-cache-v1`: **PRESERVED** (Zero collateral deletion)

---

## 4. Screenshot Evidence Register

All nine key application states were captured in headless Chromium and persisted under `review/screenshots/`:

| Screenshot File | Resolution | Verification Phase | Observed Visual State |
| :--- | :---: | :--- | :--- |
| [`online_360x740.png`](file:///d:/HealthCalendar365/review/screenshots/online_360x740.png) | 360×740 | Online Baseline | Clean single-column studio layout, zero horizontal overflow |
| [`online_412x915.png`](file:///d:/HealthCalendar365/review/screenshots/online_412x915.png) | 412×915 | Online Baseline | Modern Android layout, properly scaled canvas preview |
| [`offline_360x740.png`](file:///d:/HealthCalendar365/review/screenshots/offline_360x740.png) | 360×740 | Offline Mode | App-shell intact, complete bilingual navigation bar visible |
| [`offline_412x915.png`](file:///d:/HealthCalendar365/review/screenshots/offline_412x915.png) | 412×915 | Offline Mode | Offline canvas rendered, quick-week pill scroll active |
| [`offline_date_navigation.png`](file:///d:/HealthCalendar365/review/screenshots/offline_date_navigation.png) | 412×915 | Offline Interaction | Stepped to October 15 White Cane Day, 4-card grid refreshed |
| [`cold_offline_launch.png`](file:///d:/HealthCalendar365/review/screenshots/cold_offline_launch.png) | 412×915 | Cold Offline Launch | Fresh tab in offline context, complete PWA shell loaded |
| [`network_restored.png`](file:///d:/HealthCalendar365/review/screenshots/network_restored.png) | 412×915 | Online Recovery | Network re-enabled, zero console errors, full interactivity |
| [`post_update_360x740.png`](file:///d:/HealthCalendar365/review/screenshots/post_update_360x740.png) | 360×740 | Post SW Upgrade | Updated worker active, layout maintains `scrollWidth: 360px` |
| [`post_update_412x915.png`](file:///d:/HealthCalendar365/review/screenshots/post_update_412x915.png) | 412×915 | Post SW Upgrade | Updated worker active, layout maintains `scrollWidth: 412px` |

---

## 5. Technical Regression Verification

All four automated remediation suites were re-executed following runtime offline testing:

- **[`test_remediation_round3.py`](file:///d:/HealthCalendar365/test_remediation_round3.py):** **PASS**
  - Image decoding verification, aspect ratio $1200\times600$ rejection, rollback, recovery.
- **[`test_remediation_round4.py`](file:///d:/HealthCalendar365/test_remediation_round4.py):** **PASS**
  - Missing backup fail-closed, corrupt pointer quarantine, dry-run invariance, contradictory QA rejection, provenance citations.
- **[`test_remediation_round5.py`](file:///d:/HealthCalendar365/test_remediation_round5.py):** **PASS**
  - Preflight corrupt backup rejection, missing pre-transaction hashes, dry-run zero mutation, active promotion QA rejection.
- **[`test_remediation_round6.py`](file:///d:/HealthCalendar365/test_remediation_round6.py):** **PASS**
  - Manifest builder `project_dir` isolation, live service worker non-mutation, recovery/rollback failure blocking, recording stub parameter inspection.

---

## 6. Deferred Final Acceptance Register

In accordance with release governance rules, the following ten verification activities are strictly deferred to the final human acceptance phase. **None of these items have been converted to PASS based on automation:**

| Register ID | Deferred Verification Item | Mandatory Execution Standard | Current Status |
| :--- | :--- | :--- | :---: |
| `DEF-ACC-01` | Physical Android-device testing | Physical Android 12+ device running mobile Chrome | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-02` | Manual PWA installation | "Install App" prompt, standalone launch, splash screen | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-03` | WhatsApp export & compression review | Direct share to WhatsApp Status & WhatsApp Group chat | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-04` | Human visual inspection | Qualified design reviewer inspection of framing and color | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-05` | User experience & usability testing | Healthcare worker usability walkthrough | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-06` | User acceptance testing | Sign-off by project sponsors / public health team | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-07` | Clinical review & sign-off | Qualified medical professional (MBBS/MD) sign-off on 40 cards | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-08` | Gujarati-language review & sign-off | Native Gujarati health communication specialist sign-off | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-09` | Accessibility testing with actual users| Evaluation by visually impaired users with screen readers | `DEFERRED_TO_FINAL_ACCEPTANCE` |
| `DEF-ACC-10` | Human approval of images & copy | Final promotion authorization in `approved_manifest.json` | `DEFERRED_TO_FINAL_ACCEPTANCE` |

---

## 7. Release Governance Compliance Summary

- **Production Hold:** STRICTLY ACTIVE.
- **Approval Ledger:** 0 APPROVED, 31 PENDING_CLINICAL_SIGN_OFF, 9 REJECTED_MISMATCH.
- **External Spending:** USD 0.00.
- **Live Assets & Data Files:** 100% Unchanged.
