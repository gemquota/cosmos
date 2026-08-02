---
type: "concept"
title: "Rate Limit Headers"
description: "Rate-limit response headers and Retry-After"
tags: ["rate-limiting", "headers", "http", "api-design", "429"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ietf.org/archive/id/draft-ietf-httpapi-ratelimit-headers-08.html", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After"]
---

# Rate Limit Headers

## Summary
Rate-limit headers tell clients how much budget remains and when they can retry: RateLimit-Limit, RateLimit-Remaining, RateLimit-Reset, and Retry-After. Without them, a 429 is a wall; with them, clients can pace themselves and back off intelligently.

## Details
- The IETF draft set: RateLimit-Limit (quota per window), RateLimit-Remaining (left in window), RateLimit-Reset (seconds or HTTP-date until reset).
- Retry-After: sent with 429 Too Many Requests or 503 Service Unavailable, giving seconds or a date — the authoritative retry hint.
- Legacy variants: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset (GitHub, Stripe) predate the standard; support both during transition.
- Granularity: limits may be per token, per IP, per endpoint, or global — document which policy the headers report.
- Preemptive pacing: clients should read remaining/limit and slow down before hitting 429, not only react after.
- Accuracy: headers must match the enforcement counter, or clients get confusing retry storms; test boundary behavior (limit-1, limit, limit+1).
- Errors: keep 429 responses structured and consistent (Problem Details), and never leak quota state for unauthenticated or internal consumers.

## Related
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — the counters behind the headers
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 429 and 503 carry Retry-After
- [[wiki/api-protocols/retry-policies|Retry Policies]] — clients honor reset times
- [[wiki/api-protocols/problem-details|Problem Details]] — structured 429 bodies
- [[wiki/api-protocols/api-analytics|API Analytics]] — limit exhaustion shows up in metrics
