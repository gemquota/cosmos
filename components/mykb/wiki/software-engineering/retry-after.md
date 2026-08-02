---
type: "concept"
title: "Retry-After"
description: "The HTTP header and convention telling clients when to retry"
tags: ["retry-after", "http", "rate-limiting", "retry"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Retry-After

## Summary
Retry-After tells a client when a resource will be available again — used with 429, 503, and 503-style responses. Honoring it is the polite and correct behavior when a server says it is throttled or down.

## Details
- Value is either an HTTP date or seconds; clients should wait at least that long.
- Servers that set it reduce retry storms; clients that ignore it cause them.
- Cap client patience: a huge Retry-After may mean the client should fail and surface the issue.
- mykb relevance: the fetcher honors Retry-After from source sites instead of guessing.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]]
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/software-engineering/backoff-cap|Backoff Cap]]
