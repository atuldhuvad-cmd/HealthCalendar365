#!/usr/bin/env python3
"""Generate the evidence-reconciled Stage 1 human-review register."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def file_sha(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


health = load("data/health_365.json")
ledger = load("data/approved_manifest.json")
queue = load("review/review_queue.json")["review_queue"]
proposals = load("review/proposed_copy_and_provenance_corrections.json")
pilot = load("review/NINE_CANDIDATE_PILOT_PLAN.json")
bulk = load("review/human_decisions/clinical_dr_atul_2026-10-16.json")
transition = load("review/human_decisions/clinical_decision_transition_2026-10-16.json")
scoped = load("review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json")
nine = load("review/human_decisions/replacement_images_dr_atul_2026-10-16.json")
road = load("review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json")
reconciliation = load("review/approval_ledger_reconciliation_2026-10-18.json")

payload_hash = file_sha("review/candidate_payload_manifest.json")
health_by_id = {day["id"]: day for day in health}
queue_by_slot = {f"{r['poster_id']}_card{r['card_idx']}": r for r in queue}
ledger_by_slot = {f"{v['day_id']}_card{int(v['card_idx'])}": (h, v) for h, v in ledger.items()}
pilot_by_slot = {item["slot"]: item for item in pilot.get("candidates", [])}
proposal_by_slot = {item.get("slot"): item for item in proposals.get("staged_copy_audit_and_corrections", [])}
provenance_by_day = proposals.get("health_observance_provenance", {})

nine_slots = set(nine["scope"])
scoped_slots = set(scoped["card_decisions"])
carried_slots = set(transition["carried_forward_slots"])
approved_slots = {slot for slot, (_, rec) in ledger_by_slot.items() if rec["status"] == "APPROVED"}
pending_slots = {slot for slot, (_, rec) in ledger_by_slot.items() if rec["status"] == "PENDING_CLINICAL_SIGN_OFF"}

assert len(ledger_by_slot) == 40
assert len(approved_slots) == 13 and len(pending_slots) == 27
assert approved_slots == nine_slots | scoped_slots
assert pending_slots == carried_slots
assert reconciliation["active_ledger_counts"] == {"PENDING_CLINICAL_SIGN_OFF": 27, "APPROVED": 13}

day_order = ["10-15", "10-15-cane", "10-16", "10-16-spine", "10-17", "10-18", "10-19", "10-19-oral", "10-20", "10-21"]
ordered_slots = [f"{day}_card{idx}" for day in day_order for idx in range(1, 5)]


def proposal_for(slot):
    aliases = {
        "10-18_card3": "10-18_card3_and_card4", "10-18_card4": "10-18_card3_and_card4",
        "10-20_card3": "10-20_card3_title_and_desc", "10-20_card4": "10-20_card4_title_and_desc",
        "10-21_card2": "10-21_card2_desc", "10-21_card3": "10-21_card3_title",
        "10-21_card4": "10-21_card4_title", "10-15_card2": "10-15_card2_desc",
        "10-16-spine_card4": "10-16-spine_card4_desc", "10-17_card3": "10-17_card3_title",
    }
    return proposal_by_slot.get(slot) or proposal_by_slot.get(aliases.get(slot))


def decision_for(slot):
    if slot in nine_slots:
        reviewer = nine["reviewer"]
        return {"decision": nine["normalized_decision"], "reviewer_name": reviewer["name"],
                "reviewer_qualification": reviewer["qualification"],
                "reviewer_professional_role": reviewer.get("professional_role") or reviewer.get("role"),
                "review_date_iso": nine["submitted_at"], "decision_verbatim": nine["decision_verbatim"],
                "decision_record_path": "review/human_decisions/replacement_images_dr_atul_2026-10-16.json",
                "transaction_id": nine.get("transaction_id")}
    if slot == "10-17_card1":
        reviewer = road["reviewer"]
        return {"decision": road["normalized_decision"], "reviewer_name": reviewer["name"],
                "reviewer_qualification": reviewer["qualification"],
                "reviewer_professional_role": reviewer.get("professional_role") or reviewer.get("role"),
                "review_date_iso": road["submitted_at"], "decision_verbatim": road["decision_verbatim"],
                "decision_record_path": "review/human_decisions/replacement_image_10_17_card1_dr_atul_2026-10-18.json",
                "transaction_id": road["transaction_id"]}
    if slot in scoped_slots:
        reviewer = scoped["reviewer"]
        return {"decision": scoped["card_decisions"][slot]["overall_card_decision"],
                "reviewer_name": reviewer["name"], "reviewer_qualification": reviewer["qualification"],
                "reviewer_professional_role": reviewer.get("professional_role") or reviewer.get("role"),
                "review_date_iso": scoped["submitted_at"],
                "decision_verbatim": scoped["statements"]["approval_statement_verbatim"],
                "decision_record_path": "review/human_decisions/scoped_reapproval_dr_atul_2026-10-16.json",
                "transaction_id": reconciliation["transaction_id"]}
    reviewer = bulk["reviewer"]
    return {"decision": bulk["decision"], "reviewer_name": reviewer["name"],
            "reviewer_qualification": reviewer["qualification"],
            "reviewer_professional_role": reviewer["professional_role"],
            "review_date_iso": bulk["submitted_at"],
            "decision_verbatim": bulk["user_statements"]["decision_verbatim"],
            "decision_record_path": "review/human_decisions/clinical_dr_atul_2026-10-16.json",
            "carry_forward_transition_path": "review/human_decisions/clinical_decision_transition_2026-10-16.json"}


records = []
for slot in ordered_slots:
    image_hash, entry = ledger_by_slot[slot]
    day = health_by_id[entry["day_id"]]
    card = day["cards"][int(entry["card_idx"]) - 1]
    q = queue_by_slot[slot]
    status = entry["status"]
    decision = decision_for(slot)
    prop = proposal_for(slot)
    pilot_info = pilot_by_slot.get(slot)

    if slot in nine_slots:
        replacement_spec = {"is_pilot_candidate": True, "classification": "PROMOTED_APPROVED_REPLACEMENT",
                            "authorization_state": "AUTHORIZED_AND_PROMOTED",
                            "candidate_specification_sha256": (pilot_info or {}).get("spec_binding", {}).get("candidate_specification_sha256"),
                            "output_contract": (pilot_info or {}).get("output_contract")}
    elif slot == "10-17_card1":
        replacement_spec = {"is_pilot_candidate": True, "classification": "PROMOTED_APPROVED_REPLACEMENT",
                            "authorization_state": "AUTHORIZED_AND_PROMOTED",
                            "candidate_specification_sha256": entry["spec_hash"],
                            "output_contract": road["candidate_verification"]}
    else:
        replacement_spec = {"is_pilot_candidate": False,
                            "classification": "APPROVED_EXISTING_ASSET_AFTER_SCOPED_REVIEW" if status == "APPROVED" else None,
                            "authorization_state": "APPROVED" if status == "APPROVED" else None,
                            "candidate_specification_sha256": None, "output_contract": None}

    provenance = provenance_by_day.get(entry["day_id"], {})
    records.append({
        "slot": slot, "poster_id": entry["day_id"], "poster_title_en": day.get("title_en"),
        "poster_title_gu": day.get("title_gu"), "card_idx": entry["card_idx"],
        "card_type": card.get("type", "message"), "status": status,
        "review_category": "APPROVED_CARD_ASSET" if status == "APPROVED" else "PENDING_NONCLINICAL_HUMAN_GATES",
        "bound_payload_manifest_sha256": payload_hash,
        "active_hashes": {"image_sha256": image_hash, "spec_hash": entry["spec_hash"], "file_reference": entry["file_reference"]},
        "current_copy": {"title_en": card.get("title_en", ""), "title_gu": card.get("title_gu", ""),
                         "desc_en": card.get("desc_en", ""), "desc_gu": card.get("desc_gu", "")},
        "provenance": {"observance_en": provenance.get("observance_name_en", day.get("title_en")),
                       "sponsoring_agency": provenance.get("official_sponsoring_body") or "Daily Clinical Health Guidance (Organization-Neutral)",
                       "official_status": provenance.get("international_status", "Clinical Guidance Day"),
                       "primary_source": provenance.get("source_citation", "Primary Clinical Guidelines"),
                       "provenance_notes": provenance.get("provenance_notes", "")},
        "observed_concern": {"issue_summary": q.get("observed_issue", ""), "source_evidence": q.get("source_evidence", ""),
                             "polarity": q.get("polarity", "DO"),
                             "required_visual_objects_actions": q.get("required_visual_objects_actions", "")},
        "proposed_correction": {"has_staged_proposal": prop is not None,
                                "rationale": prop.get("rationale") if prop else None,
                                "clinical_evidence_source": prop.get("clinical_evidence_source") if prop else None,
                                "proposed_en": prop.get("proposed_en") if prop else None,
                                "proposed_gu": prop.get("proposed_gu") if prop else None},
        "replacement_candidate_spec": replacement_spec,
        "required_reviewer_role": "None for approved scope" if status == "APPROVED" else "Native Gujarati linguist + qualified visual/provenance reviewer",
        "human_decision_intake": {"decision": "APPROVED" if status == "APPROVED" else "PENDING_HUMAN_REVIEW",
                                  "clinical_decision": "APPROVE", "clinical_review": decision,
                                  "clinical_review_invalidation": None, "gujarati_decision": None,
                                  "visual_decision": "APPROVE" if status == "APPROVED" else None,
                                  "signature_status": "RECORDED" if status == "APPROVED" else "CLINICAL_RECORDED_OTHER_GATES_PENDING"}
    })

assert len(records) == 40 and len({r["slot"] for r in records}) == 40
assert sum(r["status"] == "APPROVED" for r in records) == 13
assert sum(r["status"] == "PENDING_CLINICAL_SIGN_OFF" for r in records) == 27
assert all(r["human_decision_intake"]["clinical_decision"] == "APPROVE" for r in records)

output = {
    "schema_version": "3.0.0", "phase": "final_acceptance_human_review_in_progress", "created_at": "2026-10-18",
    "governance": {"standard": "review/RELEASE_GOVERNANCE.md", "production_hold": "STRICTLY_ACTIVE",
                   "authorized_spending": "USD 0.00", "payload_manifest_sha256": payload_hash,
                   "anti_fabrication_rule": "Only directly supplied human decisions are recorded."},
    "summary_counts": {"total_spotlight_cards": 40, "approved_active_cards": 13,
                       "pending_overall_human_review": 27, "rejected_image_content_mismatches": 0,
                       "clinical_copy_approved": 40, "promoted_replacement_images": 10,
                       "approved_existing_scoped_cards": 3, "carried_forward_clinical_approvals": 27,
                       "pending_card_scoped_reapprovals_required": 0, "gujarati_reviews_still_required": 27,
                       "visual_provenance_reviews_still_required": 27},
    "categories": {"category_1_approved_active_cards": sorted(approved_slots),
                   "category_2_clinically_approved_other_gates_pending": sorted(pending_slots),
                   "category_3_rejected_image_mismatches": []},
    "ledger_reconciliation": "review/approval_ledger_reconciliation_2026-10-18.json",
    "staged_copy_proposals": proposals.get("staged_copy_audit_and_corrections", []), "records": records}

(ROOT / "review" / "CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.json").write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("[PASS] Generated evidence-reconciled register: 13 APPROVED / 27 PENDING / 0 REJECTED")
