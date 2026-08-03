---
type: "concept"
title: "Paint Triggers"
description: "Property changes that force repainting of pixels"
tags: ["performance", "rendering", "paint", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Paint Triggers

## Summary

Paint triggers are property changes that force the browser to re-raster pixels — color, background, box-shadow, text, border. They are cheaper than layout but still main-thread work; containing their scope is the path to smooth 60fps updates.

## Details
- Mechanism: changing color, background-color, border-color, box-shadow, or text properties invalidates paint for the element's layer; the browser redraws that layer and composites. Paint cost scales with the layer's pixel area, so large areas and blurred shadows are expensive per change.
- Concrete example: animating background-color on a full-screen element repaints the whole viewport each frame; fading it via opacity on a pre-rendered layer only composites. A box-shadow pulse on 50 cards each frame repaints 50 regions — worse than it looks in DevTools' paint-flash view.
- Failure modes: assuming paint is cheap (large layers, complex shadows, filters make it not); layout-trigger properties (they repaint anyway) masking the paint cost; paint invalidation cascading to ancestor layers with overlap; and using will-change: paint on everything, exploding memory and creating layers that must be updated anyway.
- Operational tradeoffs: minimize per-frame paint by pre-rendering static layers and animating transform/opacity; where color changes are required (theme switches, state changes), batch them into one style pass rather than per-frame. Profile with the paint-flash tool and the layer view, not intuition.
- RSIS3/mykb relevance: dashboard theme switches batch token changes into a single style recalculation, and paint-heavy embeds are flagged by the rendering telemetry reviewed in loop cycles.
- Layer audit: use DevTools' layer view to confirm promoted layers are few and purposeful; dozens of will-change-promoted layers cost more memory than the repaints they save.
- Cost containment: keep box-shadow and filter effects off animated regions, and prefer opacity-based glow; a blurred shadow repaints a large area per frame and quietly defeats the compositor path.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/layout-triggers|Layout Triggers]]
- [[wiki/web-platforms/content-visibility|content-visibility CSS]]
- [[wiki/web-platforms/contain-property|CSS Containment]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
