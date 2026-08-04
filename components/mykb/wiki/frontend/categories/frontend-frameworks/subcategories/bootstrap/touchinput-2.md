---
type: "entity"
title: "TouchInput"
description: "TouchInput: touch events, gestures, and pointer unification"
tags: ["api", "ast", "aws", "bash", "bootstrap", "bug", "entity", "touch"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# TouchInput

## Summary

TouchInput is the bootstrap-cluster entity for touch interaction: handling taps, drags, and multi-touch gestures on touch surfaces. Unified pointer events simplify supporting both touch and mouse. It matters because touch input is the primary interface on mobile and increasingly common on desktop. Touch handling done well is invisible; done badly, it makes the whole app feel broken.

## Details

- **Definition** — Touch input maps physical contact with a screen into application events: taps, drags, pinches, and rotations.
- **Pointer events** — Unified pointer events abstract mouse, pen, and touch into one model, with contact size and pressure where available.
- **Gestures** — Recognizers distinguish taps from drags and compose multi-touch gestures with thresholds and cancellation.
- **Targeting** — Touch targets must be large enough and hit-testing must account for the contact area, not a single point.
- **Scroll and zoom** — Touch scrolls and zooms compete with custom gestures; ownership rules prevent both firing.
- **Worked example** — A node editor supports one-finger pan, two-finger zoom, and long-press to open context menus.
- **Failure modes** — Unhandled multi-touch, gesture conflicts with scrolling, and passive listeners that block cancellation cause broken UX.
- **Practical relevance** — Accessible touch input includes keyboard alternatives, so touch design is also inclusive design.
- **Thresholds** — Movement thresholds distinguish taps from drags; too-low thresholds make taps unreliable.
- **Cancellation** — Gestures must cancel cleanly when the pointer is released or another gesture claims it.
- **Desktop parity** — Testing touch emulation catches missing handlers that desktop-only development misses.
- **Haptic feedback** — Subtle visual or haptic responses to touch confirm that input registered, reducing double-taps.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/documenttouch|DocumentTouch]] — touch event neighbor
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodeeditor|NodeEditor]] — touch-driven graph editing
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/noderenderer|NodeRenderer]] — visual feedback for touch
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dimensions|Dimensions]] — touch target sizing
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/edgeid|EdgeId]] — hit-target identity
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/decisiontype|DecisionType]] — gesture decision types
