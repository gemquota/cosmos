---
type: "entity"
title: "Canvas"
status: "growing"
---


## Canvas

HTML5 element for drawing 2D graphics via JavaScript. Used in the mykb graph viewer for rendering the force-directed knowledge graph canvas.

**Related technologies:** bash, cli, css, dom

**Domain:** OS & Shell › [[wiki/web-platforms/index|Shell Environment]] › [[wiki/web-platforms/index|Web Dev]] › Canvas

## Overview

Canvas is the HTML5 element for drawing 2D graphics programmatically via JavaScript, and in the Cosmos wiki it is the rendering surface behind the mykb graph viewer's force-directed knowledge graph. Instead of describing a picture in markup, canvas exposes a drawing context with methods for shapes, paths, text, images, and pixel manipulation; the code decides what appears on every frame.

The knowledge graph viewer uses canvas because graphs are dense and dynamic: nodes and edges move as forces settle, and redrawing the scene per animation frame is far cheaper in canvas than in the DOM. The typical loop clears the canvas, recomputes node positions from the physics simulation, draws edges and nodes, and repeats with requestAnimationFrame. Hit testing — mapping a click back to a node — is done in code because canvas has no DOM elements to attach handlers to.

## Key Properties

- Drawing model: immediate-mode rendering through a 2D context.
- Performance: thousands of shapes per frame are feasible with careful code.
- Interactivity: clicks and hovers must be translated to coordinates manually.
- Retina support: devicePixelRatio scaling keeps output sharp on high-DPI screens.

## Notes for the Corpus

This page anchors the canvas technique in the web-dev tree. When sessions extend the graph viewer — zooming, panning, node dragging, or rendering improvements — linking here records the surface they were changing. The distinction between canvas drawing and DOM-based visualization is the key design fact to preserve.

## Related Entities

- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/analysis-2|Analysis 2]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/budget|Budget]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/chemical-playground|Chemical Playground]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/context-2|Context 2]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/defi|Defi]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/diffusion-simulator|Diffusion Simulator]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/engine-telemetry-core|Engine Telemetry Core]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/fields|Fields]]
