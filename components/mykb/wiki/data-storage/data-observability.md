---
type: "concept"
title: "Data Observability"
description: "Freshness, volume, and schema monitoring for pipelines"
tags: ["data-observability", "monitoring", "pipelines", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/deploy/dashboard-status-tiles", "https://en.wikipedia.org/wiki/Data_observability"]
---

# Data Observability

## Summary
Data observability applies the five signals of monitoring to data: freshness, volume, schema, quality, and lineage. Instead of "is the pipeline running?", it asks "is the data correct and current?" — catching silent failures that orchestrators miss because the job exited 0.

## Details
- **Freshness** — the age of the newest row or table update; a freshness SLA ("orders must be < 1h old") is the first signal to break silently, often before any error.
- **Volume** — row counts and byte sizes per partition; sudden drops mean truncated loads, jumps mean duplication or replayed data. Volume anomalies are the classic "job succeeded, data is wrong" case.
- **Schema** — column add/remove/type-change detection; drift breaks downstream SQL, and without schema monitoring it surfaces as a mystery failure in a report.
- **Quality** — the checks from dbt/Great Expectations running in production: null rates, uniqueness, range violations, with pass/fail history over time.
- **Lineage** — knowing which dashboards and models depend on a failing table turns an alert into a prioritized incident.
- **Tooling** — open-source stacks compose dbt tests, Airflow sensors, and Prometheus metrics; vendors (Monte Carlo, Soda, Bigeye) package the signals; the key is history, alerting, and an owning team.

## Related
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — the assertions being observed
- [[wiki/data-storage/data-lineage|Data Lineage]] — dependency context for alerts
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — the scheduler being watched
- [[wiki/devops-infra/observability|Observability]] — the broader monitoring philosophy
- [[wiki/devops-infra/golden-signals|Golden Signals]] — the metrics analog
