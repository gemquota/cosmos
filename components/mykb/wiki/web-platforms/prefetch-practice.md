---
type: "concept"
title: "Prefetch Practice"
description: "Fetching likely-next resources during idle time"
tags: ["performance", "loading", "html", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Prefetch Practice

## Summary

Prefetch downloads resources for a future navigation during idle time, trading bandwidth for perceived speed on the next page. It pays off on predictable paths and costs on speculative ones — measure before adopting.

## Details
- Mechanism: <link rel="prefetch" href="..."> or the Fetch API's priority: 'low' fetches at idle priority and stores in the HTTP cache; the next navigation reuses the bytes. It differs from preload (same-navigation, high priority) and from prerender (renders the next page).
- Concrete example: a docs site prefetches the next-article HTML and its critical CSS when the reader hovers the link (or via an IntersectionObserver near the bottom); the perceived next-page load drops because HTML+CSS are already cached.
- Failure modes: prefetching resources the next page will not use, wasting mobile data; large prefetches competing with current-page LCP under bandwidth constraints; prefetching authenticated pages into a shared cache (privacy leak); and prefetch of dynamic URLs that change server state — GET prefetches can trigger side effects.
- Operational tradeoffs: only prefetch with evidence (navigation analytics, hover intent); respect Save-Data and network conditions; keep prefetch lists short and versioned. Prerender is strictly more powerful but more expensive — reserve it for the top 1-2 predictable destinations.
- RSIS3/mykb relevance: the wiki prefetches the synthesis graph page's JSON when a user opens its card, an interaction pattern measured in dashboard telemetry before the loop scales it further.
- Save-Data and effective connection type: gate prefetch behind client hints or matchMedia('(prefers-reduced-data)') so metered users are not charged for speculative bytes.
- Cache semantics: prefetch populates the HTTP cache, so it also affects same-navigation later fetches; keep prefetch URLs immutable (hashed filenames) to avoid stale reuse.
- Privacy note: prefetching authenticated URLs can leak them into shared caches or trigger server state changes; restrict prefetch to public, idempotent GET resources.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]]
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]]
- [[wiki/web-platforms/priority-hints|Priority Hints]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
