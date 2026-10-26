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

## 5. Current State (updated 27 October 2026)

- **Personal-use app.** All 365 dates / 1,460 cards are active. There is no approval, sign-off, freeze or
  release-gate workflow; the doctor-owner edits content and images directly.
- **Release:** production is v1.27 (Cloudflare Pages). The local source is the v1.28 candidate: renderer fixes so
  titles and captions are never clipped or silently truncated (targeted wrap / shrink-to-fit only where a string
  overflows; every other poster renders byte-identically).
- **Image generation:** `generate_with_gemini.py` writes candidates to `photos/staging/` only. Inspect a candidate,
  copy it into `photos/`, point the card at it in the dataset sources, then run `build_calendar_data.py` and
  `build_precache_manifest.py` (and raise `CACHE_NAME` in `sw.js`).
- **Provenance kept:** observance dates and sources (`data/verified_health_observances_2026.json`), image
  provenance (`CALENDAR_IMAGE_AUDIT.md`, generation records in `review/`), photo derivative hashes
  (`review/DERIVATIVE_OPTIMIZATION_2026-10-24.json`).
- **NOT TESTED:** live image-API generation, physical Android installs/upgrades, real WhatsApp sharing.
