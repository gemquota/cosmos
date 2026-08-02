---
type: "concept"
title: "CSS Positioning"
description: "Static, relative, absolute, fixed, and sticky containing-block rules"
tags: [css", "positioning", "layout", "z-index", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/position", "https://www.w3.org/TR/css-position-3/"]
---

# CSS Positioning

## Summary
The position property moves elements out of the default static flow. Relative shifts an element against its normal spot, absolute positions it against the nearest positioned ancestor, fixed against the viewport, and sticky blends relative with fixed behavior. The containing block rules determine what coordinates mean, which is where most positioning bugs live.

## Details
- Relative: keeps layout space and offsets visually with top, right, bottom, left; also establishes a containing block for children.
- Absolute: removes the element from flow and anchors it to the nearest ancestor with position not static; otherwise the initial containing block.
- Fixed: anchors to the viewport (or a transformed ancestor), useful for headers, tooltips, and modal backdrops.
- Sticky: behaves relative until a scroll threshold, then sticks; works only while its container is on screen.
- Z-index: positioned elements participate in stacking contexts; transform, filter, and opacity also create contexts.
- Practice: prefer flexbox and grid alignment over absolute hacks; reserve absolute for overlays and decorative layers.

## Related
- [[wiki/frontend/box-model|CSS Box Model]] — geometry positioning moves around
- [[wiki/frontend/flexbox|Flexbox]] — alignment alternative to offsets
- [[wiki/frontend/reflow-repaint|Reflow and Repaint]] — positioning changes trigger layout
- [[wiki/frontend/css-grid|CSS Grid]] — track-based placement vs coordinate offsets
- [[wiki/web-platforms/css-layout|CSS Layout]] — the positioning model in context
- [[wiki/frontend/floats|CSS Floats]] — the legacy flow-out mechanism
