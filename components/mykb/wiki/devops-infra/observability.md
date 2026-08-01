---
type: "concept"
title: "Observability"
description: "Measuring system behavior through metrics, logs, and traces to answer questions about any state"
tags: ["observability", "monitoring", "telemetry", "opentelemetry", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://opentelemetry.io/docs/"]
---

# Observability

## Summary
Observability is the ability to infer a system's internal state from its outputs — metrics, logs, and traces, the "three pillars." OpenTelemetry standardizes how telemetry is generated, transported, and correlated across services. For RSIS3, observability means the pulse engine's telemetry becomes inspectable, not just recorded.

## Details
- Pillars: metrics (counters/gauges/histograms), logs (structured events), and traces (distributed request paths); correlation IDs tie them together.
- OpenTelemetry: vendor-neutral SDKs and the OTLP protocol for metrics/logs/traces; the CNCF incubating project backs most backends.
- Instrumentation: auto-instrumentation for HTTP/DB frameworks plus manual spans for domain logic (e.g. a pulse evaluation cycle).
- Backends: Prometheus + Grafana for metrics, Loki/Elastic for logs, Jaeger/Tempo for traces; or managed APMs.
- Golden signals: latency, traffic, errors, and saturation — the four metrics that reveal most production problems.
- Alerting: derive SLOs from signals (e.g. "search p95 < 200ms over 30 days"), alert on error budgets rather than raw thresholds.
- Worked example: instrumenting the mykb daemon with OTel spans per search request, plus a pulse telemetry metric per RSIS3 loop, would make the dashboard's telemetry view live data rather than static JSON.

## Related
- [[wiki/api-protocols/health-checks|Health Checks]] — liveness/readiness for orchestrators
- [[wiki/api-protocols/http-caching|HTTP Caching]] — performance signals guide cache policy
- [[wiki/api-protocols/timeouts|Timeouts]] — latency budgets surface via traces
- [[wiki/devops-infra/feature-flags|Feature Flags]] — behavior changes become measurable
- [[wiki/devops-infra/kubernetes|Kubernetes]] — platform consumes OTel signals
- [[wiki/concepts/triad-architecture|Triad Architecture]] — pulse telemetry across the triad
- [[wiki/ops/gap-report|Gap Analysis Report]] — observability gaps noted
