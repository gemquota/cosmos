---
type: "concept"
title: "Critical CSS"
description: "Inlining above-the-fold styles to speed first paint"
tags: [performance", "css", "critical-path", "optimization", "first-paint"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/extract-critical-css", "https://web.dev/articles/critical-rendering-path"]
---

# Critical CSS

## Summary
Critical CSS inlines the styles needed for above-the-fold content directly into the HTML head, so first paint is not blocked by a full stylesheet download. The remaining styles load asynchronously and apply once the viewport content has rendered. It is one of the most reliable ways to improve LCP and First Contentful Paint.

## Details
- Extraction: build tools analyze the rendered HTML at viewport sizes and emit a minimal CSS subset — critical, everything else deferred.
- Inlining: a small <style> block in the head parses with the HTML; no extra request, no render blocking.
- Deferral: the full stylesheet loads with media="print" or a JavaScript swap, then activates after load.
- Trade-offs: hand-maintained critical CSS rots as components change, so automate extraction in the build pipeline.
- Cache note: inline CSS is not cacheable separately; keep it truly critical and move everything else to the cached file.
- Fit: marketing pages, dashboards, and anything where first paint defines perceived speed.

## Related
- [[wiki/frontend/critical-rendering-path|Critical Rendering Path]] — why inlining beats linking
- [[wiki/frontend/render-blocking-resources|Render-Blocking Resources]] — the problem critical CSS solves
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — LCP gains from earlier style application
- [[wiki/frontend/minification|Minification]] — shrinking the deferred stylesheet
- [[wiki/frontend/module-bundlers|Module Bundlers]] — where extraction plugins run
- [[wiki/frontend/performance-budgets|Performance Budgets]] — budgetting CSS weight
