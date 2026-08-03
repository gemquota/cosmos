---
type: "concept"
title: "Repaint vs Reflow"
description: "Distinguishing pixel repainting from layout reflow work"
tags: ["performance", "rendering", "layout", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Repaint vs Reflow

## Summary

Reflow (layout) recomputes geometry; repaint redraws pixels. Repaints are cheaper than reflows, but both are main-thread work — the performance goal is to trigger neither during animation and to localize both during updates.

## Details
- Mechanism: a style change triggers style recalc, then layout if geometry changed (reflow), then paint if appearance changed (repaint), then composite. Reflow is recursive — a width change on a container re-layouts descendants and may shift siblings; repaint redraws the affected layers, which scales with area and complexity.
- Concrete example: changing color repaints only; changing width reflows the subtree and repaints the shifted regions; animating left triggers both every frame, while transform triggers only compositing. Reading offsetWidth after a write forces a synchronous reflow, doubling the cost.
- Failure modes: assuming repaint is free (large layers, shadows, filters make it measurable); layout changes inside scroll handlers (scroll-linked resizing) causing reflow-per-frame; batch failures from interleaved reads and writes; and micro-optimizing one while ignoring the other — both show up as long tasks.
- Operational tradeoffs: prefer transforms/opacity for motion, batch DOM writes, and isolate dynamic regions (containment, layers); measure with the rendering timeline and treat forced reflows in third-party widgets as a dependency risk to be contained.
- RSIS3/mykb relevance: dashboard updates follow a read-batch-write discipline, and repaint/reflow hotspots from embedded viewers are flagged by the long-task telemetry the loop reviews.
- Scope containment: CSS containment (contain: layout paint) and content-visibility localize reflow/repaint to a subtree; use them where a large region updates independently.
- Measuring: DevTools' rendering tab shows layout/paint regions live; the Performance panel attributes each long task to the responsible script so fixes target the real trigger.
- Diagnostic tools: paint-flash and layout-shift regions in DevTools localize the cost; use them before micro-optimizing, since the visual evidence beats the guess.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/frame-budget|Frame Budget]]
- [[wiki/web-platforms/input-latency|Input Latency]]
- [[wiki/web-platforms/interaction-to-next-paint|Interaction to Next Paint]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
