---
type: "concept"
title: "Container Query Units"
description: "Length units relative to a container's size"
tags: ["css", "units", "container-queries", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Container Query Units

## Summary

Container query units — cqw, cqh, cqi, cqb, cqmin, cqmax — size children relative to a query container instead of the viewport. They make components respond to their own context, not the page.

## Details
- Mechanism: a parent becomes a query container with container-type: inline-size (or size), then children can use cqi (1% of container inline size), cqw (width), cqh (height), cqb (block size), cqmin/cqmax. Units resolve only inside a container; outside one they fail back to small-viewport units.
- Concrete example: a card grid where each card sizes its heading font with clamp(1rem, 0.5rem + 3cqi, 1.5rem) scales by the card's own width, so a sidebar card and a full-width card stay proportionally consistent without media queries per placement.
- Failure modes: container-type: size requires explicit sizing and can collapse un-sized containers; nesting containers changes which ancestor the unit resolves against (nearest one wins); inline-size containment also isolates layout, which can break floats and sticky descendants; and unsupported browsers ignore the units, so provide fallbacks.
- Operational tradeoffs: container units and container queries shift responsibility from page-level breakpoints to component-level ones — better encapsulation, but harder to reason about a component in isolation without container context in DevTools. Use them where the same component appears in many widths (widgets, embeds, dashboards).
- RSIS3/mykb relevance: dashboard panels are built as container-query components, so the same telemetry card renders correctly in the overview grid and the full-screen detail view.
- Fallback order: declare a viewport-relative or rem fallback before container units; browsers that ignore cqi drop the declaration and keep the fallback, so layout survives legacy engines.
- Container type choice: container-type: inline-size is sufficient for width-based sizing and avoids the explicit-height requirement of size; reserve size for cases that genuinely need both axes.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/responsive-units|Responsive Units]]
- [[wiki/web-platforms/vw-vh|vw and vh Units]]
- [[wiki/web-platforms/vw-vh|vw and vh Units]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
