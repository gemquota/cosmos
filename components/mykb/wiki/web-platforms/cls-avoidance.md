---
type: "concept"
title: "CLS Avoidance"
description: "Techniques that prevent unexpected layout shift"
tags: ["performance", "layout", "core-web-vitals", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CLS Avoidance

## Summary

Cumulative Layout Shift (CLS) measures how much the page moves after users start interacting. Avoiding it means reserving space for everything that loads late: images, embeds, fonts, ads, and async content.

## Details
- Mechanism: the browser scores layout shifts that occur without a recent user input, weighted by distance and affected area; CLS is the sum over the session. Because the window covers the whole session, a shift deep into a long read still counts.
- Concrete example: an article page without width/height on its hero image shifts the headline down when the image arrives; adding dimensions or an aspect-ratio box removes the shift, as does preloading the LCP image so it paints in its reserved slot.
- Main sources: images and iframes without dimensions, web fonts swapping metrics (FOIT/FOUT), injected content above existing content (ads, banners, cookie notices), and late animations that move layout rather than transform.
- Failure modes: fixing one source while introducing another — e.g. lazy-loading everything makes reserve slots uncertain; content-visibility can mask shifts by delaying rendering until scroll, which surfaces them later; and measuring only lab CLS misses field shifts from slow connections and runtime-injected widgets.
- Operational tradeoffs: reserving space can letterbox media or leave empty gaps; the goal is a defensible layout, not a gap-free one. Prioritize the biggest measured contributors, re-measure in the field, and keep layout animations to transform/opacity.
- RSIS3/mykb relevance: the dashboard tracks CLS from the Performance API as a rack pulse so regressions from new embeds trigger a loop-level warning rather than shipping silently.
- Budgeting: set a CLS budget (<0.1) and gate releases on field data; a budget makes layout stability a product requirement instead of an accident of whoever adds the next embed.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/font-shift|FOIT and Font Shift]]
- [[wiki/web-platforms/reserved-space|Reserving Layout Space]]
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
