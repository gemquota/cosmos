---
type: "concept"
title: "picture Element"
description: "Art-directed and format-variant responsive images"
tags: ["images", "responsive", "html", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# picture Element

## Summary

The <picture> element chooses among image sources by media query or format support, while <img srcset> chooses by density or width. Together they deliver art-directed, correctly-sized, next-generation-format images to every device.

## Details
- Mechanism: <picture> wraps <source> elements (with media, type, or srcset) and a fallback <img>; the browser picks the first matching source, otherwise the img's src. type="image/avif" lets browsers with AVIF support use it while others fall back to WebP/JPEG — without polyfill scripts.
- Concrete example: a hero image ships picture with source type=image/avif srcset 1600w, source type=image/webp 1600w, and img src JPEG + sizes; art direction swaps a landscape crop on wide screens for a square crop on narrow ones via media queries in the sources.
- Failure modes: forgetting sizes, so the browser guesses the image's display width; media queries in sources that never match, silently using the fallback; srcset widths that do not match real rendered sizes (wasted bytes or blur); and using picture where plain srcset would do — picture is for format/art-direction, srcset for resolution.
- Operational tradeoffs: picture adds markup weight but removes client-hint and preload guessing; it also complicates LCP preload, since the preload tag must match the chosen source. Generate sources in your asset pipeline and validate with real network throttling.
- RSIS3/mykb relevance: the wiki browser serves note thumbnails via picture with AVIF/WebP sources, keeping the OKF graph images light on slow connections.
- Preload interplay: to preload the picture's chosen candidate, replicate its media/type conditions on the link tag, or accept that the img loads without the preload boost.
- Test matrix: verify AVIF-unsupported browsers, no-JS crawlers (img fallback), and layout at each srcset width to catch broken candidates.
- Alt text: the fallback img carries the alt text and is the accessibility surface for every source; do not put accessible names on the sources, which are ignored by assistive tech.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/webp-vs-avif|WebP vs AVIF]]
- [[wiki/web-platforms/svg-scaling|SVG Scaling]]
- [[wiki/web-platforms/retina-displays|Retina Displays]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
