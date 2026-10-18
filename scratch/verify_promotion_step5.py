import json
import hashlib
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(r"D:\HealthCalendar365")
sys.path.insert(0, str(ROOT))
from generate_with_gemini import compute_card_spec_hash

print("=== Running Comprehensive Promotion Verification ===")

# 1. active_transaction.json must be absent
pointer = ROOT / "data" / "active_transaction.json"
assert not pointer.exists(), "active_transaction.json is not absent!"
print("  [PASS] data/active_transaction.json is absent.")

# 2. Both transaction plans must be FINALIZED
tx1_plan = ROOT / "data" / "transactions" / "tx_20261016_approved_replacements" / "tx_plan.json"
assert tx1_plan.exists(), "tx1 plan does not exist!"
assert json.loads(tx1_plan.read_text(encoding="utf-8")).get("state") == "FINALIZED"

tx2_plan = ROOT / "data" / "transactions" / "tx_20261018_approved_replacement_10_17_card1" / "tx_plan.json"
assert tx2_plan.exists(), "tx2 plan does not exist!"
assert json.loads(tx2_plan.read_text(encoding="utf-8")).get("state") == "FINALIZED"
print("  [PASS] Both transaction plans (tx1: 9 images, tx2: 1 image) are FINALIZED.")

# 3. Active ledger counts
ledger = json.loads((ROOT / "data" / "approved_manifest.json").read_text(encoding="utf-8"))
approved = [v for v in ledger.values() if v["status"] == "APPROVED"]
pending = [v for v in ledger.values() if v["status"] == "PENDING_CLINICAL_SIGN_OFF"]
rejected = [v for v in ledger.values() if v["status"] == "REJECTED_MISMATCH"]
assert len(ledger) == 40, f"Expected 40 ledger records, got {len(ledger)}"
assert len(approved) == 13, f"Expected 13 APPROVED, got {len(approved)}"
assert len(pending) == 27, f"Expected 27 PENDING, got {len(pending)}"
assert len(rejected) == 0, f"Expected 0 REJECTED, got {len(rejected)}"
print(f"  [PASS] data/approved_manifest.json: 13 APPROVED, 27 PENDING_CLINICAL_SIGN_OFF, 0 REJECTED_MISMATCH.")

# 4. Check 10-17_card1 specifically
target_10_17 = ROOT / "photos" / "oct17_do1.png"
assert target_10_17.exists()
h_10_17 = hashlib.sha256(target_10_17.read_bytes()).hexdigest()
assert h_10_17 == "247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6"
assert h_10_17 in ledger
assert ledger[h_10_17]["status"] == "APPROVED"
assert ledger[h_10_17]["day_id"] == "10-17"
assert ledger[h_10_17]["card_idx"] == 1
assert ledger[h_10_17]["spec_hash"] == "122c6a71707940d0b503e0d86e9774af8db33dddd619416bb20f4b501a5d42e1"
with Image.open(target_10_17) as img:
    assert img.format == "PNG"
    assert img.size == (1200, 900)
    assert img.mode == "RGB"
print("  [PASS] 10-17_card1 live asset matches candidate SHA-256 and is valid 1200x900 RGB PNG.")

# 5. Check all 40 spec hashes match current calendar dataset
health = json.loads((ROOT / "data" / "health_365.json").read_text(encoding="utf-8"))
days = {d["id"]: d for d in health}
for h, rec in ledger.items():
    card = days[rec["day_id"]]["cards"][rec["card_idx"] - 1]
    expected_spec = compute_card_spec_hash(card, rec["day_id"])
    assert rec["spec_hash"] == expected_spec, f"Spec hash mismatch for {rec['day_id']}_card{rec['card_idx']}"
print("  [PASS] All 40 active ledger records strictly match canonical card spec hashes.")

# 6. Check historical superseded archives
arch1 = json.loads((ROOT / "review" / "superseded" / "rejected_assets_pre_replacement_2026-10-16.json").read_text(encoding="utf-8"))
assert len(arch1["records"]) == 9
arch2 = json.loads((ROOT / "review" / "superseded" / "rejected_assets_10_17_card1_pre_replacement_2026-10-18.json").read_text(encoding="utf-8"))
assert len(arch2["record"]) == 1
print("  [PASS] Historical rejection records preserved across superseded archives (9 + 1 = 10).")

# 7. Check human decision files
dec1 = ROOT / "review" / "human_decisions" / "replacement_images_dr_atul_2026-10-16.json"
assert dec1.exists()
dec2 = ROOT / "review" / "human_decisions" / "replacement_image_10_17_card1_dr_atul_2026-10-18.json"
assert dec2.exists()
dec2_data = json.loads(dec2.read_text(encoding="utf-8"))
assert dec2_data["normalized_decision"] == "APPROVE_REPLACEMENT_AND_PROMOTE"
print("  [PASS] Human decision records verified.")

print("\nALL PROMOTION VERIFICATION CHECKS PASSED SUCCESSFULLY (10/10)!")
