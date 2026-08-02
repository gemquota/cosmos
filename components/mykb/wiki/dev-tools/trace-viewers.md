---
type: "concept"
title: "Trace Viewers"
description: "UIs for exploring distributed traces across services and spans"
tags: ["tracing", "observability", "tooling", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Trace Viewers

## Summary
Trace viewers (Jaeger UI, Zipkin, Grafana Tempo) render a request as a timeline of spans across services. They make latency waterfalls visible and support filtering by service, error, or duration.

## Details
- Waterfall views show where time is spent inside a single request; critical-path highlighting finds the bottleneck.
- Query by trace ID, service, or tags; store traces for a retention window to support post-incident analysis.
- Integrate with sampling policies so the viewer has enough traces without overwhelming storage.
- RSIS3 relevance: trace the multi-agent pipeline to see where handoffs and retries add latency.

## Related
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/devops-infra/distributed-tracing-revisited|Distributed Tracing Revisited]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/request-tracing|Trace Viewers]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
