# HealthCalendar365 — Production Hosting Evaluation & Strategy

**Date:** October 16, 2026  
**Document ID:** `EVAL-HOSTING-20261016`  
**Status:** PROPOSED & EVALUATED — ZERO EXTERNAL CHANGES EXECUTED  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Production Hold:** STRICTLY ACTIVE

---

## 1. Executive Summary

In accordance with Step 8 of the Release Standard, GitHub is maintained as the single source of truth. This document evaluates hosting options for the static Progressive Web App (PWA) HealthCalendar365: **GitHub Pages** vs. **Cloudflare Pages**.

### Key Evaluation Criteria:
1. Static PWA & Service Worker compatibility
2. HTTPS & Security Headers control
3. Immutable preview deployments for reviewer acceptance
4. CDN cache behavior & service worker update propagation
5. Instant rollback capability
6. Traceability to Git commit SHA
7. Financial cost (Strictly USD 0.00)
8. Operational simplicity

---

## 2. Comparative Evaluation Matrix

| Criterion | GitHub Pages | Cloudflare Pages | Comparative Finding |
| :--- | :--- | :--- | :--- |
| **Static PWA & Offline Support** | Native static file serving. Supports `manifest.json`, `sw.js`, WOFF2 fonts. | Native static file serving. Supports `manifest.json`, `sw.js`, WOFF2 fonts. | **TIED** — Both platforms fully support offline-first PWAs. |
| **URL Root & Pathing** | Typically serves from subdirectory: `https://<org>.github.io/<repo>/` unless custom domain configured. | Serves from apex root of subdomain: `https://<project>.pages.dev`. | **CLOUDFLARE ADVANTAGE** — Subdomain root avoids subdirectory pathing issues with Service Worker scopes. |
| **Automatic HTTPS** | Automatic Let's Encrypt certificate. Enforces HTTPS. | Automatic Universal SSL / Cloudflare Edge SSL. Enforces HTTPS. | **TIED** — Both enforce HTTPS required for Service Worker registration. |
| **Custom HTTP Headers (`_headers`)** | Not natively supported without complex Jekyll plugins. Default MIME types applied. | Native `_headers` file support. Allows precise `Cache-Control`, `X-Content-Type-Options: nosniff`, and CSP. | **CLOUDFLARE ADVANTAGE** — Essential for ensuring `sw.js` is served with `Cache-Control: max-age=0, no-cache`. |
| **Preview Deployments** | Single live deployment per repository. No native preview URLs for pull requests. | **Automatic immutable preview URLs** for every non-main branch or pull request. | **MAJOR CLOUDFLARE ADVANTAGE** — Medical reviewers can inspect exact release candidates on physical devices prior to production merge. |
| **CDN Cache Invalidation** | ~10-minute default caching; can experience edge propagation delay during quick updates. | **Instant global cache purge** upon deployment completion. | **CLOUDFLARE ADVANTAGE** — Eliminates stale PWA assets during emergency release updates. |
| **Rollback Mechanism** | Requires pushing a Git revert commit (`git revert`) to trigger a new deployment. | **Instant 1-Click Rollback** in dashboard to any previous immutable deployment ID. | **CLOUDFLARE ADVANTAGE** — Near-instant recovery from unexpected clinical or rendering defects. |
| **Deployment Traceability** | Traced to GitHub Actions workflow run and commit SHA. | Traced to GitHub commit SHA, author, branch, and immutable build ID. | **TIED** — Both provide complete Git traceability. |
| **Hosting Cost** | Free tier included with public GitHub repositories. | Free tier includes unlimited bandwidth, 500 builds/month, unlimited preview environments. | **TIED (USD 0.00)** — Zero cost on both platforms. |
| **Operational Simplicity** | Zero external accounts needed; managed entirely within GitHub repository settings. | Requires connecting repository to a Cloudflare account via GitHub OAuth. | **GITHUB ADVANTAGE** — GitHub Pages requires zero third-party accounts. |

---

## 3. Technical Recommendation

### Primary Recommendation: **Cloudflare Pages**
Cloudflare Pages is the technically superior platform for HealthCalendar365 because:
1. **Immutable Preview URLs:** Enables clinical and Gujarati reviewers to test exact release candidate builds on physical Android devices via real URLs (e.g., `https://rc-v1-0-0.healthcalendar365.pages.dev`) *before* touching production.
2. **Instant 1-Click Rollback:** Critical for clinical governance; an emergency rollback can be executed in $<5$ seconds from the dashboard without waiting for Git revert commits and CI builds.
3. **Explicit Header Control:** A `_headers` file ensures `sw.js` and `data/health_365.json` are served with `Cache-Control: no-cache, no-store, must-revalidate`, preventing stale service-worker traps.

### Secondary Fallback: **GitHub Pages**
GitHub Pages remains an immediate, zero-configuration fallback if third-party account creation is undesired:
- Requires only enabling GitHub Pages in `https://github.com/atuldhuvad-cmd/HealthCalendar365/settings/pages` on branch `main` / root `/`.

---

## 4. Staged Cloudflare Headers Configuration (`_headers`)

To prepare for future deployment without mutating existing code, the recommended `_headers` configuration has been drafted:

```http
# Ensure Service Worker and Manifest are never stale in browser cache
/sw.js
  Cache-Control: max-age=0, no-cache, no-store, must-revalidate
  Service-Worker-Allowed: /

/manifest.json
  Cache-Control: max-age=0, no-cache, must-revalidate
  Content-Type: application/manifest+json

# Aggressive immutable caching for static fonts and active photos
/fonts/*
  Cache-Control: public, max-age=31536000, immutable

/photos/*
  Cache-Control: public, max-age=86400, stale-while-revalidate=604800

# Security Headers for all requests
/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
```

---

## 5. Deployment Authorization Gate

In accordance with Step 8 acceptance criteria:
- **DNS / Hosting Status:** Zero DNS records created; zero external hosting services configured.
- **Production Hold:** Strictly ACTIVE.
- **Deployment Requirement:** Production deployment requires explicit human authorization naming the exact reviewed commit SHA and target host.
