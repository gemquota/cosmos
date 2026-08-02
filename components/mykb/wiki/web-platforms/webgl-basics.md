---
type: "concept"
title: "WebGL Basics"
description: "OpenGL ES in the browser: shaders, buffers, and the rendering pipeline for 2D/3D graphics"
tags: ["webgl", "graphics", "gpu", "shaders", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API", "https://www.khronos.org/webgl/"]
---
# WebGL Basics

## Summary
WebGL exposes OpenGL ES to JavaScript, letting pages render accelerated 2D and 3D graphics. Programs run on the GPU as vertex and fragment shaders; the CPU uploads buffers and issues draw calls. WebGL2 is broadly supported, and WebGPU is its successor.

## Details
- **Pipeline** — vertex shaders transform geometry; fragment shaders color pixels; state (blending, depth, culling) configures rasterization.
- **Buffers and programs** — attribute buffers feed vertices; uniform and texture data feeds shaders; a program is a linked shader pair.
- **Performance** — batch draw calls, minimize state changes, and use instancing and vertex buffer objects; GPU memory is finite.
- **Frameworks** — Three.js and Babylon.js abstract the API; raw WebGL suits small, custom renderers.
- **Worked example** — a 3D knowledge graph view of the mykb wiki renders nodes as instanced cubes with a single draw call per frame.
- **Relevance** — RSIS3's visualization work should weigh WebGL/WebGPU against SVG and Canvas per use case.

## Related
- [[wiki/web-platforms/will-change|will-change CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]] — adjacent concept in this wiki
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
