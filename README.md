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

### 3. Layout: 4-Card Grid (2×2)
- **Header:** date badge, observance badge, bilingual title, theme capsule.
- **Cards:** 4 photographs in rounded containers with action badges and bilingual
  captions. Source assets are 4:3 (720×540 or 1200×900); the rendered crop differs by
  format — vertical draws 465×350, square draws 465×215.
- **No footer bar** (removed 2026-10-18). The **Doctor Branding** panel still saves to
  local storage, but nothing it holds is drawn on the poster while the footer is absent.

**Artwork status:** the 10 spotlight posters (Oct 15–21) use dedicated photography. The
remaining 358 posters / 1,432 cards still use 5 generic category placeholders. Ledger in
[`CALENDAR_IMAGE_AUDIT.md`](CALENDAR_IMAGE_AUDIT.md) and [`MEMORY.md`](MEMORY.md).

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
Click any card on the canvas or sidebar to swap in your own photo, copy that card's
Gemini prompt, or reset it to the default.

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

> Serve `build/preview-runtime`, never the repo root, and keep the port fixed — both
> reasons are explained in the linked procedure.

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
