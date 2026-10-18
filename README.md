# 365-Day Health Poster Studio - India (આરોગ્ય કેલેન્ડર ૩૬૫)

An offline-first, mobile-responsive **Progressive Web App (PWA)** created specifically for Indian Doctors and Public Health Advocates to instantly generate, customize, and share high-resolution bilingual health awareness posters directly to **WhatsApp Posts, Groups, and Status**.

---

## 🌟 Modern Indian Clinical Editorial Visual Style

### 1. Dual Format Toggle (1-Click)
- **Square (1080×1080 px):** Optimized for WhatsApp Posts, Groups, Instagram & Facebook feeds.
- **Vertical Portrait (1080×1920 px):** Optimized for WhatsApp Status & Instagram Stories.

### 2. Trilingual Typography Toggle
- **Bilingual (English + ગુજરાતી):** High-impact bilingual clinical editorial poster with English headers and Gujarati vernacular guidance.
- **Gujarati Only (સરળ ગુજરાતી):** Pure Gujarati vernacular messaging for maximum reach in Gujarat.
- **English Only:** Clean global public health typography.

### 3. Layout: 4-Card Visual Grid (2×2 Modular Architecture)
- **Header Section:**
  - Date Badge (e.g. `15 OCTOBER | ૧૫ ઓક્ટોબર`) with smooth pill border.
  - Observance Badge: `WHO Global Health Day` or `MoHFW National Health Day` with priority tier glow.
  - Large bold bilingual title in Plus Jakarta Sans + Noto Sans Gujarati.
  - Clinical Theme Subtitle Capsule.
- **Center 4-Card Grid:**
  - 4 independent high-resolution photographs (source assets are 4:3, 720x540 or 1200x900).
  - Rendered crop differs by format: Vertical draws 465x350 (4:3); Square draws 465x215 (a wider editorial crop).
  - Clean rounded containers with subtle clinical border (`#284454`) and soft shadow.
  - Distinct Action Badges (`માર્ગદર્શન #૧`, `માર્ગદર્શન #૨`, `માર્ગદર્શન #૩`, `માર્ગદર્શન #૪`).
  - Bilingual Action Header and concise medical captions.
- **Bottom Area:**
  - **No footer bar.** The poster ends with the 4-card grid. Earlier builds carried an
    `Issued in Public Interest for Health Awareness | જાહેર આરોગ્ય હિતમાં` / custom
    doctor-branding footer; it was removed on 2026-10-18.
  - The **Doctor Branding** settings panel is still present in the UI and still saves to
    local storage, but while the footer is absent none of its fields are drawn on the poster.

---

## 🤖 Gemini Image Generation Pipeline ("Gemini Banav")

The studio integrates directly with Google Gemini / Imagen 3 for photorealistic Indian clinical assets:

### 1. Gemini Imagen 3 Prompt Formula
Every card in `data/health_365.json` strictly adheres to this photorealistic template:
> *"Ultra-photorealistic 4:3 close-up photograph of [SUBJECT / ACTION]. Warm natural lighting, authentic Indian domestic or clinical setting, clean clinical hygiene, cinematic depth of field, 8k resolution, editorial medical magazine quality. No text, no logos, no distorted hands."*

### 2. Image Generation Script (`generate_with_gemini.py`)
Run the Python pipeline using the official `google-genai` SDK:
```bash
# Preview prompts for October 15 without API calls
python generate_with_gemini.py --dry-run --day 10-15

# Generate missing photo assets for a specific day
python generate_with_gemini.py --day 10-15

# Scan all 365 days for missing photo assets
python generate_with_gemini.py --all-missing

# Force regenerate assets using Imagen 3 or Gemini Native model
python generate_with_gemini.py --force --day 10-15 --model imagen-3.0-generate-002
```

### 3. UI Studio Integration
- **Click any card on the live canvas or sidebar:**
  - 📷 **Upload / Swap Photo:** Upload a custom photo from your clinic or phone gallery.
  - ✨ **Copy Gemini Prompt:** 1-click copies the exact Gemini Imagen 3 prompt to clipboard.
  - 🔄 **Reset Photo:** Restores the default photo.

---

## 🔍 Visual Integrity & Full-Calendar Discrepancy Audit

To eliminate subject mismatches, gender inversions, and cross-topic swaps, every card in the studio is audited against **5 Strict Quality Gates**:

1. **Gender & Physiological Match Gate:** Female-specific observances (Menopause, Maternal Health) must strictly feature female subjects/doctors; never male subjects.
2. **Direct Subject Correlation Gate:** The visual must directly depict the subject of the card (e.g. Ear Care must show ears/ENT, NOT teeth; Oral Care must show teeth/gums, NOT ear anatomy; Tobacco must show anti-tobacco/lungs, NOT ear buds; Iodine Day must show iodized salt packaging/jars, NOT refrigerators).
3. **Authentic Indian Context Gate:** All visuals must feature authentic Indian families, Indian domestic kitchens, Indian road settings (certified ISI full-face helmets, fastened 3-point seatbelts), and Indian clinical environments. No Western stock imagery.
4. **Zero Cross-Card Duplication Gate:** The 4 cards of every poster must feature distinct, unique perspectives without duplicating images.
5. **Zero Cross-Topic Swap Gate:** Assets must never be cross-contaminated between health days.

