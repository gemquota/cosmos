---
type: "concept"
title: "Contrast Ratios"
description: "WCAG luminance contrast for text legibility"
tags: ["accessibility", "color", "wcag", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Contrast Ratios

## Summary

Contrast ratio quantifies the luminance difference between text and background, and WCAG 2.x sets thresholds (4.5:1 normal text, 3:1 large text and UI components). It is the baseline, not the whole story, of readable text.

## Details
- Mechanism: ratio = (L1 + 0.05) / (L2 + 0.05) from relative luminance, which weighs channels by human perception (linearized, sRGB-weighted). The math treats color pairs, so two designs can pass the same ratio while differing wildly in readability.
- Concrete example: #777777 gray on white just fails 4.5:1 (about 4.48:1), while #757575 passes (about 4.61:1); moving to the darker shade costs little aesthetically and keeps body text WCAG AA. Going darker still, #595959 reaches about 7.0:1, a comfortable margin. Large text (>=24px or >=19px bold) and icons need only 3:1.
- Failure modes: passing ratios on small low-contrast fonts that still strain readers; anti-aliasing and thin font weights reduce effective contrast beyond the math; backgrounds with gradients or images defeat pair-based checks; and WCAG ratios say nothing about hue-dependence, so red/green status colors still fail color-blind users.
- Operational tradeoffs: higher contrast ratios can fight brand palettes; pick accessible brand pairings early rather than darkening text ad hoc. Audit at the design-token level — check every text/background combination in the theme, not just sampled pages, and re-check after color-mix or alpha changes.
- RSIS3/mykb relevance: the dashboard's theme tokens are contrast-checked as part of the design-note wiki, and the rack telemetry includes a periodic contrast audit of key surfaces.
- Measurement tooling: automate the audit with axe-style checks plus a token-level contrast test across every surface pair; manual sampling misses the dark-mode and hover-state pairs that fail.
- Beyond the ratio: large-font and UI-component thresholds are 3:1, not 4.5:1 — apply the right threshold per element type, and remember that focus indicators, placeholder text, and disabled states all need their own checks.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/color-blind-considerations|Color Blind Accessibility]]
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]]
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
