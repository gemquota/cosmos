---
type: "concept"
title: "Timeouts"
description: "Upper bounds on how long a call may take, preventing hung operations from consuming resources"
tags: ["timeouts", "reliability", "distributed-systems", "latency"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Timeouts

## Summary
Timeouts cap how long an operation may wait before failing. Every outbound call — HTTP, database, queue, or RPC — needs one so a slow peer cannot hang the caller indefinitely, exhausting threads, connections, and memory while users wait on a request that will never succeed.

## Details
- Mechanism: a timeout is a deadline on a single operation, distinct from retries (what happens after the deadline passes) and circuit breakers (what happens when deadlines keep passing). The values matter as much as the presence: a connect timeout bounds the TCP handshake, a request timeout bounds the full round trip including body transfer, and a total timeout bounds everything including retries. Timeouts that are too long let failures cascade; timeouts that are too short abort slow-but-healthy operations and create retry storms.
- Set connect, request, and total timeouts with margins below the consumer's own deadline. A good pattern is a ladder: if the UI or client can wait 5 seconds, give the service 4 seconds total, the database 2 seconds per query, and the retry budget a fraction of the remainder, so each layer fails before its caller does.
- Propagate deadlines across call chains (gRPC deadlines, HTTP `timeout` params) so the whole path fails fast. Without propagation, a front-end service that times out at 5 seconds still leaves its downstream call running to a 30-second database timeout, wasting resources on work nobody will consume; propagated deadlines let every hop cancel eagerly.
- Combine with retries and circuit breakers: timeouts trigger retries, circuit breakers stop the pattern when persistent. A timeout alone without a retry policy converts transient slowness into user-visible failures; retries without a circuit breaker convert a slow dependency into a self-inflicted flood of duplicate work.
- Failure modes: the hung-operation failure (missing timeout entirely) is the classic outage amplifier, but timeout misconfiguration has its own failure modes — per-operation timeouts that do not include queueing time (a request can sit in a backlog and still "time out" late), timeouts that reset on activity rather than bounding total elapsed time, and cancellation that is not propagated, so timed-out work keeps running server-side.
- Operational tradeoffs: strict timeouts improve tail latency and resource utilization but increase error rates on long-tail workloads, so tune them from real latency percentiles rather than guesses. Log timeout events with the operation name and configured value, and track timeout rate per dependency so a rising trend is visible before it becomes an outage.
- RSIS3/mykb relevance: RSIS3 loop workers that call the MyKB daemon, SPACE engine, or external APIs need the same ladder: per-call timeouts, propagated deadlines, bounded retries, and circuit breakers, so one slow component cannot stall the whole self-improvement cycle.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — what happens after a timeout
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — stops repeated timeout waits
- [[wiki/api-protocols/grpc|gRPC]] — native deadline propagation
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — timeouts free pooled connections
- [[wiki/devops-infra/observability|Observability]] — timeout metrics expose latency
