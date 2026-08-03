---
type: "entity"
title: "FLIP"
description: "FLIP animation technique: First, Last, Invert, Play for smooth layout transitions"
tags: ["entity", "acronym", "frontend", "animation", "layout"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# FLIP

## Summary

FLIP stands for First, Last, Invert, Play, a frontend technique for animating layout changes without expensive layout recalculations per frame. It works by measuring an element's start and end positions and using a CSS transform to fake the motion. It matters because it turns janky, layout-triggering animations into smooth GPU-composited transitions.

## Details

- **Acronym** — First captures the element's starting position and size; Last captures where it ends after the layout change; Invert applies a transform that puts it back; Play animates to zero.
- **Why it exists** — Animating width, top, or transform-to-layout properties forces layout on every frame; FLIP animates only transforms and opacity, which compositors handle cheaply.
- **Core mechanics** — The delta between start and end is computed once and expressed as a CSS transform, which the browser then animates smoothly back to identity.
- **Worked example** — A list reorders on filter; each item's old position is measured, the DOM updates, and a translate transform slides the item from its old spot to its new one.
- **Limitations** — Text reflow inside the element is not smoothly animated, and anything that depends on the element's visual size mid-transition can glitch.
- **Common failure modes** — Measuring after the DOM update instead of before, forgetting to clear transforms, and animating large subtrees that still trigger layout are typical mistakes.
- **Variants** — FLIP for lists, staggered FLIP for multiple items, and inverse transforms for modal open-close are common refinements.
- **Frameworks** — Libraries such as Vue's transition-group and Framer Motion implement FLIP-style enter and move animations under the hood.
- **Practical relevance** — Understanding FLIP helps diagnose why supposedly animated elements jump, scale incorrectly, or drop frames in modern web apps.
- **Telemetry note** — The stub tagged FLIP against IP/networking context, but the frontend animation reading matches the session categories in which it was observed.
- **Measuring costs** — Measuring layout positions triggers synchronous layout; batching measurements before any DOM mutation avoids forced reflow jank.
- **Accessibility** — Reduced-motion preferences should disable FLIP transitions, and animated content must not obscure keyboard focus or screen-reader state.
- **Worked example** — A drag-and-drop list uses FLIP so siblings glide into place after a drop, with a transform transition that the compositor animates off the main thread.

## Related

- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]] — how compositing works
- [[wiki/web-platforms/browser-engines|Browser Engines]] — layout and paint internals
- [[wiki/frontend/localization|Localization]] — UI adaptation that can trigger layout shifts
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — client-side behavior
- [[wiki/concepts/event-segmentation|Event Segmentation]] — perceiving motion as events
- [[wiki/web-platforms/caniuse-practice|Can I Use Practice]] — feature support checks
