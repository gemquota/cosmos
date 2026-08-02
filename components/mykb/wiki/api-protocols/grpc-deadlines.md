---
type: "concept"
title: "gRPC Deadlines"
description: "Deadline propagation and cancellation"
tags: ["grpc", "deadlines", "timeouts", "cancellation", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/what-is-grpc/core-concepts/#deadlines", "https://grpc.io/blog/deadlines/"]
---

# gRPC Deadlines

## Summary
A gRPC deadline is an absolute time by which a call must complete; clients set them per call and servers see a deadline that propagates across the call graph. When time expires the call fails with DeadlineExceeded and cancellation cascades, freeing resources throughout the chain.

## Details
- Deadline vs timeout: a timeout is relative duration; a deadline is an absolute timestamp — deadlines survive retries and proxy hops better.
- Wire transport: the grpc-timeout field carries remaining time; each hop re-derives its own deadline from the incoming one, so propagation is automatic.
- Cancellation: exceeding the deadline cancels the stream, and the cancel propagates via HTTP/2 RST_STREAM to the server, which should stop work.
- Chained calls: a service receiving a 5-second deadline should give its own downstream calls shorter deadlines (for example 4s), leaving a buffer for itself.
- Server hygiene: honor the context — check ctx.cancelled() or cancelled status in loops and return the cancellation instead of continuing.
- Defaulting: no deadline means a call can hang forever; clients should always set one, even if generous.
- Status: DeadlineExceeded is retryable only when the client believes the work did not start; servers mark partial work with other codes.

## Related
- [[wiki/api-protocols/deadline-propagation|Deadline Propagation]] — the distributed pattern gRPC implements natively
- [[wiki/api-protocols/timeouts|Timeouts]] — relative timeouts vs absolute deadlines
- [[wiki/api-protocols/grpc-status-codes|gRPC Status Codes]] — DeadlineExceeded is the terminal status
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — long streams need deadlines too
- [[wiki/api-protocols/retry-policies|Retry Policies]] — deadline-aware retry budgets
