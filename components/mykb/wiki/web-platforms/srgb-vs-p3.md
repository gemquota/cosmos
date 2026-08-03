---
type: "concept"
title: "sRGB vs Display P3"
description: "Wide-gamut color and browser support differences"
tags: ["css", "color", "display", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# sRGB vs Display P3

## Summary

sRGB is the web's default color space; Display-P3 covers ~45% of visible color vs sRGB's ~35%, and modern displays ship P3. Choosing between them determines how vivid colors are — and how they degrade on narrower displays.

## Details
- Mechanism: color values are interpreted in a space; sRGB is the compatibility baseline every browser handles; P3 (display-p3() in CSS, P3 in images via ICC profiles or AVIF/HEIC) reaches more saturated colors. The browser converts and gamut-maps between spaces depending on the display's actual gamut.
- Concrete example: a brand red #FF2D2D exists in both, but a vivid green or orange specified in P3 is impossible in sRGB — on an sRGB laptop it is clipped to the nearest representable color, shifting brand appearance; images in AVIF can carry P3 color and look richer on P3 screens, duller on sRGB ones.
- Failure modes: assuming the authoring monitor matches the audience (most office laptops are sRGB); color-mix and gradients interpolating in different spaces producing unexpected midpoints; screenshots and exports re-encoding P3 to sRGB and losing the intent; and testing only on wide-gamut hardware.
- Operational tradeoffs: author in oklch/oklab for generated colors and use P3 where vividness is the point, with sRGB fallbacks; for brand-critical color, pick values that survive gamut mapping, and verify on both gamuts. Wide-gamut support in CSS is broad by 2024+, but fallback ordering still matters.
- RSIS3/mykb relevance: the dashboard theme tokens specify sRGB fallbacks before oklch/P3 values, and the design note records the verified fallback pairs for brand accents.
- Display testing: verify on both a wide-gamut and a standard display; gamut mapping differences between browsers mean the same P3 color renders differently across engines.
- Asset pipeline: tag exported images with their color profile so the browser converts correctly; untagged P3 files render washed out on sRGB displays.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/color-mix|color-mix() CSS]]
- [[wiki/web-platforms/contrast-ratios|Contrast Ratios]]
- [[wiki/web-platforms/color-blind-considerations|Color Blind Accessibility]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
