---
type: "concept"
title: "Browser Caching"
description: "Cache-Control, validators, and stale-while-revalidate patterns"
tags: [performance", "caching", "http", "browser", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching", "https://web.dev/articles/http-cache"]
---

# Browser Caching

## Summary
Browser caching stores responses locally so repeat visits skip network downloads. Cache-Control headers set freshness (max-age, s-maxage), revalidation rules (no-cache, must-revalidate), and stale-serving policies (stale-while-revalidate); ETag and Last-Modified validators confirm whether a cached copy is still current. Correct caching turns second visits into near-instant loads.

## Details
- Freshness: max-age defines seconds a response stays fresh; immutable plus a hashed URL means a file never needs revalidation.
- Revalidation: no-cache stores but always revalidates with the server; validators make that a cheap 304 response.
- stale-while-revalidate: serves stale content instantly while refreshing in the background — the pattern behind ISR-style UIs.
- Privacy: private for user-specific responses; no-store for sensitive data; public for shared cacheable assets.
- CDN layers: s-maxage controls shared caches above the browser, letting origin and client rules differ.
- Cache busting: hashed filenames (app.a1b2c3.js) make content updates instant while leaving old URLs cacheable.

## Related
- [[wiki/api-protocols/http-caching|HTTP Caching]] — the protocol-level model
- [[wiki/frontend/service-workers|Service Workers]] — programmatic caching beyond headers
- [[wiki/frontend/performance-budgets|Performance Budgets]] — what caching can and cannot fix
- [[wiki/frontend/resource-hints|Resource Hints]] — preloading what caching will miss
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — shared cache layers
- [[wiki/api-protocols/api-versioning|API Versioning]] — cache-safe URL design
