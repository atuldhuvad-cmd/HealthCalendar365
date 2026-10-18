# HealthCalendar365 — Automated Browser & PWA Lifecycle Test Report

**Date:** October 16, 2026  
**Document ID:** `REPORT-BROWSER-PWA-20261016-R2`  
**Execution Environment:** Headless Chromium (Playwright / Node.js) on Local HTTP Server  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Status:** 21 PASS, 0 FAIL (Mobile Horizontal Viewport Defect Resolved)  
**Production Hold:** STRICTLY ACTIVE

---

## 1. Executive Summary

An automated suite of browser, PWA lifecycle, typography, canvas rendering, and layout tests was executed against `D:\HealthCalendar365` following the resolution of the mobile horizontal-overflow defect. All tests completed successfully without incurring any external API expenditure ($0.00 spend) or mutating any active calendar data, manifests, copy, or approval ledgers.

### Overall Results:
- **Total Test Checks:** 21
- **PASS:** 21 (100% of tested browser criteria)
- **FAIL:** 0
- **Remediated Defects:** 1 (Mobile Horizontal-Overflow Defect eliminated across 320px, 360px, 390px, and 412px viewports)
- **NOT TESTED:** Physical Target Android installation, hardware offline cold-boot, and live WhatsApp JPEG/WebP compression.

---

## 2. Test Execution Matrix

| Test Domain | Specific Verification Item | Specification / Criteria | Result | Observed Evidence |
| :--- | :--- | :--- | :---: | :--- |
| **Root & Metadata** | Root URL Loading | HTTP 200 via local HTTP server | **PASS** | HTTP Status: `200 OK` |
| **Root & Metadata** | Document Title | Non-empty descriptive title | **PASS** | `365-Day Health Poster Studio - India \| આરોગ્ય કેલેન્ડર ૩૬૫` |
| **Root & Metadata** | Viewport Meta Tag | `<meta name="viewport">` with device-width | **PASS** | Viewport tag found in DOM `<head>` |
| **PWA Manifest** | Manifest Syntax & Mode | `manifest.json` valid JSON, `display: standalone` | **PASS** | `name: "365-Day Health Poster Studio - India"`, `display: "standalone"` |
| **PWA Manifest** | High-Resolution Icons | Dedicated 192x192 & 512x512 PNG icons present on disk | **PASS** | Both 192x192 and 512x512 icons confirmed present and valid PNGs |
| **Typography** | Font Context Check | Google Fonts loaded in browser context | **PASS** | `Noto Sans Gujarati`: True, `Plus Jakarta Sans`: True (40 fonts loaded) |
| **Data Engine** | Calendar Dataset | `window.HEALTH_CALENDAR_DATA` populated | **PASS** | Complete 368-poster dataset loaded into browser memory |
| **UI Interaction** | Navigation Controls | Month/Date select & navigation buttons present | **PASS** | `#dateSelectInput`, `#prevDayBtn`, `#nextDayBtn` initialized |
| **Canvas Export** | Square English Render | $1080\times1080$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1080$, DataURL size: 1.86 MB |
| **Canvas Export** | Square Gujarati Render | $1080\times1080$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1080$, DataURL size: 1.89 MB |
| **Canvas Export** | Square Bilingual Render | $1080\times1080$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1080$, DataURL size: 2.00 MB |
| **Canvas Export** | Vertical English Render | $1080\times1920$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1920$, DataURL size: 2.89 MB |
| **Canvas Export** | Vertical Gujarati Render | $1080\times1920$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1920$, DataURL size: 2.93 MB |
| **Canvas Export** | Vertical Bilingual Render | $1080\times1920$ px canvas, valid PNG dataURL | **PASS** | Canvas size $1080\times1920$, DataURL size: 3.05 MB |
| **Service Worker** | Lifecycle Handlers | `install`, `activate`, `fetch` listeners in `sw.js` | **PASS** | All three lifecycle event listeners verified in code |
| **Service Worker** | Precache Asset List | Core HTML/CSS/JS, WOFF2 fonts, and active images | **PASS** | `PRECACHE_ASSETS` array contains 97 offline assets |
| **Service Worker** | Scoped Cache Eviction | Eviction restricted to owned cache prefix | **PASS** | `key.startsWith('health-poster-')` verified; no foreign cache deletion |
| **Accessibility** | Focusable Controls | Tabindex and interactive button focus | **PASS** | 49 interactive controls verified focusable |
| **Console Quality** | Browser Console Errors | Zero unhandled runtime exceptions | **PASS** | 0 console errors logged during navigation and rendering |
| **Responsive Layout** | Ultra-compact Mobile (320px) | `document.scrollWidth <= 320px` | **PASS** | `scrollWidth: 320px` matches `innerWidth: 320px` |
| **Responsive Layout** | Small Mobile (360px) | `document.scrollWidth <= 360px` | **PASS** | `scrollWidth: 360px` matches `innerWidth: 360px` |
| **Responsive Layout** | Mid Mobile (390px) | `document.scrollWidth <= 390px` | **PASS** | `scrollWidth: 390px` matches `innerWidth: 390px` |
| **Responsive Layout** | Modern Android (412px) | `document.scrollWidth <= 412px` | **PASS** | `scrollWidth: 412px` matches `innerWidth: 412px` |
| **Responsive Layout** | Tablet Portrait (768px) | `document.scrollWidth <= 768px` | **PASS** | `scrollWidth: 768px` matches `innerWidth: 768px` |
| **Responsive Layout** | Desktop Wide (1440px) | `document.scrollWidth <= 1440px` | **PASS** | `scrollWidth: 1440px` matches `innerWidth: 1440px` |

