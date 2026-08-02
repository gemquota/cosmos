---
type: "concept"
title: "ETag Negotiation"
description: "Using entity tags to skip downloads of unchanged resources"
tags: ["etag", "http", "caching", "conditional-requests"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ETag Negotiation

## Summary
ETags are opaque validators for a resource version; clients send them in If-None-Match and servers reply 304 Not Modified when nothing changed. ETag negotiation cuts bandwidth by making conditional requests the norm.

## Details
- Strong ETags change on any byte; weak ones (W/) tolerate semantic equivalence.
- Generate ETags from content hashes for cheap correctness; random UUIDs break caching.
- Combine with Last-Modified and Cache-Control for layered freshness decisions.
- mykb relevance: wiki sync uses ETags so unchanged raw captures are not re-fetched.

## Related
- [[wiki/tooling/conditional-requests|Conditional Requests]]
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]]
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]]
- [[wiki/communities/checksums|Checksums]]
- [[wiki/compositions/sync-engines|Sync Engines]]
