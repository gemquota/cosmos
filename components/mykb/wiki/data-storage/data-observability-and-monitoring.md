---
type: "concept"
title: "Data Observability and Monitoring"
description: "Seeing inside data systems to detect and fix problems"
tags: ["observability", "monitoring", "data-quality", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Observability", "https://grafana.com/docs/grafana/latest/"]
---

# Data Observability and Monitoring

## Summary

Data observability exposes the health of pipelines, tables, and freshness.
It combines logs, metrics, lineage, and quality checks.
Fast detection shortens mean time to data recovery.
Observability shortens the distance between failure and understanding.

## Details

- Five pillars: freshness, volume, schema, quality, lineage.
- Monitor runs, latency, row counts, and anomaly drift.
- Centralize logs and metrics with alerting.
- Lineage connects symptoms to root causes.
- SLOs and budgets make reliability measurable.
- Instrument everything once, then slice by team and dataset.
- Post-incident reviews should produce new monitors.
- Observability is what separates data teams that react from those that respond.

## Related

- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — pipeline alerts
- [[wiki/data-storage/table-health-and-quality-metrics|Table Health And Quality Metrics]] — table health
- [[wiki/data-storage/data-lineage-and-provenance|Data Lineage and Provenance]] — lineage
- [[wiki/data-storage/data-observability|Data Observability]] — existing note
- [[wiki/infrastructure/pipeline-sla-and-latency-budgets|Pipeline Sla And Latency Budgets]] — SLAs
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability

