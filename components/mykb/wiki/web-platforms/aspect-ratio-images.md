---
type: "concept"
title: "Aspect Ratio for Images"
description: "Using width and height attributes to reserve image space"
tags: ["images", "layout", "performance", "html"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Aspect Ratio for Images

## Summary

Declaring image dimensions — via width and height attributes or CSS — lets the browser reserve the correct aspect ratio before the image downloads, preventing layout shift. It is a cheap, high-impact performance practice.

## Details
- Mechanism: modern browsers use the intrinsic ratio of width and height attributes to compute the aspect-ratio box, even after CSS overrides the size; aspect-ratio then fills in until the image arrives. The attributes act as hints, not hard constraints, so responsive images still work.
- Concrete example: <img src="photo.jpg" width="1600" height="900" alt="..."> with CSS max-width: 100% keeps the 16:9 box at every viewport width; without the attributes the browser only knows the ratio after download, so paragraphs below shift down when the image loads.
- Where this matters most: images above the fold, hero images, and any image near interactive controls. Below-the-fold images still matter because users scroll faster than slow connections deliver bytes.
- Failure modes: wrong attributes cause distorted letterboxing rather than layout shift — the browser trusts the declared ratio; omitting one attribute defeats the mechanism entirely; and switching from a ratio-changing srcset (different crops per breakpoint) requires updating attributes to match each candidate.
- Operational tradeoffs: attributes are zero-cost hints and should be the default; for truly unknown ratios (user uploads) reserve space with aspect-ratio CSS or a placeholder box instead of guessing.
- RSIS3/mykb relevance: the wiki browser's thumbnail grids declare dimensions so the OKF graph and search result lists stay stable during image hydration, keeping measured CLS near zero on the dashboard telemetry.
- Source switching: when srcset swaps crops with different ratios per breakpoint, the width/height attributes must match each candidate or letterboxing appears; keep ratio-consistent crops to avoid the mismatch.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/srcset-practice|srcset in Practice]]
- [[wiki/web-platforms/sizes-attribute|sizes Attribute]]
- [[wiki/web-platforms/picture-element|picture Element]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
