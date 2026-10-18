# HealthCalendar365 — Full-Calendar Content & Structure Audit Report


> **CURRENT-STATE NOTICE (2026-10-18):** This document contains historical checkpoint counts. The authoritative current state is `13 APPROVED / 27 PENDING / 0 REJECTED`; all 40 clinical copies are approved, while 27 records retain other human gates. See `review/approval_ledger_reconciliation_2026-10-18.json`.
**Date:** October 16, 2026  
**Document ID:** `AUDIT-FULL-CALENDAR-20261016`  
**Status:** AUDITED — TECHNICAL STRUCTURAL BASELINE VERIFIED  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Production Hold:** STRICTLY ACTIVE

---

## 1. Executive Summary

A comprehensive full-calendar audit was executed across all records in `data/health_365.json` and all active image references in `photos/`.

### Key Verification Metrics:
- **Total Calendar Poster Records:** `368`
- **Calendar Dates Represented:** `365 / 365` (100% full-year calendar coverage)
- **Multi-Observance Split Records:** `3` dates with dedicated multi-topic posters
- **Total Card Slots Audited:** `1,472` ($368 \text{ posters} \times 4 \text{ cards}$)
- **Dedicated Spotlight Card Assets:** `40` cards across 10 spotlight posters
- **Generic Category Placeholders:** `1,432` cards backed by 5 verified category assets
- **Empty or Missing Text Fields:** `0` (Zero missing English or Gujarati titles/descriptions)
- **Missing Image References on Disk:** `0` (All 1,472 card photo references exist in `photos/`)
- **Corrupt Image Decoding Errors:** `0` (All 57 physical photo files in `photos/` decode with PIL)
- **Canonical Specification Hashes Generated:** `1,472 / 1,472` canonical hashes computed and recorded in [`review/full_calendar_audit.json`](file:///d:/HealthCalendar365/review/full_calendar_audit.json)

---

## 2. Calendar Date Coverage & Multi-Observance Separation

All 365 calendar days from January 1 through December 31 are accounted for. Three specific dates feature dual public health observances that are properly maintained as independent, decoupled poster records:

| Date | Primary Observance ID & Title | Decoupled Observance ID & Title | Clinical Domain |
| :---: | :--- | :--- | :--- |
| **October 15** | `10-15`: Global Handwashing Day | `10-15-cane`: World White Cane Day | Infection Control & Hygiene vs. Visual Impairment & Eye Health |
| **October 16** | `10-16`: World Food Day | `10-16-spine`: World Spine Day | Nutrition & Food Security vs. Musculoskeletal & Spine Ergonomics |
| **October 19** | `10-19`: Ear & Hearing Care | `10-19-oral`: Oral Health & Tobacco-Free Life | ENT Primary Care vs. Dental Health & Oral Cancer Prevention |

All other 362 calendar dates are mapped 1-to-1 with single dedicated health observances or daily clinical guidance topics.

---

## 3. Monthly Distribution of Posters & Card Slots

| Month | Month Name | Poster Records | Total Card Slots | Dedicated Cards | Placeholder Cards |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **01** | January | 31 | 124 | 0 | 124 |
| **02** | February | 28 | 112 | 0 | 112 |
| **03** | March | 31 | 124 | 0 | 124 |
| **04** | April | 30 | 120 | 0 | 120 |
| **05** | May | 31 | 124 | 0 | 124 |
| **06** | June | 30 | 120 | 0 | 120 |
| **07** | July | 31 | 124 | 0 | 124 |
| **08** | August | 31 | 124 | 0 | 124 |
| **09** | September | 30 | 120 | 0 | 120 |
| **10** | October | 34 *(31 + 3 splits)* | 136 | 40 | 96 |
| **11** | November | 30 | 120 | 0 | 120 |
| **12** | December | 31 | 124 | 0 | 124 |
| **TOTALS** | **Full Year** | **368** | **1,472** | **40** | **1,432** |

---

## 4. Visual Asset Distribution & Placeholder Inventory

### A. Dedicated Spotlight Cards (40 slots in October)
All 40 cards across the 10 dedicated October posters (`10-15` through `10-21`) reference dedicated, high-resolution photographs:
- 31 cards pending human clinical/Gujarati review.
- 9 cards identified with visual mismatches and staged for candidate re-specification.

### B. Generic Category Placeholders (1,432 slots across Months 1–12)
The remaining 1,432 cards across the calendar are backed by 5 high-resolution category placeholders:

| Category Placeholder File | Clinical Domain Covered | Active Card References | Physical Status |
| :--- | :--- | :---: | :---: |
| `photos/cat_yoga.png` | Yoga, physical exercise, physical therapy, mobility | 292 cards | Verified ($4:3$, $1080\times810$ px, valid PNG) |
| `photos/cat_mental.png` | Mental health, stress, sleep, counseling, mindfulness | 292 cards | Verified ($4:3$, $1080\times810$ px, valid PNG) |
| `photos/cat_infection.png` | Infectious diseases, immunization, sanitation, vector control | 284 cards | Verified ($4:3$, $1080\times810$ px, valid PNG) |
| `photos/cat_nutrition.png` | Diet, micronutrients, breastfeeding, diabetes nutrition | 284 cards | Verified ($4:3$, $1080\times810$ px, valid PNG) |
| `photos/cat_cardio.png` | Hypertension, cardiac care, emergency response, vitals | 280 cards | Verified ($4:3$, $1080\times810$ px, valid PNG) |
| **TOTAL PLACEHOLDERS** | **5 Core Clinical Categories** | **1,432 cards** | **100% Decodable & Present** |

---

## 5. Text Integrity & Bilingual Completeness

Every one of the 1,472 card objects was audited for text field presence:
- **`title_en`:** 1,472 / 1,472 populated (0 empty).
- **`title_gu`:** 1,472 / 1,472 populated (0 empty).
- **`desc_en`:** 1,472 / 1,472 populated (0 empty).
- **`desc_gu`:** 1,472 / 1,472 populated (0 empty).
- **`ai_prompt`:** 1,472 / 1,472 populated with structured photorealistic Indian medical prompt formulas.

Zero missing or placeholder text strings exist in the database.

---

## 6. Machine-Readable Audit Data Reference

Complete slot-by-slot canonical specification hashes and image bindings for all 1,472 cards are persisted in:
[`review/full_calendar_audit.json`](file:///d:/HealthCalendar365/review/full_calendar_audit.json).

---

## 7. Audit Conclusion & Gate Compliance

1. **Step 5 & 6 Technical Invariance:** Full calendar structure is confirmed 100% complete, decodable, and consistent.
2. **Zero-Spend Adherence:** No external APIs were invoked and zero dollars were expended during this audit.
3. **Production Hold Status:** The approval ledger remains at **`0 APPROVED`**, **`31 PENDING_CLINICAL_SIGN_OFF`**, and **`9 REJECTED_MISMATCH`**. The production hold remains strictly active.