---

## 3. Defect Remediation: Mobile Viewport Horizontal Overflow

### Defect Description:
On mobile viewports ($<470\text{px}$ width), the studio layout previously displayed horizontal overflow with document `scrollWidth` locked at `470px` (or up to `485px` with header elements), causing side-scrolling and UI truncation on mobile devices.

### Root Cause Analysis:
1. **`.studio-layout` ([`css/styles.css`](file:///d:/HealthCalendar365/css/styles.css#L277-L286)):** Specified a rigid 2-column grid (`grid-template-columns: 1.15fr 0.85fr; padding: 20px 24px 30px;`) with **zero `@media` queries**, forcing `.preview-column` and `.sidebar-column` side-by-side regardless of screen width.
2. **`.preview-toolbar` ([`css/styles.css`](file:///d:/HealthCalendar365/css/styles.css#L299-L306)):** Had a flex row with non-wrapping controls (`.toolbar-left` 150px, `.toolbar-center` 143px, `.toolbar-right` 118px) yielding minimum intrinsic width $\approx 412\text{px}$ ($+32\text{px}$ padding = $444\text{px}$).
3. **`.export-action-bar` ([`css/styles.css`](file:///d:/HealthCalendar365/css/styles.css#L368-L373)):** Rigid 3-column grid (`grid-template-columns: 1fr 1fr 1fr;`) with action buttons having intrinsic text/icon widths $>130\text{px}$ each, preventing `.preview-column` from shrinking below $414\text{px}$.
4. **`.quick-week-bar` ([`css/styles.css`](file:///d:/HealthCalendar365/css/styles.css#L183-L191)):** Non-wrapping flex container with label ($145\text{px}$) and date selector ($260\text{px}$) totalling $453\text{px}$ minimum width.
5. **Segmented Control at 320px:** Format toggle button pair had combined width of $340\text{px}$ on ultra-compact devices.

### Applied CSS Remediation:
Appended minimal responsive breakpoints to [`css/styles.css`](file:///d:/HealthCalendar365/css/styles.css) targeting $900\text{px}$, $640\text{px}$, and $380\text{px}$:
- `@media (max-width: 900px)`: Switches `.studio-layout` to single-column (`grid-template-columns: 1fr;`), stacks `.header` vertically, resets `.sidebar-column` `max-height`, and stacks `.export-action-bar` (`grid-template-columns: 1fr;`).
- `@media (max-width: 640px)`: Enables wrapping on `.quick-week-bar`, `.preview-toolbar`, and `.multi-observance-bar`; expands `.quick-week-scroll` to full width.
- `@media (max-width: 380px)`: Tightens `.segmented-control`, `.seg-btn`, and hides `.seg-badge` to fit $320\text{px}$ screens cleanly.

### Before vs. After Viewport Verification Table:

| Viewport Width | Baseline `scrollWidth` | Remediated `scrollWidth` | Viewport `innerWidth` | Defect Status |
| :---: | :---: | :---: | :---: | :---: |
| **320 px** (Ultra-compact) | 470 px (+150 px) | **320 px** | 320 px | **RESOLVED (PASS)** |
| **360 px** (Small Mobile) | 470 px (+110 px) | **360 px** | 360 px | **RESOLVED (PASS)** |
| **390 px** (Mid Mobile) | 470 px (+80 px) | **390 px** | 390 px | **RESOLVED (PASS)** |
| **412 px** (Modern Android) | 470 px (+58 px) | **412 px** | 412 px | **RESOLVED (PASS)** |
| **768 px** (Tablet Portrait) | 768 px (0 px) | **768 px** | 768 px | **PASS** |
| **1440 px** (Desktop Wide) | 1440 px (0 px) | **1440 px** | 1440 px | **PASS** |

---

## 4. Hardware-Dependent Checklist (Designated NOT TESTED)

The following items strictly require physical target Android testing and remain **`NOT TESTED`**:
1. First-time PWA Add-to-Home-Screen prompt on physical Android Chrome.
2. Cold boot launch from home screen in Airplane Mode (offline).
3. PWA service worker background upgrade after a production deployment.
4. WhatsApp Status share (1080×1920 px) and story compression inspection.
5. WhatsApp Group / Post share (1080×1080 px) JPEG compression legibility.
6. Verification of Gujarati conjunct ligatures (*શ્ર*, *દ્વા*, *ઓસ્ટીયો*) on mobile WebKit and mobile Chromium without dotted circles.
