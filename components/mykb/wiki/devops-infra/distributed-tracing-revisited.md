---
type: "concept"
title: "Distributed Tracing"
description: "Following requests across service boundaries"
tags: ["tracing", "distributed", "spans", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opentelemetry.io/docs/concepts/signals/traces/",
  "https://www.w3.org/TR/trace-context/",
]
---

# Distributed Tracing

## Summary
Distributed tracing records the path of a single request through many services as a tree of spans. It exposes latency distribution, dependency failures, and bottlenecks invisible to per-service metrics. Tracing is essential for debugging microservice architectures and complements the other observability pillars.

## Details
- A trace is a tree of spans; each span records a named unit of work with timing and attributes.
- The W3C Trace Context standardizes propagation headers for interoperability.
- OTel traces documentation covers the span lifecycle and sampling.
- Tail-based sampling keeps important traces while controlling storage cost.
- Trace comparison across versions reveals regressions after deploys.
- In mykb, tracing connects to OTel instrumentation, service meshes, and SLOs.
- Span attributes carry service, operation, and resource identifiers used for filtering and analysis.
- Trace-to-log correlation links every span to the log lines emitted during its execution.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]]
- [[wiki/os-shell/strace-and-dynamic-tracing|strace & Dynamic Tracing]]
