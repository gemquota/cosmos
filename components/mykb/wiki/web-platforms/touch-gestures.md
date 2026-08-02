---
type: "concept"
title: "Touch Gestures"
description: "Touch events, pointer events, and gesture handling for tap, swipe, pinch, and pan"
tags: ["touch", "gestures", "pointer-events", "mobile", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Touch_events", "https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events"]
---
# Touch Gestures

## Summary
Touch interfaces are driven by touch events or, better, unified pointer events that cover mouse, pen, and touch. Gestures — tap, swipe, pinch, long-press — compose from sequences of these events, and browsers add default behaviors (scroll, zoom) that touch-action controls.

## Details
- **Pointer events** — pointerdown/move/up unify input types; pointerId tracks concurrent touches; pointercancel handles interruptions.
- **Touch-action** — CSS touch-action declares which gestures the browser may handle, letting apps claim the rest.
- **Gesture recognition** — track movement deltas and thresholds; distinguish tap from swipe by time and distance.
- **Prevent default** — `touch-action: none` and passive-listener discipline stop scroll conflicts without blocking performance.
- **Worked example** — the mykb reader supports swipe-to-next-article using pointer events with touch-action: pan-y.
- **Relevance** — RSIS3's Termux-hosted UIs must treat touch as the primary input mode.
- **Gesture disambiguation** — long-press conflicts with scroll, swipe with drag; settle by distance and time thresholds, and cancel recognition on pointercancel so browsers can reclaim the gesture.

## Related
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/android-core/gesture-input|Gesture Input]] — existing coverage
