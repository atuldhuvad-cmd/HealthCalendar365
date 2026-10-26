# Physical-Device Final Acceptance Checklist

**Document:** `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`  
**Date Created:** October 16, 2026  
**Status:** DEVICE VERIFICATION IN PROGRESS (2 PASS / 6 PARTIAL / 2 NOT TESTED)
**Hardware Rule:** Every single item in this checklist must be marked **`NOT TESTED`** until physically executed and witnessed on an authentic Android mobile device. Emulated browser viewports (e.g., Chrome DevTools / Playwright) provide preflight baseline confidence only and **CANNOT** substitute for physical device checks.

**Connection Rule:** USB and USB debugging are not required. Execute the checks as an ordinary user in Android Chrome and native Android/WhatsApp interfaces. USB/ADB or `chrome://inspect` may be used only as optional diagnostic tooling.

**Current Candidate:** `health-poster-v1.11` draws the selected day number inside the calendar badge instead of the platform emoji's fixed 17, adds the Common Yoga Protocol assets, resets the erroneous card-text shadow, and uses official NHSRC CHO manuals as supporting references for selected Oral/Eye/ENT/Emergency/MNS provenance and preventive copy. Module wording is optional and must be rejected when contradictory under `review/cho_module_content_alignment_2026-10-18.json`. Automated offline and responsive tests pass; one online reopen followed by a second launch is required before physical review of this candidate.

---

## 1. Physical Device Verification Ledger

