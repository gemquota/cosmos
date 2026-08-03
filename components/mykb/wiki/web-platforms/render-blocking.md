---
type: "concept"
title: "Render Blocking"
description: "Resources that delay first paint until fetched and parsed"
tags: ["performance", "css", "fonts", "loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Render Blocking

## Summary

Render-blocking resources — CSS in <head>, synchronous scripts, and fonts — delay first paint because the browser cannot render until it fetches and processes them. Managing the blocking set is the highest-leverage startup optimization.

## Details
- Mechanism: HTML parsing pauses for synchronous scripts; CSS blocks rendering because layout/paint need the stylesheet (the browser also blocks script execution on prior CSS); blocking resources add their fetch+parse time to the critical path before first contentful paint. async/defer scripts and media-query-scoped CSS (print styles) do not block.
- Concrete example: an analytics script in <head> without defer delays first paint on slow networks; moving it to defer or loading it after load() removes it from the critical path. A 200KB CSS file blocks everything; inlining critical CSS and deferring the rest (or splitting per-route) shrinks first paint dramatically.
- Failure modes: inline scripts placed before CSS still block; loading="lazy" on stylesheets is not a reliable escape; fonts are render-blocking only for text that uses them (font-display: swap avoids hiding); and service workers complicate caching but not the blocking model — a cache miss still blocks.
- Operational tradeoffs: inlining critical CSS trades HTML size for a paint win; code-splitting and preload shift blocking earlier rather than removing it; the goal is a short, correct critical path — measure with the Performance panel and Lighthouse's render-blocking audit.
- RSIS3/mykb relevance: the wiki browser inlines its critical CSS and defers non-critical scripts, a startup budget recorded here so the loop keeps new embeds out of the critical path.
- Measurement: profile the critical path in the Performance panel; the render-blocking audit lists exactly which resources delay first paint, turning optimization into a checklist instead of folklore.
- Script placement: load non-critical JS with defer at the end of body; parser-blocking scripts in head are the most common self-inflicted render delay.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/preload-practice|Preload Practice]]
- [[wiki/web-platforms/prefetch-practice|Prefetch Practice]]
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
