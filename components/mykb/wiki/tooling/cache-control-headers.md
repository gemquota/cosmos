---
type: "concept"
title: "Cache-Control Headers"
description: "HTTP headers that tell caches how long and how aggressively to store responses"
tags: ["cache-control", "http", "caching", "headers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cache-Control Headers

## Summary
Cache-Control is the HTTP header contract with every cache in the path — browser, CDN, proxy — stating max-age, revalidation policy, and who may store the response. Correct values prevent both stale content and cache misses.

## Details
- max-age, s-maxage, no-cache (revalidate before use), no-store (never persist), private vs public.
- no-cache does not mean no caching: it means revalidate — a common confusion.
- Versioned assets (content-hash URLs) get long max-age; HTML gets short or no-cache.
- mykb relevance: the wiki serves immutable article hashes with long max-age.

## Related
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/tooling/conditional-requests|Conditional Requests]]
- [[wiki/tooling/cdn-practice|CDN Practice]]
- [[wiki/api-protocols/http-caching|HTTP Caching]]
- [[wiki/tooling/ttl-caches|TTL Caches]]
