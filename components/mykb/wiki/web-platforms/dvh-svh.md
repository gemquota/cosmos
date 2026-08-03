---
type: "concept"
title: "Dynamic and Small Viewport Units"
description: "Handling mobile browser chrome with dvh and svh"
tags: ["css", "units", "viewport", "mobile"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Dynamic and Small Viewport Units

## Summary

Viewport units dvh/svh/lvh solve the mobile URL-bar problem: 100vh is taller than the visible area on mobile browsers, while 100dvh tracks the dynamic viewport as chrome shows and hides. svh/lvh are the stable small and large bounds.

## Details
- Mechanism: vh historically equals the largest viewport on mobile (large viewport), so a 100vh hero is partially hidden behind the URL bar or clipped; dvh resolves to the actual visible viewport as it changes; svh is the smallest state; lvh the largest. CSS uses dynamic/small/large viewport sizes, and units apply to width (dvw/swv/lvw) and height alike.
- Concrete example: a sticky bottom action bar with height: 100dvh-adjacent padding stays above the keyboard; a full-screen modal with 100svh never overflows when the bar is visible; fallback order is vh → svh → dvh so old browsers keep the large-viewport behavior.
- Failure modes: dvh changes when the browser UI collapses, which can restart transitions or resize maps; using dvh for heights that should be stable makes elements jump on scroll-triggered chrome changes; and supporting iOS Safari's keyboard behavior still needs extra handling since keyboards are not always reflected.
- Operational tradeoffs: prefer svh/lvh for layout boxes that must not resize and dvh for interactive surfaces that should track reality; where legacy browsers matter, provide vh fallback before the new units since unknown declarations are dropped, not errored.
- RSIS3/mykb relevance: the dashboard's mobile layout uses dvh for the bottom pulse bar and svh for panels, with the fallback order documented in the wiki style notes.
- Keyboard behavior: iOS keyboards are not always reflected in dvh; test with the keyboard open and closed and size interactive shells with svh plus safe-area padding where needed.
- Fallback order: declare vh first, then svh, then dvh, so unsupported engines keep the closest safe behavior.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/em-vs-rem|em vs rem]]
- [[wiki/web-platforms/px-vs-rem|px vs rem]]
- [[wiki/web-platforms/container-relative-units|Container Query Units]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
