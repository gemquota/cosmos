---
type: "concept"
title: "Network Observability"
description: "Collecting and correlating network signals for operations"
tags: ["observability", "network", "metrics", "tracing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opentelemetry.io/docs/concepts/observability-primer/",
  "https://en.wikipedia.org/wiki/Observability",
]
---

# Network Observability

## Summary
Network observability collects, correlates, and analyzes network signals so teams can answer why a request was slow or failed. It combines device metrics, flow data, and tracing with the application view. Without it, network problems look like application problems.

## Details
- Signals include interface counters, flow logs, latency probes, and packet captures, each answering a different question.
- Flow data (NetFlow/sFlow/flow logs) shows conversation-level detail: who talks to whom, how much, and over what path.
- Synthetic probes measure path health actively, complementing passive collection.
- Correlation with traces maps network segments to request latency, revealing where time is spent.
- The OpenTelemetry observability primer frames the shared vocabulary of metrics, logs, and traces that network telemetry must integrate with.
- In mykb, network observability links to observability pillars, tracing, and packet analysis articles.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/infrastructure/network-policy|Network Policy]]
