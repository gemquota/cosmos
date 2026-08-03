---
type: "concept"
title: "sizes Attribute"
description: "Telling the browser rendered image widths for candidate selection"
tags: ["images", "responsive", "html", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# sizes Attribute

## Summary

The sizes attribute tells the browser how wide an image will render, so it can pick the right srcset candidate before download. It is the missing half of responsive images — srcset without sizes guesses, usually wrong.

## Details
- Mechanism: sizes="(min-width: 1200px) 60vw, 100vw" is a media-condition-to-width map evaluated against the current viewport; the browser picks the smallest srcset candidate whose listed width meets that resolved size at the device pixel ratio. It does not resize the image — CSS does that — it only informs candidate selection.
- Concrete example: a sidebar image rendered at 300px on desktop and full-width on mobile uses sizes="(min-width: 768px) 300px, 100vw" with srcset 400w 800w 1200w; a 2x phone picks the 1200w candidate, a 1x phone the 400w. Omitting sizes makes the browser assume 100vw and fetch oversized images on desktop.
- Failure modes: sizes not matching the real CSS width (wrong candidate, blurry or wasted bytes); media conditions overlapping or ordering wrong; forgetting that DPR multiplies the resolved width; and using sizes with fixed pixel values that do not update when layout changes (container queries need container-relative sizes support or JS).
- Operational tradeoffs: sizes adds markup but saves real bytes — the difference between downloading 200KB and 800KB on a phone; keep the conditions identical to the CSS breakpoints and verify the picked candidates in DevTools.
- RSIS3/mykb relevance: the wiki browser generates sizes/srccset per image from its layout tokens, so the same note image stays sharp at every panel width.
- DPR interplay: sizes resolves against CSS width, then the browser multiplies by DPR to pick candidates; re-check sizes when layout tokens change so a 2x phone stops downloading desktop-sized images.
- Container-query caveat: sizes evaluates against the viewport, not containers; container-relative image sizing still needs JS or container-query-aware tooling until the spec catches up.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/picture-element|picture Element]]
- [[wiki/web-platforms/webp-vs-avif|WebP vs AVIF]]
- [[wiki/web-platforms/svg-scaling|SVG Scaling]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
