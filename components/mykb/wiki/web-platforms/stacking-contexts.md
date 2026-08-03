---
type: "concept"
title: "Stacking Contexts"
description: "The z-axis grouping that determines paint order"
tags: ["css", "z-index", "layout", "rendering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Stacking Contexts

## Summary

A stacking context is a paint-domain boundary: elements inside it are painted as a unit above/below other contexts, and z-index compares only within the same context. Misunderstanding contexts causes the classic "z-index: 9999 still hidden" bug.

## Details
- Mechanism: a context is created by position + z-index (non-auto), opacity < 1, transform, filter, will-change, isolation: isolate, mix-blend-mode, contain: paint, and others. Inside a context, children order by z-index; the context itself participates in its parent's order as one unit — so a child's huge z-index cannot escape its parent's stacking level.
- Concrete example: a modal inside a transform-animated card stays under a sibling with a lower-looking z-index because the transformed card forms a context; the fix is isolation on the overlay root or moving the modal outside the transformed subtree. position: fixed also participates once an ancestor creates a context.
- Failure modes: adding z-index without checking ancestor contexts; animations (transform/opacity) silently creating contexts mid-transition, changing paint order; negative z-index children disappearing behind backgrounds; and iframes, video, and canvas having their own stacking behavior in old engines.
- Operational tradeoffs: explicit isolation: isolate on component roots makes stacking predictable and cheap to reason about; the cost is another mental model layer. Debug via DevTools' layer/stacking-context visualization, and keep z-index usage tokenized (a small scale) rather than arbitrary values.
- RSIS3/mykb relevance: dashboard overlays (tooltips, modals) use isolation boundaries and a tokenized z-index scale, documented here so loop-generated popups cannot float under charts.
- isolation practice: put isolation: isolate on component roots (cards, panels, overlays) so stacking stays local; a component that creates its own context cannot leak z-index fights into its neighbors.
- Animation interplay: opacity and transform create stacking contexts while animating, so a mid-animation z-index change is unreliable; settle stacking before adding motion, or the paint order flips visibly.

## Related
- [[wiki/web-platforms/css-architecture|CSS Architecture]]
- [[wiki/web-platforms/z-index-management|Z-Index Management]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/component-architecture|Component Architecture]]
- [[wiki/web-platforms/web-components|Web Components]]
