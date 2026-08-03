---
type: "concept"
title: "CSS Layout"
description: "The mechanisms — flexbox, grid, floats — that position elements on the page"
tags: ["css", "layout", "flexbox", "grid"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# CSS Layout

## Summary

CSS layout today means flexbox and grid over legacy floats: flex for one-dimensional distribution, grid for two-dimensional placement. Choosing the right mechanism — and understanding intrinsic sizing — determines how robust a layout is.

## Details
- Mechanism: flexbox distributes along a main axis with wrap, grow, and shrink; grid defines explicit rows/columns with gap, tracks, and areas, plus auto-placement. Both resolve against the box's intrinsic and definite sizes, which is why min-width: 0 on flex children and minmax(0, 1fr) in grid are common fixes.
- Concrete example: a toolbar is flex (one row, spacing); a dashboard panel grid is grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) so panels wrap to the available width; a two-column article layout is grid with an explicit sidebar track.
- Failure modes: flex children overflowing because default min-width: auto prevents shrinking below content; grid blowouts from 1fr tracks that refuse to shrink below max-content; fixed pixel layouts that break at unexpected viewports; and deeply nested flex/grid creating unpredictable intrinsic sizes.
- Operational tradeoffs: grid is more powerful but has a steeper mental model; prefer the simpler mechanism that expresses the intent. Modern layout also includes container queries, subgrid, and logical properties — learn them together so layouts survive direction changes.
- RSIS3/mykb relevance: the dashboard's tab and panel chrome is grid/flex with logical properties; layout bugs are recorded as failure-mode notes so the loop does not re-learn them.
- Intrinsic sizing: auto tracks size to content; min-content/max-content and fit-content let authors express intent explicitly, which stabilizes grid and flex behavior across content changes.
- Directionality: flex and grid map to logical axes automatically under direction, so layouts mirror correctly in RTL without duplicated styles.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — CSS layout is standardized
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — layout order affects keyboard and screen-reader order
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — layout is a rendering cost
- [[wiki/web-platforms/component-architecture|Component Architecture]] — components encapsulate their layout
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — layout sits inside the web stack
