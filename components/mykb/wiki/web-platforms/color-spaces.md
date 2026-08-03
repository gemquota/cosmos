---
type: "concept"
title: "CSS Color Spaces"
description: "sRGB, Display P3, and other color spaces in CSS"
tags: ["css", "color", "design", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Color Spaces

## Summary

Color spaces define the coordinate system colors are expressed in. Modern CSS moved from sRGB-only to wide-gamut spaces — display-p3, oklab, oklch — enabling richer screens and perceptually uniform manipulation.

## Details
- Mechanism: a color space maps coordinates to visible colors; sRGB covers ~35% of human-visible color, display-p3 ~45%, and cameras/screens increasingly ship p3. CSS now lets authors write lab(), lch(), oklab(), and oklch() values that the browser gamut-maps onto the display.
- Concrete example: an accent gradient written in oklch keeps even perceived steps between stops, while the same gradient in hex sRGB visibly band-steps in the midtones; using oklch for hue shifts (hue + 30deg) produces a consistent rotation instead of an unpredictable hex jump.
- Failure modes: assuming the display reproduces the gamut — a p3 color on an sRGB laptop is clipped or mapped, changing brand appearance; mixing legacy hex with wide-gamut colors creates inconsistent results across devices; and color spaces affect blending: gradients and color-mix interpolate per space, so the same endpoints look different in srgb vs oklch.
- Operational tradeoffs: authoring in oklch/oklab is a future-proof choice for generated colors (tints, harmonies, themes); brand-critical colors still need an sRGB fallback and a checked reference. Test on both wide and standard displays since gamut mapping differs by browser.
- RSIS3/mykb relevance: the dashboard theme tokens are stored in oklch with sRGB fallbacks, and the wiki documents the choice so future palette edits stay perceptually consistent.
- Gamut mapping: when a P3 color lands on an sRGB display, the browser clips or maps it; verify brand colors on both gamuts and keep the sRGB fallback first in the declaration order.
- Authoring default: write new color tokens in oklch with explicit sRGB fallbacks; the wide-gamut value expresses intent while the fallback preserves legacy behavior on standard displays.
- Wide-gamut assets: images can carry P3 via ICC profiles or AVIF/HEIC; tag exported images with their profile so the browser converts correctly, because untagged P3 files render washed out on sRGB displays, and screenshots or exports re-encoded to sRGB lose the vividness intent.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/color-mix|color-mix() CSS]]
- [[wiki/web-platforms/contrast-ratios|Contrast Ratios]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
