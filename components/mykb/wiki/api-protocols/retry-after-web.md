---
type: "concept"
title: "Retry-After"
description: "HTTP header telling clients when a temporarily unavailable resource may be retried"
tags: ["http", "retry", "headers", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Retry-After

## Summary
Retry-After is the HTTP header a server uses to tell clients when it expects to be available again, whether the response is a 429 Too Many Requests, a 503 Service Unavailable, or a 301/302 redirect during maintenance. Honoring it is the difference between a graceful recovery and a thundering herd that makes an outage worse.

## Details
- Mechanism: Retry-After carries either an HTTP-date (for example, `Wed, 21 Oct 2026 07:28:00 GMT`) or a non-negative integer counting seconds from receipt (`Retry-After: 120`). It is defined for 503 in RFC 9110 and is conventionally honored by clients on 429 and 3xx responses as well. Intermediaries, including CDNs and reverse proxies, may also inject or rewrite it, so clients cannot assume the value came from the origin.
- Concrete examples: a rate-limited API returns `429` with `Retry-After: 30` so a queue worker backs off for half a minute instead of hammering; a service doing a rolling deploy returns `503` with a date pointing at the end of the maintenance window; a scheduler that scrapes a job endpoint on a fixed cadence reads the header to skip the next few runs instead of retrying immediately.
- Failure modes: ignoring the header is the classic mistake — every client retries at its own interval, the server stays saturated, and the recovery is delayed (the thundering herd problem). Clients that blindly clamp the value to a short maximum can also misfire: if the server says 3600 and the client retries in 60 seconds, the server must handle the surge anyway. Conversely, servers that emit absurd values (hours or days) break interactive flows where users expect near-immediate retries; the header is a hint with a defined format but no defined ceiling.
- Operational tradeoffs: from the server side, emit Retry-After only when you can actually predict recovery, prefer delay-seconds over dates because they are immune to clock skew between server and client, and combine it with `Retry-After`-aware load shedding so the queue drains during the wait. From the client side, treat the header as the primary backoff input, still cap it with an application-level maximum, add jitter so synchronized clients do not all wake at the same instant, and log when the server's suggested delay is absurdly long so ops can investigate.
- RSIS3/mykb relevance: RSIS3 loop workers that poll the MyKB daemon or telemetry endpoints should honor Retry-After so a degraded storage layer recovers instead of being flooded; encoding the header value into checkpoint state also lets a restarted session resume the same backoff schedule.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/429-handling|Handling 429]] — related coverage in the same cluster
- [[wiki/api-protocols/503-handling|Handling 503]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
