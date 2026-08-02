---
type: "concept"
title: "Browser Rendering Pipeline"
description: "How browsers turn HTML, CSS, and JavaScript into pixels: parse, style, layout, paint, composite"
tags: ["browsers", "rendering", "performance", "css", "web-platforms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work", "https://web.dev/articles/rendering-performance"]
---
# Browser Rendering Pipeline

## Summary
Every page load runs through the same pipeline: fetch, parse into DOM and CSSOM, build the render tree, compute layout, paint, and composite. Understanding where work happens — and which properties trigger which stage — is the basis of all frontend performance work.

## Details
- **Parsing** — HTML becomes the DOM; CSS becomes the CSSOM; both block rendering, which is why render-blocking CSS matters.
- **Style and layout** — the render tree pairs DOM nodes with computed styles; layout (reflow) computes geometry in CSS pixels; it cascades through subtrees.
- **Paint and compositing** — paint fills pixels per layer; compositing stitches layers on the GPU. Transform and opacity can skip layout and paint entirely.
- **Long tasks** — scripts, style, layout, and paint share the main thread; long tasks block input and push INP up.
- **Worked example** — profiling the mykb dashboard shows the SPA's initial render is dominated by stylesheet parse and layout; trimming CSS and reserving image space cut CLS.
- **Relevance** — RSIS3's UI work should reason about frame budgets the same way the rendering pipeline does.

## Related
- [[wiki/web-platforms/content-visibility|content-visibility CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/contain-property|CSS Containment]] — adjacent concept in this wiki
- [[wiki/web-platforms/will-change|will-change CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
