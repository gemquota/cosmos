---
type: "concept"
title: "Server-Side Rendering (SSR)"
description: "Generating HTML per request on the server and its latency tradeoffs"
tags: [rendering", "ssr", "javascript", "performance", "seo"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/rendering-on-the-web", "https://nextjs.org/docs/app/building-your-application/rendering"]
---

# Server-Side Rendering (SSR)

## Summary
Server-side rendering generates the complete HTML document on the server for each request, so the browser can paint meaningful content before any JavaScript executes. Search engines and users on slow devices benefit immediately. The cost is latency: every request depends on a server round trip, and slow data sources or cold starts push out Time to First Byte.

## Details
- Per-request cost: rendering, data fetching, and serialization happen on the server; response time is the sum of those steps.
- First-load wins: fully formed markup means LCP can beat client-side rendering even on slow connections.
- SEO is natural — no crawler JavaScript execution required — which is why commerce and content sites favor SSR.
- State transfer: the server serializes application state (often a JSON blob) so the client can hydrate without refetching.
- Scaling: rendered responses are cacheable at the CDN when personalized data is hoisted out of the page.
- Hybrid reality: most frameworks now mix SSR with client components, streaming, and static generation per route.

## Related
- [[wiki/frontend/client-side-rendering|Client-Side Rendering]] — the in-browser alternative
- [[wiki/frontend/hydration|Hydration]] — wiring events onto SSR HTML
- [[wiki/frontend/edge-rendering|Edge Rendering]] — moving rendering closer to users
- [[wiki/api-protocols/http-caching|HTTP Caching]] — making SSR responses cacheable
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — where TTFB fits in
- [[wiki/frontend/static-site-generation|Static Site Generation]] — pre-rendering instead of per-request work
