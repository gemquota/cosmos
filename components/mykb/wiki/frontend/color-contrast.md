---
type: "concept"
title: "Color Contrast"
description: "Contrast ratios and AA/AAA text requirements"
tags: [accessibility", "color", "contrast", "a11y", "wcag"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html", "https://web.dev/articles/color-and-contrast-accessibility"]
---

# Color Contrast

## Summary
Color contrast measures the luminance difference between text and its background; WCAG 2.2 requires at least 4.5:1 for normal text and 3:1 for large text and UI components at AA. Contrast affects everyone — in sunlight, on poor displays, and with low vision — so it is one of the highest-impact accessibility fixes.

## Details
- Ratio math: contrast ratio = (L1 + 0.05) / (L2 + 0.05) using relative luminance, ranging from 1:1 to 21:1.
- AA thresholds: 4.5:1 for normal text, 3:1 for large text (18px, or 14px bold) and non-text UI components.
- AAA: 7:1 for normal text is the enhanced level, often impractical for decorative copy and brand palettes.
- Exceptions: disabled controls, logos, and incidental text are exempt; placeholder text is a common failure.
- Tools: axe, Lighthouse, and browser checkers report ratios; pair them with vision simulations for gradients and overlays.
- Next generation: WCAG 3 drafts use APCA, a perception-based model, but WCAG 2.2 ratios remain the compliance baseline.

## Related
- [[wiki/frontend/wcag|WCAG]] — the criteria contrast belongs to
- [[wiki/frontend/theming|Theming]] — dark mode palettes must maintain ratios
- [[wiki/frontend/design-tokens|Design Tokens]] — contrast-safe color scales
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — automated contrast checks
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — color as an accessibility concern
- [[wiki/frontend/utility-css|Utility-First CSS]] — tokenized colors used in utilities
