---
type: "concept"
title: "Flexbox in Practice"
description: "One-dimensional layout: main and cross axes, growth, shrinking, and alignment"
tags: ["css", "flexbox", "layout", "frontend", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout", "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox"]
---
# Flexbox in Practice

## Summary
Flexbox lays out items along one axis with precise control over growth, shrink, order, and alignment. It excels at toolbars, nav bars, card actions, and centering. Combined with Grid for two dimensions, it covers the vast majority of modern layout.

## Details
- **Axes** — `flex-direction` chooses row or column; `justify-content` aligns on the main axis; `align-items`/`align-self` on the cross axis.
- **Sizing** — `flex-grow`, `flex-shrink`, and `flex-basis` (the `flex` shorthand) negotiate space; `min-width: 0` unblocks shrinking.
- **Order and wrapping** — `order` reorders visually (use sparingly for a11y); `flex-wrap` handles overflow into rows.
- **Auto margins** — `margin-inline: auto` pushes items apart for spacer-style layouts.
- **Worked example** — the mykb header is a flex row with the title, search, and theme toggle; `margin-inline-start: auto` right-aligns the controls.
- **Relevance** — component-level flex patterns are the default for RSIS3-generated UI primitives.
- **Baseline alignment** — `align-items: baseline` lines up items by their text baselines, which beats fixed padding for heterogeneous rows; `gap` replaces margins in both axes.

## Related
- [[wiki/web-platforms/logical-properties|CSS Logical Properties]] — adjacent concept in this wiki
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]] — adjacent concept in this wiki
- [[wiki/web-platforms/aspect-ratio-css|aspect-ratio in CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/rtl-support|RTL Support]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — existing coverage
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
