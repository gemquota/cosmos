---
type: "concept"
title: "HTTP Caching Directives"
description: "Cache-Control, Expires, and Vary semantics for shared and private caches"
tags: ["caching", "http", "headers", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# HTTP Caching Directives

## Summary
HTTP caching directives — Cache-Control, Expires, ETag, Vary — tell browsers and intermediate caches how long a response can be reused and when it must be revalidated. Correct directives turn repeated fetches into local cache hits; wrong ones serve stale content or defeat caching entirely.

## Details
- Cache-Control families: `max-age` (freshness window), `no-cache` (must revalidate before reuse), `no-store` (never cache — sensitive data), `private` (only the browser cache, not shared caches), `public` (shared caches allowed), `stale-while-revalidate` (serve stale while refreshing in background), `immutable` (never revalidate for stable assets).
- Mechanism: a response with `Cache-Control: max-age=3600` may be reused for an hour without contacting the origin; `no-cache` forces a conditional request (ETag/If-None-Match) that returns 304 when unchanged; `Vary: Accept-Encoding` keeps separate cached copies per encoding so a Brotli client never receives a gzip body.
- Concrete example: static assets use `Cache-Control: public, max-age=31536000, immutable` with hash-named URLs; API responses use `no-cache` plus ETag so every request revalidates cheaply; authenticated pages use `private, no-store`.
- Failure modes: `max-age` too long on mutable content (stale pricing, outdated security state); `no-store` on everything, destroying cache efficiency; missing `Vary` headers causing cross-user or cross-encoding cache poisoning; intermediate caches (CDN, corporate proxies) honoring or ignoring directives inconsistently; cache keys that ignore query parameters, serving wrong variants.
- Tradeoffs: aggressive caching improves latency and cuts origin load but widens the staleness window; revalidation keeps correctness at the cost of a round trip per request; the right policy is per-resource: immutable hashed assets, revalidating dynamic data, no-store for secrets.
- Operational notes: set directives at the origin or CDN consistently, test with curl and a CDN debug header, and monitor cache hit ratios per route.
- RSIS3 relevance: the dashboard's static bundle can be served immutable while live snapshot JSON uses no-cache revalidation — the directive choice directly controls how fresh RSIS3's telemetry appears.

## Related
- [[wiki/cloud-infra/http-protocols|HTTP Protocols]]
- [[wiki/devops-infra/build-caching-and-artifacts|Build Caching & Artifacts]]
- [[wiki/cloud-infra/http-2-multiplexing|HTTP/2 Multiplexing]]
- [[wiki/cloud-infra/http-3-0-rtt|HTTP/3 0-RTT]]
