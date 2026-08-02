---
type: "concept"
title: "Metrics, Logs & Traces"
description: "The three signal types and how they complement each other"
tags: ["metrics", "logs", "traces", "telemetry"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opentelemetry.io/docs/concepts/signals/",
  "https://opentelemetry.io/docs/concepts/observability-primer/",
]
---

# Metrics, Logs & Traces

## Summary
Metrics, logs, and traces each answer a different question: what changed, what happened, and where did time go. Modern stacks collect all three with shared correlation identifiers. This node details the signals, their data models, and the tools that store them.

## Details
- Metrics drive alerting and dashboards: Prometheus-style counters, gauges, and histograms.
- Logs provide the event narrative for debugging, with structured formats like JSON for querying.
- Traces show per-span timings and dependencies, exposing hidden latency in distributed calls.
- The OpenTelemetry signals documentation maps each pillar to its data model and SDKs.
- Storage economics differ: metrics compress well, logs dominate volume, traces need sampling.
- In mykb, this node links to Prometheus, logging pipelines, and distributed tracing.
- Sample rates and retention policies differ per signal, shaping storage and cost architecture.
- An on-call workflow typically starts from a metric alert, drills into a trace, and reads logs for the final detail.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/progressive-rollout-metrics|Progressive Rollout Metrics]]
- [[wiki/cloud-infra/flow-logs-and-analysis|Flow Logs & Analysis]]
- [[wiki/infrastructure/north-star-metrics|North Star Metrics]]
- [[wiki/infrastructure/counter-metrics|Counter Metrics]]
