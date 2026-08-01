---
type: "concept"
title: "Distributed Tracing"
description: "Correlating a single request's path across many services via trace IDs, spans, and context propagation"
tags: ["tracing", "observability", "opentelemetry", "microservices", "w3c"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/TR/trace-context/"]
---

# Distributed Tracing

## Summary
Distributed tracing follows one request through every service it touches by attaching a trace ID and propagating it in headers. Each hop records a span — name, timing, and attributes — so the full path can be reconstructed and latency attributed to specific components. The W3C Trace Context specification standardizes the propagation headers.

## Details
- Model: a trace is a tree of spans; the root span is the initial request, child spans are downstream calls; each span records start/end time, service, and operation.
- Propagation: the traceparent header carries trace-id and parent-id between services; trace context survives HTTP, gRPC, and message queues, including async hops.
- Sampling: recording every request is expensive, so head-based sampling keeps a fraction of traces; tail-based sampling preserves the rare, expensive-to-store failures.
- Correlation: trace IDs join logs and metrics — a failing span links to the log lines and metric series of the same request.
- Instrumentation: OpenTelemetry provides automatic and manual SDKs; agents inject context with no code changes, while manual spans capture business semantics.
- Worked example: a mykb search request produces spans for gateway, retriever, and LLM call; a p95 latency regression is traced to the retriever span, not the model.
- Integration: tracing works alongside log aggregation and dashboards as the third pillar of observability.

## Related
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — tracing locates the latency to optimize
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — trace summaries surface on dashboards
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — logs correlated by trace ID
- [[wiki/devops-infra/golden-signals|Golden Signals]] — service-level metrics traced end to end
- [[wiki/devops-infra/observability|Observability]] — the pillar tracing belongs to
- [[wiki/api-protocols/grpc|gRPC]] — carries trace context over RPC
