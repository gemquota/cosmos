---
type: "concept"
title: "Handling 429"
description: "Client and server behavior for HTTP Too Many Requests responses"
tags: ["http", "rate-limiting", "status-codes", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Handling 429

## Summary
429 Too Many Requests tells clients they are rate-limited and, with Retry-After, exactly when to retry. Correct client handling turns a hard failure into a schedule instead of a hammer.

## Details
The server returns 429 when a client exceeds an agreed limit — requests per second, per minute, per user, per IP, or per API key. RFC 6585 defines the code, and Retry-After (delta-seconds or HTTP-date) tells the client how long to wait. Well-designed APIs also return rate-limit headers (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset) so well-behaved clients can slow down before hitting the wall.

The mechanism on the client side: on 429, read Retry-After if present and wait that long; if absent, use exponential backoff with full jitter, capped at a maximum (commonly 30-60 seconds for interactive flows, minutes for batch jobs). Crucially, the retry must respect the same credential and scope, and concurrent retries must be coalesced — if ten in-flight requests all get 429, they should share one backoff rather than each waiting and then hammering the server together.

Concrete example: a batch job syncing wiki entries gets 429 after 100 requests. Retry-After says 30. The job parks the whole batch for 30 seconds, halves its concurrency, and resumes, avoiding the thundering herd that naive per-request retry would create. A UI client instead surfaces "slow down" and throttles input rather than blocking the main thread on sleep.

Failure modes: ignoring Retry-After and retrying immediately is the number one cause of limit escalation — servers often ban after repeated violations; treating 429 as terminal drops work that was merely delayed; sleeping longer than Retry-After wastes throughput; and distributed clients that don't share rate-limit state each burn their own budget against a global quota. Monitoring must distinguish 429s caused by user behavior from 429s caused by quota misconfiguration.

Operational tradeoffs: server-side, strict limits protect capacity but anger integrators, so providers pair 429 with generous documented limits and burst allowances. Client-side, honoring Retry-After trades latency for reliability; ignoring it trades reliability for raw throughput. Idempotency keys matter here — a retried request that actually landed server-side must not double-apply, which is why webhook and payment APIs pair 429 handling with idempotency.

RSIS3/mykb relevance: RSIS3 loops that call external LLM APIs during ideation must encode 429 plus Retry-After handling into their retry protocols; capturing the effective limits as wiki facts keeps the loops' backoff tuned.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/503-handling|Handling 503]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/504-handling|Handling 504]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
