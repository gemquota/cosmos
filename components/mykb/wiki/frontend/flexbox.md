---
type: "concept"
title: "Flexbox"
description: "One-dimensional alignment and distribution of flex items"
tags: [css", "flexbox", "layout", "styling", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout", "https://www.w3.org/TR/css-flexbox-1/"]
---

# Flexbox

## Summary
Flexbox lays out children along a single axis — row or column — with powerful alignment and space distribution. The flex container controls direction, wrapping, and alignment, while items control growth, shrinkage, and their own cross-axis position. It replaced float-based rows and remains the workhorse for toolbars, navs, cards, and inline clusters.

## Details
- Axes: flex-direction sets the main axis (row or column); the cross axis is perpendicular; justify-content aligns the main axis, align-items the cross axis.
- Sizing: flex-grow, flex-shrink, and flex-basis combine into the flex shorthand, distributing free space and handling overflow.
- Wrapping: flex-wrap lets items flow onto multiple lines, forming a gap-separated grid-like cluster.
- Alignment: align-self overrides per item; margin: auto on an item absorbs remaining space for classic push-right patterns.
- Gap: the gap property spaces items without negative-margin hacks; safe alignment keywords avoid unreachable positions on overflow.
- Versus grid: flexbox distributes one dimension of a set; grid arranges items in two dimensions with track control.

## Related
- [[wiki/frontend/css-grid|CSS Grid]] — the two-dimensional counterpart
- [[wiki/frontend/box-model|CSS Box Model]] — item sizing flexbox builds on
- [[wiki/frontend/responsive-design|Responsive Design]] — flex reflows at breakpoints
- [[wiki/frontend/container-queries|Container Queries]] — sizing flex layouts from containers
- [[wiki/frontend/css-positioning|CSS Positioning]] — overlay behavior alongside flex
- [[wiki/web-platforms/css-layout|CSS Layout]] — the layout platform family
