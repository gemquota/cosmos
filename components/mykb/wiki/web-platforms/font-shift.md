---
type: "concept"
title: "FOIT and Font Shift"
description: "Layout jank caused by webfont loading and swapping"
tags: ["fonts", "performance", "layout", "core-web-vitals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# FOIT and Font Shift

## Summary

Font shift (often conflated with CLS) is the layout movement caused when a web font swaps in with different metrics than the fallback. Controlling it means matching fallback metrics or accepting a bounded, deliberate swap.

## Details
- Mechanism: while a font loads, text renders in the fallback; when the web font arrives, lines re-measure — widths, heights, and line breaks change, shifting everything below. font-display: swap makes the timing predictable (fallback first, swap on load) but the shift is a function of metric difference, not of font-display.
- Concrete example: body text falling back to Times New Roman then swapping to a wider Inter is visibly wider and taller before the swap, reflowing the whole article; using a metric-compatible fallback (Arial with size-adjust) keeps line positions nearly identical, dropping shift to a few pixels.
- Failure modes: measuring CLS in lab with fonts already cached (no swap visible) while real users see it; loading a large font late so the swap happens mid-reading; per-page font subsets with different metrics causing inconsistent reflow; and swapping fonts on hover/theme change, which re-triggers measurement.
- Operational tradeoffs: the robust combo is font-display: swap + @font-face size-adjust/override metrics matched to the fallback; self-hosting and preloading shrink the swap window; alternatively accept FOUT as a feature for non-critical text. Budget the swap shift as part of your CLS budget and re-measure in the field.
- RSIS3/mykb relevance: dashboard headline numbers use metric-overridden fallbacks so the LCP text does not move when the telemetry font loads.
- Swap timing: preload the primary font so the swap happens early, before the user reads the paragraph; a swap after reading starts is a visible reflow even when metrics match.
- Measurement: quantify swap shift in the CLS lab test with the web font throttled; the number tells you whether metric matching is needed.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/reserved-space|Reserving Layout Space]]
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]]
- [[wiki/web-platforms/frame-budget|Frame Budget]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
