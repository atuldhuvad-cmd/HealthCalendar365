# Master Pending Decisions Register (2026 Calendar Review)

**Document ID:** `DEC-REG-2026-V1`  
**Status:** Review-Only Proposal — Awaiting Public Health & Clinical Decisions  
**Target Reviewer:** Dr. Atul Dhuvad (Senior Medical Doctor, Public Health Specialist, District Health Trainer, Gujarat)  
**Date:** 2026-10-23  

---

## Executive Summary

This register consolidates all matters requiring clinical judgment, administrative policy guidance, or scheduling discretion across the complete 365-day 2026 calendar for `HealthCalendar365`. 

Every decision is assigned a permanent, stable ID (`DEC-01` through `DEC-19`). No dataset modifications, image generations, git commits, or calendar activations will occur until explicit sign-off is granted by Dr. Atul Dhuvad.

---

## Decision Matrix Summary

| Decision ID | Domain | Scope / Affected Items | Recommended Resolution | Status |
| :--- | :--- | :--- | :--- | :--- |
| **`DEC-01`** | Observance Approval | Batch 3 (Items 25–36, 12 campaigns, 48 cards) | Approve clinical copy & prompts in [`BATCH_3_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_3_CLINICAL_REVIEW.md) | **PENDING** |
| **`DEC-02`** | Observance Approval | Batch 4 (Items 37, 39–48, 11 campaigns, 44 cards) | Approve clinical copy & prompts in [`BATCH_4_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_4_CLINICAL_REVIEW.md) | **PENDING** |
| **`DEC-03`** | Observance Approval | Batch 5 (Items 49–74, 26 campaigns, 104 cards) | Approve clinical copy & prompts in [`BATCH_5_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_5_CLINICAL_REVIEW.md) | **PENDING** |
| **`DEC-04`** | Routine Replacements | Maternal, Child, Mamta & AMB (17 sets, 66 dates, 68 cards) | Approve clinical copy & placement manifest in [`maternal_child_amb_manifest_2026.json`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/maternal_child_amb_manifest_2026.json) | **PENDING** |
| **`DEC-05`** | Observance Additions | 8 Climate/Health Additions (32 cards) | Approve 8 additions in [`PROPOSED_OBSERVANCE_ADDITIONS_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/PROPOSED_OBSERVANCE_ADDITIONS_REVIEW.md) | **PENDING** |
| **`DEC-06`** | Schedular Conflict | Item 53 (`09-23-national-ayurveda-day`) | Retain `09-23` provisionally vs reassigning to Dhanteras (`11-06`) | **PENDING** |
| **`DEC-07`** | Schedular Conflict | Item 65 (`11-15-world-prematurity-day`) | Retain `11-15` alongside Newborn Care Week vs shifting to `11-17` | **PENDING** |
| **`DEC-08`** | Multi-Campaign Date | November 18 (`11-18`): Items 67, 68, 69 | Prioritize AMR Week (`11-18`) as Primary; COPD Day secondary; Naturopathy complementary | **PENDING** |
| **`DEC-09`** | Multi-Campaign Date | January 30 (`01-30`): Items 5, 6 | Coexist World Leprosy Day + National NTD Day (dual tracks) | **PENDING** |
| **`DEC-10`** | Multi-Campaign Date | May 05 (`05-05`): Items 23, 24 | Coexist World Asthma Day + World Hand Hygiene Day | **PENDING** |
| **`DEC-11`** | Multi-Campaign Date | August 01 (`08-01`): Items 43, 44 | Prioritize World Breastfeeding Week; maintain Lung Cancer Day secondary | **PENDING** |
| **`DEC-12`** | Placement Track | Food Adulteration & FSSAI DART Testing (4 cards) | Option A (coexist on `06-07` / `10-16`) vs Option B (replace duplicate Eat Right slot `11-05`) | **PENDING** |
| **`DEC-13`** | Calendar Gaps | Retained Baseline Gaps (Adolescents & Palliative Care) | Confirm Mamta Taruni quarterly bridging for RKSK; consider Q4 palliative swap | **PENDING** |
| **`DEC-14`** | Retained Routine Revision | Hypertension Card 3 (Hash `e59865343a6e`, 9 dates) | Correct numerical conflation of 5g salt with 5g sodium (<5g salt = <2g sodium) | **PENDING** |
| **`DEC-15`** | Retained Routine Revision | COPD & Asthma Cards 1 & 4 (Hash `ac54dd49cd74`, 9 dates) | Device-specific spacer advice (pMDI only) & remove 'zero side effects' claim | **PENDING** |
| **`DEC-16`** | Retained Routine Revision | Cancer Screening Cards 2 & 4 (Hash `dc1f8cd74427`, 9 dates) | Remove '100% cancer cure' guarantee & qualify HPV protection scope | **PENDING** |
| **`DEC-17`** | Retained Routine Revision | Snakebite First Aid Card 4 (Hash `1b4fee7365be`, 6 dates) | Remove '100% life saved' guarantee; emphasize prompt hospital antivenom | **PENDING** |
| **`DEC-18`** | Retained Routine Revision | RBSK Screening Card 4 (Hash `727476e5a39f`, 4 dates) | Remove '100% surgically correctable' guarantee; state surgical correction is available | **PENDING** |
| **`DEC-19`** | Retained Routine Revision | Diabetes Glycemic Control Card 1 (Hash `218d778d421c`, 8 dates) | Qualify rigid 'HbA1c <7%' target with physician-guided individualized target | **PENDING** |

