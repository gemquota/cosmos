---
type: "concept"
title: "Priority Hints"
description: "The fetchpriority attribute steering resource loading order"
tags: ["performance", "loading", "html", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Priority Hints

## Summary

Priority Hints (fetchpriority) let developers nudge resource fetch priority — high for the LCP image, low for below-the-fold media — giving the browser better scheduling signal than default heuristics.

## Details
- Mechanism: fetchpriority="high|low|auto" on <img>, <link>, <script>, <iframe>, and fetch() requests adjusts the resource's priority relative to same-class resources; the browser still decides the final schedule, so hints are advisory, not commands.
- Concrete example: a page with many images marks the hero fetchpriority="high" and the rest low/auto, so the LCP image's request wins the connection over decorative shots; a lazy third-party script gets fetchpriority="low" so it never delays first paint.
- Failure modes: marking everything high (the browser flattens it); high-priority hints stealing bandwidth from the document's own HTML/CSS; priority hints that contradict preload ordering; and ignoring that different browsers implement hint strength differently — Safari historically ignored fetchpriority.
- Operational tradeoffs: hints are cheap and mostly harmless when accurate; they matter most in contention-heavy pages (many images, ads, trackers). Combine with preload for the LCP asset and verify via DevTools priority columns; re-check after layout changes that move the LCP element.
- RSIS3/mykb relevance: the dashboard marks its chart data fetch high and analytics low, a policy documented here so generated pages inherit the same defaults.
- Contention: hints matter most when requests compete; on simple pages default heuristics already do well, so apply hints only where the waterfall shows mis-scheduling.
- Fallback: browsers without fetchpriority support simply ignore it, so hints are safe to ship as progressive enhancements — but verify the page still performs without them.
- Verification: confirm in the DevTools priority column that the hint changed the actual request priority; a hint with no visible effect is cargo-culting the LCP budget.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/speculative-loading|Speculative Loading]]
- [[wiki/web-platforms/link-rel-attributes|Link rel Attributes]]
- [[wiki/web-platforms/render-blocking|Render Blocking]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
