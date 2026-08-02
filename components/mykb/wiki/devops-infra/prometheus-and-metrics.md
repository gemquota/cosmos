---
type: "concept"
title: "Prometheus & Metrics"
description: "Pull-based time-series monitoring with PromQL"
tags: ["prometheus", "metrics", "monitoring", "timeseries"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://prometheus.io/docs/introduction/overview/",
  "https://prometheus.io/docs/prometheus/latest/querying/basics/",
]
---

# Prometheus & Metrics

## Summary
Prometheus is the standard open-source time-series monitoring system, pulling metrics over HTTP and querying them with PromQL. Its pull model and label-based data model shape the whole metrics ecosystem. Prometheus is the default observability backend for Kubernetes deployments.

## Details
- Prometheus scrapes targets on a schedule, storing samples in a local TSDB with label-based indexing.
- The overview documents architecture: exporters, pushgateway, Alertmanager, and federation.
- PromQL enables aggregations, rates, and thresholds for dashboards and alerts.
- Service discovery finds targets from Kubernetes, DNS, or cloud APIs.
- Retention and cardinality are the operational limits: labels multiply series quickly.
- In mykb, Prometheus connects to Grafana, metrics-logs-traces, and Kubernetes observability.
- Recording rules precompute expensive queries, and Alertmanager handles deduplication and routing of alerts.
- The pushgateway covers short-lived jobs that finish before a scrape can collect them.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/progressive-rollout-metrics|Progressive Rollout Metrics]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/infrastructure/north-star-metrics|North Star Metrics]]
- [[wiki/infrastructure/counter-metrics|Counter Metrics]]
