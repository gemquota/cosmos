---
type: "concept"
title: "Cumulative Layout Shift"
description: "CLS: quantifying unexpected visible layout movement"
tags: ["performance", "metrics", "core-web-vitals", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cumulative Layout Shift

## Summary

Cumulative Layout Shift (CLS) scores unexpected movement of visible content during a page's lifetime. It is a Core Web Vital because shifting pages are disorienting and cause mis-clicks, especially on mobile.

## Details
- Mechanism: each shift without a recent user gesture scores impact fraction (how much viewport moved) times distance fraction; CLS sums these. Recent-input windows (e.g. typing) suppress shifts, which is why injected banners or late images after interaction still count.
- Concrete example: a news page inserting an ad above the article after load scores high CLS, while the same ad in a reserved slot scores zero. Product pages that load review widgets below the fold but before scroll still shift, so reserve space for every async insertion.
- Main causes: media without dimensions, font metric swaps, injected above-the-fold content, and layout-changing animations. Each maps to a fix: aspect-ratio/width-height, font-display and metric-compatible fallbacks, reserved slots, and transform/opacity-only motion.
- Failure modes: optimizing for lab CLS while field conditions differ (slow networks load later, LCP images swap dimensions); lazy-loading everything without reserved sizes; and measuring only the landing viewport — CLS accumulates for the whole session, including scrolled sections.
- Operational tradeoffs: reserving space is cheap and mostly invisible; letterboxing is the main aesthetic cost. Budget CLS < 0.1, monitor via field data (CrUX), and treat any regression as a release-blocking defect for content-heavy pages.
- RSIS3/mykb relevance: the dashboard reports CLS from real sessions into rack telemetry so layout regressions from new wiki embeds trigger the improvement loop automatically.
- Interaction windows: shifts after a user gesture are discounted, so late-arriving ads below a clicked button can still score; reserve space everywhere async content can land, not just above the fold.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/cls-avoidance|CLS Avoidance]]
- [[wiki/web-platforms/font-shift|FOIT and Font Shift]]
- [[wiki/web-platforms/reserved-space|Reserving Layout Space]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