---

## Detailed Decision Records

### DEC-01: Clinical Sign-off for Batch 3 Observances
- **Scope:** 12 Campaigns / 48 Cards (Items 25–36: May 08 to July 01).
- **Campaigns:**
  - Item 25: `05-08-world-thalassemia-day`
  - Item 26: `05-10-world-lupus-day`
  - Item 27: `05-12-international-nurses-day`
  - Item 28: `05-17-world-hypertension-day`
  - Item 29: `05-19-world-family-doctor-day`
  - Item 30: `05-20-world-autoimmune-arthritis-day`
  - Item 31: `05-28-world-hunger-day`
  - Item 32: `05-31-world-no-tobacco-day`
  - Item 33: `06-07-world-food-safety-day`
  - Item 34: `06-14-world-blood-donor-day`
  - Item 35: `06-21-international-day-of-yoga`
  - Item 36: `07-01-national-doctors-day`
- **Clinical Evidence & Modifications:** All universal screening claims and rigid drug dosages removed. Side-by-side English/Gujarati reviewed against MoHFW/WHO clinical guidelines.
- **Recommended Action:** Formally approve clinical copy and draft visual prompts in [`BATCH_3_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_3_CLINICAL_REVIEW.md).

---

### DEC-02: Clinical Sign-off for Batch 4 Observances
- **Scope:** 11 Campaigns / 44 Cards (Item 37, Items 39–48: July 06 to September 17; Item 38 already approved).
- **Campaigns:**
  - Item 37: `07-06-world-zoonoses-day`
  - Item 39: `07-17-world-day-for-international-justice` (Clinical trauma & medicolegal care)
  - Item 40: `07-21-national-cpr-day`
  - Item 41: `07-28-world-hepatitis-day`
  - Item 42: `07-29-world-ors-day` (IAP ORS & Rehydration Week)
  - Item 43: `08-01-world-breastfeeding-week`
  - Item 44: `08-10-national-deworming-day-august-round`
  - Item 45: `08-19-world-humanitarian-day` (Frontline community health workers)
  - Item 46: `08-25-national-eye-donation-fortnight`
  - Item 47: `09-01-national-nutrition-week` (Poshan Maah)
  - Item 48: `09-17-world-patient-safety-day`
- **Clinical Evidence & Modifications:** Verification of National CPR Day (21 July / Cardiological Society of India & IRC), IAP ORS Day (29 July / Indian Academy of Pediatrics), and August Deworming Round against NHM operational manuals. Universal guarantees and legal/police procedures removed.
- **Recommended Action:** Formally approve clinical copy and draft visual prompts in [`BATCH_4_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_4_CLINICAL_REVIEW.md).

