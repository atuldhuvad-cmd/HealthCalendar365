# Codex Handoff — HealthCalendar365

**Date:** October 18, 2026
**Project:** `D:\HealthCalendar365`
**Repository:** https://github.com/atuldhuvad-cmd/HealthCalendar365 (**public**)
**Production hold:** **ACTIVE**
**Recorded external provider spend:** **USD 0.00**

Supersedes `review/ANTIGRAVITY_HANDOFF_2026-10-18.md` (16:36). That document's state
figures are still correct for the ledger, but its build figures are stale: it records
service-worker cache `v1.5`, and the app shell changed after it was written.

---

## 1. Authoritative current state (verified, not inherited)

- Git: branch `main`, HEAD `02f2a0f`, **in sync with origin**, 4 commits, working tree
  has 4 uncommitted entries (all line-ending-only, `git diff -w` is empty on each).
- Approval ledger: **13 APPROVED / 27 PENDING_CLINICAL_SIGN_OFF / 0 REJECTED_MISMATCH**.
- Freeze checksums: 2/2 MATCH.
- Dataset: 368 posters, 1,472 cards. **1,432 cards (97.3%) still use 5 generic
  placeholders**; only the 10 spotlight posters (Oct 15–21) have dedicated photography.
- Service worker: `CACHE_NAME = 'health-poster-v1.6'`, 97 precached assets, ~40 MB.
- Physical-device gates: **all 10 still NOT TESTED**.
- Repo hygiene: no `.exe` tracked, no generated `build/` tracked, no blob > 5 MB.

