#!/usr/bin/env python3
"""Render the evidence-reconciled Stage 1 register as Markdown."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "review" / "CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.json").read_text(encoding="utf-8"))
records = data["records"]
summary = data["summary_counts"]
payload_hash = data["governance"]["payload_manifest_sha256"]

lines = [
    "# HealthCalendar365 - Human Review Decision Register",
    "",
    "**Date:** October 18, 2026",
    "**Production Hold:** **STRICTLY ACTIVE**",
    "**Recorded external provider spend:** **USD 0.00**",
    f"**Bound payload-manifest SHA-256:** `{payload_hash}`",
    "**Ledger state:** `13 APPROVED`, `27 PENDING_CLINICAL_SIGN_OFF`, `0 REJECTED_MISMATCH`",
    "",
    "> The 27 pending ledger records already have carried clinical-copy approval. They remain blocked because the original bulk decision explicitly excluded visual/accessibility, Gujarati linguistic, provenance, asset-promotion and release authorization.",
    "",
    "## Decision reconciliation",
    "",
    f"- Clinical copy approved: **{summary['clinical_copy_approved']} / 40**",
    f"- Release-eligible active cards: **{summary['approved_active_cards']} / 40**",
    f"- Promoted replacement images: **{summary['promoted_replacement_images']}**",
    f"- Approved existing scoped cards: **{summary['approved_existing_scoped_cards']}**",
    f"- Clinical approvals carried forward with other gates pending: **{summary['carried_forward_clinical_approvals']}**",
    f"- Active rejected mismatches: **{summary['rejected_image_content_mismatches']}**",
    "",
    "## Approved active cards",
    "",
    "| Slot | Observance | English title | Image | Decision evidence |",
    "| :--- | :--- | :--- | :--- | :--- |",
]

for rec in records:
    if rec["status"] == "APPROVED":
        decision = rec["human_decision_intake"]["clinical_review"]
        lines.append(f"| `{rec['slot']}` | {rec['poster_title_en']} | {rec['current_copy']['title_en']} | `{rec['active_hashes']['file_reference']}` | `{decision['decision_record_path']}` |")

lines += [
    "",
    "## Clinically approved cards with other gates pending",
    "",
    "| Slot | Observance | English title | Clinical decision | Remaining gates |",
    "| :--- | :--- | :--- | :---: | :--- |",
]

for rec in records:
    if rec["status"] == "PENDING_CLINICAL_SIGN_OFF":
        lines.append(f"| `{rec['slot']}` | {rec['poster_title_en']} | {rec['current_copy']['title_en']} | APPROVE carried forward | Gujarati, visual/accessibility, provenance and release authorization |")

lines += [
    "",
    "## Remaining acceptance work",
    "",
    "- Obtain explicit visual/accessibility, Gujarati-language and provenance decisions for the 27 pending cards.",
    "- Complete the ten physical Android/PWA/WhatsApp checks in `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`.",
    "- Keep production, commit, push and deployment actions on hold until every required gate is recorded.",
]

(ROOT / "review" / "CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("[PASS] Generated reconciled Markdown register")
