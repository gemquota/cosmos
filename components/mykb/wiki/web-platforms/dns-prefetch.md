---
type: "concept"
title: "DNS Prefetch"
description: "Resolving hostnames early to cut navigation latency"
tags: ["performance", "dns", "network", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DNS Prefetch

## Summary

dns-prefetch resolves a hostname's DNS records ahead of need, removing one round trip from the critical path of future requests. It is the cheapest of the preconnect-family hints and safe to overuse.

## Details
- Mechanism: <link rel="dns-prefetch" href="https://api.example.com"> tells the browser to resolve that origin's DNS early, in idle time, before any request targets it. Unlike preconnect it opens no connection, so the cost is a DNS lookup the page may or may not use.
- Concrete example: a wiki page that loads images from assets.example.com and data from api.example.com adds dns-prefetch for both; when the user navigates or scrolls to lazy content, the lookup is already cached, saving a typical 20–50ms (or 100ms+ on cold caches).
- Failure modes: prefetching origins never used wastes a lookup but is cheap; the hint is a no-op in HTTP/2 environments where the browser already coalesces connections; it does nothing for origins already visited (DNS cached); and for the same-origin or preconnected hosts it is redundant — pick one hint per origin and let preconnect subsume DNS.
- Operational tradeoffs: dns-prefetch is strictly less powerful than preconnect (which also does TCP+TLS) but costs almost nothing, so use it liberally for known third-party origins, especially when they are not needed on first paint. Combine with preload only when the resource itself is critical.
- RSIS3/mykb relevance: the dashboard hints dns-prefetch for the rack API and wiki asset hosts so telemetry fetch latency excludes DNS on cold starts.
- Cost check: dns-prefetch is nearly free, but a prefetch of an origin that never loads still wastes a lookup; audit the hint list quarterly against actual network requests.
- Coalescing note: with HTTP/2, browsers reuse connections per origin, so dns-prefetch mainly pays for cold origins; skip the hint for origins already preconnected.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/priority-hints|Priority Hints]]
- [[wiki/web-platforms/speculative-loading|Speculative Loading]]
- [[wiki/web-platforms/link-rel-attributes|Link rel Attributes]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
