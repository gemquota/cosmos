---
type: "concept"
title: "Metric Backends"
description: "Time-series stores that persist and query metrics from services and infrastructure"
tags: ["metrics", "time-series", "monitoring", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Metric Backends

## Summary
Metric backends (Prometheus, Mimir, Thanos, VictoriaMetrics, InfluxDB) store labeled time series and answer range queries for dashboards and alerts. Label design and retention shape how useful they are.

## Details
- Prometheus-style pull with a service discovery layer is the dominant open-source model; push gateways cover batch jobs.
- Cardinality explosions (unique label values per request) are the classic failure mode — keep labels bounded.
- Retention and downsampling trade storage for query speed; long-term archives belong in cheaper stores.
- mykb relevance: track article creation, link density, and curation lag as labeled time series.

## Related
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs, Traces]]
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]]
- [[wiki/dev-tools/dashboards-practice|Dashboards Practice]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]]
