---
type: "concept"
title: "Virtual Scrolling"
description: "Rendering only visible rows of large lists: windowing, recycling, and measurements"
tags: ["virtual-scrolling", "performance", "lists", "react", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://web.dev/learn/performance", "https://react-window.vercel.app/"]
---
# Virtual Scrolling

## Summary
Virtual scrolling renders only the rows near the viewport, recycling DOM nodes as the user scrolls. It makes thousands- or millions-row lists smooth by keeping the DOM small. Fixed-height rows are easy; variable heights need measurement and estimation.

## Details
- **Windowing** — a spacer holds total height; visible slice renders; scroll position maps to row indices.
- **Fixed vs variable** — fixed sizes allow exact math; variable sizes require estimation, measurement caches, and dynamic spacers.
- **Overscan** — render extra rows beyond the viewport to cover fast scrolls and async images.
- **Accessibility** — keep semantics sane: real scroll containers, and avoid hiding content from AT.
- **Worked example** — the mykb log viewer virtualizes tens of thousands of pulse entries with fixed-height rows and overscan.
- **Relevance** — agent-generated logs and long knowledge lists are exactly the case for virtualized rendering.
- **Measurement caching** — variable-height rows cache measured sizes keyed by item id, then spacer height equals sum of cached plus estimated rows; libraries like react-virtualized and @tanstack/react-virtual implement this.

## Related
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-snap|Scroll Snap]] — adjacent concept in this wiki
- [[wiki/web-platforms/sticky-position|position: sticky]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — existing coverage
