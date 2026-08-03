---
type: "concept"
title: "API Throttling"
description: "Enforcing per-client call rates to protect capacity and shape traffic"
tags: ["api", "rate-limiting", "reliability", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Throttling

## Summary
Throttling caps how fast a client can call an API and applies a backoff contract (usually 429 plus Retry-After) when the cap is exceeded, protecting capacity and shaping client behavior.

## Details
Throttling (or rate limiting) bounds request volume per client identity — key, token, user, IP, or a combination — over a window. The two dominant algorithms are the token bucket (allows bursts up to a capacity, refills at a rate) and the sliding window (counts requests in the last N seconds). The HTTP contract is 429 Too Many Requests plus Retry-After, and often X-RateLimit-* headers so compliant clients can self-throttle before the 429.

The mechanism: a middleware reads the client identity from the auth header (never trust IP alone behind proxies), looks up the bucket or window counter in an in-memory or Redis store, increments or decrements, and either lets the request through or returns 429. Distributed limits need a shared store with atomic increments (Redis INCR plus EXPIRE or Lua) and careful clock handling; per-instance limits are simpler but uneven under load balancing.

Concrete example: a public wiki API allows 100 requests per minute per key with a burst of 20. A script that respects the headers paces itself at 95 per minute; a misbehaving crawler gets 429s with Retry-After: 30. When the service is under heavy load, an emergency throttle (for example 10 requests per minute) can be applied to non-essential consumers to protect core traffic — load shedding via throttle tiers.

Failure modes: counting only by IP behind a shared NAT blocks whole offices; per-key limits without auth fall back to IP and are trivially bypassed by rotating identity; counters that never expire accumulate stale state; and clients that ignore 429 and Retry-After escalate into bans. Off-by-one races in distributed counters either over-admit (no protection) or under-admit (false 429s), so limits should be enforced with atomic operations and verified with load tests.

Operational tradeoffs: strict throttling protects capacity and revenue but adds latency and support burden; generous limits reduce 429s but invite abuse. The practical design is tiered limits (free, paid, internal), documented retry semantics, and monitoring that separates "client exceeded limit" from "limit misconfigured." Throttling should be layered with authentication, since unauthenticated endpoints can only throttle coarsely.

RSIS3/mykb relevance: RSIS3 loops calling external model APIs must obey documented throttle tiers; encoding the Retry-After contract here keeps the loops' backoff logic aligned with provider limits.

## Related
- [[wiki/api-protocols/rate-limiting-api|Rate Limiting for APIs]]
- [[wiki/api-protocols/throttling-vs-debouncing|Throttling vs Debouncing]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]]
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]]
