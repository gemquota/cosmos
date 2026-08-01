---
type: "concept"
title: "Monitoring Dashboards"
description: "Curated metric and log views that answer operational questions without paging through raw data"
tags: ["dashboards", "monitoring", "observability", "grafana"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Monitoring Dashboards

## Summary
Dashboards turn metrics and logs into curated, glanceable views — service health, SLO burn, traffic patterns. Done well, they answer questions fast; done badly, they are wall-sized decoration.

## Details
- Structure by audience and question: service-level, business-level, on-call triage.
- Feature the golden signals: latency, traffic, errors, saturation per service.
- Links, annotations, and log drill-downs turn dashboards into investigation launchpads.
- Open question: how to keep dashboards honest as systems evolve.

## Related
- [[wiki/devops-infra/golden-signals|Golden Signals]] — what dashboards should feature
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]] — dashboards answer questions
- [[wiki/devops-infra/observability|Observability]] — the data dashboards visualize
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — log panels inside dashboards
