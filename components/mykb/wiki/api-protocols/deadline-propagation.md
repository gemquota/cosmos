---
type: "concept"
title: "Deadline Propagation"
description: "Timeout propagation across distributed calls"
tags: ["deadlines", "timeouts", "distributed-systems", "reliability", "propagation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/blog/deadlines/", "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/"]
---

# Deadline Propagation

## Summary
Deadline propagation carries a call's time budget through the whole request chain: each service subtracts its own latency from the incoming deadline before calling downstream. Without it, one slow upstream can burn the entire budget, leaving downstream calls to hang or time out independently — the classic cause of cascading latency.

## Details
- The rule: if a request arrives with 3 seconds left, a service should give its downstream calls less (say 2s), reserving time for its own work.
- Carriers: HTTP headers (x-deadline, grpc-timeout, W3C traceparent contexts), metadata, and thread-local context objects propagated by frameworks.
- Cancellation: a deadline that expires cancels downstream calls (HTTP/2 RST_STREAM, gRPC cancellation), freeing server work early.
- Budget math: subtract elapsed time, not fixed per-hop slices, so fast hops preserve budget; cap the total so retries cannot exceed it.
- Retries interact: a retry consumes the same deadline — total attempts must fit within the budget, or a retry storm outlives the user's patience.
- Anti-patterns: fixed per-service timeouts that multiply (5 services x 30s = 150s), or clients that keep waiting past the server's deadline.
- Observability: record deadline remaining at each hop (spans with timeout fields) to find budget burners.

## Related
- [[wiki/api-protocols/grpc-deadlines|gRPC Deadlines]] — native deadline support in gRPC
- [[wiki/api-protocols/timeouts|Timeouts]] — relative timeouts vs absolute deadlines
- [[wiki/api-protocols/retry-policies|Retry Policies]] — retries must fit the deadline
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — tracing shows where budget burns
- [[wiki/api-protocols/backpressure|Backpressure]] — deadlines bound waiting work
