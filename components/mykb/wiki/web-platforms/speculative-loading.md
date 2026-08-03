---
type: "concept"
title: "Speculative Loading"
description: "Preload, prefetch, and prerender heuristics for likely navigation"
tags: ["performance", "loading", "browsers", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Speculative Loading

## Summary

Speculative loading covers every hint that fetches or renders before need — preload, prefetch, preconnect, prerender, and the Speculation Rules API. Used deliberately it removes network stalls from the critical path; used casually it wastes bytes.

## Details
- Mechanism: hints trade idle resources for latency: preload (same-navigation, high priority), prefetch (future navigation, idle), preconnect (early handshakes), prerender (future page fully rendered in background), and Speculation Rules (prerender/prefetch triggered by hover, viewport, or heuristics). Browsers schedule these within their own priority systems.
- Concrete example: a search results page adds Speculation Rules to prerender the top result's URL on hover, so the next navigation paints instantly; the same page prefetches the next-page API payload and preconnects to the media CDN. On mobile, over-speculation drains data — gate behind connection hints.
- Failure modes: speculating on URLs with side effects (logout, form submissions); prerendering authenticated pages that leak session data into the cache; resource competition where speculative fetches starve the current page's LCP; and cache pollution from speculation that never resolves.
- Operational tradeoffs: start with preconnect and preload (cheap, well-understood), add prefetch where navigation data shows predictable paths, and reserve prerender for the top 1-2 destinations; measure data usage and render cost per added hint.
- RSIS3/mykb relevance: the wiki adds preconnect for its API and prerenders the most-visited synthesis from Speculation Rules, with data-usage telemetry reviewed by the loop.
- Monitoring: expose speculative fetch count and bytes in RUM so each hint's cost is visible; a hint that never converts is a candidate for removal.
- Same-site constraints: prerender is limited to same-origin (or same-site with opt-in) destinations; plan the URL allowlist accordingly and exclude state-changing endpoints.
- Budget control: cap speculative bytes per navigation and monitor the conversion rate; speculation that does not convert is a tax on mobile data and cache space.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/link-rel-attributes|Link rel Attributes]]
- [[wiki/web-platforms/render-blocking|Render Blocking]]
- [[wiki/web-platforms/preload-practice|Preload Practice]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
