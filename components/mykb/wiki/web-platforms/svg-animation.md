---
type: "concept"
title: "SVG Animation"
description: "Animating SVG with CSS, SMIL, and JavaScript APIs"
tags: ["svg", "animation", "css", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SVG Animation

## Summary

SVG animation moves vector graphics via SMIL, CSS, or the Web Animations API — animating paths, strokes, transforms, and filters with full resolution. Choosing the mechanism depends on control needs and browser support.

## Details
- Mechanism: SMIL (<animate>, <animateTransform>, <animateMotion>) is declarative and lives inside the SVG; CSS animations target SVG presentation properties (fill, stroke, transform, opacity) and are compositor-friendly when limited to transforms/opacity; the Web Animations API gives JS timeline control (play, pause, seek) over CSS/SMIL-like keyframes.
- Concrete example: a loading spinner animates stroke-dashoffset via CSS; a map marker path bobs with SMIL animateTransform; an icon's fill morphs on state change via CSS transitions; charts animate path d morphing with a library (flubber) or SMIL when simplicity matters.
- Failure modes: animating path d with CSS is unsupported in some engines (use SMIL or JS); transform-origin differs between HTML and SVG (SVG defaults to the viewport origin — set transform-box: fill-box); SMIL is deprecated-in-spirit in Chrome but still supported, causing lint noise; and heavy filter animations rasterize per frame, losing the compositor path.
- Operational tradeoffs: CSS animation is the best default for UI icons; SMIL is simplest for self-contained SVG files; Web Animations API for orchestration. Respect prefers-reduced-motion, keep animated area small, and test in the target engines since SVG animation support varies.
- RSIS3/mykb relevance: the OKF graph animates node transitions with CSS transforms; this note records which SVG animation mechanisms the loop may use in generated diagrams.
- Motion budget: keep animated SVG areas small and limited to transform/opacity where possible; filter and path animations rasterize per frame and blow the frame budget on complex shapes.
- Performance test: measure frame rate on low-end devices for filter and path animations; an animation that is smooth on the dev laptop may rasterize at 20fps on the fleet's entry-level hardware.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]]
- [[wiki/web-platforms/inline-svg|Inline SVG]]
- [[wiki/web-platforms/svg-animation|SVG Animation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
