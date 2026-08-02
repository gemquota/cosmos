---
type: "concept"
title: "Container Queries"
description: "Styling components from their container's size"
tags: [css", "container-queries", "responsive", "components", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries", "https://www.w3.org/TR/css-contain-3/"]
---

# Container Queries

## Summary
Container queries let components style themselves based on the size of their container rather than the viewport. A container is declared with container-type, and descendants query it with @container. This makes responsive behavior reusable: the same card component adapts correctly whether it sits in a sidebar or a full-width grid.

## Details
- Setup: container-type: inline-size on an element creates a query container for its inline axis; container-name labels it.
- Querying: @container (min-width: 400px) applies styles when the nearest named container crosses the threshold.
- Units: container query units such as cqw and cqh size children relative to the container, similar to vw/vh for viewports.
- Containment: container-type applies size containment, so containers need explicit or content-driven sizing care.
- Use cases: dashboard cards, product tiles, split panels, and component libraries where one design must fit many slots.
- Browser support: stable in all major engines since 2023, with style queries for container state still evolving.

## Related
- [[wiki/frontend/media-queries|Media Queries]] — the viewport-based predecessor
- [[wiki/frontend/responsive-design|Responsive Design]] — the model container queries extend
- [[wiki/frontend/component-composition|Component Composition]] — why container-aware components matter
- [[wiki/frontend/css-grid|CSS Grid]] — grids place components that then adapt
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — passing container-derived values
- [[wiki/web-platforms/css-layout|CSS Layout]] — the layout platform container queries join
