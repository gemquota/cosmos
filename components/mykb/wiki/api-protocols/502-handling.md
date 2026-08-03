---
type: "concept"
title: "Handling 502"
description: "Bad Gateway responses and debugging upstream failures behind proxies"
tags: ["http", "status-codes", "proxies", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Handling 502

## Summary
502 Bad Gateway means an upstream server sent an invalid response to a gateway or proxy. It is a symptom, not a cause, and handling it well means classifying, retrying carefully, and surfacing the upstream that failed.

## Details
A 502 Bad Gateway is produced by a gateway, reverse proxy, load balancer, or API gateway when the upstream it contacted returned something unusable — an empty response, a malformed response, a connection that died mid-transfer, or a protocol violation. The gateway itself is usually healthy; the upstream is not. Contrast with 504, where the upstream simply did not answer in time.

The mechanism: the proxy opens a connection to the upstream (or reuses one from the pool), sends the request, and waits. If the connection resets, the TLS handshake fails, or the response headers are garbage, the proxy aborts and synthesizes 502, typically logging the upstream host, error reason, and request id. Some proxies retry idempotent requests on a different upstream before returning 502, which is why a single failure can be invisible to clients until the retry also fails.

Concrete example: an API gateway fronts three app instances; one instance crashes and its pool connections are stale. Requests routed to it get "connection reset by peer" and the gateway retries on a healthy instance, so clients see success. When all instances die, the gateway returns 502 with an empty body. Client-side, 502 is usually worth one careful retry with backoff, because transient upstream restarts and deploy churn are common.

Failure modes: naive client retry storms amplify an upstream outage into a gateway outage — the proxy's retry budget and connection pools saturate; a 502 from a misconfigured proxy hides whether the problem is DNS, TLS, or the app; and cached 502s can lock users out of a recovering service. Treating 502 as retryable when the request is idempotent, but terminal for non-idempotent writes, is the standard split.

Operational tradeoffs: enabling proxy retries adds latency and can double-execute non-idempotent requests, so only retry safe methods; disabling retries exposes every blip to clients. Proxies should emit structured logs with the upstream host and error code, and gateways should map 502 to their own error envelope with a trace id so support can correlate. Health checks and connection draining prevent most 502s by keeping dead instances out of the pool.

RSIS3/mykb relevance: the dashboard's telemetry views treat 5xx clusters as L1 loop inputs; documenting which upstream generates 502s turns raw error rates into actionable failure-mode notes.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/504-handling|Handling 504]]
- [[wiki/api-protocols/quota-headers|Quota Headers]]
- [[wiki/api-protocols/retry-after-web|Retry-After]]
- [[wiki/api-protocols/429-handling|Handling 429]]
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/error-contract-design|Error Contract Design]]
