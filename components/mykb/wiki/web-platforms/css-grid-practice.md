---
type: "concept"
title: "CSS Grid in Practice"
description: "Two-dimensional layout: tracks, areas, alignment, and auto-placement"
tags: ["css", "grid", "layout", "frontend", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout", "https://developer.mozilla.org/en-US/docs/Web/CSS/grid"]
---
# CSS Grid in Practice

## Summary
CSS Grid is the two-dimensional layout system: rows and columns defined by track sizing, with items placed by line, area, or auto-flow. It replaced table layouts and float hacks for page and card grids, and it composes with flexbox for one-dimensional alignment.

## Details
- **Track sizing** — `fr` distributes free space; `minmax()` clamps; `repeat()` and `auto-fit/auto-fill` build responsive grids without media queries.
- **Placement** — `grid-template-areas` names regions for readable layouts; line-based placement handles asymmetric designs; `auto-flow` handles dynamic content.
- **Alignment** — `justify-*` and `align-*` properties place items in their cells; `gap` replaces margins.
- **Subgrid** — `subgrid` inherits parent tracks, aligning nested content.
- **Worked example** — the mykb wiki index uses a `repeat(auto-fit, minmax(220px, 1fr))` grid so card columns adapt without breakpoints.
- **Relevance** — grid layouts keep agent-generated dashboards aligned across viewports.
- **Named grid lines** — `grid-template-columns: [main-start] 1fr [main-end]` names lines for readable placement; `grid-area` shorthand then maps items into the named areas defined by `grid-template-areas`.

## Related
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]] — adjacent concept in this wiki
- [[wiki/web-platforms/clamp-practice|clamp() in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/aspect-ratio-css|aspect-ratio in CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/container-relative-units|Container Query Units]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
