---
type: "concept"
title: "Rate Limiting for APIs"
description: "Algorithms, headers, and client behavior for enforcing per-client request budgets"
tags: ["rate-limiting", "api", "reliability", "http", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429", "https://www.rfc-editor.org/rfc/rfc6585"]
---
# Rate Limiting for APIs

## Summary
Rate limiting caps how many requests a client may make in a window, protecting shared capacity from bursts, abuse, and cascading failures. Server-side, it is token buckets or sliding windows; client-side, it is honoring 429s, Retry-After, and backoff. Together they keep APIs healthy.

## Details
- **Algorithms** — fixed window is simple but bursty at boundaries; sliding window smooths it; token bucket allows controlled bursts; leaky bucket enforces a constant rate.
- **Headers** — RateLimit-Limit/Remaining/Reset (and Retry-After) make limits machine-readable so clients can adapt.
- **Client behavior** — on 429, back off by Retry-After, queue non-urgent work, and degrade gracefully instead of retrying hot.
- **Distributed limits** — Redis counters or edge quotas keep limits consistent across instances.
- **Worked example** — the mykb daemon rate-limits its wiki-writing workers per pass and retries with jittered backoff on 429s.
- **Relevance** — RSIS3's acquisition workers must budget source fetches; the wiki tracks algorithms and headers to keep quotas auditable.

## Related
- [[wiki/api-protocols/throttling-vs-debouncing|Throttling vs Debouncing]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-throttling|API Throttling]] — adjacent concept in this wiki
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — existing coverage
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — existing coverage
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]] — existing coverage
