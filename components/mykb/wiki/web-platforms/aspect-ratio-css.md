---
type: "concept"
title: "aspect-ratio in CSS"
description: "The aspect-ratio property reserving element proportions"
tags: ["css", "layout", "media", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# aspect-ratio in CSS

## Summary

The CSS aspect-ratio property lets an element declare a preferred width/height ratio so the browser reserves space before content loads. It is the modern replacement for the padding-top hack and is essential for layout stability.

## Details
- Mechanism: aspect-ratio: 16 / 9 computes the block size from the inline size (or vice versa when height is definite), leaving the other axis auto. Content that does not fit is not clipped by default — the box grows — so pair it with overflow: hidden or object-fit only when clipping is intended.
- Concrete example: a video embed wrapper with aspect-ratio: 16 / 9 and width: 100% renders at the correct height before the iframe loads, eliminating the collapse-and-jump that previously needed a padding-top: 56.25% wrapper with absolutely positioned children.
- Interaction with intrinsic size: replaced elements like images already carry an intrinsic ratio, so aspect-ratio on them mainly matters when one dimension is stretched; for boxes with no intrinsic size it fully defines the ratio. When both width and height are set, aspect-ratio is ignored.
- Failure modes: combining aspect-ratio with min-height or max-height can produce surprising overflow because min/max constraints win; grid and flex stretching can fight the ratio since stretch sets the cross-size directly; and older browsers ignore the property, so fall back to the padding hack only where layout stability matters on legacy engines.
- Operational tradeoffs: reserving space improves CLS but can leave letterboxing when the real content has a different ratio; content-visibility and lazy-loaded media interact well because the reserved box gives the compositor a stable region.
- RSIS3/mykb relevance: the dashboard's embedded iframes and chart canvases use aspect-ratio wrappers so telemetry panels do not shift when rack data loads asynchronously.
- Content fit: decide whether overflow should clip or expand; aspect-ratio reserves the box but does not clip — pair with overflow: hidden or object-fit: cover where the visual requires it.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/logical-properties|CSS Logical Properties]]
- [[wiki/web-platforms/rtl-support|RTL Support]]
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
