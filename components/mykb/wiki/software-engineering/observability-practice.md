---
type: "concept"
title: "Observability Practice"
description: "Instrumenting systems so their internal state is inferable from outputs"
tags: ["observability", "telemetry", "metrics", "traces"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Observability_(software)", "https://opentelemetry.io/docs/concepts/observability-primer/"]
---

# Observability Practice

## Summary
Observability is the property that lets you ask new questions about a running system without shipping new code, using metrics, logs, and traces. Practice means deliberate instrumentation at every boundary, with correlation between the three signals.

## Details
- The three pillars — metrics, logs, traces — answer different questions: what happened, why, and along which path.
- Correlation is the multiplier: trace IDs in logs, span attributes on metrics, and structured fields everywhere.
- Instrument the boundaries: entry points, external calls, queues, databases, and failure paths.
- Observability is a product decision, not a side effect: SLOs tell you what to watch; cardinality discipline keeps it affordable.
- OpenTelemetry standardizes instrumentation and is the de facto vendor-neutral path.
- For the mykb bundle, observability covers the acquisition pipeline: fetch latency, curation lag, and link-check outcomes.

Worked example — a slow curation run: the trace shows a source fetch taking 12s, its span attributes name the site, and the log line carries the same trace ID. The metric 'fetch_p99' shows the same site is degrading all week.

## Related
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]]
- [[wiki/software-engineering/logging-strategies|Logging Strategies]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs & Traces]]
