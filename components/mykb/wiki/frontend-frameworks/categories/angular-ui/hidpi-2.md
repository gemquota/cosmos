---
type: "entity"
title: "HiDPI"
description: "HiDPI: rendering crisply on high-density and retina displays"
tags: ["android", "angular", "api", "ast", "aws", "bash", "bootstrap", "bug", "bun", "cli", "cloud", "css", "dom", "entity", "display"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# HiDPI

## Summary

HiDPI is the angular-ui entity for high-density displays: screens whose device pixel ratio exceeds one, requiring crisp rendering at native resolution. Canvas, images, and layout must account for the ratio or they appear blurry. It matters because most modern devices are HiDPI. HiDPI correctness is a baseline expectation; blurriness reads as broken regardless of logic.

## Details

- **Definition** — HiDPI displays pack multiple physical pixels per CSS pixel; the device pixel ratio (DPR) quantifies the scaling.
- **Canvas sharpness** — Canvas bitmaps must be sized in physical pixels and scaled down by the DPR or they render blurry.
- **Image assets** — Responsive images serve higher-resolution sources to dense screens, balancing clarity against bandwidth.
- **CSS units** — Most CSS stays in logical pixels; sharpness is preserved because the browser scales the composited page.
- **Performance cost** — Rendering at high DPR multiplies pixel work; offscreen and lower-DPR fallbacks manage the cost.
- **Worked example** — A canvas element multiplies its width and height by the DPR and scales its style size back, producing crisp lines.
- **Failure modes** — Ignoring DPR changes, scaling text bitmaps, and burning GPU on needless resolutions are the classic mistakes.
- **Practical relevance** — HiDPI handling is a baseline expectation; blurry rendering reads as broken even when logic is correct.
- **Dynamic changes** — Moving windows between screens with different DPRs requires re-measuring and redrawing.
- **Image selection** — Serving the right resolution per DPR balances quality against bandwidth.
- **Testing** — DPR emulation in browser tooling verifies crispness without physical devices.
- **Memory** — High-resolution buffers cost memory; releasing them when off-screen keeps long sessions stable.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dpi|DPI]] — density measurement sibling
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/canvaspool-2|CanvasPool]] — canvas resource management
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — GPU rendering at high DPR
- [[wiki/frontend-frameworks/categories/angular-ui/00-index|Angular UI Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dimensions|Dimensions]] — pixel sizing
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/canvas-non|Canvas Non]] — rendering at high DPR
