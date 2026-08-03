---
type: "concept"
title: "Distributed Tracing IDs"
description: "Unique identifiers that tie spans of one logical request together across services"
tags: ["tracing", "ids", "observability", "correlation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Distributed Tracing IDs

## Summary
A trace ID is a globally unique identifier shared by every span of one logical request, letting systems reassemble a distributed call graph. Generation and propagation rules determine whether traces actually line up — the ID is the glue, and the rules are the discipline.

## Details
- Mechanism: W3C trace-context defines traceparent and tracestate headers so tools interoperate across vendors; the trace ID (16 random bytes) plus parent span ID travel in the header; each service creates child spans referencing the incoming parent, preserving the causal chain; tracestate carries vendor-specific flags.
- Concrete example: an edge gateway generates a trace ID for a request; the API service, its DB client, and a downstream call all record spans under it; a trace viewer reassembles the waterfall showing 50ms in the API and 400ms in the database call; a retried request shares the trace ID but each attempt gets its own child spans.
- Failure modes: ID collisions from weak generation, corrupting the call graph at scale; propagation drops where a hop strips or rewrites headers, severing the chain; trace IDs that leak internal topology (never encode service names); sampling at the wrong layer, losing the trace before it completes; IDs not propagated into logs, so traces and logs cannot be joined.
- Tradeoffs: trace IDs enable whole-request visibility at the cost of propagation discipline and header overhead; the alternative — per-service IDs — loses the end-to-end view; the mature pattern is W3C-standard IDs, generate-once at the edge, propagate everywhere, and log them alongside correlation IDs.
- Operational notes: validate propagation in integration tests, log trace IDs, and keep sampling rules aligned across services.
- RSIS3 relevance: every agent run gets a run ID that doubles as a trace ID for the whole acquisition pipeline — the same reassembly RSIS3 needs across loop components.

## Related
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/sampling-traces|Sampling Traces]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
