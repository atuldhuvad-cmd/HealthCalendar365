# Versioned Annual Calendar 2026 Review Snapshot (v1.0.0)

**Snapshot Timestamp:** 2026-10-23T02:30:00+05:30  
**Target Reviewer:** Dr. Atul Dhuvad (Senior Medical Doctor, Public Health Specialist, District Health Trainer, Gujarat)  
**Governance Level:** Review-Only Proposal — In-Project Versioned Mirror  

---

## 1. Purpose & Air-Gap Independence

This directory (`review/annual_review_2026_snapshot_v1/`) contains an immutable, self-contained snapshot of all clinical review dossiers, placement manifests, decision registers, and validation outputs for the complete 365-day 2026 calendar.

By embedding these review artifacts directly into the `HealthCalendar365` repository:
1. The project build, offline review tooling, and service worker do NOT depend on external conversational directories or transient paths.
2. Complete auditability is preserved directly within the codebase for version control.
3. Review status remains strictly separated from clinical sign-off, activation, and asset generation.

---

## 2. Inventory of Snapshot Documents

| File Name | File Size | Primary Purpose |
| :--- | :--- | :--- |
| `ANNUAL_CALENDAR_2026_FINAL_REVIEW_PACKET.md` | 10,994 bytes | Executive summary, audit methodology & readiness packet |
| `PENDING_DECISIONS_REGISTER.md` | 30,139 bytes | Master Pending Decisions Register (DEC-01 to DEC-19) |
| `ROUTINE_CALENDAR_CARD_LEVEL_AUDIT.md` | 129,358 bytes | Card-level audit of all 207 retained baseline routine days across 34 topics |
| `MATERNAL_CHILD_AMB_CLINICAL_REVIEW.md` | 155,317 bytes | Full 4-card clinical copy for 17 routine replacement sets (68 cards) |
| `PROPOSED_OBSERVANCE_ADDITIONS_REVIEW.md` | 80,894 bytes | Full 4-card clinical copy for 8 additions + food adulteration (36 cards) |
| `BATCH_5_CLINICAL_REVIEW.md` | 210,887 bytes | Batch 5 draft observance campaigns (Items 49–74, 104 cards) |
| `BATCH_4_CLINICAL_REVIEW.md` | 87,478 bytes | Batch 4 draft observance campaigns (Items 37, 39–48, 44 cards) |
| `BATCH_3_CLINICAL_REVIEW.md` | 100,859 bytes | Batch 3 draft observance campaigns (Items 25–36, 48 cards) |
| `ITEM_38_CLINICAL_REVIEW.md` | 14,909 bytes | Item 38 (World Brain Day) approved clinical copy (4 cards) |
| `annual_placement_manifest_2026.json` | 433,272 bytes | Machine-readable 365-day placement manifest (Schema v2.1.0) |
| `annual_coverage_index_2026.json` | 405,417 bytes | Curriculum coverage index across all CPHC health topics |
| `annual_calendar_2026_validation_output.txt` | 10,028 bytes | Reproducible output of master 365-day validator script (0 errors) |

---

## 3. Governance Boundaries & Review Protocol

- **Active Calendar Preservation:** `data/health_365.json`, `data/pending_observance_content_2026.json`, and `data/observance_overrides.json` are 100% frozen.
- **Review View Separation:** The PWA's Calendar Review view consumes `data/annual_review_2026.json` and `js/review-data.js` independently.
- **Visual Status Discipline:** Existing photos are marked `CURRENT_ACTIVE_ASSET`. Proposed visual briefs and AI prompts are marked `PROPOSED_BRIEF_AWAITING_GENERATION` and must NEVER be presented as approved matches for revised copy.
- **Pending Judgments:** All decisions requiring clinical, administrative, or scheduling judgment remain strictly **PENDING** in `PENDING_DECISIONS_REGISTER.md` (`DEC-01` to `DEC-19`).
