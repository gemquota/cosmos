---
type: "entity"
title: "DoubleSide"
description: "Rendering or processing both sides of a surface or data structure"
tags: ["entity", "rendering", "materials", "graphics", "states"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# DoubleSide

## Summary

DoubleSide describes geometry or materials rendered on both faces — front and back — rather than culling the side facing away from the camera. In graphics, double-sided rendering matters for open surfaces like leaves or paper where both sides are visible. The term also appears generically for anything with two observable faces or states.

## Details

- **Definition** — Back-face culling skips polygons whose winding order faces away; disabling it renders both sides of a surface.
- **Why culling exists** — Culling halves rasterization work on closed solids, which only need the front faces; it is a performance optimization with a correctness cost.
- **When double-sided is needed** — Thin, open, or transparent surfaces — leaves, cloth, hair, cutouts — show their backs and need double-sided rendering.
- **Lighting nuance** — Back faces often need flipped normals, or lighting looks wrong even when both sides are drawn.
- **Worked example** — A paper sheet model disappears from behind until double-sided rendering is enabled, then the back face lights correctly with flipped normals.
- **Common failure modes** — Missing faces on open geometry, wrong winding order that culls the visible side, and double-sided rendering that costs performance on large meshes.
- **Practical relevance** — Understanding double-sidedness helps debug disappearing geometry and material glitches in 3D views and games.
- **Telemetry note** — The stub mis-tags DoubleSide to IDE; the rendering reading matches the graphics-heavy session context that recorded it.
- **Performance** — Rendering both sides doubles rasterization work on those surfaces; closed meshes should keep culling enabled for speed.
- **Normals** — Flipped or missing normals on back faces produce dark or noisy shading, so material setup usually accompanies the double-sided flag.
- **Worked example** — A fence mesh renders from both sides once double-sided is enabled and back-face normals are flipped; screenshots verify lighting on each side.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/perspectivemesh|PerspectiveMesh]] — mesh rendering context
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/draw-error|Draw Error]] — when faces vanish
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/mockcanvas|MockCanvas]] — testing draw paths
- [[wiki/web-platforms/canvas-2d|Canvas 2D]] — 2D drawing surface
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/bxgubd3|BxgUbd3]] — visualization rendering
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — client-side rendering
