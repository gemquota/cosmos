---
type: "concept"
title: "color-mix() CSS"
description: "Mixing two colors in a chosen color space"
tags: ["css", "color", "functions", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# color-mix() CSS

## Summary

color-mix() blends two colors in a specified color space, giving designers a way to derive tints, shades, and hover states from a token instead of hand-picking hex values. It keeps palettes consistent and themable.

## Details
- Mechanism: color-mix(in oklch, var(--primary) 70%, white) takes two color values and a percentage, interpolating in the named color space. The in <space> argument matters: oklch and lab interpolate perceptually evenly, while srgb interpolates through RGB channels with muddy midpoints.
- Concrete example: generating hover states as color-mix(in oklch, var(--accent) 85%, black) means every accent change propagates automatically; a dark-mode stylesheet can re-mix the same tokens against different base surfaces instead of redefining every hex.
- Failure modes: mixing in the wrong space produces gray or neon midpoints (srgb red-to-blue goes through purple-gray); percentages that do not sum to 100% are normalized, which surprises authors expecting overflow; older browsers ignore the declaration, so fall back to a solid token; and mixing colors from different color spaces is fine but the interpolation space dominates the result.
- Operational tradeoffs: color-mix reduces palette maintenance but makes the computed color less inspectable — the DevTools value is a resolved color, not the recipe. Keep the recipe in the token name (e.g. --surface-muted) and use it for derived states only, not for brand colors that must match a spec exactly.
- RSIS3/mykb relevance: the wiki's CSS tokens use color-mix for hover and focus rings so the dashboard theme stays consistent when the accent token changes between projects.
- Interpolation space choice: mix in oklch for perceptual evenness across hues, srgb for quick legacy tints; document the space per token group so a palette edit does not silently change midpoints.
- Fallback strategy: declare a plain token before the color-mix declaration so legacy engines get the base color; the enhanced mix is progressive, not required for correctness.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/contrast-ratios|Contrast Ratios]]
- [[wiki/web-platforms/color-blind-considerations|Color Blind Accessibility]]
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
