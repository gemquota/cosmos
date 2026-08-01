---
type: "concept"
title: "Responsive Design"
description: "UIs that adapt to screen size, orientation, and form factor across phones, tablets, and foldables"
tags: ["responsive", "design", "layout", "adaptive", "accessibility"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"]
---

# Responsive Design

## Summary

Responsive design makes interfaces adapt to screen size, orientation, and form factor instead of assuming one canvas. On mobile it means density-independent units, window size classes, and adaptive layouts rather than pixel guessing. The same principles span Android, iOS, and the web.

## Details

- Density-independent units: dp on Android and CSS media queries on the web abstract away raw pixels; sp scales text with user settings.
- Window size classes (compact, medium, expanded) drive navigation and content layout decisions.
- Fluid grids and breakpoints reflow content; components stretch, constrain, or switch forms at each breakpoint.
- Adaptive patterns: list-detail panes on tablets, navigation rail on large screens, bottom bar on phones.
- Foldables add hinged postures, display cutouts, and continuity across folds.
- Accessibility is part of responsiveness: dynamic type, touch targets, and readable line lengths scale together.
- RSIS3 relevance: the mykb dashboard should render the same graph on a phone, tablet, and desktop without separate builds.

## Related

- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — Android window-size-class implementation
- [[wiki/android-core/dp-vs-px|DP vs PX]] — density units are the responsive foundation
- [[wiki/mobile-platform/tablet-support|Tablet Support]] — large-screen layout patterns
- [[wiki/android-core/foldables-support|Foldables Support]] — hinged form factors extend responsive rules
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — dynamic type scales with responsive layouts
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — the web side of the same design discipline
- [[wiki/frontend/static-site-generation|Static Site Generation]] — generated dashboards still need responsive CSS
