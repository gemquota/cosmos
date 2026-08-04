---
type: "entity"
title: "Canvas Non"
description: "Canvas Non: choosing DOM and SVG rendering over canvas"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "rendering"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# Canvas Non

## Summary

Canvas Non is the bootstrap-cluster entity for the decision of when not to use canvas: choosing DOM, SVG, or other rendering paths instead. Canvas excels at dense custom graphics but loses accessibility and text handling. It matters because the wrong rendering choice compounds cost for years. Rendering choice is a decision-type problem: the criteria determine the answer.

## Details

- **Definition** — Canvas Non captures the alternatives to canvas rendering and the criteria for choosing them.
- **Canvas strengths** — Canvas is fast for thousands of custom shapes and gives pixel-level control with no DOM overhead.
- **Canvas weaknesses** — It offers no built-in accessibility, text selection, or hit testing, all of which must be rebuilt.
- **DOM alternative** — The DOM provides accessibility, layout, and events for free, and is best when content is structured.
- **SVG alternative** — SVG keeps vector semantics and styling while scaling crisply, at a cost in dense-scene performance.
- **Hybrids** — Layered approaches combine canvas for dynamic regions with DOM for interactive controls.
- **Worked example** — A data table uses DOM rows for accessibility; only its heatmap background is drawn on a canvas layer.
- **Practical relevance** — Choosing the rendering substrate is a decision-type problem: name the criteria, then pick per context.
- **Cost model** — DOM scales poorly past thousands of elements; canvas scales poorly at rich text and accessibility.
- **Maintenance** — Framework-rendered DOM benefits from declarative updates; canvas needs manual diffing.
- **Progressive enhancement** — Starting with DOM or SVG and adding canvas layers only where needed keeps both simple.
- **Decision record** — Recording why a rendering path was chosen, and revisiting it when requirements change, prevents sunk-cost attachment.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/noderenderer|NodeRenderer]] — canvas-based node rendering
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — the GPU canvas alternative
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dimensions|Dimensions]] — sizing across render paths
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/canvaspool-2|CanvasPool]] — reusing canvas resources
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/physicsconfig|PhysicsConfig]] — rendering physics scenes
