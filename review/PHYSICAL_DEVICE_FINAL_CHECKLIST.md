# Physical-Device Final Acceptance Checklist

**Document:** `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`  
**Date Created:** October 16, 2026  
**Status:** PRODUCTION HOLD ACTIVE — REAL HARDWARE VERIFICATION GATE OPEN  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///D:/HealthCalendar365/review/RELEASE_GOVERNANCE.md) & [`review/CONTENT_RELEASE_ACCEPTANCE.md`](file:///D:/HealthCalendar365/review/CONTENT_RELEASE_ACCEPTANCE.md)  
**Hardware Rule:** Every single item in this checklist must be marked **`NOT TESTED`** until physically executed and witnessed on an authentic Android mobile device. Emulated browser viewports (e.g., Chrome DevTools / Playwright) provide preflight baseline confidence only and **CANNOT** sign off physical device gates.

**Connection Rule:** USB and USB debugging are not required. Execute the checks as an ordinary user in Android Chrome and native Android/WhatsApp interfaces. USB/ADB or `chrome://inspect` may be used only as optional diagnostic tooling.

---

## 1. Physical Device Verification Ledger

| Item # | Verification Scope | Target Requirement / Procedure | Status | Evidence / Observation Field | Sign-Off Date |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **G-DEV-01** | **Android Installation from Hosting Origin** | Navigate to the production/staging HTTPS URL in Google Chrome for Android. Verify native "Install app" / "Add to Home Screen" mini-infobar prompt appears. Verify Web App Manifest decodes `name`, `short_name`, `theme_color` (#061320), `background_color` (#061320), and standalone display mode. Verify app icon installs cleanly on Android home screen without badging distortion. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-02** | **Installed-PWA Launch & Offline Relaunch** | 1. Launch installed app from Android home screen in standalone mode (no browser URL bar).<br>2. Browse several dates.<br>3. Enable Android Airplane Mode (all Wi-Fi and Cellular data OFF).<br>4. Force-kill the app from Android Recent Apps switcher.<br>5. Cold relaunch the app from the home screen icon while completely offline.<br>6. Confirm app shell, datasets (368 observances), and active photos render instantly with zero network errors. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-03** | **Service-Worker Upgrade from v1.6 to Future Release** | 1. Establish initial baseline installation with active cache `health-poster-v1.6` (97 cached items).<br>2. Deploy a staged service-worker increment (e.g., `health-poster-v1.7`).<br>3. Reconnect device to network and reopen app.<br>4. Verify background fetch of new worker, clean activation on reload, immediate caching of updated assets, and atomic deletion of the obsolete `health-poster-v1.6` cache from Android Cache Storage without corrupting user state.<br>**Note:** the new worker activates in the background while the already-loaded page still runs the old code, so the updated build is observable on the *next* launch, not the current one. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-04** | **Offline Fonts & All Six Poster Styles** | While in Airplane Mode, generate and visually inspect all six poster layout combinations:<br>1. *Square (1080×1080) — English*<br>2. *Square (1080×1080) — Gujarati*<br>3. *Square (1080×1080) — Bilingual*<br>4. *Vertical Story (1080×1920) — English*<br>5. *Vertical Story (1080×1920) — Gujarati*<br>6. *Vertical Story (1080×1920) — Bilingual*<br>Confirm embedded WOFF2 fonts (`Noto Sans Gujarati` 400/600/700/800 and `Plus Jakarta Sans` 400/500/600/700/800) render identically to online renders without font flash (FOIT/FOUT) or fallback to system sans-serif. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-05** | **320px & Common Android Viewport Rendering** | Test responsive layout on physical screens including compact budget devices (320px–360px width, e.g. JioPhone Next / Galaxy A03) and standard modern devices (390px–412px, e.g. Pixel 7 / Samsung Galaxy S22+):<br>1. Confirm zero horizontal body scroll (`scrollWidth === innerWidth`).<br>2. Confirm quick-week bar scrolls horizontally without clipping container.<br>3. Verify touch target accessibility (all buttons and date pills ≥ 44×44px touch area).<br>4. Check portrait and landscape orientation switching. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-06** | **Gujarati Font Rendering & Typography** | Inspect complex Gujarati conjuncts, matras, rasva/dirgha, and numerals (`૦૧૨૩૪૫૬૭૮૯`) on the physical canvas and DOM:<br>1. Confirm proper rendering of complex ligatures: `દ્રષ્ટિ`, `સર્વાઇકલ`, `ક્ષ`, `જ્ઞ`, `શ્ર`, `હસ્ત`, `સ્વચ્છ`.<br>2. Verify no broken dotted circles (indicating unattached matras) appear on canvas exports or UI text.<br>3. Confirm numeral consistency between Gujarati date picker and rendered canvas. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-07** | **Image Export at 720×540 & High-Res Posters** | 1. Tap "Download Poster" for both Square (1080×1080) and Story (1080×1920) orientations.<br>2. Verify image generation triggers native Android file download / Gallery save.<br>3. Inspect generated PNG/JPEG in Android Gallery / Google Photos.<br>4. Confirm card photos are drawn edge-to-edge with no letterboxing or distortion, at high sharpness and zero pixelation. Rendered crop boxes differ by format and are **not** both 4:3: Vertical renders 465×350 (≈4:3); Square renders 465×215 (≈2.16:1 wide crop) by design. Source assets are 720×540 or 1200×900. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-08** | **WhatsApp Sharing & Compression Handling** | 1. Use the Web Share API or manually share exported poster PNG/JPEG files into WhatsApp (individual chat and WhatsApp Status).<br>2. Verify WhatsApp image compression does not render Gujarati text unreadable or blur critical medical instructions.<br>3. Inspect the WhatsApp image preview card before sending to verify proper framing. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-09** | **Downloaded Image Readability & Contrast** | 1. Open the downloaded poster on mobile at 50% and 100% screen brightness under bright ambient daylight.<br>2. Confirm title, description, and badge text achieve high legibility (minimum WCAG AA 4.5:1 visual contrast against card background).<br>3. Verify that emergency numbers (e.g. 108 ambulance on Oct 17) and key clinical guidance remain immediately legible to elderly readers. | **NOT TESTED** | *Pending test on real Android device* | — |
| **G-DEV-10** | **Update Recovery, Cache Eviction & Data Preservation** | 1. After prolonged offline usage and repeated cache queries, simulate a network reconnection.<br>2. Verify IndexedDB database (`HealthPosterStudioDB`, object stores `custom_photos` and `app_settings`) retains swapped card photos without eviction. Note: doctor-branding settings persist in `localStorage` under `doctor_branding_settings`, not IndexedDB.<br>3. Verify browser does not evict critical assets under storage pressure (confirming `navigator.storage.persist()` behavior if requested).<br>4. Validate smooth recovery when an in-flight network request fails gracefully back to cache. | **NOT TESTED** | *Pending test on real Android device* | — |

