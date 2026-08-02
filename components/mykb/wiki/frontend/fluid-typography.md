---
type: "concept"
title: "Fluid Typography"
description: "Viewport-relative type scaling with clamp()"
tags: [css", "typography", "fluid", "responsive", "clamp"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/clamp", "https://www.w3.org/TR/css-values-4/#funcdef-clamp"]
---

# Fluid Typography

## Summary
Fluid typography scales font size continuously between viewport bounds using clamp(), which takes a minimum, a preferred value, and a maximum. The preferred value usually mixes a fixed unit with vw so type grows with the viewport but never becomes unreadably small or absurdly large. It replaces rigid breakpoint font jumps.

## Details
- Formula: font-size: clamp(1rem, 0.9rem + 0.5vw, 1.5rem) interpolates between bounds as the viewport changes.
- Interpolation: the preferred expression linear-scales with viewport width; vh, cqw, or container units work where relevant.
- Accessibility: avoid compounding vw alone — text that shrinks with the viewport can fall below readable sizes; clamp prevents that.
- Line height and measure: pair fluid sizes with proportional line-height and reasonable measure (45-75 characters) for legibility.
- System integration: expose fluid scale as custom properties so spacing and type stay in sync across components.
- Trade-offs: fluid type complicates design specs slightly; fallbacks are unnecessary since clamp is widely supported.

## Related
- [[wiki/frontend/responsive-design|Responsive Design]] — fluid type within fluid layouts
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — hosting the fluid scale
- [[wiki/frontend/mobile-first-design|Mobile-First Design]] — small-screen baseline sizing
- [[wiki/frontend/media-queries|Media Queries]] — the breakpoint alternative
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — readable type as an a11y requirement
- [[wiki/frontend/design-tokens|Design Tokens]] — where type scales are defined
