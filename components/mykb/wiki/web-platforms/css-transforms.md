---
type: "concept"
title: "CSS Transforms"
description: "translate, scale, and rotate operations on elements"
tags: ["css", "transforms", "animation", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Transforms

## Summary

CSS transforms (translate, rotate, scale, skew, matrix) move and reshape elements in 2D or 3D space without affecting layout. They are the primary tool for compositor-friendly motion and visual effects.

## Details
- Mechanism: transform applies a geometric change to the element's rendered box after layout, so transformed elements leave their original layout slot intact; transform-origin sets the pivot point. translate/rotate/scale are individual properties in modern CSS, each compositable independently.
- Concrete example: a hover pop: transform: scale(1.05) with a transition animates on the compositor; a flip card uses rotateY(180deg) with perspective on the parent; dragging feedback uses translate3d for a dedicated compositor layer.
- Failure modes: transforms create a containing block for fixed/absolute descendants, changing their positioning; 3D transforms and filters can force repaint or rasterization, losing the compositor benefit; percentage transforms resolve against the element's own box, surprising authors expecting parent-relative math; and transforms do not change hit-testing geometry as expected in some cases unless the transform is applied to the hit-test element.
- Operational tradeoffs: transforms are cheap to animate but should not be used for layout adjustments — the layout slot stays fixed, so moved elements can overlap neighbors; use them for motion and effects, and layout properties for structure. Overflow and clipping interact with transformed children (containing block semantics again).
- RSIS3/mykb relevance: the dashboard's chart tooltips and tab indicators animate with transforms only, keeping repaints off the critical path.
- Perspective: perspective on a parent and perspective-origin control 3D depth for rotateX/rotateY children; too little perspective looks flat, too much looks distorted, so tune with the element's size.
- Backface-visibility: hidden avoids mirror flashes when flipping cards, and transform-style: preserve-3d keeps children in shared 3D space.
- Hit testing: transforms change the rendered position but hit-testing follows the transformed box; verify click targets after scaling or rotating, especially on small touch targets.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/css-transitions|CSS Transitions]]
- [[wiki/web-platforms/css-animations|CSS Animations]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/component-architecture|Component Architecture]]
- [[wiki/web-platforms/web-apis|Web APIs]]
