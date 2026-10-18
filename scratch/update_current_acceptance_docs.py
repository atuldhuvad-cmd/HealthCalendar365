#!/usr/bin/env python3
"""Write concise current acceptance documents from authoritative records."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


ledger = load("data/approved_manifest.json")
audit = load("review/approval_ledger_reconciliation_2026-10-18.json")
register = load("review/CLINICAL_GUJARATI_VISUAL_DECISION_REGISTER.json")
queue = load("review/candidate_generation_queue.json")
payload_path = ROOT / "review" / "candidate_payload_manifest.json"
payload_hash = hashlib.sha256(payload_path.read_bytes()).hexdigest()
payload = load("review/candidate_payload_manifest.json")

counts = {key: sum(r["status"] == key for r in ledger.values()) for key in
          ("APPROVED", "PENDING_CLINICAL_SIGN_OFF", "REJECTED_MISMATCH")}
assert counts == {"APPROVED": 13, "PENDING_CLINICAL_SIGN_OFF": 27, "REJECTED_MISMATCH": 0}
pending = register["categories"]["category_2_clinically_approved_other_gates_pending"]
assert len(pending) == 27

content_release = f"""# Content and Release Acceptance

**Date:** October 18, 2026
**Status:** **PRODUCTION HOLD ACTIVE**
**Active ledger:** `13 APPROVED`, `27 PENDING_CLINICAL_SIGN_OFF`, `0 REJECTED_MISMATCH`
**Recorded external provider spend:** **USD 0.00**

All 40 spotlight-card clinical copies have Dr. Atul's approval. Ten replacement images have been approved and promoted, including `10-17_card1`; three existing images were approved with their scoped revised copy. The remaining 27 records retain clinical approval but are not release eligible because the original 31-card decision explicitly excluded visual/accessibility, Gujarati linguistic, provenance, asset-promotion and release authorization.

## Closed gates

- Image replacement queue: **0 pending**.
- Active image/spec hash mismatches: **0**.
- Scoped clinical reapprovals: **0 pending**.
- Active rejected mismatches: **0**; historical evidence remains under `review/superseded/`.
- External image API calls for the `10-17_card1` replacement: **0**.

## Open gates

- Complete visual/accessibility, Gujarati-language and provenance decisions for the 27 ledger-pending records.
- Complete all ten physical Android/PWA/WhatsApp checks in `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`.
- Record final release authorization after all remaining gates pass.

## Pending slots

{chr(10).join(f'- `{slot}`' for slot in pending)}

No commit, push, deployment or publication is authorized by this document.
"""

final_packet = f"""# Final Acceptance Packet

**Candidate date:** October 18, 2026
**Production hold:** **STRICTLY ACTIVE**
**Payload manifest SHA-256:** `{payload_hash}`
**Payload files:** `{payload['total_files']}`
**Recorded external provider spend:** **USD 0.00**

## Current result

- Active ledger: **13 APPROVED / 27 PENDING / 0 REJECTED**.
- Clinical copy: **40/40 approved**.
- Replacement images: **10 promoted and approved**.
- Existing scoped cards approved after revision: **3**.
- Replacement queue: **empty**.
- `10-17_card1`: approved replacement image hash `247e56b88b76fc31e0ac6ac68bdbdcc9a84f695973ac8b04ceb5e28be0caedf6`.
- Service-worker cache: `health-poster-v1.5`.

## Evidence boundary

The 27 pending tokens do not mean their clinical copy lacks approval. They remain blocked from release because the bulk clinical decision excluded the other human gates required by `review/RELEASE_GOVERNANCE.md`. They must not be converted to `APPROVED` without additional explicit decisions.

## Remaining acceptance

1. Review the 27 pending cards for visual/accessibility, Gujarati-language and provenance acceptance.
2. Run the ten physical-device checks on genuine Android hardware.
3. Reconcile results and obtain explicit final release authorization.

Automated browser evidence cannot substitute for physical-device, WhatsApp-compression or human-language review. No commit, push or deployment has been performed by this phase.
"""

missing = f"""# Missing Evidence Register

**Date:** October 18, 2026
**Production hold:** **ACTIVE**
**Ledger:** `13 APPROVED`, `27 PENDING_CLINICAL_SIGN_OFF`, `0 REJECTED_MISMATCH`

## Outstanding evidence

- **27 cards:** clinical approval is recorded; visual/accessibility, Gujarati-language and provenance/release decisions remain unrecorded.
- **10 physical-device gates:** all remain **NOT TESTED** on genuine Android hardware.
- **Final release authorization:** not supplied.

## Closed evidence gaps

- Four revised clinical-copy scopes are approved.
- The dual-steering-wheel image was replaced, reviewed, approved and promoted.
- The replacement candidate queue is empty.
- Active image and specification hash mismatches are zero.

## Pending slots

{chr(10).join(f'- `{slot}`' for slot in pending)}

The historical counts `0 APPROVED / 31 PENDING / 9 REJECTED` describe the pre-remediation snapshot and are not the current ledger state.
"""

(ROOT / "review" / "CONTENT_RELEASE_ACCEPTANCE.md").write_text(content_release, encoding="utf-8")
(ROOT / "review" / "FINAL_ACCEPTANCE_PACKET.md").write_text(final_packet, encoding="utf-8")
(ROOT / "review" / "MISSING_EVIDENCE_REGISTER.md").write_text(missing, encoding="utf-8")

for rel in ("review/FREEZE_CHAIN_OF_CUSTODY.md", "review/FULL_CALENDAR_AUDIT_REPORT.md", "review/RUNTIME_OFFLINE_PWA_TEST_REPORT.md"):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    marker = "> **CURRENT-STATE NOTICE (2026-10-18):**"
    if marker not in text:
        lines = text.splitlines()
        lines.insert(2, "")
        lines.insert(3, marker + " This document contains historical checkpoint counts. The authoritative current state is `13 APPROVED / 27 PENDING / 0 REJECTED`; all 40 clinical copies are approved, while 27 records retain other human gates. See `review/approval_ledger_reconciliation_2026-10-18.json`.")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("[PASS] Updated current acceptance and missing-evidence documents")
