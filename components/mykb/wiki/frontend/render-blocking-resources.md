---
type: "concept"
title: "Render-Blocking Resources"
description: "Identifying and deferring blocking scripts and stylesheets"
tags: [performance", "render-blocking", "css", "javascript", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/render-blocking-resources", "https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work"]
---

# Render-Blocking Resources

## Summary
Render-blocking resources are files the browser must fetch and process before it can paint — synchronous scripts and stylesheets in the head, plus the HTML they parse. Every blocking resource stretches the critical rendering path. The fix is to identify them with audits, then defer, inline, or async-load what is not needed for first paint.

## Details
- Stylesheets: all <link rel="stylesheet"> in the head block rendering until fetched; media-attribute queries can narrow scope.
- Scripts: parser-blocking scripts halt HTML parsing; async ignores order and fires when ready, defer preserves order after parsing.
- Fonts: font-display: swap and preload limit text-invisible blocking from webfonts.
- Detection: Lighthouse flags blocking chains with their transfer size; DevTools network waterfall shows where parsing stalls.
- Strategy: inline critical CSS, defer non-critical scripts to after first paint, and avoid render-blocking analytics.
- Measure: verify with LCP and FCP before and after, since aggressive deferral can push interactivity later instead.

## Related
- [[wiki/frontend/critical-rendering-path|Critical Rendering Path]] — the pipeline these resources delay
- [[wiki/frontend/critical-css|Critical CSS]] — inlining the styles that block
- [[wiki/frontend/resource-hints|Resource Hints]] — prioritizing what must load early
- [[wiki/frontend/long-tasks|Long Tasks]] — parse and execution time after download
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — the metrics blocking hurts
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the umbrella
