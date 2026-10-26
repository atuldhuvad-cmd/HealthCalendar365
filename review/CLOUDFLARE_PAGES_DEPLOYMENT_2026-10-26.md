# HealthCalendar365 Cloudflare Pages deployment

Published on 26 October 2026 following the owner's explicit request to use Cloudflare Pages and successful account authorization.

- Owner account: `atuldhuvad@gmail.com` (verified with Wrangler).
- Project: `healthcalendar365`; production branch: `main`; Direct Upload.
- Permanent app URL: https://healthcalendar365.pages.dev/index.html
- Deployment URL: https://13204207.healthcalendar365.pages.dev
- Deployment ID: `13204207-aabd-469f-90fc-1774c5ad1058`.
- Release: `health-poster-v1.26`; compatibility date: `2026-10-01`.
- Uploaded bundle: `build/cloudflare-pages-v1.26`, 264 files, 123,589,891 bytes; all file hashes match the current local runtime sources.
- Only precache runtime files plus `sw.js` were uploaded. Repository history, staging images, backups, scripts, local review reports, and credentials were excluded. The app's own Calendar Reference data remains included as required by its runtime.
- Git HEAD `5749793223302c6a290c998381c9dd866f0a7350` is provenance only: the deployed bundle includes the existing local uncommitted changes. No Git staging, commit, or push was performed.

## Verification

PASS: production URL returns HTTP 200; 365 runtime calendar dates; 390×844 layout fits; search works; complete v1.26 cache contains 264 entries; 263 distinct cached runtime file paths match the prepared release hashes (root and index.html share one file); saved settings survive offline reload; all 365 square bilingual posters and October 26 vertical English/Gujarati/bilingual posters render offline; zero browser exceptions.

Evidence: `cloudflare_prepared_verification_2026-10-26.json`, `cloudflare_published_verification_2026-10-26.json`, and `cloudflare_upload_manifest_2026-10-26.json`. Repeatable browser check: `node scratch/verify_pages_release.cjs https://healthcalendar365.pages.dev/index.html`.

NOT TESTED: physical mobile installation, WhatsApp sharing/compression, interrupted installation, or transfer of personal settings/photos from an older preview origin. The app still defaults to October 15 by source design; this deployment did not change startup-date behavior.

## Mobile installation

Open the permanent app URL in Android Chrome while online. Allow the approximately 124 MB offline download to finish, then use Chrome's Install app/Add to Home screen action. Verify the new installation offline before removing the old temporary-preview installation. Settings and uploaded photos are stored per address and do not transfer automatically.

For future releases, rebuild and verify a clean runtime bundle, update the service-worker cache version when runtime files change, and upload to this same Pages project. Deployment remains a separate explicit owner action.
