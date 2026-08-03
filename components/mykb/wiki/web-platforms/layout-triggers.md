---
type: "concept"
title: "Layout Triggers"
description: "Property changes that invalidate and recompute layout"
tags: ["performance", "rendering", "layout", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Layout Triggers

## Summary

Layout triggers are the property changes that force the browser to recompute geometry — the most expensive rendering stage. Knowing which properties trigger layout, and how far the invalidation spreads, is the core of render-performance debugging.

## Details
- Mechanism: changing geometry-affecting properties (width, height, margin, padding, top/left, font-size, display, flex/grid changes) invalidates layout; the browser recomputes the affected subtree (or the whole document for some properties like scrollbar). Reading layout after a write forces synchronous layout — "forced reflow" — with no batching.
- Concrete example: animating height or margin on hover re-layouts every frame; replacing it with transform: scaleY keeps layout untouched. A loop that writes style.left then reads offsetWidth forces a full reflow per iteration — classic jank from interleaved reads/writes.
- Failure modes: assuming only size properties matter (font-loading, text changes, and sibling interference re-layout too); layout invalidation spreading to ancestors/siblings, making a local change expensive; forced reflows hidden inside libraries (reading scrollWidth to center elements); and measuring with DevTools recording only the frame cost, not the cause.
- Operational tradeoffs: layout is unavoidable for initial render; the goal is to stop triggering it during interaction and animation. Batch reads and writes, use transform/opacity for motion, and keep layout-affecting changes in style pass rather than rAF loops where possible.
- RSIS3/mykb relevance: dashboard re-renders batch DOM writes and avoid forced reflows; layout-trigger regressions from new widgets surface in the long-task telemetry that feeds loop reviews.
- Read-after-write rule: batch all reads (offset*, getBoundingClientRect, scroll*) before any writes in a frame, or the browser re-layouts per interleaving; rAF alignment makes this automatic.
- DevTools: the Performance panel's layout events show which properties and elements invalidate; use it to verify a suspected trigger before refactoring.
- Trigger table: keep a reference list of layout/paint/composite property classes handy in the wiki; the table converts performance debates into mechanical facts.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/content-visibility|content-visibility CSS]]
- [[wiki/web-platforms/contain-property|CSS Containment]]
- [[wiki/web-platforms/will-change|will-change CSS]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
