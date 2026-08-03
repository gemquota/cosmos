---
type: "concept"
title: "font-display: swap"
description: "Controlling how long text waits before fallback fonts render"
tags: ["fonts", "css", "performance", "typography"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# font-display: swap

## Summary

font-display: swap shows fallback text immediately and swaps to the web font when it loads, trading a flash of unstyled text (FOUT) for zero invisible text and better perceived performance. It is the default recommendation for body text.

## Details
- Mechanism: font-display controls the font loading timeline: block hides text up to a short block period, swap shows fallback then swaps, fallback shows fallback for a short period then sticks, optional shows fallback and never blocks. The @font-face descriptor applies per family.
- Concrete example: body text with font-display: swap renders in the fallback at first paint, so the LCP text is visible immediately; when the font arrives, the browser re-renders with real glyphs. Pairing with size-adjust fallback metrics keeps the swap from shifting layout.
- Failure modes: swap re-layouts text when the font lands, causing CLS unless fallback and web font have matching metrics (use size-adjust/ascender-override or a metric-compatible fallback); block on slow connections hides text for seconds; and display: swap on icon fonts that never load leaves missing glyphs — reserve space or subset them.
- Operational tradeoffs: swap maximizes perceived speed but accepts a metric shift; optional is best for decorative fonts where rendering without them is fine; block only for critical brand text. Self-host fonts and preload the primary one to shrink the swap window.
- RSIS3/mykb relevance: the dashboard uses swap with metric-compatible fallbacks so headline numbers never sit invisible while telemetry fonts load.
- FOIT vs FOUT policy: decide per family — swap for body text that must be readable immediately, optional for decorative faces, block only for brand-critical short strings; the same font-display value that hides text for 3s on a slow connection is a UX regression.
- Loading discipline: preload the primary face, subset aggressively, and keep font-display: swap so first paint never waits; the remaining swap shift is a CLS cost you budget explicitly.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/subsetting-fonts|Font Subsetting]]
- [[wiki/web-platforms/woff2|WOFF2 Format]]
- [[wiki/web-platforms/icon-fonts|Icon Fonts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
