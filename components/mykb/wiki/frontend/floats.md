---
type: "concept"
title: "CSS Floats"
description: "Legacy text-wrap and column layout via float behavior"
tags: [css", "floats", "layout", "legacy", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/float", "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Floats"]
---

# CSS Floats

## Summary
Floats move an element left or right within its container so following content wraps around it. They were the standard way to build multi-column layouts before flexbox and grid, and remain useful for text wrapping around images and decorative drop caps. The technique needs explicit clearing because floated elements leave normal flow.

## Details
- Behavior: float: left or right lifts the element out of normal flow; inline content flows along the remaining space.
- Clearing: clear: both on a following block (or a clearfix on the parent) prevents containers from collapsing around floats.
- Layout origins: float-based grids used percentage widths and gutters, with all their column-height and ordering quirks.
- Modern role: wrapping images in articles and inline drop caps; layout itself now belongs to flexbox and grid.
- Pitfalls: floats complicate vertical rhythm, backgrounds, and RTL handling; logical properties do not apply to float directly.
- Migration: replace float rows with flex or grid; keep floats only where text wrapping is genuinely wanted.

## Related
- [[wiki/frontend/flexbox|Flexbox]] — replaced floats for most layout work
- [[wiki/frontend/css-grid|CSS Grid]] — the modern two-dimensional replacement
- [[wiki/frontend/box-model|CSS Box Model]] — the sizing model float layout exploited
- [[wiki/frontend/responsive-design|Responsive Design]] — how float layouts broke responsively
- [[wiki/frontend/css-positioning|CSS Positioning]] — the other flow-out mechanism
- [[wiki/web-platforms/css-layout|CSS Layout]] — where floats sit in layout history
