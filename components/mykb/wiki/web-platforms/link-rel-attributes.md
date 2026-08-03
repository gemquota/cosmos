---
type: "concept"
title: "Link rel Attributes"
description: "The rel values that control resource hints and relationships"
tags: ["html", "performance", "links", "loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Link rel Attributes

## Summary

Link rel attributes declare relationships and loading hints: preload, prefetch, preconnect, dns-prefetch, modulepreload, and the SEO/alternate family. Choosing the right one changes the browser's resource scheduling; choosing wrong wastes bandwidth.

## Details
- Mechanism: <link rel="preload" as="font"> starts fetching immediately for a resource needed this navigation; rel="preconnect" opens early connections; rel="prefetch" fetches for a likely future navigation at idle priority; rel="modulepreload" preloads ES modules with correct dependency handling. rel="canonical", "alternate", and "manifest" are metadata, not loading hints.
- Concrete example: the LCP hero image gets rel="preload" as="image" with fetchpriority="high"; the API origin gets preconnect; the next page's critical CSS gets prefetch. Applying preload to the wrong asset (e.g. a font used only below the fold) steals bandwidth from the LCP.
- Failure modes: preloading resources that never render (wasted bytes); prefetching too aggressively (bandwidth/cache pollution on mobile); omitting as= or crossorigin on fonts, breaking the request; and preload+prefetch confusion — they target different navigations and have different priorities.
- Operational tradeoffs: hints are best-effort; browsers ignore them when unhelpful, but honoring them costs network. Use preload for the few critical above-the-fold assets, preconnect for 2-3 origins, prefetch sparingly based on real navigation patterns, and verify with DevTools network priority columns.
- RSIS3/mykb relevance: the dashboard preloads the telemetry font and preconnects to the rack API; the wiki documents which assets each hint targets so the loop does not duplicate hints.
- Priority guidance: preload is high priority, prefetch low/idle — never use prefetch for the current navigation's critical assets.
- CSP interplay: preloaded resources still respect Content-Security-Policy; a mismatched policy can make a preload fail silently while the resource loads later anyway.
- Crossorigin discipline: fonts fetched via CSS require crossorigin="anonymous" on preload to match the eventual request; a missing crossorigin silently wastes the preload.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/render-blocking|Render Blocking]]
- [[wiki/web-platforms/preload-practice|Preload Practice]]
- [[wiki/web-platforms/prefetch-practice|Prefetch Practice]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
