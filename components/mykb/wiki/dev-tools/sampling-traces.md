---
type: "concept"
title: "Sampling Traces"
description: "Recording only a subset of traces to control storage and cost while keeping signal"
tags: ["tracing", "sampling", "cost", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sampling Traces

## Summary
Trace sampling decides which requests get fully recorded, because capturing every span is expensive at scale. Head-based sampling decides at the start; tail-based sampling decides after seeing the outcome.

## Details
- Head sampling (probability or rate per route) is simple but misses rare slow or failed traces.
- Tail sampling buffers spans briefly and keeps the interesting ones — errors, high latency, specific customers.
- Sampling rates should be tunable per service and during incidents; priority sampling protects critical routes.
- mykb relevance: sample agent traces aggressively except for errors and high-cost runs.

## Related
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/dev-tools/distributed-tracing-ids|Distributed Tracing IDs]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/devops-infra/observability|Observability]]