---

## 2. Test Execution Protocol

### Hardware Requirements
- **Primary Device:** Authentic Android device running Android 10+ (API level 29+) with Google Chrome 115+.
- **Secondary Device (Optional but Recommended):** Low-spec or budget Android device (2GB RAM, 720p screen) to evaluate memory and canvas performance under hardware constraints.
- **Network Environment:** High-speed Wi-Fi, throttled 3G/4G, and completely severed Airplane Mode.

### Recording Evidence
When conducting the tests on physical hardware:
1. Capture screenshots of each phase (home screen icon, offline launch, rendered poster, WhatsApp preview).
2. Note device model, Android OS version, and Chrome browser version.
3. Record exact date, time, and tester identity in the table above.
4. Update item status from **`NOT TESTED`** to **`PASS`** or **`FAIL`** only upon empirical verification.

---

## 3. Mandatory Release Gate Condition

> [!CAUTION]
> **Production Hold Rule:** HealthCalendar365 CANNOT be released, deployed to production hosting, or distributed publicly until:
> 1. Dr. Atul provides explicit clinical decisions on all 4 text-modified cards (`10-15_card2`, `10-16-spine_card4`, `10-17_card1`, `10-18_card4`).
> 2. All 10 physical device test gates in this checklist are executed and verified with PASS status on genuine hardware.

---

## 4. Correction Log

**2026-10-18 — Acceptance-criteria corrections (documentation only).**

Five gates specified criteria that contradicted the committed application. Each would have produced a **false FAIL** against a correctly functioning build. Only the criteria were corrected; **no gate status was changed and all ten remain `NOT TESTED`.** No application code, poster content, image asset or approval record was touched, and the approval ledger (13 APPROVED / 27 PENDING_CLINICAL_SIGN_OFF / 0 REJECTED_MISMATCH) is unaffected.

| Gate | Was | Corrected to | Verified against |
| :--- | :--- | :--- | :--- |
| G-DEV-01 | `theme_color` #0ea5e9, `background_color` #0f172a | both `#061320` | `manifest.json`, `index.html` meta |
| G-DEV-03 | baseline v1.4 → v1.5 | baseline v1.6 → v1.7, plus a note that the new worker is observable on the next launch | `sw.js` `CACHE_NAME` |
| G-DEV-04 | `Inter` 400/600/700; Noto Sans Gujarati 400/500/600/700 | `Plus Jakarta Sans` 400/500/600/700/800; Noto Sans Gujarati 400/600/700/800 | `css/fonts.css`, `fonts/` |
| G-DEV-07 | card photo crops at exactly 720×540 (or 4:3) | Vertical 465×350 (≈4:3), Square 465×215 (≈2.16:1) by design; 720×540 / 1200×900 are source sizes | `js/canvas-renderer.js` |
| G-DEV-10 | IndexedDB `health-calendar-db` | `HealthPosterStudioDB` (stores `custom_photos`, `app_settings`); branding lives in `localStorage` | `js/db.js` |

Pre-correction copy preserved at `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.pre_correction_2026-10-18.md.bak`.

**Superseded evidence.** The poster layout changed on 2026-10-18 (footer removed; vertical cards and typography reflowed). `review/AUTOMATED_BROWSER_PWA_TEST_REPORT.md` and `review/runtime_offline_pwa_test_results.json` describe the earlier layout at cache `health-poster-v1.5` and are historical snapshots, not evidence for the current build.
