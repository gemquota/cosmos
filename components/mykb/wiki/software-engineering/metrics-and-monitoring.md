---
type: "concept"
title: "Metrics and Monitoring"
description: "Collecting time-series data and watching it for health and trends"
tags: ["metrics", "monitoring", "dashboards", "alerting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Application_performance_management", "https://opentelemetry.io/docs/concepts/observability-primer/"]
---

# Metrics and Monitoring

## Summary
Metrics are numeric time series — requests per second, latency percentiles, error rates, saturation — and monitoring is the practice of collecting, storing, and watching them. Monitoring answers what happened; alerting turns the answers into action.

## Details
- Choose metrics that map to user experience: the four golden signals (latency, traffic, errors, saturation) are the core set.
- Dashboards are for investigation, alerting is for action — do not conflate a chart with a pager.
- Label discipline controls cardinality: bounded label values keep metrics affordable at scale.
- Histograms and percentiles beat averages for latency; watch p99 and the tail.
- Monitoring is only as good as its coverage of failure modes — instrument the paths you fear.
- For the mykb bundle, metrics would track curation lag, link-check outcomes, and article growth per area.

Worked example — the wiki would publish four golden signals per service: request latency histogram, throughput, error ratio, and queue depth. Dashboards would show them per area; alerts would fire only on error-budget burn.

## Related
- [[wiki/dev-tools/metric-backends|Metric Backends]]
- [[wiki/dev-tools/dashboards-practice|Dashboards Practice]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
- [[wiki/software-engineering/observability-practice|Observability Practice]]
- [[wiki/dev-tools/four-golden-signals|Four Golden Signals]]
- [[wiki/dev-tools/latency-percentiles|Latency Percentiles]]
- [[wiki/dev-tools/slo-budgets|SLO Budgets]]
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs & Traces]]
