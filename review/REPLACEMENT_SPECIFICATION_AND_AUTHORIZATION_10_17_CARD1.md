# Replacement Specification & Generation Authorization Sheet — `10-17_card1`

**Slot Identifier:** `10-17_card1`  
**Card Title:** Wear ISI-Marked Full-Face Helmet & Seatbelt / ISI ચિહ્નિત ફુલ-ફેસ હેલ્મેટ અને સીટબેલ્ટ પહેરો  
**Day Observance:** October 17 — World Trauma Day (Road Safety & Golden Hour)  
**Document ID:** `SPEC-AUTH-10-17-CARD1-20261016` (Updated 2026-10-18)  
**Date:** October 18, 2026  
**Status:** APPROVED AND PROMOTED — TRANSACTION `tx_20261018_approved_replacement_10_17_card1` FINALIZED  
**Authorized Spend:** **USD 0.00** (Actual Provider Spend: **USD 0.00**)  
**Production Hold:** **STRICTLY ACTIVE** (Pending physical-device hardware gates)

---

## 1. Provenance & Hash Verification

| Parameter | Value | Verification Status |
| :--- | :--- | :--- |
| **Slot Identifier** | `10-17_card1` (Day `10-17`, Card Index `1`) | Canonical |
| **Current Live Image Path** | [`photos/oct17_do1.png`](file:///D:/HealthCalendar365/photos/oct17_do1.png) | Active on Disk |
| **Current Live Image SHA-256** | `247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6` | Verified Exact Match in Ledger & Disk |
| **Approved Clinical Spec Hash** | `122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1` | Verified Match in Ledger |
| **Clinical Copy Status** | **APPROVED** by Dr. Atul (MBBS) | Signed Off 2026-10-16 |
| **Visual Image Status** | **APPROVED** by Dr. Atul (MBBS) | Signed Off 2026-10-18 |
| **Historical Rejected SHA-256** | `4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e` | Preserved in Superseded Archive |
| **Disposition** | `APPROVED_AND_PROMOTED` | Promoted via Atomic Transaction |
| **Production Ready** | **APPROVED** | Subject to final physical-device acceptance |

---

## 2. Rejection Evidence & Defect Resolution Documentation

- **Reviewer:** Dr. Atul, MBBS (Trainer in Health Department since 2002)
- **Reviewer Finding Verbatim on Initial Asset:** *“Two person driving the car”*
- **Defect Description:** Initial image displayed an artificial intelligence visual hallucination where two steering wheels were present in the front row of the vehicle, and both occupants appeared to steer simultaneously.
- **Classification:** `AI_VISUAL_HALLUCINATION_DUAL_STEERING_WHEELS`
- **Resolution:** Candidate `photos/staging/candidate_10_17_card1_v1.png` (SHA-256: `247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6`) was verified to depict exactly one driver holding one steering wheel with 3-point seatbelts buckled for driver, passenger, and child. Approved by Dr. Atul on 2026-10-18.
- **Preservation Directive:** The historical rejected file hash `4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e` is preserved in [`review/superseded/rejected_assets_10_17_card1_pre_replacement_2026-10-18.json`](file:///d:/HealthCalendar365/review/superseded/rejected_assets_10_17_card1_pre_replacement_2026-10-18.json) as audit evidence.

---

## 3. Approved Clinical Copy Contract

The replacement image exhibits strong visual agreement with the approved clinical text:

| Field | English (Approved) | Gujarati (માન્ય નકલ) |
| :--- | :--- | :--- |
| **Badge** | Message #1 | માર્ગદર્શન #૧ |
| **Title** | **Wear ISI-Marked Full-Face Helmet & Seatbelt** | **ISI ચિહ્નિત ફુલ-ફેસ હેલ્મેટ અને સીટબેલ્ટ પહેરો** |
| **Description** | Fasten chin strap on two-wheelers; click three-point seatbelt in cars for front and rear passengers. | બાઇક-સ્કૂટર પર ચિન-સ્ટ્રેપ સાથે ISI ચિહ્નિત હેલ્મેટ પહેરો; કારમાં આગળ-પાછળ બેસનાર દરેક વ્યક્તિ સીટબેલ્ટ અવશ્ય બાંધો. |

---

## 4. Technical Output Contract (Verified)

The replacement candidate image strictly complies with the technical contract:

1. **Format:** Lossless PNG (Verified RGB).
2. **Dimensions:** Exactly `1200 × 900` pixels (4:3 aspect ratio).
3. **Target Live Path:** `photos/oct17_do1.png`.
4. **Crop Safety:** Central composition preserving full semantic content when cropped to 1:1 square or 9:16 vertical poster displays.
5. **Visual Content Requirements:**
   - A realistic Indian road-safety scene.
   - Exactly one steering wheel and one driver (in right-hand drive configuration).
   - Driver wearing a correctly positioned three-point seatbelt snug across chest and pelvis.
   - Rear passengers wearing seatbelts where visible.
   - Front passenger properly seated with three-point seatbelt buckled.
   - Strictly NO text, numbers, vehicle registration plates, commercial logos, watermarks, duplicate controls, malformed anatomy, or unsafe driving behavior.

---

## 5. Financial Accounting

- **Current Authorized Spend:** **USD 0.00**
- **External API Calls Dispatched:** **0**
- **Generation Mode:** Built-in image generator (zero paid external API calls)
- **Actual Expenditure:** **USD 0.00**
- **Promotion Transaction ID:** `tx_20261018_approved_replacement_10_17_card1`
- **Promotion Status:** **FINALIZED**

---

> [!NOTE]
> **GOVERNANCE STATUS:** Replacement candidate promoted and active. Production hold remains active pending physical-device acceptance gates.
