---
type: "concept"
title: "Preconnect Practice"
description: "Opening early connections to origins that will be used"
tags: ["performance", "loading", "network", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Preconnect Practice

## Summary

preconnect opens early connections (DNS + TCP + TLS) to origins the page will use, cutting round trips before the first request. It is a strong hint for critical third-party origins but costs resources for every connection opened.

## Details
- Mechanism: <link rel="preconnect" href="https://api.example.com"> starts DNS, TCP, and TLS handshakes in idle time; the browser keeps the connection warm for the first real request. It subsumes dns-prefetch, so use one hint per origin — preconnect where the origin is critical, dns-prefetch elsewhere.
- Concrete example: a page calling api.example.com on load adds preconnect and saves one full RTT (often 50–150ms on TLS); the wiki dashboard preconnects to its rack API and font CDN so first telemetry render is not connection-bound.
- Failure modes: preconnecting origins never used, wasting connections on mobile radios; more than 4-6 preconnects, which browsers start ignoring; preconnect without crossorigin on CORS-fetched fonts failing to share the connection; and preconnecting on slow first visits where handshakes compete with the document itself.
- Operational tradeoffs: preconnect is strongest for origins hit early in the critical path; measure with the DevTools connection timing to confirm savings, and prefer self-hosting when the cost of third-party handshakes dominates.
- RSIS3/mykb relevance: the dashboard preconnects to exactly two origins (rack API, fonts); the hint list is versioned in this note so the loop does not grow it casually.
- Cross-origin fetch nuance: fetches with CORS mode need crossorigin on the preconnect link, otherwise the early connection is not reused; match the mode the request actually uses.
- Server timing: confirm preconnect value with the DevTools connection timing view per origin; a hint that shows zero saved RTTs is a candidate for removal.
- Server-timing check: compare RTT with and without the hint in the connection view; a preconnect that saves nothing is a sign the origin is already warm or the hint targets the wrong host.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]]
- [[wiki/web-platforms/priority-hints|Priority Hints]]
- [[wiki/web-platforms/speculative-loading|Speculative Loading]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
