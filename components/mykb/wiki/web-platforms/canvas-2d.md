---
type: "concept"
title: "Canvas 2D API"
description: "Immediate-mode 2D drawing: paths, text, images, and pixel access on a bitmap surface"
tags: ["canvas", "graphics", "2d", "web", "rendering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API", "https://html.spec.whatwg.org/multipage/canvas.html"]
---
# Canvas 2D API

## Summary
The Canvas 2D API draws shapes, text, images, and filters onto a bitmap surface in immediate mode. It is ideal for charts, games, image editing, and pixel manipulation, and it scales from simple diagrams to full 2D engines. Rendering happens on the main thread unless offloaded to an OffscreenCanvas.

## Details
- **Context** — `getContext('2d')` returns a drawing context; state like fill, stroke, and transforms persists between calls.
- **Immediate mode** — the canvas holds pixels, not objects; redraw on change, and structure scenes in layers for partial updates.
- **Performance** — batch paths, avoid shadow blur and filter churn, cap DPR scaling, and reuse offscreen canvases for sprites.
- **Pixels** — `getImageData`/`putImageData` enable filters and analysis; `toDataURL`/`toBlob` export.
- **Worked example** — the mykb pulse timeline draws bars and sparklines on canvas, redrawing only the changed region per update.
- **Relevance** — agent-generated charts should pick canvas vs SVG vs WebGL by update frequency and element count.

## Related
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]] — adjacent concept in this wiki
- [[wiki/web-platforms/inline-svg|Inline SVG]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]] — adjacent concept in this wiki
- [[wiki/web-platforms/retina-displays|Retina Displays]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
