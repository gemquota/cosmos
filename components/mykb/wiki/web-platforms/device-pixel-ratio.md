---
type: "concept"
title: "Device Pixel Ratio"
description: "CSS pixels per physical pixel on a screen"
tags: ["density", "display", "responsive", "css"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Device Pixel Ratio

## Summary

Device pixel ratio (DPR) is the ratio of physical pixels to CSS pixels on a screen. It drives when to serve 2x/3x image assets and explains why text and layout metrics differ from raw hardware resolution.

## Details
- Mechanism: CSS pixels are the coordinate system for layout; a 375×667 CSS layout on an iPhone is rendered on 750×1334 or 1179×2556 physical pixels, so DPR is 2 or 3. The browser and GPU scale the composited page; assets need correspondingly more pixels to stay sharp.
- Concrete example: an image at 800px wide displayed at 400 CSS px looks crisp at DPR 2 only when served as 800px; srcset with 1x/2x/3x candidates plus sizes lets the browser choose by actual DPR and layout width. SVG and icon fonts scale losslessly and sidestep the problem entirely.
- Failure modes: serving only 1x assets makes UI blurry on high-DPR screens; serving 3x everywhere wastes bandwidth and decode time on low-DPR laptops; DPR varies with zoom and OS scaling, so fixed media queries on DPR are brittle; and using DPR to detect "mobile" is wrong — many phones sit at 2-3x but some desktop monitors do too.
- Operational tradeoffs: the correct fix is responsive images (srcset/sizes) plus vector assets, not manual DPR branches. Memory matters: 3x raster layers cost 9x pixels, so cap layers and prefer SVG for UI chrome. Canvas and WebGL must multiply backing-store size by DPR for crispness, then scale via CSS.
- RSIS3/mykb relevance: dashboard charts render to canvas at DPR-scaled resolution so telemetry stays sharp on Retina-class displays without blurring the axes and gridlines.
- Zoom interaction: browser zoom changes effective DPR from the renderer's perspective; test critical raster assets at 200% zoom to catch the softness that only appears on high-DPR + zoom.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/aspect-ratio-images|Aspect Ratio for Images]]
- [[wiki/web-platforms/srcset-practice|srcset in Practice]]
- [[wiki/web-platforms/sizes-attribute|sizes Attribute]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
