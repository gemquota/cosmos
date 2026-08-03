---
type: "concept"
title: "CSS Transitions"
description: "Interpolating property changes over a duration"
tags: ["css", "animation", "transitions", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Transitions

## Summary

CSS transitions interpolate property values when they change, providing smooth state changes with a declarative easing and duration. They are the default tool for hover, focus, and class-driven UI feedback.

## Details
- Mechanism: transition-property, duration, timing-function, and delay define how a change from value A to B animates; the browser interpolates any animatable property between computed values. Only animatable properties transition — display and other discrete properties jump.
- Concrete example: a button background-color transitions over 150ms on hover; a drawer's transform: translateX animates on class toggle; a theme switch transitions colors by listing the CSS custom properties that change.
- Failure modes: transitioning layout properties (width, height, top) causes reflow each frame; missing from/to states (both endpoints must be resolvable) makes the transition no-op; transitioning custom properties requires registered properties (@property) with a defined syntax, otherwise the change snaps; and long durations on many elements create jank and motion sickness — respect prefers-reduced-motion.
- Operational tradeoffs: transitions are stateless and cheap to author, but complex orchestration (sequenced multi-step) belongs in CSS animations or the Web Animations API. Keep durations 150–300ms for UI feedback, and transition only compositor-friendly properties for frame-rate stability.
- RSIS3/mykb relevance: dashboard hover states and theme changes transition tokens, and the wiki tracks which properties are transition-safe to keep loop-generated UI consistent.
- Transitioning gradients and shadows: these are animatable but expensive — box-shadow interpolation re-paints each frame; prefer opacity layering for glow effects.
- Entry and exit: transitions need an explicit initial state; elements appearing with display: none do not transition in unless you animate via keyframes or force a reflow between state changes.
- Entrance states: elements that start hidden need an initial style the transition can interpolate from; display: none to visible is instant, so use opacity/transform with a mounted state instead.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/css-animations|CSS Animations]]
- [[wiki/web-platforms/css-transforms|CSS Transforms]]
- [[wiki/web-platforms/css-transitions|CSS Transitions]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/component-architecture|Component Architecture]]
- [[wiki/web-platforms/web-apis|Web APIs]]
