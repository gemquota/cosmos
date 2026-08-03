---
type: "concept"
title: "SVG Scaling"
description: "Keeping vector graphics crisp across sizes and densities"
tags: ["svg", "images", "responsive", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SVG Scaling

## Summary

SVG scales crisply at any size when its viewBox, width/height, and preserveAspectRatio are set deliberately. The recurring bugs — blurry, stretched, or wrong-size SVGs — are almost always missing or mismatched geometry attributes.

## Details
- Mechanism: viewBox defines the coordinate system (e.g. 0 0 24 24); width/height (or CSS) set the rendered size; preserveAspectRatio controls how the two reconcile (meet keeps aspect ratio and letterboxes, slice crops, none stretches). With viewBox present, the SVG scales its internal coordinates to the rendered box automatically.
- Concrete example: an icon with viewBox="0 0 24 24" and width="48" height="48" scales cleanly; the same SVG without viewBox but with CSS width: 100% collapses or overflows unpredictably. A logo that must crop (not letterbox) inside a fixed box uses preserveAspectRatio="xMidYMid slice".
- Failure modes: missing viewBox makes the SVG unresponsive to CSS sizing; width/height attributes conflicting with CSS (attributes are presentational, CSS wins); text inside SVG scaling with font-size rather than the viewBox transform; and raster-like blur when the SVG is rendered as a background without explicit dimensions.
- Operational tradeoffs: inline SVG gives full control (it inherits CSS sizing); <img> SVG needs explicit dimensions or it defaults oddly in some engines. Prefer a viewBox-based workflow, generate assets with consistent coordinate systems, and verify at multiple rendered sizes.
- RSIS3/mykb relevance: the OKF graph icons and dashboard diagrams define viewBoxes and scale via CSS tokens; this note pins the geometry rules for loop-generated vector assets.
- Fallback sizing: when SVG must render as an img background, give the box explicit dimensions; intrinsic-ratio behavior differs across engines once the SVG is detached from the document flow.
- ViewBox discipline: always declare viewBox with the intended coordinate system and let CSS control rendered size; relying on width/height attributes alone breaks when styles override them.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/retina-displays|Retina Displays]]
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]]
- [[wiki/web-platforms/aspect-ratio-images|Aspect Ratio for Images]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
