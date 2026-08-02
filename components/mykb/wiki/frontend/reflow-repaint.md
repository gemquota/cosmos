---
type: "concept"
title: "Reflow and Repaint"
description: "Layout and paint invalidation costs and avoidance"
tags: [performance", "layout", "paint", "browser", "css"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/rendering-performance", "https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path"]
---

# Reflow and Repaint

## Summary
Reflow (layout) recalculates the geometry of elements when the DOM or CSS changes; repaint redraws affected pixels. Both are expensive, but reflow is worse because it cascades — changing one element can invalidate its ancestors and descendants. Animation and interactivity code that triggers constant reflow is the classic cause of jank.

## Details
- Reflow triggers: DOM insertion, class changes, font loading, viewport resizing, and reading forced-synchronous layout properties.
- Forced synchronous layout: reading offsetHeight or getBoundingClientRect right after a write forces the browser to flush layout early.
- Batching: group reads and writes separately (or use a library) so the browser computes layout once per frame.
- Scoping: modern engines limit invalidation to affected subtrees, but large documents still pay a proportional cost.
- Paint-only changes: color, background, and box-shadow can repaint without layout, which is cheaper but still rasterizes.
- Compositor path: transform and opacity changes skip layout and paint entirely, running on the compositor thread.

## Related
- [[wiki/frontend/critical-rendering-path|Critical Rendering Path]] — where layout and paint sit in the pipeline
- [[wiki/frontend/animation-performance|Animation Performance]] — avoiding reflow in animations
- [[wiki/frontend/dom-api|DOM API]] — the mutations that trigger reflow
- [[wiki/frontend/long-tasks|Long Tasks]] — jank shows up as long main-thread tasks
- [[wiki/web-platforms/browser-engines|Browser Engines]] — how engines implement invalidation
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — minimizing layout cost
