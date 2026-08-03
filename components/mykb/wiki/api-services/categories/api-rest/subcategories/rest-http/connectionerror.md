---
type: "entity"
title: "ConnectionError"
description: "An exception raised when a network connection cannot be established or is lost"
tags: ["entity", "exceptions", "networking", "errors", "resilience"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# ConnectionError

## Summary

ConnectionError is an exception type raised when a network connection fails to establish, drops mid-use, or times out. It is the most common failure class in distributed systems, so handling it well is a core reliability skill. Good handling distinguishes transient failures, which deserve retry, from permanent ones, which should fail fast with clear diagnostics.

## Details

- **Definition** — Connection errors signal problems at the transport level: DNS failure, refused connections, timeouts, resets, or interrupted transfers.
- **Causes** — Unreachable hosts, closed ports, firewalls, DNS misconfiguration, load balancer churn, and network partitions all produce connection errors.
- **Transient vs permanent** — Timeouts and resets are often transient; DNS failures and refused connections can be either, so classification drives retry policy.
- **Retry semantics** — Retries with backoff and jitter recover from blips; retrying permanent failures only multiplies load and latency.
- **Worked example** — A client retries a POST three times with exponential backoff after ConnectionError, then reports the failure with the request id for correlation.
- **Common failure modes** — Retrying non-idempotent requests blindly, infinite retry loops that outlive the outage, and swallowing the error until the user sees a blank screen.
- **Practical relevance** — APIs should surface connection failures distinctly so clients can decide between retry, fallback, and user-facing messaging.
- **Telemetry note** — Recorded in API and shell sessions with bug tags, reflecting real outages during which this error was observed.
- **Timeouts** — Connection attempts need deadlines: a hanging connect can outlive the user's patience, so timeout and dial-timeout settings bound the wait.
- **Observability** — Logging host, port, and attempt count makes connection failures diagnosable across DNS, network, and server causes.
- **Worked example** — A daemon's health check catches ConnectionError to a database, marks the service degraded, and retries with backoff while alerting the on-call.
- **Idempotency** — Retrying requests requires idempotency keys or safe methods, otherwise a success that lost its response gets applied twice.

## Related

- [[wiki/api-protocols/retry-backoff|Retry Backoff]] — the retry policy
- [[wiki/api-protocols/timeouts|Timeouts]] — bounding connection waits
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — agent-level retry design
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/cloud-infra/timeouts-and-deadlines|Timeouts and Deadlines]] — distributed failure bounds
