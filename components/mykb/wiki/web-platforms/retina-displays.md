---
type: "concept"
title: "Retina Displays"
description: "High-density screens and what they mean for image assets"
tags: ["images", "density", "display", "responsive"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Retina Displays

## Summary

Retina-class displays run at 2x or 3x device pixel ratio, so 1x raster assets look soft. Serving appropriately dense images — via srcset, responsive APIs, or vector formats — keeps UI crisp without wasting bandwidth on every device.

## Details
- Mechanism: the display packs 2-3 physical pixels per CSS pixel; an 800px-wide image shown at 400 CSS px uses 800 device pixels when the DPR is 2, so the source must provide ~800px of detail. Browsers pick from srcset 1x/2x/3x candidates based on DPR; sizes decides which candidate's width applies.
- Concrete example: an avatar shown at 40px ships 40/80/120px candidates; a hero ships width-based candidates (srcset 800w 1600w + sizes="(min-width: 1200px) 1200px, 100vw") so a 2x phone gets exactly the detail it needs. Icons and logos as SVG or icon fonts scale losslessly.
- Failure modes: serving 2x everywhere (mobile data waste) or 1x everywhere (blurry on new phones); canvas/WebGL ignoring DPR and rendering soft text; background images in CSS without image-set() density variants; and CSS pixel vs device pixel confusion in analytics or layout code.
- Operational tradeoffs: density-aware delivery is mostly a srcset/sizes discipline plus vector assets for UI chrome; the memory cost of 3x raster layers is real on low-end devices, so cap sizes and prefer SVG. Verify by screenshotting at each DPR.
- RSIS3/mykb relevance: the wiki browser serves thumbnails through a density-aware srcset, and this node records the image pipeline rules the loop uses when adding new visuals.
- Verification: screenshot key views at 1x/2x/3x in DevTools and inspect edges; text rendered from a too-small canvas or a 1x background image is the regression that blends into daily review.
- Memory tradeoff: 3x raster layers cost 9x pixels; cap decorative raster backgrounds at 2x and use SVG for UI chrome so high-DPR devices do not pay a memory tax.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]]
- [[wiki/web-platforms/aspect-ratio-images|Aspect Ratio for Images]]
- [[wiki/web-platforms/srcset-practice|srcset in Practice]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
