---
type: "concept"
title: "Responsive Design Systems"
description: "Fluid layouts, breakpoints, and adaptive behavior across viewport sizes and input modes"
tags: ["responsive", "css", "design-systems", "layout", "mobile"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design", "https://web.dev/articles/responsive-web-design-basics"]
---
# Responsive Design Systems

## Summary
Responsive design makes one codebase work from phones to desktops: fluid grids, flexible media, and breakpoints that respond to available space. It combines media queries, container queries, and viewport units, and it must account for touch, hover, and reduced-motion input modes.

## Details
- **Fluid foundations** — rem/em sizing, percentage widths, `clamp()`, and `minmax()` keep layouts proportional instead of pixel-locked.
- **Breakpoints** — content-driven width thresholds with mobile-first `min-width` queries; container queries respond to the component's container, not the viewport.
- **Images and media** — `srcset`, `sizes`, and the `picture` element serve the right asset; `aspect-ratio` reserves space.
- **Interaction** — `hover: hover`, `pointer: coarse`, and safe-area insets adapt to touch and notches.
- **Worked example** — the mykb wiki reader switches from a two-column layout to a single column at its content breakpoint, with container queries for embedded cards.
- **Relevance** — RSIS3's dashboards must read well on Termux-sized mobile screens, making responsive systems a hard requirement.

## Related
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]] — adjacent concept in this wiki
- [[wiki/web-platforms/clamp-practice|clamp() in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
- [[wiki/web-platforms/web-standards|Web Standards]] — existing coverage
