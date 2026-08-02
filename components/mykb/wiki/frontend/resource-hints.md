---
type: "concept"
title: "Resource Hints"
description: "preload, prefetch, preconnect, and dns-prefetch"
tags: [performance", "resource-hints", "preload", "prefetch", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload", "https://www.w3.org/TR/resource-hints/"]
---

# Resource Hints

## Summary
Resource hints tell the browser about connections and resources ahead of time. preload fetches critical assets early, prefetch warms future-navigation resources, preconnect opens cross-origin connections, and dns-prefetch resolves hostnames. Used precisely, they shave network latency; used carelessly, they waste bandwidth.

## Details
- preload: <link rel="preload" as="image" href="hero.webp"> starts the download immediately and raises its priority; needs as and crossorigin attributes for fonts.
- prefetch: fetches low-priority resources for the next navigation, such as route chunks; wasteful if never used.
- modulepreload: preloads ES module dependencies ahead of execution, useful for critical import graphs.
- preconnect: opens DNS, TCP, and TLS to origins the page will fetch from — font hosts and CDNs are prime candidates.
- dns-prefetch: resolves DNS only, the lightest hint, typically paired before preconnect as a fallback.
- Pitfalls: preloading too much competes with real content; measure the difference before keeping hints in production.

## Related
- [[wiki/frontend/render-blocking-resources|Render-Blocking Resources]] — what hints prioritize
- [[wiki/frontend/critical-css|Critical CSS]] — preloading the styles that matter
- [[wiki/frontend/browser-caching|Browser Caching]] — hints interact with cached responses
- [[wiki/frontend/lazy-loading|Lazy Loading]] — the opposite deferral strategy
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the discipline
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — latency effects of hints
