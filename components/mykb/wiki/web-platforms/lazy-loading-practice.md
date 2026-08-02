---
type: "concept"
title: "Lazy Loading in Practice"
description: "Deferring off-screen images, iframes, and code until needed, and knowing when not to"
tags: ["lazy-loading", "performance", "images", "javascript", "loading"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/lazy-loading", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img"]
---
# Lazy Loading in Practice

## Summary
Lazy loading defers resources until they are near the viewport or actually needed: native `loading="lazy"` for images and iframes, dynamic `import()` for code, and IntersectionObserver for custom cases. Done well it cuts initial bytes and main-thread work; done badly it hurts LCP and scroll stability.

## Details
- **Native attributes** — `loading="lazy"` on images/iframes is zero-JS; above-the-fold content should stay eager to protect LCP.
- **Code splitting** — dynamic imports split bundles; route-level splitting loads page code on navigation.
- **IntersectionObserver** — virtualized lists and infinite scroll trigger loading as items approach; reserve space to avoid CLS.
- **Anti-patterns** — lazy-loading hero images or fonts delays first paint; layout shift from late images needs width/height reservation.
- **Worked example** — the mykb wiki renders article lists with lazy images and imports the markdown renderer only when a reader opens an article.
- **Relevance** — RSIS3's data-heavy UIs should defer everything below the fold by default.

## Related
- [[wiki/web-platforms/render-blocking|Render Blocking]] — adjacent concept in this wiki
- [[wiki/web-platforms/preload-practice|Preload Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/prefetch-practice|Prefetch Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/api-protocols/http-caching|HTTP Caching]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
