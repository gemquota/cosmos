---
type: "concept"
title: "Conditional Requests"
description: "HTTP requests that only transfer content when a validator shows a change"
tags: ["conditional-requests", "http", "caching", "bandwidth"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Conditional Requests

## Summary
Conditional requests carry validators — If-None-Match, If-Modified-Since — so servers answer 304 without the body when nothing changed. They are how clients and caches avoid paying for content they already have.

## Details
- If-None-Match pairs with ETags; If-Modified-Since pairs with Last-Modified (weaker).
- Validators cover more than GET: If-Match prevents overwriting concurrent edits.
- A 304 still costs a round trip — validators save bandwidth, not latency.
- mykb relevance: the wiki sync client issues conditional requests for every capture.

## Related
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]]
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/compositions/sync-engines|Sync Engines]]
