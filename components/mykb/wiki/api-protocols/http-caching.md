---
type: "concept"
title: "HTTP Caching"
description: "Storing and reusing HTTP responses via Cache-Control, ETags, and validators to cut latency and bandwidth"
tags: ["http", "caching", "performance", "rest", "web-platforms"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://httpwg.org/specs/rfc9111.html"]
---

# HTTP Caching

## Summary
HTTP caching lets intermediaries and clients store responses and reuse them for identical requests, governed by explicit freshness and validation rules. RFC 9111 defines how caches decide what is stored, how long it stays fresh, and when to revalidate. Correct caching is one of the cheapest performance wins for read-heavy APIs and static frontends.

## Details
- `Cache-Control` directives drive behavior: `max-age`, `s-maxage`, `no-store`, `no-cache`, `public`, and `private`.
- Validators: `ETag` (opaque token) and `Last-Modified` enable conditional requests — `If-None-Match` returns 304 Not Modified when content is unchanged.
- Cache tiers: browser caches, CDN edge caches, and reverse proxies (Nginx, Caddy, Cloudflare) each honor freshness headers differently.
- `Vary` matters when representations depend on headers such as `Accept-Encoding` or `Accept-Language`.
- REST fit: GET responses are naturally cacheable; unsafe methods (POST/PUT/DELETE) must invalidate affected URLs.
- Worked example: a mykb search endpoint returning identical results for identical queries can set `max-age=60`, cutting dashboard load and daemon backpressure.
- Pitfalls: over-caching stale auth data (set `private, no-store` on personalized responses) and cache-key collisions when query parameters are ignored.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — cacheable GET semantics are core to REST
- [[wiki/frontend/static-site-generation|Static Site Generation]] — pre-rendered HTML is trivially cacheable
- [[wiki/devops-infra/nginx|Nginx]] — reverse-proxy caching layer
- [[wiki/frontend/edge-functions|Edge Functions]] — caching at the network edge
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — complementary traffic control mechanisms
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — indexing pipelines benefit from cached lookups
- [[wiki/ops/gap-report|Gap Analysis Report]] — performance gaps noted for the daemon
- [[wiki/devops-infra/cloudflare|Cloudflare]] — edge caching on a global CDN
