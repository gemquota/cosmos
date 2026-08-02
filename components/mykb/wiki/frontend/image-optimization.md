---
type: "concept"
title: "Image Optimization"
description: "Formats, compression, dimensions, and encoding choices"
tags: [performance", "images", "optimization", "formats", "web"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/learn/images/", "https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types"]
---

# Image Optimization

## Summary
Image optimization delivers pictures at the right format, dimensions, and compression for each context. Modern formats such as WebP and AVIF beat legacy JPEG and PNG on size; resizing to display dimensions and recompressing removes most wasted bytes. Images typically dominate page weight, so this is usually the highest-return performance work.

## Details
- Formats: WebP and AVIF offer strong compression; SVG for vector and icons; PNG for transparency; JPEG for photos without alpha.
- Dimensions: serve images at or near rendered size; oversized originals waste bandwidth even when visually identical.
- Compression: quality settings, chroma subsampling, and metadata stripping; tools like squoosh and sharp automate it.
- Delivery: CDN image pipelines resize and re-encode on the fly from one source asset; srcset provides candidates per viewport.
- Painting: decoding="async" avoids decode jank; loading="lazy" defers offscreen; fetchpriority="high" boosts the LCP image.
- Layout: explicit width and height attributes reserve space and prevent CLS during decode.

## Related
- [[wiki/frontend/responsive-images|Responsive Images]] — selecting the right candidate
- [[wiki/frontend/lazy-loading|Lazy Loading]] — deferring image downloads
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — LCP is usually an image
- [[wiki/frontend/browser-caching|Browser Caching]] — cache-optimized image URLs
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]] — image pipeline hosting
- [[wiki/frontend/performance-budgets|Performance Budgets]] — image weight limits
