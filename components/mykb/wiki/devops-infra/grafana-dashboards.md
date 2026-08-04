---
type: "entity"
title: "Grafana Dashboards"
description: "Visualizing telemetry and the dashboard design loop"
tags: ["grafana", "dashboards", "visualization", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://grafana.com/docs/grafana/latest/dashboards/",
  "https://grafana.com/oss/grafana/",
]
---

# Grafana Dashboards

## Summary
Grafana turns telemetry into dashboards and alerting, querying Prometheus, Loki, and many other data sources. Dashboards are the shared operational interface for teams. Good dashboard design follows from good metric design and makes incidents visible faster.

## Details
- Grafana connects to data sources with a common panel model: time series, tables, and logs.
- The dashboards documentation covers panels, variables, and templating.
- Alerting rules evaluate queries and route notifications through contact points.
- Annotations mark deploys and incidents on graphs for correlation.
- Dashboards as code, stored as JSON, enable review, versioning, and reproducible setup across teams.
- In mykb, Grafana connects to Prometheus, observability pillars, and log aggregation.
- Team folders and provisioning as code keep dashboards reviewable and consistent across environments.
- Panel thresholds and legend labels should encode the SLO targets the team cares about.
- Alert rules share the same query language as panels, so thresholds stay consistent with what is displayed.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]]
- [[wiki/devops-infra/acid|ACID]]
