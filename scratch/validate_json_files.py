import json
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")

# 1. Validate review/scoped_clinical_reapproval_packet.json
p1 = ROOT / "review" / "scoped_clinical_reapproval_packet.json"
assert p1.exists(), f"{p1} does not exist!"
d1 = json.loads(p1.read_text(encoding="utf-8"))

assert "packet_id" in d1
assert "title" in d1
assert "reviewer" in d1
assert "cards" in d1
assert len(d1["cards"]) == 4, f"Expected 4 cards in packet, got {len(d1['cards'])}"

for c in d1["cards"]:
    assert "slot" in c
    assert "title_en" in c
    assert "title_gu" in c
    assert "desc_en" in c
    assert "desc_gu" in c
    assert "image_file" in c
    assert "image_sha256" in c
    assert "spec_hash" in c
    assert "decision" in c
    assert c["decision"] in ["PENDING", "APPROVE", "REJECT", "COPY_APPROVED_IMAGE_PENDING_REPLACEMENT"]
    assert c["valid_choices"] == ["APPROVE", "REJECT"]
    # verify file existence and hash
    img_path = ROOT / c["image_file"]
    assert img_path.exists(), f"Image {img_path} missing!"

print("[PASS] review/scoped_clinical_reapproval_packet.json is 100% structurally valid.")

# 2. Validate scratch/four_cards_info.json
p2 = ROOT / "scratch" / "four_cards_info.json"
assert p2.exists(), f"{p2} does not exist!"
d2 = json.loads(p2.read_text(encoding="utf-8"))
assert len(d2) == 4
for item in d2:
    assert "slot" in item
    assert "card" in item
    assert "ledger_entry" in item

print("[PASS] scratch/four_cards_info.json is 100% structurally valid.")
print("[ALL JSON VALIDATION PASSED]")
