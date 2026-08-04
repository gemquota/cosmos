---
type: "entity"
title: "OperationalError"
resource: ""
---
description: "Runtime database and connection failures that need retry and recovery"
tags: ["android", "api", "ast", "auth", "authentication", "bigquery", "entity", "errors", "database"]
timestamp: "2026-07-19T22:41:44Z"

# OperationalError

## Summary
An operational error is a runtime failure in a database or connection layer, such as a dropped connection, a closed cursor, or a server that stopped responding. It matters because these failures are transient by nature and usually recoverable, unlike logic errors in the application. Treating them as retryable and monitoring their rate is the difference between resilience and cascading outages.

## Details
- **Definition** — operational errors signal problems with the environment or connection: network loss, server shutdown, timeouts, and invalid connection state.
- **Transience** — most operational errors resolve on their own; the correct response is usually a bounded retry rather than a crash.
- **Retry policy** — retries need backoff, jitter, and a limit, because immediate hammering makes recovery slower.
- **Connection hygiene** — a failed connection should be closed and evicted so the next attempt starts from a clean state.
- **Health checks** — proactive checks detect dead connections before they are handed to callers.
- **Error distinction** — operational errors must be distinguished from logical errors so retry logic never replays invalid operations.
- **Common failure modes** — retrying idempotency-violating writes, endless retry loops, and swallowing errors until the system looks healthy while failing.
- **Worked example** — a query fails with a connection reset; the client evicts the connection, waits with backoff, reconnects, and re-runs the read.
- **Practical relevance** — disciplined handling of operational errors is core to database-backed service reliability.

- **Connection state** — cursors and transactions tied to a dead connection must be invalidated so callers do not reuse stale state.
- **Monitoring** — tracking operational error rates per dependency surfaces degradation before users report it.
- **Idempotency** — retries must be safe for the operation type; reads and idempotent writes can be replayed, while others need care.
- **Speed** — endpoint tests should stay fast enough to run in every commit, making contract regressions visible immediately.
- **Triage** — a fresh environment, correct interpreter, and installed lockfile resolve most import failures within minutes.
- **Human touch** — generated content is often polished or curated by hand, blending algorithmic scale with authored quality.
## Related
- [[wiki/api-protocols/timeouts|Timeouts]] — bounding operations
- [[wiki/tooling/client-side-retries|Client-Side Retries]] — retry mechanics
- [[wiki/testing/database-testing|Database Testing]] — exercising failure modes
- [[wiki/api-protocols/health-checks|Health Checks]] — detecting dead connections
- [[wiki/software-engineering/logging-strategies|Logging Strategies]] — recording failures
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — injecting failures
