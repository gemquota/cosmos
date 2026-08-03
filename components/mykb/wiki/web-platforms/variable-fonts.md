---
type: "concept"
title: "Variable Fonts"
description: "Single font files exposing weight, width, and optical axes"
tags: ["fonts", "typography", "css", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Variable Fonts

## Summary

Variable fonts pack a family (weights, widths, italics, optical sizes) into one file with continuous axes, replacing dozens of static files and enabling real-time axis animation. They are the future of web typography — with subsetting and feature caveats.

## Details
- Mechanism: a variable font defines axes (wght 100-900, wdth, ital, opsz, plus custom axes) and the browser interpolates; CSS font-variation-settings (or the font-weight/width properties when mapped) selects axis values. One 100KB variable file can replace eight static weights totaling 500KB+.
- Concrete example: Inter Variable serves all weights from one file; a headline animates weight between 200-800 via CSS transitions on font-variation-settings; optical-size axes (opsz) automatically pick the right drawing for display vs body sizes when font-optical-sizing: auto is set.
- Failure modes: browsers without variable support need static font fallbacks (font-display + fallback stack); subsetting variable fonts requires keeping the axis tables intact or the file grows oddly; animating axes causes per-frame font rasterization (expensive — keep axis animations small); and some axes (ital, slnt) affect layout metrics.
- Operational tradeoffs: variable fonts cut weight and enable dynamic type at the cost of a slightly larger single file and the need for fallback strategy; check axis support (font-tech() in @supports) and provide static fallbacks for older WebViews.
- RSIS3/mykb relevance: the dashboard uses a variable font for its data labels and records the axis settings in this note so chart typography stays consistent.
- Design tokens: expose axes as CSS custom properties (--font-weight-strong, --font-optical) instead of raw variation values so type usage stays consistent and themeable.
- Testing: render a glyph coverage and axis sanity test at build time; missing axis tables or stripped subsets fail the font pipeline before shipping.
- Fallback testing: render key pages with the variable font blocked to verify the static fallback; the fallback is what legacy WebViews and reduced-motion users actually see.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/web-fonts|Web Fonts]]
- [[wiki/web-platforms/font-display-swap|font-display: swap]]
- [[wiki/web-platforms/subsetting-fonts|Font Subsetting]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
