---
type: "concept"
title: "OffscreenCanvas"
description: "Rendering canvas work on a worker thread away from the main thread"
tags: ["offscreencanvas", "canvas", "workers", "performance", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas", "https://html.spec.whatwg.org/multipage/canvas.html#the-offscreencanvas-interface"]
---
# OffscreenCanvas

## Summary
OffscreenCanvas moves 2D and WebGL rendering to a Web Worker, keeping heavy drawing off the main thread. Workers render into an OffscreenCanvas and transfer bitmaps back for display. It protects input responsiveness in games, dashboards, and image pipelines.

## Details
- **Transfer** — `canvas.transferControlToOffscreen()` hands a canvas to a worker; the worker renders and commits via `transferToImageBitmap`.
- **Contexts** — 2D and WebGL contexts work off the main thread; WebGL2 and WebGPU offscreen paths exist.
- **Communication** — message passing carries state; keep high-frequency updates to transferred bitmaps rather than data copies.
- **Benefits** — long renders no longer block input or paint; the main thread only composites.
- **Worked example** — the mykb pulse chart renders in an OffscreenCanvas worker, updating 60fps while the UI stays responsive.
- **Relevance** — RSIS3's live telemetry UIs should offload continuous rendering the same way.
- **Bitmap transfer** — transferToImageBitmap hands ownership to the main thread; transferring instead of copying keeps the worker's render loop at frame rate even with large canvases.

## Related
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]] — adjacent concept in this wiki
- [[wiki/web-platforms/retina-displays|Retina Displays]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
