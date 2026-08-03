---
type: "concept"
title: "Largest Contentful Paint"
description: "LCP: timing the largest visible content element"
tags: ["performance", "metrics", "core-web-vitals", "loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Largest Contentful Paint

## Summary

Largest Contentful Paint (LCP) marks when the page's largest content element becomes visible — the moment users feel the page is here. It is a Core Web Vital and is dominated by server response, render-blocking resources, and image loading.

## Details
- Mechanism: LCP reports the render time of the largest image, text block, or video poster in the viewport, updating as larger elements paint; the metric is the final LCP at p75. It cannot be reported for elements below the fold, so above-the-fold design directly drives the score.
- Concrete example: an article's hero image is the LCP element; making it load fast means compressing/WebP-AVIF, adding fetchpriority="high" + preload, and removing render-blocking CSS/JS in its way. If the LCP element is text, it wins or loses on server response time and font blocking.
- Failure modes: optimizing the wrong element (the largest isn't always the hero — a huge header can be the LCP); lazy-loading the hero; a slow server or TTFB eating most of the budget; redirect chains and uncached third-party fonts; and image decoding after download delaying the paint.
- Operational tradeoffs: the LCP budget (~2.5s) is spent across TTFB, resource loading, and rendering; every layer competes, so fix the biggest contributor first and re-measure in the field (CrUX) — lab and field often disagree on cache states.
- RSIS3/mykb relevance: the dashboard reports LCP per route from field data; when wiki pages regress, the loop attaches the performance trace and the largest-element selector to the improvement note.
- Element selection: the LCP element is whatever is largest in the viewport — a huge header or hero image; know which element wins per route before optimizing, or you may polish the wrong asset.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/cumulative-layout-shift|Cumulative Layout Shift]]
- [[wiki/web-platforms/cumulative-layout-shift|Cumulative Layout Shift]]
- [[wiki/web-platforms/font-shift|FOIT and Font Shift]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
