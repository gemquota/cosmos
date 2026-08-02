---
type: "concept"
title: "Pointer Events"
description: "Unified mouse, touch, and pen input model"
tags: [pointer-events", "input", "javascript", "web-apis", "touch"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events", "https://www.w3.org/TR/pointerevents3/"]
---

# Pointer Events

## Summary
Pointer Events unify mouse, touch, and pen input behind one event model. pointerdown, pointermove, and pointerup fire for any input type, with properties like pointerType and pressure distinguishing them. pointer capture routes all events of a gesture to one element, which fixes drag and swipe implementations.

## Details
- Unified model: one set of listeners handles mouse, touch, and pen; pointerType identifies the source.
- Pointer capture: setPointerCapture keeps subsequent events targeting the capture element, solving finger-slip drags.
- touch-action: CSS tells the browser which gestures to handle natively (pan, pinch-zoom), so pointer events arrive as intended.
- Compatibility: mouse events still fire after pointer events unless suppressed; the Pointer Events spec defines the fallback order.
- Contact details: width, height, pressure, tiltX, and tiltY support drawing and stylus apps.
- Best practice: build with pointer events and test with real touch and pen devices, not only mouse emulation.

## Related
- [[wiki/frontend/dom-api|DOM API]] — the event system pointer events build on
- [[wiki/frontend/debouncing-throttling|Debouncing and Throttling]] — rate-limiting gesture work
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — the input-parity counterpart
- [[wiki/web-platforms/web-apis|Web APIs]] — the API family
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — touch-first layouts
- [[wiki/frontend/responsive-design|Responsive Design]] — input-agnostic interfaces