---

### DEC-03: Clinical Sign-off for Batch 5 Observances
- **Scope:** 26 Campaigns / 104 Cards (Items 49–74: September 21 to December 25).
- **Campaigns:**
  - Item 49: `09-21-world-alzheimers-day`
  - Item 50: `09-23-world-sign-languages-day`
  - Item 51: `09-25-world-pharmacists-day`
  - Item 52: `09-26-world-environmental-health-day`
  - Item 53: `09-23-national-ayurveda-day` (See `DEC-06`)
  - Item 54: `09-28-world-rabies-day`
  - Item 55: `09-29-world-heart-day`
  - Item 56: `10-01-international-day-of-older-persons`
  - Item 57: `10-10-world-mental-health-day`
  - Item 58: `10-11-international-day-of-the-girl-child`
  - Item 59: `10-12-world-arthritis-day`
  - Item 60: `10-15-global-handwashing-day`
  - Item 61: `10-16-world-food-day`
  - Item 62: `10-20-world-osteoporosis-day`
  - Item 63: `10-24-world-polio-day`
  - Item 64: `11-14-world-diabetes-day`
  - Item 65: `11-15-world-prematurity-day` (See `DEC-07`)
  - Item 66: `11-17-national-epilepsy-day`
  - Item 67: `11-18-national-naturopathy-day` (See `DEC-08`)
  - Item 68: `11-18-world-antimicrobial-resistance-amr-awareness-week` (See `DEC-08`)
  - Item 69: `11-18-world-copd-day` (See `DEC-08`)
  - Item 70: `11-25-international-day-for-the-elimination-of-violence-against-women`
  - Item 71: `12-01-world-aids-day`
  - Item 72: `12-03-international-day-of-persons-with-disabilities`
  - Item 73: `12-12-universal-health-coverage-day`
  - Item 74: `12-25-good-governance-day` (Digital health, Ayushman Bharat ABHA, e-Sanjeevani)
- **Clinical Evidence & Modifications:** Verified against WHO, MoHFW, NVBDCP, NACO, and Gujarat public health protocols.
- **Recommended Action:** Formally approve clinical copy and draft visual prompts in [`BATCH_5_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/BATCH_5_CLINICAL_REVIEW.md).

---

### DEC-04: Approval of Maternal, Child, Mamta & AMB Routine Replacement Manifest
- **Scope:** 17 Distinct Sets / 66 Proposed Calendar Dates / 68 Bilingual Cards.
- **Sets Breakdown:**
  - Mamta Outreach Sets 1–4: 16 dates (all strictly verified 2026 Wednesdays; aligned with user-confirmed Gujarat practice: Monday facility Mamta at PHC/CHC/UPHC/SDH/DH; Wednesday rural outreach according to microplans).
  - Maternal Care Sets 5–7: 12 dates (ANC danger signs, INC emergency recognition without public 12h threshold, PNC danger signs through 42 days without pad-waiting instructions).
  - Essential Newborn Care Sets 8–9: 8 dates (Immediate newborn care, danger signs recognition without bypassing capable local facilities).
  - Community Child Health Sets 10–11: 8 dates (HBNC home visits on days 3, 7, 14, 21, 28, 42; HBYC quarter visits at 3, 6, 9, 12, 15 months).
  - School Health & RBSK Sets 12, 13A, 13B: 12 dates (SHWP adolescent promotion, RBSK 4Ds screening, RBSK referral pathways).
  - Anemia Mukt Bharat Sets 14–16: 10 dates (AMB-A community/IFA syrup, AMB-B school/WIFS, AMB-C pregnancy/lactation/testing).
- **Zero Protected Collisions:** All 66 dates verified to displace only unprotected, generic, highly-repetitive CPHC dates.
- **Recommended Action:** Formally approve the manifest and clinical copy in [`maternal_child_amb_manifest_2026.json`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/maternal_child_amb_manifest_2026.json) and [`MATERNAL_CHILD_AMB_CLINICAL_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/MATERNAL_CHILD_AMB_CLINICAL_REVIEW.md).

