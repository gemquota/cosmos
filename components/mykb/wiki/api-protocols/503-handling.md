---
type: "concept"
title: "Handling 503"
description: "Service Unavailable responses, maintenance windows, and overload signaling"
tags: ["http", "status-codes", "ops", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Handling 503

## Summary
503 Service Unavailable is an intentional signal that the service is temporarily unable to handle requests, often with Retry-After telling clients when to come back. It is the honest alternative to vague 500s during maintenance and overload.

## Details
503 Service Unavailable means the server is up but cannot serve right now: a deploy draining instances, a dependency (database, cache, upstream) down, capacity exhausted, or a circuit breaker open. Because it is a deliberate status, it should come with Retry-After (delta-seconds or HTTP-date) and often Cache-Control: no-store so clients and caches don't replay stale failures.

The mechanism differs from 500: a 500 means an unexpected internal error, while a 503 is an expected, often orchestrated condition. Load balancers and orchestrators use health checks to pull failing instances out of rotation and return 503 with a static maintenance body, and connection draining on shutdown makes in-flight requests finish while new ones get 503. Circuit breakers return 503 (or 429) for the open state so callers stop hammering a failing dependency.

Concrete example: during a rolling deploy, the orchestrator marks an instance unhealthy; the load balancer stops routing to it and briefly answers 503 for new connections until the replacement is ready. A client that honors Retry-After waits five seconds and retries, hitting the healthy pool. A misbehaving client that ignores it spins on 503s, keeping the balancer's error logs noisy and delaying recovery traffic.

Failure modes: returning 503 without Retry-After forces clients to guess backoff; returning 503 during routine overload instead of shedding load (429 or queuing) can make recovery slower; and monitoring that counts every 503 as an incident misses the point that 503 is often the system working as designed. Caches must not store 503 bodies, or users keep seeing "down for maintenance" after recovery.

Operational tradeoffs: 503 with Retry-After trades short-term unavailability for controlled recovery, while failing open (letting requests through degraded) risks cascading failures. Webhooks should treat 503 as retryable and respect Retry-After, and batch clients should pause the whole batch rather than hammering. Distinguishing "draining" 503s from "dependency down" 503s in logs is what makes the code actionable.

RSIS3/mykb relevance: RSIS3 check-practices runs can treat sustained 503 rates as a signal that an L1 loop's action produced overload; documenting the Retry-After contract makes those postmortems reproducible.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/504-handling|Handling 504]] — related coverage in the same cluster
- [[wiki/api-protocols/quota-headers|Quota Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
