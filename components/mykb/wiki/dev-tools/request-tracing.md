---
type: "concept"
title: "Request Tracing"
description: "Following a single request through every service, queue, and call it touches"
tags: ["tracing", "observability", "distributed-systems", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Request Tracing

## Summary
Request tracing assigns a trace ID to a request and records spans for each hop, so engineers can follow a single user action across services. It turns distributed debugging from guesswork into a timeline — the answer to where did this request go and how long did each stop take.

## Details
- Mechanism: a trace is a tree of spans — each span names an operation, its duration, and its parent; trace context propagates through HTTP headers (W3C traceparent), message metadata, and async boundaries, or the trace fragments; a trace viewer reassembles spans by trace ID into a waterfall; logs carry the trace ID so they join the same story.
- Concrete example: an article import flows through ingestion, transformation, and publishing; a trace shows 200ms in ingestion, 3s in transformation (the suspect), and 50ms in publishing; a retried step appears as sibling spans; logs for the failed span share the trace ID for deep inspection.
- Failure modes: propagation gaps — one uninstrumented hop severs the trace, leaving two fragments; sampling that drops the interesting traces (tail-based sampling helps); high overhead from too many spans; async boundaries that lose context; trace IDs not logged, so traces and logs cannot be joined.
- Tradeoffs: tracing gives whole-request visibility at the cost of instrumentation and propagation discipline across every service; the alternative — per-service logs with correlation IDs — is cheaper and loses the timeline; the mature pattern is W3C-standard context, automated instrumentation, and traces joined with logs.
- Operational notes: validate propagation in tests, log trace IDs everywhere, and keep sampling policies aligned.
- RSIS3 relevance: agent runs produce natural traces — one run ID, many tool calls and model turns — the same timeline RSIS3 needs when a loop step fails.

## Practice
- Start a trace at every external boundary and retry with the same trace ID so retried attempts stay in one story.
## Related
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs, Traces]]
