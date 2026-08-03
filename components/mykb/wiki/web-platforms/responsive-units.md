---
type: "concept"
title: "Responsive Units"
description: "Choosing units that scale with viewport, container, or root"
tags: ["css", "units", "responsive", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Responsive Units

## Summary

Responsive units — %, vw/vh/dvw/dvh, cqw/cqi, em/rem, clamp expressions — size elements relative to their context so layouts adapt without per-breakpoint overrides. Choosing the right unit per property is the craft.

## Details
- Mechanism: percentages resolve against the parent's size; viewport units against the viewport (dynamic variants track browser chrome); container units against a query container; em/rem against font sizes. clamp() combines a preferred fluid expression with hard bounds, so a unit like clamp(1rem, 2vw + 1rem, 2rem) scales smoothly.
- Concrete example: fluid typography uses vw inside clamp for continuous scaling; a full-bleed hero uses 100dvw (careful — it can overflow the scrollbar gap, so width: 100% is usually safer); grid tracks use fr or minmax so columns share space; spacing uses rem for consistency.
- Failure modes: vw for widths causing horizontal overflow when a vertical scrollbar appears (use 100% or account for it); % heights collapsing without a definite parent height; mixing relative units in one formula producing unpredictable compound sizes; and ignoring that font-based units inherit and compound.
- Operational tradeoffs: relative units are the responsive default but need a documented policy — rem for spacing/type, %/fr for layout distribution, container units inside components, vw reserved for truly viewport-bound effects. Test at multiple zoom levels since all relative units respond to zoom.
- RSIS3/mykb relevance: dashboard panels use fr/minmax grids with rem spacing and container units internally; the unit policy is recorded here so loop-generated UI follows the same rules.
- Composition caution: relative units compound — a vw font inside a container-unit component resolves against different references; document which unit answers which question per layer so formulas stay readable.
- Documentation: keep a unit policy table (property → unit → rationale) in the design notes; ambiguous units are the source of the recurring full-width-overflow bugs.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/vw-vh|vw and vh Units]]
- [[wiki/web-platforms/dvh-svh|Dynamic and Small Viewport Units]]
- [[wiki/web-platforms/em-vs-rem|em vs rem]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
