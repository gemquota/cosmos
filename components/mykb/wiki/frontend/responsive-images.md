---
type: "concept"
title: "Responsive Images"
description: "srcset, sizes, and picture element selection"
tags: [images", "html", "responsive", "performance", "srcset"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images", "https://web.dev/learn/images/"]
---

# Responsive Images

## Summary
Responsive images serve different image files to different devices and contexts using srcset, sizes, and the picture element. The browser picks the candidate matching the rendered slot and device pixel ratio instead of downloading one oversized image. This cuts bandwidth dramatically on mobile while keeping sharpness on high-DPI screens.

## Details
- srcset with w descriptors: srcset="img-800.jpg 800w, img-1600.jpg 1600w" lists candidates by intrinsic width.
- sizes: sizes="(min-width: 900px) 50vw, 100vw" tells the browser the rendered slot, which drives candidate selection.
- Density descriptor: srcset="img-1x.jpg 1x, img-2x.jpg 2x" switches by device pixel ratio for fixed-size images.
- picture element: source media attributes enable art direction — cropping or a different aspect per breakpoint — and type for format fallbacks.
- Width and height: setting both attributes lets the browser reserve aspect-ratio space, preventing CLS during selection.
- LCP: give the hero image fetchpriority="high" and eager loading so candidate selection does not delay the largest contentful paint.

## Related
- [[wiki/frontend/image-optimization|Image Optimization]] — formats and compression behind candidates
- [[wiki/frontend/lazy-loading|Lazy Loading]] — deferring non-hero images
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — LCP and CLS effects
- [[wiki/frontend/responsive-design|Responsive Design]] — the layout context images adapt to
- [[wiki/frontend/mobile-first-design|Mobile-First Design]] — mobile bandwidth priorities
- [[wiki/web-platforms/web-apis|Web APIs]] — native image loading semantics
