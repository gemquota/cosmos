---
type: "concept"
title: "Incremental Static Regeneration (ISR)"
description: "Revalidating static pages on demand after build"
tags: [ssg", "rendering", "caching", "nextjs", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration", "https://web.dev/articles/rendering-on-the-web"]
---

# Incremental Static Regeneration (ISR)

## Summary
Incremental static regeneration keeps the performance of static generation while allowing pages to refresh after the build. A page is generated once, served from cache, then regenerated in the background when a revalidation window expires or an on-demand trigger fires. Visitors always receive a cached page; the freshest version arrives on the next request.

## Details
- Time-based revalidation: a page with a revalidate period is rebuilt in the background after the window passes, so stale content is never served for long.
- On-demand invalidation: webhooks or CMS events can purge and rebuild specific paths immediately after an edit.
- Serving semantics: while regenerating, the CDN serves the previous HTML; this stale-while-revalidate behavior keeps availability high.
- Stampede control: only one regeneration runs per page at a time, avoiding a herd of concurrent rebuilds.
- Granularity: ISR works per route, letting teams freeze marketing pages while frequently refreshing product listings.
- Fit: content sites, docs, and catalogs where full SSG is too stale and full SSR is too slow.

## Related
- [[wiki/frontend/ssg|Static Site Generation]] — the baseline model ISR extends
- [[wiki/frontend/static-site-generation|Static Site Generation]] — the hub's fully static deployment
- [[wiki/api-protocols/http-caching|HTTP Caching]] — the cache semantics underneath
- [[wiki/frontend/browser-caching|Browser Caching]] — how clients store regenerated pages
- [[wiki/frontend/edge-rendering|Edge Rendering]] — an alternative for per-request freshness
- [[wiki/frontend/vercel|Vercel]] — ISR support on Vercel's network