---

### DEC-05: Approval of Climate-Health & Environmental Observances
- **Scope:** 8 Proposed Additions (32 cards) + 1 Food Adulteration Set (4 cards).
- **Dates & Additions:**
  - `04-22`: Earth Day (International Mother Earth Day)
  - `06-05`: World Environment Day
  - `09-07`: International Day of Clean Air for Blue Skies
  - `09-19`: International Snakebite Awareness Day
  - `09-26`: World Environmental Health Day
  - `10-13`: International Day for Disaster Risk Reduction
  - `10-24`: International Day of Climate Action (Secondary track alongside World Polio Day)
  - `12-02`: National Pollution Control Day
  - `DEC-12`: Food Adulteration & FSSAI DART Rapid Testing Set
- **Clinical Evidence:** NPCCHH MoHFW guidelines, WHO Snakebite Envenoming Roadmap, NDMA Disaster Management, FSSAI DART Book.
- **Recommended Action:** Formally approve the additions in [`PROPOSED_OBSERVANCE_ADDITIONS_REVIEW.md`](file:///C:/Users/dhuva/.gemini/antigravity/brain/5544f2e0-4810-4f12-a3e7-ad2df15c991e/PROPOSED_OBSERVANCE_ADDITIONS_REVIEW.md).

---

### DEC-06: Date Reconciliation for Item 53 (National Ayurveda Day)
- **Problem:** In [`pending_observance_content_2026.json`](file:///D:/HealthCalendar365/data/pending_observance_content_2026.json), Item 53 is assigned slot `09-23-national-ayurveda-day` (`09-23`). However, Ministry of Ayush celebrates National Ayurveda Day annually on Dhanwantari Jayanti (Dhanteras). In 2026, Dhanteras falls on **06 November 2026**. Furthermore, September 23 is officially celebrated as **Ayushman Bharat Diwas / PM-JAY Anniversary**.
- **Options:**
  - **Option 1 (Recommended):** Retain `09-23` provisionally in the pending dataset to avoid breaking existing dataset pointers, with a reviewer note that in Gujarat local microplans it aligns with Dhanteras (`11-06`).
  - **Option 2:** Reassign Item 53 to `11-06` (Dhanteras) and update `09-23` to celebrate Ayushman Bharat Diwas / PM-JAY.
- **Decision Required:** Select Option 1 or Option 2.

---

### DEC-07: Date Reconciliation for Item 65 (World Prematurity Day)
- **Problem:** World Prematurity Day is globally observed on **17 November**. In `pending_observance_content_2026.json`, Item 65 is registered at slot `11-15-world-prematurity-day` (`11-15`), coexisting with National Newborn Care Week (`11-15` to `11-21`). On November 17 (`11-17`), the calendar currently has National Epilepsy Day (Item 66).
- **Options:**
  - **Option 1 (Recommended):** Keep Item 65 on `11-15` as the inaugural anchor of National Newborn Care Week, emphasizing prematurity alongside newborn care.
  - **Option 2:** Relocate Item 65 to its strict global date (`11-17`) as a dual-track campaign alongside National Epilepsy Day.
- **Decision Required:** Select Option 1 or Option 2.

---

### DEC-08: Triple Collision Handling on November 18 (`11-18`)
- **Problem:** November 18 has three distinct items registered in `pending_observance_content_2026.json`:
  1. Item 67: `national-naturopathy-day`
  2. Item 68: `world-antimicrobial-resistance-amr-awareness-week`
  3. Item 69: `world-copd-day`
- **Clinical & Epidemiological Priority:** AMR Awareness Week (WHO global health security threat, MoHFW red-line campaign) carries the highest urgent public health priority. COPD Day is a high-burden non-communicable disease priority. Naturopathy Day provides lifestyle wellness counseling.
- **Recommended Coexistence Plan:**
  - **Primary Campaign:** World AMR Awareness Week (Item 68) — Featured in primary calendar view.
  - **Secondary Coexisting Campaign:** World COPD Day (Item 69) — Available via tab/secondary card track.
  - **Complementary Feature:** National Naturopathy Day (Item 67) — Complementary lifestyle wellness card.
- **Decision Required:** Confirm the proposed tiered prioritization.

---

### DEC-09: Multi-Campaign Coexistence on January 30 (`01-30`)
- **Items:** Item 5 (`national-anti-leprosy-day` / Martyrs' Day) and Item 6 (`world-neglected-tropical-diseases-ntd-day`).
- **Policy Context:** Both are top MoHFW priorities in India. NLEP focuses on leprosy disability prevention and early MDT; NTD Day covers Lymphatic Filariasis (MDA), Kala-azar, and Soil-Transmitted Helminths.
- **Recommended Action:** Maintain both campaigns as coexisting dual tracks on January 30.

---

### DEC-10: Multi-Campaign Coexistence on May 05 (`05-05`)
- **Items:** Item 23 (`world-asthma-day`) and Item 24 (`world-hand-hygiene-day`).
- **Policy Context:** Asthma Day focuses on inhaler stigma and symptom control; Hand Hygiene Day is the core pillar of Infection Prevention and Control (IPC) in healthcare facilities.
- **Recommended Action:** Maintain both campaigns as coexisting dual tracks on May 05.

---

### DEC-11: Multi-Campaign Coexistence on August 01 (`08-01`)
- **Items:** Item 43 (`world-breastfeeding-week`) and Item 44 (`world-lung-cancer-day`).
- **Policy Context:** Breastfeeding Week spans 01–07 August and is the foremost maternal-infant health observance of Q3; Lung Cancer Day focuses on tobacco cessation and early pulmonary referral.
- **Recommended Action:** Prioritize World Breastfeeding Week as primary banner; display Lung Cancer Day as secondary clinical track.

---

### DEC-12: Placement Selection for Food Adulteration & FSSAI DART Testing
- **Content:** 4 Bilingual Cards on Toxic Adulterants, Household Rapid Tests (FSSAI DART), Official Reporting via 1800-112-100, and 14-digit License Verification.
- **Placement Options:**
  - **Option A (Coexisting Observance Track):** Attach as supplementary track to World Food Safety Day (`06-07`) or World Food Day (`10-16`).
  - **Option B (Routine Replacement — Recommended):** Replace one of the duplicate generic "Eat Right: Desi Balanced Thali & Shree Anna Millets" days in the retained baseline calendar (e.g., November 05 `11-05` or December 09 `12-09`), giving food adulteration a dedicated full-day feature.
- **Decision Required:** Select Option A or Option B.

---

### DEC-13: Management of Factual Multi-Month Gaps in Retained Routine Calendar
- **Audit Findings:**
  1. **Adolescent Health (RKSK):** Only 2 baseline routine days remain (`02-16` and `12-21`), leaving a 10-month gap. However, this is **completely remediated** by the 4 proposed quarterly Mamta Taruni outreach dates (`01-28`, `04-29`, `07-22`, `10-28`), giving adolescent health robust quarterly coverage.
  2. **Palliative Care & Chronic Pain Relief:** Baseline calendar has only 3 dates (`03-01`, `04-05`, `08-21`), leaving a 6-month gap between August and March.
- **Recommendation:** Accept the current factual distribution as baseline, or authorize swapping one repetitive Q4 hypertension/diabetes slot (e.g., in November) to Palliative Care.
- **Decision Required:** Confirm whether to retain current factual distribution or schedule a Q4 palliative slot swap.

---

---

### DEC-14: Clinical Correction of Salt vs. Sodium Conflation in Hypertension Card 3
- **Scope:** Retained Baseline Topic *Hypertension Screening & Blood Pressure Control* (Card 3).
- **Normalized Content Hash:** `e59865343a6e`
- **Affected Calendar Dates (9 dates):** `01-18`, `02-22`, `03-26`, `04-30`, `06-03`, `07-07`, `08-11`, `11-23`, `12-27`
- **Primary Sourced Authority:** WHO Guideline on Sodium Intake for Adults and Children (2020); MoHFW NP-NCD Operational Guidelines; ICMR Guidelines for Management of Hypertension.
- **Problem Statement:** Card 3 currently instructs: *'Restrict total daily sodium intake to less than 1 level teaspoon (5g)'*. Chemically, 5 g of table salt (NaCl) contains approximately 2 g (2000 mg) of elemental sodium. Inadvertently calling 5 g the *sodium* ceiling suggests that 5 g of sodium is permissible, which equals 12.5 g of salt (over double the safe physiological limit recommended by WHO and ICMR).
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English:** *Restrict total daily salt intake to less than 1 level teaspoon (5 g), which corresponds to under 2 g (2000 mg) of sodium. Avoid adding raw salt at the table, and limit pickles, papads, and salted snacks.*
  - **Gujarati:** *દૈનિક મીઠાનો વપરાશ ૧ નાની ચમચી (૫ ગ્રામ મીઠું, જે ૨ ગ્રામ સોડિયમ બરાબર છે) થી ઓછો રાખો; જમવામાં ઉપરથી કાચું મીઠું ન નાખો અને અથાણાં, પાપડ કે ખારી વસ્તુઓ મર્યાદિત કરો.*
- **Status:** **PENDING**

---

### DEC-15: Clinical Correction of Device-Specific Spacer Advice & Adverse Effects in COPD/Asthma Cards 1 & 4
- **Scope:** Retained Baseline Topic *Chronic Respiratory Health (COPD & Asthma)* (Cards 1 & 4).
- **Normalized Content Hash:** `ac54dd49cd74`
- **Affected Calendar Dates (9 dates):** `01-23`, `02-27`, `03-31`, `05-04`, `06-08`, `07-12`, `08-16`, `09-20`, `11-28`
- **Primary Sourced Authority:** Global Initiative for Chronic Obstructive Lung Disease (GOLD 2024); Global Initiative for Asthma (GINA 2023); National College of Chest Physicians (NCCP) India Consensus Guidelines.
- **Problem Statement:** 
  1. *Card 1 (Device Specificity):* Currently advises universal spacer usage (*'Use Prescribed Inhalers with Spacer Daily'*). Spacers/valved holding chambers are exclusively designed for pressurized Metered Dose Inhalers (pMDIs). Dry Powder Inhalers (DPIs like Rotahalers, Accuhalers, Turbuhalers) and breath-actuated devices must never be used with a spacer.
  2. *Card 4 (Absolute Claim):* Gujarati copy claims inhalers improve breathing *'without side effects'* (*'આડઅસર વગર'*). Inhaled corticosteroids (ICS) and bronchodilators carry recognized adverse effects (oral candidiasis, dysphonia, tachycardia, local irritation). Rinsing the mouth and gargling after steroid inhalers is clinically mandatory; claiming zero side effects undermines essential patient vigilance.
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English (Card 1):** *Use prescribed inhalers daily as instructed for your device; for pressurized metered-dose inhalers (pMDIs), a spacer helps deliver medication effectively into the airways.*
  - **Gujarati (Card 1):** *ડૉક્ટરની સલાહ મુજબ યોગ્ય પદ્ધતિથી નિયમિત ઇનહેલર લો; મીટર્ડ-ડોઝ ઇનહેલર (pMDI) સાથે સ્પેસર સાધન વાપરવાથી દવા ફેફસાં સુધી સરળતાથી પહોંચે છે.*
  - **English (Card 4):** *Inhalers deliver targeted, low-dose medicine directly to the lungs with far fewer systemic effects than oral steroid tablets; they are non-addictive maintenance therapies. Always rinse your mouth after steroid inhalers.*
  - **Gujarati (Card 4):** *ઇનહેલરથી દવા સીધી ફેફસાં સુધી પહોંચતી હોવાથી ગોળીઓ કરતાં ઘણી ઓછી આડઅસર થાય છે અને તેની કોઈ આદત પડતી નથી; સ્ટીરોઈડ ઇનહેલર લીધા પછી હંમેશા મોં સાફ કરી કોગળા કરો.*
- **Status:** **PENDING**

---

### DEC-16: Clinical Correction of Oncological Cure Claims & HPV Protection Scope in Cancer Cards 2 & 4
- **Scope:** Retained Baseline Topic *Breast & Cervical Cancer Early Screening* (Cards 2 & 4).
- **Normalized Content Hash:** `dc1f8cd74427`
- **Affected Calendar Dates (9 dates):** `02-25`, `03-29`, `05-02`, `06-06`, `07-10`, `08-14`, `09-18`, `11-26`, `12-30`
- **Primary Sourced Authority:** Operational Framework for Comprehensive Primary Health Care: Screening of Common NCDs, MoHFW; WHO Cervical Cancer Screening Guidelines.
- **Problem Statement:**
  1. *Card 2 (Absolute Cure Guarantee):* Gujarati copy claims early-detected cervical cancer is *'100% curable'* (*'પ્રારંભિક તબક્કે કેન્સર ૧૦૦% સાજું થાય છે'*). Absolute 100% cure guarantees are medically untenable in oncology; early detection enables highly successful treatment and dramatically improves survival, but cannot guarantee 100% cure.
  2. *Card 4 (Translation Mismatch):* Gujarati copy claims HPV vaccination provides *'lifelong protection'* (*'આજીવન રક્ષણ'*), whereas English accurately notes it prevents up to 90% of cervical cancers (oncogenic types 16 & 18). Promising absolute lifelong immunity risks vaccinated women skipping recommended routine adult screening (VIA/pap smear).
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English (Card 2):** *Women aged 30-65 should undergo free VIA screening every 5 years at Ayushman Arogya Mandir to detect cervical pre-cancer early, when treatment is most effective.*
  - **Gujarati (Card 2):** *૩૦ થી ૬૫ વર્ષની બહેનો દર ૫ વર્ષે આરોગ્ય કેન્દ્ર પર ગર્ભાશયના મુખની મફત તપાસ (VIA) કરાવો; પ્રારંભિક તબક્કે ઓળખ થવાથી સમયસર સફળ સારવાર શક્ય બને છે.*
  - **English (Card 4):** *Vaccinating adolescent girls aged 9-14 with Human Papillomavirus (HPV) vaccine prevents up to 90% of cervical cancers; routine adult screening remains recommended.*
  - **Gujarati (Card 4):** *૯ થી ૧૪ વર્ષની કિશોરીઓને HPV રસી અપાવો; આ રસી મોટાભાગના ગર્ભાશયના કેન્સર સામે મજબૂત સુરક્ષા આપે છે, છતાં પુખ્ત વયે નિયમિત તપાસ કરાવવી જરૂરી છે.*
- **Status:** **PENDING**

---

### DEC-17: Clinical Correction of Absolute Survival Guarantee in Snakebite First Aid Card 4
- **Scope:** Retained Baseline Topic *Snakebite First Aid & Poisoning Management* (Card 4).
- **Normalized Content Hash:** `1b4fee7365be`
- **Affected Calendar Dates (6 dates):** `02-01`, `03-05`, `04-09`, `05-13`, `06-17`, `11-02`
- **Primary Sourced Authority:** National Action Plan for Prevention and Control of Snakebite Envenoming (NAP-SE), MoHFW, Government of India (2024); WHO Guidelines for the Clinical Management of Snakebites in SEAR.
- **Problem Statement:** Card 4 Gujarati text states *'સમયસર હોસ્પિટલ પહોંચવાથી દર્દીનો જીવ ૧૦૦% બચે છે'* (*'reaching hospital on time 100% saves the patient's life'*). While prompt anti-snake venom (ASV) and resuscitation drastically cut mortality, severe envenoming can still cause fatal outcomes due to acute renal failure, consumptive coagulopathy, or delayed hospital access. Public health communications must avoid 100% survival promises.
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English:** *Over 70% of snakes are non-venomous; never waste critical minutes on faith healers. Reaching a capable hospital promptly for anti-snake venom is life-saving.*
  - **Gujarati:** *સાપ કરડવા પર ઝાડ-ફૂંક કે પથ્થર ઘસવામાં એક મિનિટ પણ ન બગાડો; સમયસર સક્ષમ હોસ્પિટલ પહોંચી એન્ટિ-સ્નેક વેનમ લેવાથી દર્દીનો જીવ બચાવી શકાય છે.*
- **Status:** **PENDING**

---

### DEC-18: Clinical Correction of Absolute Surgical Correction Claim in RBSK Card 4
- **Scope:** Retained Baseline Topic *Child Health Screening & Early Intervention (RBSK)* (Card 4).
- **Normalized Content Hash:** `727476e5a39f`
- **Affected Calendar Dates (4 dates):** `03-19`, `05-27`, `09-08`, `12-20`
- **Primary Sourced Authority:** Operational Guidelines on Rashtriya Bal Swasthya Karyakram (RBSK), MoHFW; DEIC Operational Manual.
- **Problem Statement:** Card 4 states *'Conditions like cleft lip, clubfoot, and congenital cataract are 100% surgically correctable for free under government RBSK program'*. Surgical correction outcomes depend upon anatomical complexity, syndromic associations, age of presentation, and post-operative rehabilitation. Promising '100% surgical correction' contradicts national clinical counseling standards.
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English:** *Conditions like cleft lip, clubfoot, and congenital cataract can be effectively treated with government-supported corrective surgeries and therapy under RBSK.*
  - **Gujarati:** *હોઠ ફાટેલો હોય, પગનો પંજો વળેલો હોય કે જન્મજાત મોતિયો હોય તો અંધશ્રદ્ધામાં ન પડો; સરકારી RBSK યોજના હેઠળ નિષ્ણાત સર્જરી અને થેરાપી દ્વારા સુધારાત્મક સારવાર ઉપલબ્ધ છે.*
- **Status:** **PENDING**

---

### DEC-19: Clinical Qualification of Rigid HbA1c Target in Diabetes Card 1
- **Scope:** Retained Baseline Topic *Diabetes Management & Glycemic Balance* (Card 1).
- **Normalized Content Hash:** `218d778d421c`
- **Affected Calendar Dates (8 dates):** `01-19`, `02-23`, `03-27`, `06-04`, `08-12`, `09-16`, `11-24`, `12-28`
- **Primary Sourced Authority:** ICMR Guidelines for Management of Type 2 Diabetes; Research Society for the Study of Diabetes in India (RSSDI) Clinical Practice Recommendations.
- **Problem Statement:** Card 1 gives a rigid public target: *'Maintain HbA1c under 7%'*. While appropriate for young adults without severe complications, clinical guidelines emphasize individualizing targets (e.g., 7.5%–8.0% for elderly individuals, those with hypoglycemia unawareness, or patients with extensive cardiovascular/renal comorbidities).
- **Proposed Corrected Copy (Pending Dr. Atul Dhuvad Sign-Off):**
  - **English:** *Monitor fasting blood sugar and quarterly HbA1c; work with your doctor toward your individualized target (typically under 7% for most adults) to prevent microvascular damage.*
  - **Gujarati:** *દર ૩ મહિને સુગર અને HbA1c તપાસ કરાવો; ડૉક્ટરે નક્કી કરેલા વ્યક્તિગત લક્ષ્ય (સામાન્ય રીતે ૭% ની અંદર) મુજબ સુગર નિયંત્રણમાં રાખી કિડની, નસો અને આંખો સુરક્ષિત રાખો.*
- **Status:** **PENDING**

---
*End of Master Decisions Register (`DEC-01` to `DEC-19`). Ready for review by Dr. Atul Dhuvad.*
