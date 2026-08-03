---
type: "concept"
title: "Z-Index Management"
description: "Controlling overlap order without stacking-context surprises"
tags: ["css", "z-index", "layout", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Z-Index Management

## Summary

z-index management is the discipline of ordering stacked elements predictably. Without a system, z-index values become arbitrary arms races, and stacking contexts make values behave non-locally. The fix is a token scale plus context discipline.

## Details
- Mechanism: z-index applies within a stacking context; non-auto z-index on positioned (or flex/grid item) elements creates one, as do opacity/transform/filter/will-change/isolation. A child cannot escape its parent's context, so a modal nested inside a transformed card stacks under sibling overlays regardless of its z-index.
- Concrete example: a token scale (--z-base, --z-dropdown, --z-sticky, --z-modal, --z-toast, --z-tooltip) gives every layer a documented home; components reference tokens, and overlays render at the document root (or an isolation: isolate boundary) so modals beat in-page content predictably.
- Failure modes: arbitrary values (9999, 10000) that collide after refactors; negative z-index children disappearing behind ancestor backgrounds; creating stacking contexts accidentally via opacity/transform mid-animation, changing paint order; and forgetting that focus rings and tooltips need their own tier above content.
- Operational tradeoffs: a small token scale plus isolation boundaries is cheap and keeps the model local; the cost is review discipline — new overlays must join the scale, not invent values. Debug with the stacking-context visualization in DevTools.
- RSIS3/mykb relevance: the dashboard's overlay tiers are tokenized and documented here; loop-generated popups are required to use the scale instead of ad-hoc values.
- Focus order: stacking and z-index do not change tab order; overlays must manage focus and inertness so keyboard users are not trapped behind a visually-raised layer.
- Animation interplay: layers promoted during transforms create contexts; re-verify overlay stacking after adding motion to cards.
- Overlay roots: render modals and toasts at the document root inside an isolation boundary; a modal inside a transformed card cannot reliably stack above page content no matter its z-index.

## Related
- [[wiki/web-platforms/css-architecture|CSS Architecture]]
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/component-architecture|Component Architecture]]
- [[wiki/web-platforms/web-components|Web Components]]
