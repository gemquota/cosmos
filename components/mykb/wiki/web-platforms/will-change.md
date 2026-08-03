---
type: "concept"
title: "will-change CSS"
description: "Hinting upcoming composited changes to the browser"
tags: ["css", "performance", "compositing", "animation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# will-change CSS

## Summary

will-change is a hint that an element's properties will animate, letting the browser promote layers and optimize in advance. It is a promise to the browser — breaking the promise wastes memory and rasterization, so it must be scoped to the animation.

## Details
- Mechanism: will-change: transform, opacity (or specific properties) tells the browser to prepare: typically promoting the element to its own compositor layer so the animation does not rebuild layers per frame. The browser may also pre-rasterize or apply other optimizations; the property itself is the hint, not the cause of performance.
- Concrete example: a card that will translate on scroll gets will-change: transform before the animation begins and it is removed after (via transitionend or a timeout); an off-canvas drawer uses will-change: transform while animating in. Applying it to 100 list items permanently multiplies layer memory.
- Failure modes: leaving will-change applied permanently (memory cost, and the promoted layer itself can hurt repaint); applying it to layout-affecting properties (top, width) which still relayout — the hint does not make them cheap; creating a stacking context and containing block, changing paint order and fixed positioning; and using it on elements that never animate.
- Operational tradeoffs: modern engines promote layers automatically when they detect animation, so will-change is often unnecessary; reserve it for elements whose animation would otherwise miss the compositor path, and pair with the same transform/opacity discipline. Measure layer count and memory in DevTools before and after.
- RSIS3/mykb relevance: the dashboard applies will-change only during panel transitions and removes it after, a rule this note enforces for loop-generated motion.
- Alternatives first: before adding will-change, try letting the browser promote automatically; only add it where the animation measurably misses the compositor path without it.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]]
- [[wiki/web-platforms/paint-triggers|Paint Triggers]]
- [[wiki/web-platforms/layout-triggers|Layout Triggers]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
