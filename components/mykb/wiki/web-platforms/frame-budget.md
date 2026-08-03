---
type: "concept"
title: "Frame Budget"
description: "The 16ms per-frame time budget for smooth 60fps interfaces"
tags: ["performance", "rendering", "animation", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Frame Budget

## Summary

A frame budget is the time slice available for a frame of interactive work: 16.7ms at 60fps, less after the browser's own work. Scripts that respect the budget yield to the compositor, keeping scroll and input smooth.

## Details
- Mechanism: at 60Hz the browser has ~16.7ms per frame; rendering, style, layout, and paint consume part of it, leaving a script budget that shrinks to single-digit milliseconds on busy pages. Long tasks (>50ms) block input entirely, and the budget shrinks to ~8ms at 120Hz displays that still expect responsiveness.
- Concrete example: a scroll handler that reads layout and re-writes styles per event overruns the budget and janks; batching via rAF and throttling to one update per frame stays inside it. Chunking a 200ms data-processing task into 5ms slices between frames keeps the UI responsive.
- Failure modes: measuring average frame time while outliers (long tasks) cause the perceived jank; hidden-tab timers or background work stealing budget; layout thrash eating the whole budget invisibly; and assuming the budget applies only to animations — input handlers share it.
- Operational tradeoffs: respecting the budget costs engineering time (deferred work, workers, virtualization); the payoff is predictable interaction. Use PerformanceObserver longtask and the frame timeline to find violators, and prefer off-main-thread work (Web Workers, OffscreenCanvas) for heavy computation.
- RSIS3/mykb relevance: the dashboard tracks long-task counts per tab in rack telemetry, and loop reviews treat frame-budget violations in embedded viewers as a rendering regression.
- Budget accounting: include style/layout/paint in the frame budget, not just script; a 5ms script that triggers a 12ms reflow still blows the frame, so measure the pipeline, not the handler.
- Long-task accounting: a 50ms+ task blocks input entirely; budget by long-task counts and p95 frame time, not averages, since users perceive the outliers.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/input-latency|Input Latency]]
- [[wiki/web-platforms/interaction-to-next-paint|Interaction to Next Paint]]
- [[wiki/web-platforms/largest-contentful-paint|Largest Contentful Paint]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
