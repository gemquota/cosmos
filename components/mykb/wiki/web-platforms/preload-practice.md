---
type: "concept"
title: "Preload Practice"
description: "Fetching critical resources early with link rel=preload"
tags: ["performance", "loading", "html", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Preload Practice

## Summary

Preload fetches a same-navigation resource early at high priority so it is ready when the parser needs it. It is for critical, late-discovered assets — fonts, hero images, module scripts — not a general speed knob.

## Details
- Mechanism: <link rel="preload" href="..." as="..."> tells the browser to start the fetch before the parser encounters the resource; as= must match the resource type (font, image, script, style, fetch) and crossorigin must mirror the eventual request or the preload is wasted.
- Concrete example: a self-hosted font referenced only from CSS gets preloaded as="font" crossorigin="anonymous" so text paints with it sooner; the LCP hero image gets preloaded with fetchpriority="high"; an ES module graph uses rel="modulepreload" so dependencies resolve without waterfall.
- Failure modes: preloading resources never used (wasted bandwidth and a console warning); preloads competing with the document's critical CSS at high priority; mismatched as=/crossorigin invalidating the hint; and preloading everything, which defeats the scheduler — preload is a scalpel, not a hammer.
- Operational tradeoffs: preload trades early bandwidth for later latency; use it only for the few resources whose discovery delay actually blocks LCP or first render, and verify each preload appears in the network waterfall at the intended priority.
- RSIS3/mykb relevance: the dashboard preloads its font and chart library chunk; the preload manifest is audited in loop reviews so it stays at a fixed, verified size.
- Cache correctness: preloaded responses are stored in the HTTP cache; a preload with wrong headers can poison a later same-URL fetch, so verify Cache-Control on preloaded assets.
- Priority audit: in DevTools, each preload should appear at high priority and complete before its consumer; a preload that finishes after use is a hint misapplied.
- Priority discipline: preload only the few assets that block first render or LCP; every additional preload competes with the document for bandwidth and can make startup slower.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/prefetch-practice|Prefetch Practice]]
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]]
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
