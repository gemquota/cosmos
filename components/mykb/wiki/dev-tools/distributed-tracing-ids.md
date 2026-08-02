---
type: "concept"
title: "Distributed Tracing IDs"
description: "Unique identifiers that tie spans of one logical request together across services"
tags: ["tracing", "ids", "observability", "correlation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distributed Tracing IDs

## Summary
A trace ID is a globally unique identifier shared by every span of one logical request, letting systems reassemble a distributed call graph. Generation and propagation rules determine whether traces actually line up.

## Details
- W3C trace-context defines traceparent/tracestate headers so tools interoperate across vendors.
- IDs must be unique enough to survive aggregation at scale and opaque to avoid leaking internal topology.
- Synthetic generation at the edge keeps IDs stable across retries; each retry can carry its own child span.
- mykb relevance: every agent run gets a run ID that doubles as a trace ID for the whole acquisition pipeline.

## Related
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/sampling-traces|Sampling Traces]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
