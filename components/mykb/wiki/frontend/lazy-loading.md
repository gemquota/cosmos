---
type: "concept"
title: "Lazy Loading"
description: "Deferring images, iframes, and components until needed"
tags: [performance", "lazy-loading", "images", "javascript", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/browser-level-image-lazy-loading", "https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/loading"]
---

# Lazy Loading

## Summary
Lazy loading defers the download and render of resources until they are needed — usually when they scroll near the viewport. Images and iframes get the native loading="lazy" attribute, components and routes use dynamic import, and CSS content can defer with content-visibility. The goal is a smaller initial request set and faster first paint.

## Details
- Native images: loading="lazy" defers offscreen images; decoding="async" avoids decode blocking; always reserve dimensions to prevent CLS.
- Iframes: lazy iframes help embeds and ad frames; loading="lazy" works in all modern browsers.
- Dynamic import: import() and React lazy load route and component chunks on demand, cutting initial JavaScript.
- IntersectionObserver: custom lazy patterns (tabs, carousels) observe visibility instead of hammering scroll events.
- content-visibility: auto skips rendering offscreen sections while keeping them in the layout — a cheap CSS-level win.
- Trade-offs: lazy loading above-the-fold content hurts LCP, and aggressive lazy patterns delay images users actually need.

## Related
- [[wiki/frontend/responsive-images|Responsive Images]] — lazy loading pairs with srcset
- [[wiki/frontend/intersection-observer|Intersection Observer]] — the JS mechanism for lazy UIs
- [[wiki/frontend/code-splitting|Code Splitting]] — lazy loading for JavaScript
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — LCP and CLS implications
- [[wiki/frontend/image-optimization|Image Optimization]] — lighter images load faster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the umbrella topic
