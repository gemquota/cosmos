---
type: "concept"
title: "CSS Containment"
description: "Isolating element style, layout, and paint to speed rendering"
tags: ["css", "performance", "rendering", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Containment

## Summary

CSS containment (contain: layout style paint size) tells the browser that a subtree's layout, style, or painting does not affect the rest of the page, enabling cheaper rendering and scoped isolation. It is a surgical performance tool with real semantics.

## Details
- Mechanism: contain: layout isolates the element's layout from ancestors and siblings, so changes inside do not invalidate outside layout; contain: paint clips the subtree and isolates painting; contain: style scopes counters and quotes; contain: size makes the box size independent of content (requires explicit sizing); contain: strict/inline-size are shorthand bundles.
- Concrete example: a long comment thread with contain: layout paint per entry means editing one comment invalidates only that entry; content-visibility: auto — which applies contain: layout style paint plus a size reserve — lets the browser skip rendering off-screen entries until scrolled near.
- Failure modes: contain: size without a declared size collapses the box to zero, hiding content; layout containment can break position: sticky and fixed descendants by creating a containing block; over-application creates many layers/paint regions, raising memory; and mixing with subgrid or exotic layout features can produce clipped or misplaced content.
- Operational tradeoffs: containment buys measurable rendering wins on document-heavy UIs at the cost of semantic constraints — verify nothing escapes the containment boundary. It is a progressive enhancement: unsupported browsers just ignore it.
- RSIS3/mykb relevance: the wiki browser's note list uses content-visibility with reserved sizes so long search results render smoothly, and containment failures are covered by the dashboard's rendering pulses.
- Semantic isolation: containment changes how the element participates in layout (contain: layout creates a containing block); verify sticky/fixed descendants still behave before adopting it on a region.
- Size containment caution: contain: size without explicit dimensions collapses the box; use it only where the element's size is fully controlled, or pair it with a min-height.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/will-change|will-change CSS]]
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]]
- [[wiki/web-platforms/paint-triggers|Paint Triggers]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
