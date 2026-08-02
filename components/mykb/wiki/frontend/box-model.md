---
type: "concept"
title: "CSS Box Model"
description: "Content, padding, border, and margin sizing behavior"
tags: [css", "box-model", "layout", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model", "https://www.w3.org/TR/css-box-4/"]
---

# CSS Box Model

## Summary
Every element is a rectangular box composed of content, padding, border, and margin. The box model determines how width and height are computed and how space is distributed around elements. Choosing border-box sizing globally is the most common modern practice because it makes declared sizes include padding and border.

## Details
- Layers: content is the innermost area; padding surrounds it; border sits outside padding; margin separates boxes from neighbors.
- content-box vs border-box: content-box adds padding and border to the declared width; border-box subtracts them from it.
- Box-sizing: the global reset `*, *::before, *::after { box-sizing: border-box }` makes layout math predictable.
- Margin collapsing: adjacent vertical margins merge into the larger value; flex and grid items and padding prevent it.
- Intrinsic sizing: min-content and max-content describe how a box shrinks or grows without fixed widths.
- Outside sizing: margin, border, and padding interplay drives overflow, alignment, and spacing bugs in tight layouts.

## Related
- [[wiki/frontend/css-grid|CSS Grid]] — two-dimensional layout built on boxes
- [[wiki/frontend/flexbox|Flexbox]] — one-dimensional box alignment
- [[wiki/frontend/css-positioning|CSS Positioning]] — moving boxes within containing blocks
- [[wiki/frontend/responsive-design|Responsive Design]] — sizing boxes across viewports
- [[wiki/web-platforms/css-layout|CSS Layout]] — the broader layout platform
- [[wiki/frontend/rtl-layouts|RTL Layouts]] — logical property variants of the box model
