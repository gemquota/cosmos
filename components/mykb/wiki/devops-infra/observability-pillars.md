---
type: "concept"
title: "Observability Pillars"
description: "Metrics, logs, and traces as the foundation of operations"
tags: ["observability", "metrics", "logs", "traces"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opentelemetry.io/docs/concepts/observability-primer/",
  "https://en.wikipedia.org/wiki/Observability",
]
---

# Observability Pillars

## Summary
Observability rests on three signal pillars: metrics, logs, and traces. Metrics summarize system state, logs capture events, and traces follow requests across services. Combining them lets teams answer unknown-unknown questions in production and is the foundation of the mykb observability cluster.

## Details
- Metrics are numeric, time-series measurements efficient to store and query over long periods.
- Logs are discrete events with context, invaluable for detail but expensive at high volume.
- Traces model request flow across services, revealing latency distribution and dependencies.
- The OpenTelemetry observability primer defines the shared vocabulary.
- Signals are correlated by common identifiers (service, trace ID, labels) during analysis.
- In mykb, the pillars anchor the monitoring, tracing, and logging pipeline articles.
- High-cardinality labels and structured logs are what make the pillars composable at scale.
- Pipelines must preserve correlation IDs across all three pillars for effective debugging.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]]
- [[wiki/infrastructure/accelerator-observability|Accelerator Observability]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]]
