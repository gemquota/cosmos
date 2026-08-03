---
type: "concept"
title: "Media Queries in Practice"
description: "Width, height, and interaction media feature usage"
tags: ["css", "responsive", "media-queries", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Media Queries in Practice

## Summary

Media queries adapt styles to viewport, device, and user preferences (width, aspect-ratio, prefers-color-scheme, prefers-reduced-motion, scripting). Good practice uses them for genuine breakpoints, not as a substitute for flexible layout.

## Details
- Mechanism: @media (min-width: 768px) gates rules on viewport size; the query list also covers height, orientation, resolution, hover/pointer, and user-preference features. CSS resolves queries at apply time, so the same rules work in iframes and when the window resizes.
- Concrete example: a dashboard grid goes from single-column on narrow screens to a 12-column grid at 1024px via a min-width query; prefers-reduced-motion disables entrance animations; hover: hover upgrades hover-dependent interactions on devices that have them.
- Failure modes: pixel breakpoints tuned to one device (foldables, split-screen, zoom break them); querying width when container context matters (use container queries for components); duplicating large rule blocks per breakpoint instead of moving layout to flex/grid; and forgetting that min-width chains must stay ordered or later queries override.
- Operational tradeoffs: prefer fluid layout (clamp, grid auto-fit, flex wrap) with media queries only where real re-layout happens; document breakpoints as tokens so design and code share the same ladder. Test at breakpoint edges and with browser zoom.
- RSIS3/mykb relevance: the dashboard's breakpoint ladder is documented in the design notes, and telemetry panels use container queries internally so they reflow within any panel size.
- User-preference queries: prefers-reduced-motion and prefers-contrast are accessibility contracts, not design choices; gate motion and low-contrast variants on them consistently.
- Overlap discipline: avoid stacking min-width and max-width ladders on the same property; a single mobile-first min-width chain is easier to audit.
- Orientation handling: orientation queries are device-dependent; prefer aspect-ratio or container-based logic that survives split-screen and window resizing.
- Query minimalism: if a component reflows correctly without a query, do not add one; every query is a maintenance point.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/feature-queries|CSS Feature Queries]]
- [[wiki/web-platforms/supports-rule|@supports Rule]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-standards|Web Standards]]