### Clinical approval chain
All 40 spotlight card copies carry Dr. Atul's approval. It lives in
`review/human_decisions/clinical_dr_atul_2026-10-16.json` (verbatim: *"APPROVE for all 31
pending clinical cards only"*), plus the scoped re-approval, the nine-replacement
decision, and the `10-17_card1` replacement record.

**Do not read the 27 PENDING records as "copy not approved."** Their `PENDING_AUDIT`
gates are the *visual* gates. Copy approval is recorded separately, as above. Converting
any of the 27 to `APPROVED` requires a new explicit human decision covering
visual/accessibility, Gujarati-linguistic and provenance — never inference.

Binding integrity re-verified 2026-10-18: of the 31 cards Dr. Atul's bulk decision was
hash-bound to, **27 are byte-identical in both spec and image**. The 4 that drifted
(`10-15_card2`, `10-16-spine_card4`, `10-17_card1`, `10-18_card4`) are exactly those
recorded in `clinical_decision_transition_2026-10-16.json`, and all 4 are now APPROVED.
**Unaccounted drift: zero.**

---

## 2. What changed on 2026-10-18 (commit `a946801` onward)

**Poster rendering**
- Footer bar removed from both formats. `renderFooter()` is retained but not invoked;
  re-enable one call at `js/canvas-renderer.js:394` to restore it.
- Vertical only: card height 725 → 786; type enlarged (EN title 21→24, GU title 22→26,
  GU body 16→19, EN body 14→17; single-language title 24→29, body 17→21).
- Vertical card titles now wrap to 2 lines. Previously unwrapped — 3 EN and 3 GU titles
  overflowed the card edge at the shipped sizes.
- Description line budgets 3 → 5. Verified across all 40 spotlight cards:
  **0 truncated, 0 title overflow.** 24/26/19/17 is the measured ceiling (354px block
  against a 374px budget); one step larger overflows on `10-20_card4`.
- Square format untouched.

**WhatsApp share** — now sends the image only. The bilingual caption builder and the
`api.whatsapp.com/send?text=` fallback are gone.

**Preview / device-test workflow**
- `serve.py` gained `--host` / `--port` / `--root`. Default is unchanged (`127.0.0.1`,
  loopback only, verified from the LAN adapter).
- New `build_preview_runtime.py` builds a SHA-256-verified mirror of exactly the 97
  precached assets into `build/preview-runtime/`.

**Documentation**
- `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.md`: **5 gate criteria corrected** that
  contradicted the app and would each have produced a false FAIL (G-DEV-01 theme
  colours, G-DEV-03 cache versions, G-DEV-04 font family/weights, G-DEV-07 crop
  geometry, G-DEV-10 IndexedDB name). No gate status changed. Correction log in §4;
  pre-edit copy at `review/PHYSICAL_DEVICE_FINAL_CHECKLIST.pre_correction_2026-10-18.md.bak`.
- `review/ANDROID_NO_USB_TEST_INSTRUCTIONS.md` rewritten for the new workflow.
- `README.md` corrected and trimmed 154 → 112 lines.

**History rewrite** — `scratch/cloudflared-preview.exe` (52.8 MB) was committed, then
purged by rewriting `67a168f` into `a946801` and force-pushing. `*.exe` and `build/` are
now gitignored. The blob is unreachable but GitHub retains unreachable objects until GC;
contact GitHub Support if it must be fully erased.

---

## 3. Traps — read before touching anything

1. **Never hand-copy a preview folder.** A snapshot at `scratch/mobile-preview-runtime-20261018-1815/`
   drifted from source and shipped a stale build to a tester's phone, producing a defect
   that did not exist in the code. Always run `build_preview_runtime.py`.
2. **`build_precache_manifest.py` rewrites `sw.js` but does NOT bump `CACHE_NAME`.**
   Run it only while also raising the cache version by hand, or installed clients keep
   serving stale assets forever.
3. **`build_calendar_data.py` would clobber the dataset.** It still emits the abandoned
   `type: "dont"` model and legacy photo paths, and would erase the 3 split observances
   and invalidate every `spec_hash`. **Do not run it.**
4. **`split_multiple_observances.py` and `convert_data_to_messages.py` have no
   `if __name__ == "__main__"` guard** — importing either one mutates `health_365.json`.
5. **`wrapText()` truncates silently**, no ellipsis. Raising a font size without raising
   the line budget cuts health guidance mid-sentence.
6. **`js/app.js` canvas click rectangles duplicate the renderer's layout constants.**
   Change card geometry in `canvas-renderer.js` and you must update
   `handleCanvasClick()` or tap targets desync silently.
7. **Service worker is cache-first with no update prompt.** A fix reaches an installed
   phone only after `CACHE_NAME` changes *and* two launches — the first installs the new
   worker in the background while the loaded page still runs old code.
8. **Serve `build/preview-runtime`, never the repo root** over `--host 0.0.0.0`. The root
   exposes `review/`, `.git` and transaction data to the LAN.
9. **Origin stability.** A PWA binds its service worker, Cache Storage and IndexedDB to
   `(scheme, host, port)`. Changing IP or port voids G-DEV-02, G-DEV-03 and G-DEV-10
   evidence. `trycloudflare` quick tunnels mint a new hostname every restart and are
   unsuitable for the gate campaign.

---

## 4. Open defects (none fixed)

**False-success reporting — treat as one class, three symptoms:**
- `db.js savePhoto()` returns `false` on quota exhaustion; `app.js` ignores it and toasts
  "Custom photo applied to Card #N!" regardless.
- `batchDownloadOctWeek()` catches per-day failures, skips the day, then unconditionally
  toasts "🎉 All 7 Days (Oct 15–21) downloaded successfully!".
- The same function hardcodes 7 IDs, so `10-15-cane` (White Cane), `10-16-spine` (Spine)
  and `10-19-oral` (Oral Health) are **silently omitted** from the Oct 15–21 batch.

**Other, lower priority:** no upload size limit and no `FileReader.onerror`; `exportPoster`
and the preview share one canvas and the `isRendering` guard does not cover export;
`handleSearch` is bound to a non-existent `#searchDayInput`; unbounded `imageCache`;
`app_settings` IndexedDB store created but unused; viewport `user-scalable=no`
(WCAG 1.4.4); modals lack `role="dialog"`, focus trap and Esc; Doctor Branding UI is now
inert; `data/health_365.json` (1.73 MB) is precached but never fetched — it duplicates
`calendar-data.js`; card `type` field is vestigial (all 1,472 are `"message"`); 20 live
photos are still named `_do`/`_dont` and several now contradict their own filename.

---

## 5. Remaining work, in order

1. Run the **10 physical-device gates** on real Android hardware. They now have correct
   criteria and a working way to serve the app. Use
   `review/ANDROID_NO_USB_TEST_INSTRUCTIONS.md`. Record device model, Android version,
   Chrome version, time and screenshots. Keep the port fixed throughout.
2. Obtain Dr. Atul's decision on the **27 pending records** using
   `review/PENDING_27_DECISION_FORM_2026-10-18.md` (proposes ACCEPT 7 / REVISION_REQUIRED 20).
3. Fix the false-success defect class in §4.
4. Cloudflare Pages deployment — **requires the account owner**; connect the repo from the
   dashboard and add the `_headers` file drafted in `review/PRODUCTION_HOSTING_EVALUATION.md`
   so `sw.js` is served `no-cache`.
5. Record final release authorization once 1–4 are done.

**Superseded evidence:** `review/AUTOMATED_BROWSER_PWA_TEST_REPORT.md` and
`review/runtime_offline_pwa_test_results.json` describe the pre-footer-removal layout at
cache `v1.5`. They are historical snapshots, not evidence for the current build.

---

## 6. Boundaries

- Do not generate images or call paid APIs. Spend stays USD 0.00.
- Do not commit, push, deploy or publish without a new explicit instruction.
- Treat audits as read-only; do not implement fixes unless asked.
- Preserve `review/superseded/`, `review/human_decisions/` and all transaction directories.
- Do not convert any of the 27 pending records without a recorded human decision.
- Report UNKNOWN or BLOCKED rather than inferring a result. Do not present static analysis
  as a test result.
