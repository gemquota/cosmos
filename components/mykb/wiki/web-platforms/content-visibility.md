---
type: "concept"
title: "content-visibility CSS"
description: "Skipping rendering of off-screen content to cut layout cost"
tags: ["css", "performance", "rendering", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# content-visibility CSS

## Summary

content-visibility: auto lets the browser skip rendering work for off-screen elements, reserving their space via contain-intrinsic-size. It is a rendering-level optimization for long pages and virtualized lists.

## Details
- Mechanism: content-visibility: auto applies layout, style, and paint containment and skips rendering the subtree until the user scrolls near it; contain-intrinsic-size: 300px tells the browser how much space to reserve so skipping does not collapse the page height.
- Concrete example: a wiki search result list of 2,000 notes renders only the ~20 visible entries; scroll jumps are avoided because each entry reserves contain-intrinsic-size equal to its measured average height.
- Failure modes: forgetting contain-intrinsic-size collapses off-screen content to zero height, breaking scrollbar and anchor navigation; content inside a skipped subtree cannot be found by find-in-page or measured by scripts until rendered; intersections, focus, and layout queries against hidden content behave as if absent; and heavy per-element containment can raise memory from layer/paint regions.
- Operational tradeoffs: the win is initial render and scroll responsiveness on document-heavy pages; the cost is subtler scripting semantics and the need to maintain good size estimates. Measure with real data — auto only skips when it can prove invisibility, and Chrome's default threshold may render more than expected.
- RSIS3/mykb relevance: the OKF graph and synthesis lists use content-visibility with measured sizes so browsing thousands of notes stays responsive on low-end hardware.
- Also consider: iframe and embed subtrees are skipped entirely when off-screen, which can delay third-party init; decide whether that is a win or a surprise for analytics embeds.
- Measuring: compare paint times with and without content-visibility on the real corpus before adopting it globally, since the skip threshold is implementation-defined.
- Find-in-page caveat: skipped subtrees are excluded from browser find and script measurements until rendered; decide whether that trade is acceptable per surface before applying content-visibility.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/contain-property|CSS Containment]]
- [[wiki/web-platforms/will-change|will-change CSS]]
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
