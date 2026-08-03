---
type: "concept"
title: "Mobile UX Patterns"
description: "Navigation, touch targets, feedback, and ergonomics that define usable mobile apps"
tags: ["mobile", "ux", "patterns", "design", "interaction"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://m3.material.io/", "https://developer.apple.com/design/human-interface-guidelines/"]
---
# Mobile UX Patterns

## Summary
Mobile UX patterns cover navigation (tabs, drawers, stacks), touch ergonomics (44-48pt targets), feedback (toasts, haptics), and thumb reach. Platform conventions — Material Design on Android, HIG on iOS — provide the shared vocabulary users expect. Patterns reduce cognitive load and increase confidence.

## Details
- **Navigation** — bottom tabs for top-level sections; hierarchical stacks for drill-down; sheets and drawers for secondary actions.
- **Touch targets** — minimum 44-48pt targets with spacing; thumb-zone placement for primary actions.
- **Feedback** — instant response (ripples, pressed states), progress indicators, and confirmations before destructive actions.
- **Adaptivity** — safe areas, dynamic type, and foldables/tablets via adaptive layouts.
- **Worked example** — the mykb mobile app uses bottom tabs, a floating compose action, and haptic feedback on save.
- **Relevance** — RSIS3's generated UIs should encode these patterns as reusable components.
- **Gesture ergonomics** — primary actions sit in the lower thumb zone, destructive actions confirm, and back gestures follow platform conventions; consistency beats novelty in mobile UX.

## Related
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-snap|Scroll Snap]] — adjacent concept in this wiki
- [[wiki/web-platforms/vw-vh|vw and vh Units]] — adjacent concept in this wiki
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — existing coverage
- [[wiki/mobile-platform/tablet-support|Tablet Support]] — existing coverage
- [[wiki/frontend-frameworks/material-design|Material Design]] — existing coverage
