---
type: "concept"
title: "Pipeline SLA and Latency Budgets"
description: "Defining how fresh data must be and where time goes"
tags: ["sla", "latency", "pipelines", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pipeline SLA and Latency Budgets

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- An SLA states freshness targets: data available by X after event time.
- Latency budgets allocate time across ingestion, transform, and load stages.
- Track percentiles (p95) and outliers, not just averages.
- Budget breaches trigger review: parallelism, batching, or architecture changes.

## Related

- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — orchestration
- [[wiki/data-storage/data-observability|Data Observability]] — observability
- [[wiki/infrastructure/data-freshness-and-sla-tracking|Data Freshness And Sla Tracking]] — tracking
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — alerting
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
