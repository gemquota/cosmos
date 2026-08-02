---
type: "concept"
title: "Critical Rendering Path"
description: "How HTML, CSS, and JS become painted pixels"
tags: [rendering", "performance", "browser", "critical-path", "paint"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/critical-rendering-path", "https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work"]
---

# Critical Rendering Path

## Summary
The critical rendering path is the sequence of steps a browser performs to turn received bytes into painted pixels: parse HTML into the DOM, parse CSS into the CSSOM, combine them into the render tree, compute layout, and paint. First paint cannot happen until the HTML and the blocking CSS are processed, so the path determines initial-load performance.

## Details
- Pipeline: bytes → characters → tokens → nodes → object model, then style calculation, layout, paint, and compositing.
- DOM and CSSOM both block: the render tree needs both, so an empty stylesheet link delays first paint as much as markup.
- JavaScript interrupts: parser-blocking scripts halt HTML parsing, which is why async and defer exist.
- Optimization levers: inline critical CSS, defer non-critical stylesheets, preload key assets, and shrink initial HTML.
- Render tree: only visible elements survive; display:none subtrees and non-applicable styles are pruned.
- Relevance: LCP, FCP, and speed index all derive from how quickly the path completes for above-the-fold content.

## Related
- [[wiki/frontend/reflow-repaint|Reflow and Repaint]] — the layout and paint stages in detail
- [[wiki/frontend/render-blocking-resources|Render-Blocking Resources]] — what stalls the path
- [[wiki/frontend/critical-css|Critical CSS]] — inlining the styles that block first paint
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — metrics that measure the path
- [[wiki/web-platforms/browser-engines|Browser Engines]] — how rendering engines implement the path
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the umbrella discipline
