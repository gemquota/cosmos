---
type: "concept"
title: "px vs rem"
description: "When fixed pixels or root-relative rems suit a design"
tags: ["css", "units", "typography", "accessibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# px vs rem

## Summary

px is absolute, rem is root-relative: the choice determines whether UI scales with the user's font-size preference and with root-level zoom. Rem is the accessibility-friendly default for text and spacing; px remains right for borders, shadows, and pixel-exact art.

## Details
- Mechanism: 1rem equals the root html font-size (16px by default; user or UA settings can change it, and it compounds with browser zoom); px values ignore root font-size but do scale with zoom and DPR rendering. Media queries in px historically match the browser's default zoom-adjusted size, so rem media queries behave differently.
- Concrete example: a user who sets their browser to "large text" (root 20px) sees rem-based body text grow while a px-based caption stays small and unreadable; a button with rem padding and em-internal spacing grows proportionally. Borders and box-shadows in px keep hairline consistency at any text size.
- Failure modes: mixing units in one component (px spacing with rem text) breaks proportional scaling; rem media queries that fire at different widths than designers expect when root size changes; and libraries/design systems that hard-code px, silently ignoring user preference.
- Operational tradeoffs: a rem-first system with px reserved for chrome (borders, shadows, radii) balances accessibility and precision; document the unit policy so contributors do not reintroduce px for spacing. Test at 200% zoom and large-text settings.
- RSIS3/mykb relevance: the dashboard's spacing/type tokens are rem-first with px borders, a convention enforced by the style audit in loop checks.
- Media query note: px-based media queries match zoom-adjusted sizes, while rem-based ones scale with root font size; pick one convention and document it so breakpoints do not move unexpectedly for large-text users.
- Accessibility check: set the browser to large-text and re-test layouts built in rem; if spacing or type stays fixed, px has crept in where rem was intended.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/container-relative-units|Container Query Units]]
- [[wiki/web-platforms/responsive-units|Responsive Units]]
- [[wiki/web-platforms/vw-vh|vw and vh Units]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
