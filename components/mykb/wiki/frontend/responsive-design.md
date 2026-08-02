---
type: "concept"
title: "Responsive Design"
description: "Fluid layouts, flexible media, and breakpoint strategy"
tags: [css", "responsive", "layout", "mobile", "web-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/responsive-web-design-basics", "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"]
---

# Responsive Design

## Summary
Responsive design makes one codebase adapt to any viewport through fluid grids, flexible media, and media queries. Ethan Marcotte coined the term for the combination of fluid layouts, flexible images, and breakpoints. The viewport meta tag enables proper scaling on phones, and modern CSS adds container queries for component-level responsiveness.

## Details
- Fluid grids: percentage or fr-based columns reflow instead of scrolling horizontally; minmax and clamp keep extremes sane.
- Flexible media: images and video cap at container width via max-width: 100% and preserve aspect ratio to avoid layout shift.
- Breakpoints: media queries change layout at meaningful widths — typically content-driven rather than device-driven.
- Mobile-first: base styles target small screens, and min-width queries add complexity as space grows.
- Component level: container queries let a card adapt to its own container rather than the viewport, enabling reuse.
- Testing: emulation tools plus real devices, orientation changes, and zoom all matter for confidence.

## Related
- [[wiki/frontend/media-queries|Media Queries]] — the breakpoint mechanism
- [[wiki/frontend/container-queries|Container Queries]] — component-scoped responsiveness
- [[wiki/frontend/mobile-first-design|Mobile-First Design]] — the authoring order
- [[wiki/frontend/fluid-typography|Fluid Typography]] — viewport-relative type
- [[wiki/frontend/responsive-images|Responsive Images]] — media that adapts with the layout
- [[wiki/web-platforms/css-layout|CSS Layout]] — layout tools responsiveness relies on
