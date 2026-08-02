---
type: "concept"
title: "Carousels in Practice"
description: "Rotating content panels: automation, controls, accessibility, and alternatives"
tags: ["carousel", "slider", "ux", "accessibility", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/tutorials/carousels/", "https://www.nngroup.com/articles/designing-effective-carousels/"]
---
# Carousels in Practice

## Summary
Carousels rotate through panels of content, but they are one of the most abused patterns: users ignore auto-rotating slides and miss content. When used, they need pause controls, manual navigation, and accessible announcements. Often a grid or list serves users better.

## Details
- **Controls** — previous/next, dots or thumbnails, and swipe; all must be keyboard-reachable.
- **Auto-play** — pause on hover/focus and respect `prefers-reduced-motion`; auto-rotation hurts comprehension.
- **Accessibility** — region with aria-roledescription="carousel", live-region announcements, and no hidden tabbables.
- **Alternatives** — static grids, tab panels, or "featured" lists usually outperform carousels.
- **Worked example** — the mykb homepage replaced its carousel with a featured-articles grid and kept a manual swipeable preview.
- **Relevance** — RSIS3's content surfaces should default to static layouts over rotation.
- **Manual-first design** — users should never depend on auto-rotation; provide next/previous, pause, and indicator controls, and stop rotation entirely when reduced motion is requested.

## Related
- [[wiki/web-platforms/scroll-snap|Scroll Snap]] — adjacent concept in this wiki
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/srcset-practice|srcset in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/picture-element|picture Element]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
