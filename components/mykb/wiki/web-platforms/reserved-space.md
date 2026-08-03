---
type: "concept"
title: "Reserving Layout Space"
description: "Holding dimensions for images and ads to prevent shift"
tags: ["layout", "performance", "images", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Reserving Layout Space

## Summary

Reserved space means allocating layout room before content loads — image dimensions, aspect-ratio boxes, font metric matches, and ad/embed slots. It is the direct, mechanical fix for cumulative layout shift and the foundation of stable pages.

## Details
- Mechanism: reserve space at parse time (width/height attributes, aspect-ratio, min-height) so the document's geometry is correct before late resources arrive; when content loads or swaps, nothing below moves. The browser uses attributes' intrinsic ratio to compute the box even while the image is still downloading.
- Concrete example: a news feed gives every card's image width/height (or aspect-ratio) so ads, embeds, and lazy images loading in any order do not reflow the list; an iframe embed gets an aspect-ratio wrapper matching its 16:9 player, and a font with size-adjust matches fallback metrics so text swaps in place.
- Failure modes: reserving space with wrong ratios (letterboxing or overflow); reserving for elements that never load (empty gaps); fixed heights that break at large text sizes (reserve min-height, not height); and reserving only above the fold while below-fold shifts still hurt the CLS session total.
- Operational tradeoffs: reserved space costs a little whitespace and requires knowing dimensions in advance — unknown-size content (user uploads, ads) needs measured median sizes or placeholders. The trade is universally worth it: reserve first, then optimize loading.
- RSIS3/mykb relevance: the dashboard reserves chart canvas and embed slots before rack data arrives, keeping telemetry panels stable; this note is the canonical reference for new embeds.
- Unknown-size content: for user uploads and ads with unpredictable dimensions, reserve a measured median box or a placeholder ratio, then let the real content replace it without reflowing neighbors.
- Font metric matching: use @font-face size-adjust and overrides so fallback and web font share metrics; this removes the swap shift that reserved image space cannot fix.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]]
- [[wiki/web-platforms/frame-budget|Frame Budget]]
- [[wiki/web-platforms/input-latency|Input Latency]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
