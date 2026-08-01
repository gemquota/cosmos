---
type: "concept"
title: "Timeouts"
description: "Upper bounds on how long a call may take, preventing hung operations from consuming resources"
tags: ["timeouts", "reliability", "distributed-systems", "latency"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Timeouts

## Summary
Timeouts cap how long an operation may wait before failing. Every outbound call — HTTP, database, queue, or RPC — needs one so a slow peer cannot hang the caller indefinitely.

## Details
- Set connect, request, and total timeouts with margins below the consumer's own deadline.
- Propagate deadlines across call chains (gRPC deadlines, HTTP `timeout` params) so the whole path fails fast.
- Combine with retries and circuit breakers: timeouts trigger retries, circuit breakers stop the pattern when persistent.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — what happens after a timeout
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — stops repeated timeout waits
- [[wiki/api-protocols/grpc|gRPC]] — native deadline propagation
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — timeouts free pooled connections
- [[wiki/devops-infra/observability|Observability]] — timeout metrics expose latency