| Item # | Verification Scope | Target Requirement / Procedure | Status | Evidence / Observation Field | Date Tested |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **G-DEV-01** | **Android Installation from Hosting Origin** | Navigate to the production/staging HTTPS URL in Google Chrome for Android. Verify native "Install app" / "Add to Home Screen" mini-infobar prompt appears. Verify Web App Manifest decodes `name`, `short_name`, `theme_color` (#061320), `background_color` (#061320), and standalone display mode. Verify app icon installs cleanly on Android home screen without badging distortion. | **PASS** | Dr. Atul confirmed installation. Physical-device screenshot shows the installed PWA launched in standalone mode without Chrome address bar/menu and with clean app/header rendering: `review/screenshots/android-g-dev-01-standalone-2026-10-18.jpg`. | 2026-10-18 |
| **G-DEV-02** | **Installed-PWA Launch & Offline Relaunch** | 1. Launch installed app from Android home screen in standalone mode (no browser URL bar).<br>2. Browse several dates.<br>3. Enable Android Airplane Mode (all Wi-Fi and Cellular data OFF).<br>4. Force-kill the app from Android Recent Apps switcher.<br>5. Cold relaunch the app from the home screen icon while completely offline.<br>6. Confirm app shell, datasets (368 observances), and active photos render instantly with zero network errors. | **PASS** | Physical-device screenshot shows Airplane mode, standalone launch, October 17 selected, and the complete photo-based poster rendered from offline storage: `review/screenshots/android-g-dev-02-offline-2026-10-18.jpg`. First paint initially showed a black canvas; reselecting/refitting rendered the poster. Separate observation: Fit produced an excessively small preview. | 2026-10-18 |
| **G-DEV-03** | **Service-Worker Upgrade from v1.7 to v1.8** | 1. Establish initial baseline installation with active cache `health-poster-v1.7` (97 cached items).<br>2. Deploy a staged service-worker increment to `health-poster-v1.8`.<br>3. Reconnect device to network and reopen app.<br>4. Verify background fetch of new worker, clean activation on reload, immediate caching of updated assets, and atomic deletion of the obsolete `health-poster-v1.7` cache from Android Cache Storage without corrupting user state.<br>**Note:** the new worker activates in the background while the already-loaded page still runs the old code, so the updated build is observable on the *next* launch, not the current one. | **PARTIAL** | Physical Android evidence confirms the installed PWA updated from v1.7 to v1.8 and loaded the corrected Vertical controls, sizing badge and preview without loss of selected-date state: `android-g-dev-03-05-v1.8-vertical-fit-2026-10-18.png`. Direct confirmation that the obsolete v1.7 Cache Storage entry was deleted remains outstanding. | 2026-10-18 |
| **G-DEV-04** | **Offline Fonts & All Six Poster Styles** | While in Airplane Mode, generate and visually inspect all six poster layout combinations:<br>1. *Square (1080×1080) — English*<br>2. *Square (1080×1080) — Gujarati*<br>3. *Square (1080×1080) — Bilingual*<br>4. *Vertical Story (1080×1920) — English*<br>5. *Vertical Story (1080×1920) — Gujarati*<br>6. *Vertical Story (1080×1920) — Bilingual*<br>Confirm embedded WOFF2 fonts (`Noto Sans Gujarati` 400/600/700/800 and `Plus Jakarta Sans` 400/500/600/700/800) render identically to online renders without font flash (FOIT/FOUT) or fallback to system sans-serif. | **PARTIAL** | Physical Android exports confirm all three 1080×1080 Square modes render completely. An Airplane-mode device screenshot plus a complete Vertical Bilingual poster confirm offline Vertical rendering. Vertical English/Gujarati and offline Square comparisons remain outstanding. Evidence: `android-g-dev-04-square-english-2026-10-18.png`, `android-g-dev-04-square-gujarati-2026-10-18.png`, `android-g-dev-04-square-bilingual-2026-10-18.png`, and `android-g-dev-07-vertical-bilingual-2026-10-18.png`. | 2026-10-18 |
| **G-DEV-05** | **320px & Common Android Viewport Rendering** | Test responsive layout on physical screens including compact budget devices (320px–360px width, e.g. JioPhone Next / Galaxy A03) and standard modern devices (390px–412px, e.g. Pixel 7 / Samsung Galaxy S22+):<br>1. Confirm zero horizontal body scroll (`scrollWidth === innerWidth`).<br>2. Confirm quick-week bar scrolls horizontally without clipping container.<br>3. Verify touch target accessibility (all buttons and date pills ≥ 44×44px touch area).<br>4. Check portrait and landscape orientation switching. | **PARTIAL** | The v1.7 physical test failed because Vertical widened the page and hid Fit. After the v1.8 update, physical Android evidence shows portrait Vertical with Fit/zoom controls visible, the correct 1080×1920 badge and no horizontal clipping: `android-g-dev-03-05-v1.8-vertical-fit-2026-10-18.png`. Automated 320/360/390/412px checks pass. Landscape orientation and a second physical screen width remain outstanding. | 2026-10-18 |
| **G-DEV-06** | **Gujarati Font Rendering & Typography** | Inspect complex Gujarati conjuncts, matras, rasva/dirgha, and numerals (`૦૧૨૩૪૫૬૭૮૯`) on the physical canvas and DOM:<br>1. Confirm proper rendering of complex ligatures: `દ્રષ્ટિ`, `સર્વાઇકલ`, `ક્ષ`, `જ્ઞ`, `શ્ર`, `હસ્ત`, `સ્વચ્છ`.<br>2. Verify no broken dotted circles (indicating unattached matras) appear on canvas exports or UI text.<br>3. Confirm numeral consistency between Gujarati date picker and rendered canvas. | **PARTIAL** | Gujarati-only and bilingual Android exports show clean Gujarati date/title/guidance rendering, including `સ્વચ્છ`, with no visible dotted circles or detached matras. The full required conjunct/numeral sample remains outstanding. Evidence: the two Gujarati-containing G-DEV-04 screenshots. | 2026-10-18 |
| **G-DEV-07** | **Image Export at 720×540 & High-Res Posters** | 1. Tap "Download Poster" for both Square (1080×1080) and Story (1080×1920) orientations.<br>2. Verify image generation triggers native Android file download / Gallery save.<br>3. Inspect generated PNG/JPEG in Android Gallery / Google Photos.<br>4. Confirm card photos are drawn edge-to-edge with no letterboxing or distortion, at high sharpness and zero pixelation. Rendered crop boxes differ by format and are **not** both 4:3: Vertical renders 465×350 (≈4:3); Square renders 465×215 (≈2.16:1 wide crop) by design. Source assets are 720×540 or 1200×900. | **PARTIAL** | Three downloaded Square PNGs are exactly 1080×1080 and show sharp edge-to-edge crops. A complete Vertical Bilingual render was received and visually passes crop/legibility inspection, but the received attachment was resized to 899×1599, so the original 1080×1920 file dimensions and Gallery-save behavior remain unverified. Evidence: the three G-DEV-04 Square files and `android-g-dev-07-vertical-bilingual-2026-10-18.png`. | 2026-10-18 |
| **G-DEV-08** | **WhatsApp Sharing & Compression Handling** | 1. Use the Web Share API or manually share exported poster PNG/JPEG files into WhatsApp (individual chat and WhatsApp Status).<br>2. Verify WhatsApp image compression does not render Gujarati text unreadable or blur critical medical instructions.<br>3. Inspect the WhatsApp image preview card before sending to verify proper framing. | **PARTIAL** | Dr. Atul confirmed posting the Gujarati Square October 19 ear-care poster to WhatsApp Status. The supplied viewer screenshot shows readable Gujarati card copy and 92 views: `review/screenshots/whatsapp-status-10-19-gujarati-2026-10-19.png`. WhatsApp's profile/name interface overlaps part of the upper title, establishing a Status safe-area defect. This proves publication and general viewer readability for the older poster copy. Individual-chat sharing, pre-send preview, source-versus-compressed pixel comparison, safe-area correction and the current v1.11 poster remain outstanding. | 2026-10-19 |
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
> **Scope:** These ten checks measure installation, offline behavior, rendering, export, sharing and update recovery. They remain `NOT TESTED` until executed on genuine hardware; they are not a clinical review.

