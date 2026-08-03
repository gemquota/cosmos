---
type: "concept"
title: "Retry-After"
description: "The HTTP header and convention telling clients when to retry"
tags: ["retry-after", "http", "rate-limiting", "retry"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Retry-After

## Summary

Retry-After is the HTTP header (and rate-limit convention) that tells a client when it may retry: an HTTP date or a delay in seconds. Honoring it is what turns polite rate limiting into a working contract; ignoring it turns 429s into thundering herds.

## Details
- Mechanism: a server responds 429 (or 503) with Retry-After: 120 (seconds) or an HTTP-date; the client must wait at least that long before retrying; related headers (RateLimit-Limit/Remaining/Reset, X-RateLimit-*) give fuller state; the contract works when clients parse the header and back off, and fails when they retry on fixed timers or ignore it entirely.
- Concrete example: an API returning Retry-After: 30 under quota lets a well-behaved client resume exactly when the window resets; a client that ignores it and retries every second turns a minor 429 into a load spike and permanent blocking. The standard client pattern: honor Retry-After if present, else exponential backoff with jitter, and cap total retries.
- Failure modes: servers sending Retry-After without honoring it themselves (resets misaligned with the clock); clients with skewed clocks misreading HTTP-date values; retry storms when many clients share a backoff schedule (add jitter); and retrying non-idempotent requests (POST) without idempotency keys.
- Operational tradeoffs: Retry-After is cheap to emit and expensive to ignore; the discipline is standardizing the headers across services, testing client backoff behavior, and logging retry counts to detect contract violations.
- RSIS3/mykb relevance: the wiki's API clients honor Retry-After with jittered backoff, and this note records the header policy so loop-generated integrations behave under rate limits.
- Server side: emit Retry-After consistently from rate-limit middleware, keep the value aligned with the actual reset, and document the headers so clients can build compliant behavior.
- Client side: parse Retry-After robustly (seconds or date), cap wait at a sane maximum, and surface 429s in logs with the remaining-limit header so rate issues are visible before they become incidents.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]]
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/software-engineering/backoff-cap|Backoff Cap]]
