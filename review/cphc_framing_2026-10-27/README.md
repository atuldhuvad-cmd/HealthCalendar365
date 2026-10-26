# Complete CPHC framing correction — published v1.27

Correction covering all 140 unique CPHC photographs, prompted by clipped faces on November 22 and November 23. The previous eleven-image correction was incomplete and is superseded by this inventory-wide review. Published on 27 October 2026 following the owner's explicit publication request. Production is now v1.27 at https://healthcalendar365.pages.dev/index.html.

The current CPHC framing map contains 123 full-scene/right-aligned entries, five top-focused close-ups, and twelve centered detail views. Full frames are used when heads and lower hands, equipment, or actions cannot fit in the same wide square crop. No source photograph was regenerated during this audit. The previously prepared nosebleed replacement remains included.

The square-card method, image-box dimensions, card heights, text sizes, wrapping, caption positions, footer behavior, and app click regions match the deployed renderer. All prior non-CPHC framing entries remain unchanged. The vertical-card method adds optional per-image badge corners used only by the new CPHC entries; its existing typography and geometry are preserved. User-uploaded photos keep their existing behavior.

## Evidence

All 140 source photographs and their corrected bilingual square/vertical photo regions were visually inspected across fourteen `comparison_*.jpg` sheets. Each row shows the source frame, the deployed square framing, the corrected square framing, and the corrected vertical framing. The prior square column compares framing on the same source bytes, including the already prepared nosebleed replacement; it is not an archived production screenshot. Subsequent close checks cover the five retained top crops and revised badge positions. Full-size photo regions are saved under `after/`; full poster previews for October 26, October 28, November 4, November 22, and November 23 are under `posters/` in both formats and all three languages.

The first comparison pass found that some top crops lost lower facial/action detail and some vertical badge corners crossed heads. Those cases were revised before the final output. Profiles and per-image reasoning are recorded in `profiles.json`.

PASS: 140 unique photos decode and render in both formats × three languages (840 card renders); no browser exceptions; source comparison limits renderer changes to CPHC profiles and optional vertical badge corners. See `verification.json`.

PASS: the isolated app-only v1.27 bundle loads all 365 dates, fits a 390×844 viewport, supports search, installs 264 offline cache entries, preserves settings across offline reload, matches all distinct cached runtime-file hashes, and renders every date in both formats and all three languages offline (2,190 renders), with no browser exceptions. See `offline_verification.json`.

PASS: the upload folder `build/cloudflare-pages-v1.27` contains 264 files whose SHA-256 hashes match the current source files.

Visual inspection validates source detail retention and badge placement at the reviewed framing; it does not make a new clinical-content approval or establish clinical-image accuracy. Existing header and square-text behavior is unchanged, including the long heading visible in the November 23 example. No claims, programme advice, date certainty, or calendar copy were changed. Physical-device updates and WhatsApp compression remain NOT TESTED.

## Reproduce

Run the local source preview on `http://127.0.0.1:8765/`, then `node scratch/verify_all_cphc_framing.cjs`. Generate comparison sheets with `scratch/make_cphc_framing_sheets.py`. The browser test writes visual-review status PENDING until its new outputs are inspected.

For the isolated full offline test, set `HEALTH_RELEASE=v1.27`, `HEALTH_ALL_MODES=1`, and `HEALTH_REPORT_PATH` to this folder's `offline_verification.json`, then run `node scratch/verify_pages_release.cjs`.

Publication was explicitly authorized by the owner and completed as production deployment `bed00e7d-84d4-4c8c-a7ea-37bdec876854` at https://bed00e7d.healthcalendar365.pages.dev. Only three of the 264 runtime files changed from v1.26: `js/canvas-renderer.js`, `photos/cphc_ent_care_oeee_card1.png`, and `sw.js`. No Git staging, commit, or push was performed.

PASS: production address loads the expected 365-date app; all cached runtime file hashes match the prepared v1.27 release; complete 264-entry cache installs; settings survive offline reload; all 2,190 date/format/language combinations render offline with no browser exceptions. See `published_verification.json`.

PASS: an isolated browser upgrade using the complete preserved v1.26 bundle and the published v1.27 bundle installs the new cache, removes the old cache, matches the updated renderer/photo hashes, preserves settings on offline restart, and renders eighteen affected-poster combinations offline. See `upgrade_verification.json`. A physical mobile upgrade remains NOT TESTED.

For installed phones, open the permanent address online, allow the update to finish, then close and reopen the app. The offline content set is approximately 124 MB, although unchanged assets may be reused by the browser. Keep existing app storage; clearing data or reinstalling is not required by this release.
