# HealthCalendar365 Active Image Inventory

**Updated:** 26 October 2026
**Workflow:** Doctor-owned personal use; no separate approval gate

The active 365-day dataset contains 1,460 card references using 208 unique local photos. Every referenced file exists and decodes. Existing topic images remain active until the doctor-owner identifies a mismatch or supplies a better replacement.

## Current dedicated replacements

The final local pass activated 24 non-Canva images across six CPHC topics: antenatal care, safe institutional delivery, dementia/fall prevention, diabetes care, eye care, and WASH/infection control. Each active replacement is normalized to 720×540 PNG and is preserved with source, original-active, and final hashes in `review/PERSONAL_USE_FINALIZATION_2026-10-26.json`.

The ANC set uses the owner-selected Mamta-card handover, tablet adherence, examination, and 108 transfer scenes. The eye-care set uses the NPCB-aligned six-metre E-chart scene plus postoperative eye protection, clean face/eye washing, and slit-lamp examination. Rejected Canva generations were not activated.

## Existing active assets

Cards without a selected replacement continue using their current CPHC or observance image. This is a non-blocking personal-use fallback, not a claim that every image is a perfect semantic match. Later owner feedback should replace only the affected slot while preserving the original and provenance.

## Quality checks

- Confirm the image depicts the card’s primary action and body system.
- Reject wrong anatomy, unsafe procedures, malformed hands, unreadable generated text, invented labels, misleading equipment, or unrelated subjects.
- Prefer authentic Indian domestic and healthcare settings.
- Check the central crop in square and vertical posters and all English/Gujarati modes.
- Avoid duplicate imagery within one poster and obvious cross-topic duplication.
- Preserve active originals and hashes before replacement.

## Historical audit

The original generic-placeholder and spotlight-week discrepancy audit is preserved unchanged at `review/HISTORICAL_CALENDAR_IMAGE_AUDIT_2026-10-15.md`. Its old release-gate terminology is historical and does not control local use.