### Audit Summary:
- **Spotlight Week (Oct 15 - Oct 21):**
  - **Oct 17 (World Trauma Day):** Fixed. Installed authentic Indian couple with prominent 3-point seatbelts (`oct17_do1.png`), certified full-face helmet (`oct17_dont1.png`), emergency 108 phone response (`oct17_do2.png`), and CPR/first-aid dummy care (`oct17_dont2.png`).
  - **Oct 18 (World Menopause Day):** Fixed. Replaced elderly male on stairs with authentic woman squatting with weights, calcium nutrition & bone model (`oct18_dont1.png`). Replaced exercise photo on Gynecologist Advice card with female gynecologist consulting female patient with anatomical uterus model (`oct18_dont2.png`).
  - **Oct 19 (Ear & Hearing Care):** Fixed. Replaced tooth image with ENT doctor explaining ear anatomy (`oct19_ear_card1.png`). Replaced smoker lungs with woman inserting cotton bud with red 'X' warning (`oct19_ear_card3.png`).
  - **Oct 19 (Oral Health & Tobacco-Free Life):** Fixed. Replaced ear anatomy with clean tooth model & toothbrush (`oct19_oral_card1.png`). Replaced cotton bud in ear with smoker black lung vs clean lung with broken cigarette (`oct19_oral_card3.png`).
  - **Oct 20 (Osteoporosis) & Oct 21 (Iodine Deficiency):** Flagged for dedicated Indian elder fall prevention and Indian kitchen iodized salt jar generation.
- **Full Year Scope:** 358 posters (1,432 cards) currently utilize 5 generic category placeholders (`cat_cardio.png`, `cat_infection.png`, `cat_mental.png`, `cat_nutrition.png`, `cat_yoga.png`). Detailed ledger tracked in [`MEMORY.md`](file:///D:/HealthCalendar365/MEMORY.md) and [`CALENDAR_IMAGE_AUDIT.md`](file:///D:/HealthCalendar365/CALENDAR_IMAGE_AUDIT.md).

---

## 🚫 Deprecated Scripts
The following old scripts have been retired and deprecated:
- `generate_realistic_assets.py` (Deprecated: Monolithic PIL canvas shape-drawing is replaced by dynamic HTML5 Canvas).
- `extract_clean_photos.py` (Deprecated: Monolithic PNG pixel-cropping is replaced by independent 4:3 high-res photos).

---

## 🚀 How to Run the App

### On this computer

1. Double-click **`start_studio.bat`** (or run `python serve.py`).
2. The browser opens automatically at `http://127.0.0.1:<port>/index.html`.
3. Click the **Install App** icon in the address bar to install the PWA on this machine.

`serve.py` binds to `127.0.0.1` only by default, so nothing is exposed to your network.

### On an Android phone (same Wi-Fi)

A phone **cannot** reach `http://127.0.0.1` — that address means "this computer" on the
phone itself. Serve the build mirror over the LAN instead:

```bash
# 1. Build the deterministic mirror of exactly the 97 precached assets (SHA-256 verified)
python build_preview_runtime.py

# 2. Serve that mirror on the local network (keep the port fixed across sessions)
python serve.py --host 0.0.0.0 --root build/preview-runtime --port 8080
```

The server prints the phone URL and the exact origin string to enter under
`chrome://flags/#unsafely-treat-insecure-origin-as-secure` in Android Chrome. Service
workers require a secure context, and a plain-HTTP LAN origin is not one by default.
Full procedure: [`review/ANDROID_NO_USB_TEST_INSTRUCTIONS.md`](review/ANDROID_NO_USB_TEST_INSTRUCTIONS.md).

> **Serve `build/preview-runtime`, never the repo root.** The root also contains
> `review/`, `.git` and transaction data, which would be readable by anything on the same
> network. `start_studio.bat` serves the root and is safe only because it stays on loopback.

> **Keep the origin stable.** A PWA's service worker, Cache Storage and IndexedDB are bound
> to `(scheme, host, port)`. Changing the IP or the port makes Android treat it as a
> different site and discards the installed app's cached state.

### Maintenance commands

```bash
# Verify calendar posters, spotlight days and PWA assets
python validate_integrity.py

# Rebuild the preview mirror after any source change
python build_preview_runtime.py

# Isolated remediation verification suites
python test_remediation_round3.py
python test_remediation_round4.py
python test_remediation_round5.py
python test_remediation_round6.py
```

> ⚠️ **`build_precache_manifest.py` is not routine.** It rewrites `PRECACHE_ASSETS` in
> `sw.js` but does **not** bump `CACHE_NAME`. Run it only if you also raise the cache
> version by hand — otherwise changed assets ship under the existing version and every
> installed client keeps serving the old ones from cache.
