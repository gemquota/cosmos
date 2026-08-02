---
type: "concept"
title: "Intersection Observer"
description: "Callbacks when elements enter or leave the viewport"
tags: [intersection-observer", "javascript", "performance", "web-apis", "lazy-loading"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API", "https://www.w3.org/TR/intersection-observer/"]
---

# Intersection Observer

## Summary
IntersectionObserver fires callbacks when an element enters or leaves the viewport (or any scroll container). It replaces scroll-position math with an asynchronous, browser-optimized notification, making lazy loading, infinite scroll, entrance animations, and ad tracking cheap and reliable.

## Details
- Setup: new IntersectionObserver(callback, {root, rootMargin, threshold}) observes targets for intersection changes.
- Thresholds: 0 fires at first pixel crossing; 1.0 at fully visible; arrays allow progressive triggers.
- rootMargin: expands or shrinks the effective viewport, enabling pre-loading just before an element appears.
- Batched: callbacks run asynchronously after layout, one batch per frame — no per-scroll handler cost.
- Use cases: loading="lazy" equivalents for custom components, scrollspy, counting views, and pause-offscreen video.
- Caveats: intersection alone cannot measure position or velocity; pair with scroll events when those are required.

## Related
- [[wiki/frontend/lazy-loading|Lazy Loading]] — the most common application
- [[wiki/frontend/debouncing-throttling|Debouncing and Throttling]] — the scroll-handler alternative
- [[wiki/frontend/animation-performance|Animation Performance]] — scroll-triggered motion
- [[wiki/web-platforms/web-apis|Web APIs]] — the API family it belongs to
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — deferral without CLS
- [[wiki/frontend/image-optimization|Image Optimization]] — deferred image loading
