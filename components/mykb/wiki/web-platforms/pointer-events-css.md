---
type: "concept"
title: "pointer-events CSS"
description: "Controlling whether elements are hit-test targets"
tags: ["css", "events", "pointer", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# pointer-events CSS

## Summary

The CSS pointer-events property controls whether an element is a target for pointer input — and whether it can be clicked through. Its use spans hit-testing control, overlay UX, and the distinction between visible and interactive.

## Details
- Mechanism: pointer-events: none makes the element transparent to pointer hit-testing; events pass through to whatever is beneath. auto restores default behavior. On SVG it has richer semantics (visiblePainted, stroke, fill) controlling which painted areas are hit-testable.
- Concrete example: a tooltip overlay pointer-events: none so it never blocks clicks on the chart behind it, while a modal backdrop keeps auto to capture and dismiss clicks; a disabled button with pointer-events: none also stops tooltips on hover, which is why many designs keep pointer events and gate the action in JS.
- Failure modes: pointer-events: none on a parent disables all children, including scroll — a scrollable panel under an overlay can become un-scrollable by accident; :hover styles still apply on some browsers for elements with pointer-events: none (they are rendered, just not hit-tested); and keyboard focus is unaffected, so keyboard users can reach a visually disabled control — pair with disabled/aria-disabled.
- Operational tradeoffs: click-through overlays are the main legitimate use; for disabled controls prefer the disabled attribute or aria-disabled plus styling, keeping pointer events for semantics. Test with touch, pen, and mouse — hit-testing behavior can differ.
- RSIS3/mykb relevance: the dashboard's chart tooltips use pointer-events: none so crosshair interactions pass through; this note records the hit-testing rules reviewers check in loop passes.
- Keyboard parity: pointer-events: none does not remove an element from the tab order; gate interactive affordances with disabled/aria-disabled too, so keyboard and AT users do not reach dead controls.
- SVG nuance: pointer-events on SVG shapes has its own values (visiblePainted, stroke, fill); the CSS none/auto values apply to HTML elements, and mixing the two semantics causes hit-testing surprises.

## Related
- [[wiki/web-platforms/touch-gestures|Touch Gestures]]
- [[wiki/web-platforms/touch-action-css|touch-action CSS]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/android-core/gesture-input|Gesture Input]]
