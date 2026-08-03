---
type: "concept"
title: "srcset in Practice"
description: "Serving density- and width-matched image candidates"
tags: ["images", "responsive", "html", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# srcset in Practice

## Summary

srcset offers the browser multiple image candidates by width (400w 800w) or density (1x 2x), letting it choose the right download for the viewport and DPR. It is the standard mechanism for responsive images — when paired with sizes.

## Details
- Mechanism: width descriptors (srcset="a.jpg 400w, b.jpg 800w") plus sizes tell the browser candidate widths; it picks the smallest candidate ≥ the resolved CSS width × DPR. Density descriptors (1x 2x) are a simpler mode for fixed-size images. The browser may also consider bandwidth (Save-Data) and connection quality.
- Concrete example: srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1600.jpg 1600w" sizes="(min-width: 900px) 800px, 100vw" delivers 400px on a narrow phone and 1600px on a 2x desktop — the right bytes for each case. Without sizes the browser defaults to 100vw and over-fetches on desktop.
- Failure modes: candidates whose widths do not match real rendered sizes; files that are not actually resized (same image renamed — the browser cannot tell and wastes bytes); missing 2x variants causing soft text in images; and srcset combined with preload needing matching sizes for the hint to work.
- Operational tradeoffs: srcset is declarative and cheap, but authoring candidates requires a build pipeline (resize + rename) and intentional sizes per breakpoint; the payoff is major mobile data savings. Verify the actual download per viewport in DevTools.
- RSIS3/mykb relevance: the wiki image pipeline generates width-bucketed candidates automatically; this note documents the bucket list the loop uses when adding new visual assets.
- Candidate hygiene: verify each srcset file is actually resized (a renamed 1600px file advertised as 400w wastes exactly the bytes it was meant to save); add an image-pipeline check that enforces dimensions.
- Save-Data behavior: browsers may choose smaller candidates under data-saving modes; verify the chosen candidate with network conditions simulated, since the browser decides, not you.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/sizes-attribute|sizes Attribute]]
- [[wiki/web-platforms/picture-element|picture Element]]
- [[wiki/web-platforms/webp-vs-avif|WebP vs AVIF]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
