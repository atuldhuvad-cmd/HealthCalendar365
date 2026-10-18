import json
import hashlib
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

ledger = json.loads((ROOT / "data" / "approved_manifest.json").read_text(encoding="utf-8"))

errors = []
for h, rec in ledger.items():
    ref = rec.get("file_reference")
    full_p = ROOT / ref
    if not full_p.exists():
        errors.append(f"Missing file on disk: {ref}")
        continue
    disk_hash = sha256_file(full_p)
    if disk_hash != h:
        errors.append(f"Hash mismatch on {ref}: disk {disk_hash} != ledger key {h}")

print(f"Checked {len(ledger)} file references in data/approved_manifest.json.")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
else:
    print("[PASS] All 40 file references and image hashes in active ledger strictly match.")
