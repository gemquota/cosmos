---
type: "concept"
title: "Request Tracing"
description: "Following a single request through every service, queue, and call it touches"
tags: ["tracing", "observability", "distributed-systems", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Request Tracing

## Summary
Request tracing assigns a trace ID to a request and records spans for each hop, so engineers can follow a single user action across services. It turns distributed debugging from guesswork into a timeline.

## Details
- A trace is a tree of spans: each span names an operation, its duration, and its parent span.
- Propagate the trace context through HTTP headers, message metadata, and async boundaries or the trace fragments.
- Tracing complements logs: logs carry the trace ID, traces show the flow, metrics show the aggregate.
- RSIS3 relevance: agent runs produce natural traces — one run ID, many tool calls and model turns.

## Related
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs, Traces]]