---

## 4. Correction Log

**2026-10-18 — Acceptance-criteria corrections (documentation only).**

Five gates specified criteria that contradicted the committed application. Each would have produced a **false FAIL** against a correctly functioning build. Only the criteria were corrected; **no gate status was changed and all ten remain `NOT TESTED`.** No application code, poster content or image asset was touched.

| Gate | Was | Corrected to | Verified against |
| :--- | :--- | :--- | :--- |
| G-DEV-01 | `theme_color` #0ea5e9, `background_color` #0f172a | both `#061320` | `manifest.json`, `index.html` meta |
| G-DEV-03 | baseline v1.4 → v1.5 | baseline v1.6 → v1.7, plus a note that the new worker is observable on the next launch | `sw.js` `CACHE_NAME` |
| G-DEV-04 | `Inter` 400/600/700; Noto Sans Gujarati 400/500/600/700 | `Plus Jakarta Sans` 400/500/600/700/800; Noto Sans Gujarati 400/600/700/800 | `css/fonts.css`, `fonts/` |
| G-DEV-07 | card photo crops at exactly 720×540 (or 4:3) | Vertical 465×350 (≈4:3), Square 465×215 (≈2.16:1) by design; 720×540 / 1200×900 are source sizes | `js/canvas-renderer.js` |
| G-DEV-10 | IndexedDB `health-calendar-db` | `HealthPosterStudioDB` (stores `custom_photos`, `app_settings`); branding lives in `localStorage` | `js/db.js` |

The pre-correction copy was removed (recovery archive only).

**Superseded evidence.** The poster layout changed on 2026-10-18 (footer removed; vertical cards and typography reflowed). `review/AUTOMATED_BROWSER_PWA_TEST_REPORT.md` and `review/runtime_offline_pwa_test_results.json` describe the earlier layout at cache `health-poster-v1.5` and are historical snapshots, not evidence for the current build.
