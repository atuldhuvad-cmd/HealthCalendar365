import json
import hashlib
import os
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def test_scoped_acceptance():
    print("=== BEGIN COMPREHENSIVE SCOPED ACCEPTANCE VALIDATION ===")
    
    # 1. Check human decision record
    human_dec_path = ROOT / "review" / "human_decisions" / "scoped_reapproval_dr_atul_2026-10-16.json"
    assert human_dec_path.exists(), "human decision record missing"
    hdec = json.loads(human_dec_path.read_text(encoding="utf-8"))
    
    card_decs = hdec["card_decisions"]
    assert len(card_decs) == 4, f"Expected 4 card decisions, found {len(card_decs)}"
    
    copy_approved = [slot for slot, d in card_decs.items() if d.get("clinical_copy_decision") == "APPROVE"]
    assert len(copy_approved) == 4, f"Expected 4 clinical copy approvals, found {len(copy_approved)}: {copy_approved}"
    
    img_rejected = [slot for slot, d in card_decs.items() if d.get("visual_image_decision") == "REJECT"]
    assert len(img_rejected) == 1 and img_rejected[0] == "10-17_card1", f"Expected exactly 1 visual rejection on 10-17_card1, got {img_rejected}"
    
    # Check Card 3 specific fields
    c3 = card_decs["10-17_card1"]
    assert c3["clinical_copy_decision"] == "APPROVE", "10-17_card1 clinical copy must be APPROVE"
    assert c3["visual_image_decision"] == "REJECT", "10-17_card1 visual image must be REJECT"
    assert c3["overall_card_decision"] == "COPY_APPROVED_IMAGE_PENDING_REPLACEMENT"
    assert c3["production_approved"] is False, "10-17_card1 must NOT be marked production approved"
    assert c3["defect_classification"] == "AI_VISUAL_HALLUCINATION_DUAL_STEERING_WHEELS"
    assert c3["required_disposition"] == "PENDING_REPLACEMENT_CANDIDATE"
    print("[PASS] Human decisions record verified (4 copy approvals, 1 visual rejection).")

    # 2. Check Candidate Generation Queue
    queue_path = ROOT / "review" / "candidate_generation_queue.json"
    assert queue_path.exists(), "candidate_generation_queue.json missing"
    qdata = json.loads(queue_path.read_text(encoding="utf-8"))
    assert qdata["total_items"] == 1, f"Expected exactly 1 item in candidate queue, got {qdata['total_items']}"
    assert len(qdata["items"]) == 1
    qitem = qdata["items"][0]
    assert qitem["slot"] == "10-17_card1"
    assert qitem["current_image_path"] == "photos/oct17_do1.png"
    assert qitem["current_image_sha256"] == "4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e"
    assert qitem["approved_spec_hash"] == "122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1"
    assert qitem["candidate_contract"]["dimensions"]["width"] == 1200
    assert qitem["candidate_contract"]["dimensions"]["height"] == 900
    assert qitem["candidate_contract"]["aspect_ratio"] == "4:3"
    assert qitem["candidate_contract"]["format"] == "PNG"
    print("[PASS] Controlled candidate generation queue verified.")

    # 3. Check Scoped Reapproval JSON Packet
    pkt_json_path = ROOT / "review" / "scoped_clinical_reapproval_packet.json"
    assert pkt_json_path.exists(), "scoped_clinical_reapproval_packet.json missing"
    pjson = json.loads(pkt_json_path.read_text(encoding="utf-8"))
    assert pjson["decisions_summary"]["clinical_copy_approved"] == 4
    assert pjson["decisions_summary"]["remaining_clinical_copy_decisions"] == 0
    assert pjson["decisions_summary"]["visual_images_accepted"] == 3
    assert pjson["decisions_summary"]["visual_images_rejected"] == 1
    assert pjson["decisions_summary"]["remaining_visual_replacements"] == 1
    assert pjson["decisions_summary"]["cards_fully_approved"] == 3
    assert pjson["decisions_summary"]["cards_pending_image_replacement"] == 1
    print("[PASS] Scoped reapproval JSON packet verified.")

    # 4. Check Markdown Packet
    md_path = ROOT / "review" / "SCOPED_CLINICAL_REAPPROVAL_PACKET.md"
    assert md_path.exists(), "SCOPED_CLINICAL_REAPPROVAL_PACKET.md missing"
    md_text = md_path.read_text(encoding="utf-8")
    assert "4 / 4 **APPROVED**" in md_text
    assert "3 **ACCEPTED** &bull; 1 **REJECTED**" in md_text
    assert "AI_VISUAL_HALLUCINATION_DUAL_STEERING_WHEELS" in md_text
    assert "Two person driving the car" in md_text
    # Ensure Card 3 has separate copy and image controls and no contradictory APPROVE on image
    assert "- [ ] **APPROVE** *(Contradictory option NOT selected)*" in md_text
    assert "- [x] **REJECT** (Recorded by Dr. Atul, 2026-10-16)" in md_text
    print("[PASS] Scoped reapproval Markdown packet verified.")

    # 5. Check HTML Packet
    html_path = ROOT / "review" / "scoped-clinical-reapproval.html"
    assert html_path.exists(), "scoped-clinical-reapproval.html missing"
    html_text = html_path.read_text(encoding="utf-8")
    assert 'name="copy_decision_10-17_card1" value="APPROVE" checked' in html_text
    assert 'name="image_decision_10-17_card1" value="REJECT" checked' in html_text
    assert 'name="image_decision_10-17_card1" value="APPROVE"' in html_text
    assert 'name="image_decision_10-17_card1" value="APPROVE" checked' not in html_text
    assert "AI_VISUAL_HALLUCINATION_DUAL_STEERING_WHEELS" in html_text
    print("[PASS] Scoped reapproval HTML packet verified.")

    # 6. Check PDF Packet
    pdf_path = ROOT / "review" / "scoped_clinical_reapproval_packet.pdf"
    assert pdf_path.exists(), "scoped_clinical_reapproval_packet.pdf missing"
    pdf_size = os.path.getsize(pdf_path)
    assert pdf_size > 100000, f"PDF file size too small: {pdf_size} bytes"
    print(f"[PASS] PDF packet exists and verified ({pdf_size} bytes).")

    # 7. Check Specification & Authorization Sheet
    auth_path = ROOT / "review" / "REPLACEMENT_SPECIFICATION_AND_AUTHORIZATION_10_17_CARD1.md"
    assert auth_path.exists(), "REPLACEMENT_SPECIFICATION_AND_AUTHORIZATION_10_17_CARD1.md missing"
    auth_text = auth_path.read_text(encoding="utf-8")
    assert "4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e" in auth_text
    assert "122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1" in auth_text
    assert "Two person driving the car" in auth_text
    assert "1200 × 900" in auth_text
    assert "USD 0.00" in auth_text
    assert "BLOCKED" in auth_text
    print("[PASS] Replacement specification and authorization sheet verified.")

    # 8. Check Existing Nine Promoted Replacements in Manifest
    manifest_path = ROOT / "data" / "approved_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    
    promoted_expected = {
        "e9c9b5762eff9648ab700190cd92d896c7cdf00b73e6e1b5df8b683af07a93bb": ("10-19-oral", 2),
        "26dbb852beccf2358c471fe69bcffb5c6562bbc514ece89eb365908b6b64f1c8": ("10-20", 1),
        "347402abd8e1ceb3aa90fcff170ebda99a2198975344260bf809f858d13afed0": ("10-20", 2),
        "28a0205f55286945f252a5ec448c1f22464bd18e3d12a39f63c9fbb312e32f4a": ("10-20", 3),
        "5de63340092a8d6a0f29116ea330690e00199dc7d396dc3082199d020a7edfe7": ("10-20", 4),
        "762e775811b51e4659137729049cd527bbe877332d3cba87d086e8637b95972b": ("10-21", 1),
        "fca3971d212004b4cccbb4f4b5efd4b2fe39906f54a5b8f893ff4eeef5ac04f2": ("10-21", 2),
        "d4ec74ea78c05daeb54fa16aa83e2f705545f03428bd1c59d1b49fd8b523ca37": ("10-21", 3),
        "f5481ee5ce7ea4f6cb985997fd7ab6685f584be8f2cbcd8c5165b1905c716153": ("10-21", 4)
    }

    for h, (day_id, card_idx) in promoted_expected.items():
        assert h in manifest, f"Promoted hash {h} missing from manifest"
        assert manifest[h]["status"] == "APPROVED", f"Promoted hash {h} status is not APPROVED: {manifest[h]['status']}"
        assert manifest[h]["day_id"] == day_id
        assert manifest[h]["card_idx"] == card_idx
        # Also check disk file matches
        file_ref = manifest[h]["file_reference"]
        disk_hash = get_sha256(ROOT / file_ref)
        assert disk_hash == h, f"Disk hash for {file_ref} ({disk_hash}) != {h}"
    
    print("[PASS] All 9 promoted replacement images remain completely unchanged and match disk/ledger.")

    # 9. Check oct17_do1.png on disk
    oct17_hash = get_sha256(ROOT / "photos" / "oct17_do1.png")
    assert oct17_hash == "4f155d0239df8c2815424dfd17a184b274fd95ddfeee37e8ecee7fe9fe3a849e", "photos/oct17_do1.png has been altered!"
    print("[PASS] photos/oct17_do1.png preserved as rejected evidence.")

    print("=== ALL VALIDATION TESTS PASSED (9/9) ===")

if __name__ == "__main__":
    test_scoped_acceptance()
