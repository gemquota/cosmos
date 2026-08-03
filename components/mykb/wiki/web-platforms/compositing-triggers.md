---
type: "concept"
title: "Compositing Triggers"
description: "Operations that move work to the compositor thread"
tags: ["performance", "rendering", "compositing", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Compositing Triggers

## Summary


Compositing is the final browser stage where painted layers are merged. Animating only compositor-friendly properties — transform and opacity — keeps frames off the main thread and avoids repaint cost per frame.

## Details
- Mechanism: rendering pipeline runs style → layout → paint → composite; changes to layout or paint invalidate those stages, while transform/opacity changes only re-composite existing layers. The browser promotes elements to their own layers when they animate or when will-change/hints request it.
- Concrete example: a card hover animating transform: translateY(-4px) with opacity tweaks composites cheaply at 60fps, whereas animating top/left or width re-runs layout and paint each frame, janking on midrange devices.
- Property taxonomy: transform, opacity, and filter (partially) compose on their own layers; top, left, width, height, margin, and padding re-run layout; color, background, and box-shadow re-run paint; clip-path, backdrop-filter, and mix-blend-mode force repaint of the element and its neighbors.
- Failure modes: transform animations that also change layout properties lose the benefit (the layout pass still runs); a transform on an element with a filter, clip-path, or backdrop-filter forces repaint of the layer anyway; layer promotion has memory cost — hundreds of promoted layers can exceed GPU memory, especially on mobile.
- Operational tradeoffs: promoting layers speeds animation but raises memory and can cause blurry text on scaled layers; leave promotion to the browser unless profiling shows a bottleneck, and use will-change sparingly and only while animating.
- RSIS3/mykb relevance: the dashboard's chart.js animations and tab transitions are transform/opacity only, keeping interaction-to-next-paint low on the low-power devices the team tracks in rack telemetry.
- Will-change scoping: apply will-change only for the duration of animation and remove it after; permanent promotion multiplies layer memory and can hurt, not help, repaint cost.
- DevTools evidence: the rendering tab's paint-flash and layer view show whether a change composites or repaints; use them before optimizing.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/paint-triggers|Paint Triggers]]
- [[wiki/web-platforms/layout-triggers|Layout Triggers]]
- [[wiki/web-platforms/content-visibility|content-visibility CSS]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
