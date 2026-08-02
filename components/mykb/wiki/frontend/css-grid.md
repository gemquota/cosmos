---
type: "concept"
title: "CSS Grid"
description: "Two-dimensional layout with rows, columns, and tracks"
tags: [css", "grid", "layout", "responsive", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout", "https://www.w3.org/TR/css-grid-1/"]
---

# CSS Grid

## Summary
CSS Grid is the browser's native two-dimensional layout system. A grid container defines rows and columns as tracks, and items are placed into cells by line, name, or automatic flow. Unlike flexbox, grid handles both axes at once, which makes page-level layouts and complex component grids straightforward.

## Details
- Track sizing: grid-template-columns: repeat(12, 1fr) divides space evenly; minmax() and auto tracks adapt to content.
- Placement: grid-column: 2 / 5 or named areas via grid-template-areas express layout directly in CSS.
- Alignment: justify-items and align-items control cell alignment; align-content and justify-content distribute tracks.
- Gap: the gap property replaces margins between tracks and never collapses.
- Auto flow: grid-auto-flow: dense fills holes in the implicit grid for card-like layouts.
- Subgrid: grid-template-rows: subgrid lets nested grids align tracks with their parent, solving inner-row alignment.
- Fit: grids dominate full-page layouts, while flexbox handles inline sequences and small components.

## Related
- [[wiki/frontend/flexbox|Flexbox]] — the one-dimensional complement
- [[wiki/frontend/box-model|CSS Box Model]] — sizing foundations tracks build on
- [[wiki/frontend/container-queries|Container Queries]] — sizing grids by their container
- [[wiki/frontend/responsive-design|Responsive Design]] — grids adapt across breakpoints
- [[wiki/web-platforms/css-layout|CSS Layout]] — the layout platform family
- [[wiki/frontend/css-positioning|CSS Positioning]] — overlay techniques alongside grids
