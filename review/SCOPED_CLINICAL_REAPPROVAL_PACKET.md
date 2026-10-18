# Scoped Clinical Reapproval Packet — Four Text-Modified Cards

**Reviewer:** Dr. Atul, MBBS (Trainer in Health Department since 2002)  
**Evaluation Completed:** October 16, 2026 (Copy) &bull; October 18, 2026 (Replacement Image Promoted)  
**Status:** PRODUCTION HOLD ACTIVE — ALL 4 CARDS FULLY APPROVED (0 IMAGES PENDING REPLACEMENT)  
**Target Cards:** Exactly 4 Cards with Updated Text  
**Decisions Breakdown:**
- **Clinical Copy Decisions:** 4 / 4 **APPROVED** (Remaining: 0)
- **Visual Photographic Images:** 4 / 4 **APPROVED** (Remaining Replacements: 0)
- **Card Dispositions:** 4 Cards Fully Approved (`10-15_card2`, `10-16-spine_card4`, `10-17_card1`, `10-18_card4`)

---

## 1. Review Determination & Governance Record

- **Reviewer Verbatim:** *"All 4 aprroved"* (Copy on 2026-10-16; Replacement Image for `10-17_card1` explicitly approved on 2026-10-18).
- **Normalized Determination:** Clinical copy for all 4 cards approved; replacement candidate for `10-17_card1` (`candidate_10_17_card1_v1.png`) independently verified (1 RHD driver, 1 steering wheel, 3-point seatbelts, 1200×900 RGB PNG, SHA-256 `247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6`) and promoted to active asset `photos/oct17_do1.png` via transaction `tx_20261018_approved_replacement_10_17_card1`.
- **Decision Record Path:** [`review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json`](file:///D:/HealthCalendar365/review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json) & [`review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json`](file:///D:/HealthCalendar365/review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json)
- **Controlled Replacement Queue Path:** [`review/candidate_generation_queue.json`](file:///D:/HealthCalendar365/review/candidate_generation_queue.json) (Status: `APPROVED_AND_PROMOTED`, Pending: 0)
- **Card 3 Replacement Specification & Authorization:** [`review/REPLACEMENT_SPECIFICATION_AND_AUTHORIZATION_10_17_CARD1.md`](file:///D:/HealthCalendar365/review/REPLACEMENT_SPECIFICATION_AND_AUTHORIZATION_10_17_CARD1.md)
- **Production Hold Active:** Zero external deployments or paid API spend. Physical-device hardware gates remain open.

---

## 2. Card-by-Card Docket & Scoped Decision Controls

### Card 1: `10-15_card2` (Global Handwashing Day) — **DECISION: FULLY APPROVED**

- **Slot Identifier:** `10-15_card2` (Day: `10-15`, Index: `2`)
- **Image Path:** [`photos/oct15_card2_scrub.png`](file:///D:/HealthCalendar365/photos/oct15_card2_scrub.png)
- **Image SHA-256:** `3e9ac5263a3d21e7694168ece237b91cb8617297d476068e3af44553c7592eb9`
- **Spec Hash:** `4f6b8cf63cc3f097a6e18a9f52974a2bcca2f9a59b79af3b567eaa52b13d7246`
- **Reason for Scoped Reapproval:** Clinical specification updated at Dr. Atul's request to explicitly name six handwashing areas (palms, backs, web spaces, fingertips/nails, thumbs, and wrists) for at least 20 seconds, and removed the unverified '80% of germs hide' claim.
- **Clinical Evidence Citation:** CDC Clean Hands Guidelines & WHO 6-Step Hand Hygiene Technique

#### Text Comparison & Verification

| Field | English (Active Production Copy) | Gujarati (સક્રિય ઉત્પાદન નકલ) |
| :--- | :--- | :--- |
| **Badge** | Action #2 | માર્ગદર્શન #૨ |
| **Title** | **Follow 6 Handwashing Steps** | **હાથ ધોવાના ૬ પગલાં અનુસરો** |
| **Description** | Rub palms, backs of hands, between fingers, fingertips and nails, thumbs, and wrists with soap for at least 20 seconds. | હથેળી, હાથનો પાછળનો ભાગ, આંગળીઓની વચ્ચે, આંગળીના ટેરવા અને નખ, અંગૂઠા તથા કાંડા સાબુથી ઓછામાં ઓછા ૨૦ સેકન્ડ ઘસો. |

![Preview 10-15_card2](file:///D:/HealthCalendar365/photos/oct15_card2_scrub.png)

#### Scoped Decision Controls

**1. Clinical Copy Decision (Bilingual Text & Guidelines):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**

**2. Visual Image Decision (`photos/oct15_card2_scrub.png`):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**
- **Reviewer Notes:** Clinical copy detailing 6 handwashing steps (palms, backs, web spaces, fingertips/nails, thumbs, and wrists) and soap lather image approved.
- **Production Ready Status:** **APPROVED** (Subject to final physical device acceptance)

---

### Card 2: `10-16-spine_card4` (World Spine Day) — **DECISION: FULLY APPROVED**

- **Slot Identifier:** `10-16-spine_card4` (Day: `10-16-spine`, Index: `4`)
- **Image Path:** [`photos/oct16_spine_card4.png`](file:///D:/HealthCalendar365/photos/oct16_spine_card4.png)
- **Image SHA-256:** `85fe501dd2645151923e249de80da365f71c91d4f8428deb891ddf2d29946edb`
- **Spec Hash:** `5e5dfd6485ce70f7f5a21d75648de82d77d03b0b1e620c23f4d87494ca1dba77`
- **Reason for Scoped Reapproval:** Removed the unverified popular science claim that forward neck flexion exerts '27 kg' on cervical vertebrae (originating from a 2014 static mathematical model), replacing it with evidence-based biomechanical guidance to hold devices near eye level and change posture frequently.
- **Clinical Evidence Citation:** World Spine Day Guidelines & Hansraj KK (2014) Contextual Clinical Ergonomics

#### Text Comparison & Verification

| Field | English (Active Production Copy) | Gujarati (સક્રિય ઉત્પાદન નકલ) |
| :--- | :--- | :--- |
| **Badge** | Action #4 | માર્ગદર્શન #૪ |
| **Title** | **Avoid 60° Mobile Text-Neck Slouch** | **મોબાઈલ જોતી વખતે ગરદન વાંકી ન વાળો** |
| **Description** | Severe forward neck flexion significantly increases mechanical load on cervical vertebrae. Hold devices closer to eye level and change posture frequently. | ડોક વધારે પડતી નીચી નમાવવાથી સર્વાઇકલ મણકા પર ભારે દબાણ આવે છે; ફોનને આંખની સામે રાખો અને વચ્ચે-વચ્ચે ગરદન હળવી કરો. |

![Preview 10-16-spine_card4](file:///D:/HealthCalendar365/photos/oct16_spine_card4.png)

#### Scoped Decision Controls

**1. Clinical Copy Decision (Bilingual Text & Guidelines):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**

**2. Visual Image Decision (`photos/oct16_spine_card4.png`):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**
- **Reviewer Notes:** Clinical copy for ergonomic mobile posture (holding phone near eye level, frequent posture relaxation) and upright sitting posture image approved.
- **Production Ready Status:** **APPROVED** (Subject to final physical device acceptance)

---

### Card 3: `10-17_card1` (World Trauma Day (Road Safety & Golden Hour)) — **DECISION: FULLY APPROVED (REPLACEMENT CANDIDATE PROMOTED)**

- **Slot Identifier:** `10-17_card1` (Day: `10-17`, Index: `1`)
- **Active Image Path:** [`photos/oct17_do1.png`](file:///D:/HealthCalendar365/photos/oct17_do1.png)
- **Active Image SHA-256:** `247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6`
- **Spec Hash:** `122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1`
- **Historical Rejected SHA-256:** `4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e` (Defect: "Two person driving the car" dual steering wheels; preserved as evidence in superseded archive)
- **Reason for Scoped Reapproval:** Added explicit 'ISI-marked' Bureau of Indian Standards specification to both English and Gujarati helmet wording at Dr. Atul's request, ensuring non-certified novelty headgear is strictly excluded.
- **Clinical Evidence Citation:** Motor Vehicles (Amendment) Act 2019 / Bureau of Indian Standards (IS 4151) / WHO Road Safety Manual

#### Text Comparison & Verification

| Field | English (Active Production Copy) | Gujarati (સક્રિય ઉત્પાદન નકલ) |
| :--- | :--- | :--- |
| **Badge** | Message #1 | માર્ગદર્શન #૧ |
| **Title** | **Wear ISI-Marked Full-Face Helmet & Seatbelt** | **ISI ચિહ્નિત ફુલ-ફેસ હેલ્મેટ અને સીટબેલ્ટ પહેરો** |
| **Description** | Fasten chin strap on two-wheelers; click three-point seatbelt in cars for front and rear passengers. | બાઇક-સ્કૂટર પર ચિન-સ્ટ્રેપ સાથે ISI ચિહ્નિત હેલ્મેટ પહેરો; કારમાં આગળ-પાછળ બેસનાર દરેક વ્યક્તિ સીટબેલ્ટ અવશ્ય બાંધો. |

![Preview 10-17_card1](file:///D:/HealthCalendar365/photos/oct17_do1.png)

#### Scoped Decision Controls

**1. Clinical Copy Decision (Bilingual Text & Guidelines):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**

**2. Visual Image Decision (`photos/oct17_do1.png`):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-18; Promoted via Transaction `tx_20261018_approved_replacement_10_17_card1`)
- [ ] **REJECT**
- **Defect Resolution:** Replacement candidate verified (1 RHD driver, 1 steering wheel, 3-point seatbelts snug across driver, front passenger, and child, no duplicate controls, no watermarks).
- **Production Ready Status:** **APPROVED** (Subject to final physical device acceptance)
- **Reviewer Notes:** Clinical copy with ISI-marked helmet and seatbelt guidance approved. Replacement candidate verified and promoted; defect fully resolved.

---

### Card 4: `10-18_card4` (World Menopause Day) — **DECISION: FULLY APPROVED**

- **Slot Identifier:** `10-18_card4` (Day: `10-18`, Index: `4`)
- **Image Path:** [`photos/oct18_dont2.png`](file:///D:/HealthCalendar365/photos/oct18_dont2.png)
- **Image SHA-256:** `eae08f7a2d1f1ee40965f58cc9d91bd592fa3a0d3dae706137528ea7f7a76c5f`
- **Spec Hash:** `8872071b598820b71e714324724ec0c6bba4e30e2dd9073457e1f331581cf42c`
- **Reason for Scoped Reapproval:** Corrected Gujarati translation error for 'Excess tea, coffee, and sugary Indian sweets', ensuring accurate rendering of vasomotor hot-flash triggers and bone calcium metabolism warnings.
- **Clinical Evidence Citation:** International Menopause Society (IMS) White Paper on Menopausal Health

#### Text Comparison & Verification

| Field | English (Active Production Copy) | Gujarati (સક્રિય ઉત્પાદન નકલ) |
| :--- | :--- | :--- |
| **Badge** | Message #4 | માર્ગદર્શન #૪ |
| **Title** | **Qualified Gynecologist Consultation** | **ગાયનેકોલોજિસ્ટની યોગ્ય સલાહ** |
| **Description** | Excess tea, coffee, and sugary Indian sweets trigger severe hot flashes and accelerate bone calcium loss. | વધુ પડતી ચા-કૉફી અને ખાંડવાળી ભારતીય મીઠાઈઓથી તીવ્ર હોટ ફ્લશ થઈ શકે છે અને હાડકાંમાં કેલ્શિયમનું નુકસાન ઝડપથી વધી શકે છે. |

![Preview 10-18_card4](file:///D:/HealthCalendar365/photos/oct18_dont2.png)

#### Scoped Decision Controls

**1. Clinical Copy Decision (Bilingual Text & Guidelines):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**

**2. Visual Image Decision (`photos/oct18_dont2.png`):**
- [x] **APPROVE** (Recorded by Dr. Atul, 2026-10-16)
- [ ] **REJECT**
- **Reviewer Notes:** Clinical copy advising qualified gynecologist consultation and corrected Gujarati translation regarding moderation of excess tea, coffee, and sweets approved.
- **Production Ready Status:** **APPROVED** (Subject to final physical device acceptance)

---

## 3. Reconciled Statuses Across Repository

| Category | Count | Status |
| :--- | :---: | :--- |
| Promoted Replacement Images | 10 | **APPROVED** (9 via `tx_20261016_approved_replacements`, 1 via `tx_20261018_approved_replacement_10_17_card1`) |
| Carried Clinical Approvals (Unmodified Cards) | 26 | **VALID** (Dr. Atul clinical approval carried forward) |
| Scoped Clinical Copy Reapprovals | 4 | **ALL 4 APPROVED** (Remaining: 0) |
| Fully Approved Cards from Scoped Docket | 4 | **ALL 4 APPROVED** (`10-15_card2`, `10-16-spine_card4`, `10-17_card1`, `10-18_card4`) |
| Image Replacement Required | 0 | **ZERO** (All visual defects resolved) |
| Controlled Candidate Generation Queue | 0 | **EMPTY** (1 item promoted; 0 pending) |
| Remaining Physical-Device Gates | 10 | **NOT TESTED** (Documented in `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`) |

> [!IMPORTANT]
> Production hold remains strictly **ACTIVE**. Release gate remains closed until all 10 physical device gates are completed on genuine hardware.
