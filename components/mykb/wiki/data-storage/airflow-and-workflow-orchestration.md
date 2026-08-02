---
type: "concept"
title: "Airflow and Workflow Orchestration"
description: "Scheduling and coordinating data workflows as code"
tags: ["airflow", "orchestration", "dags", "scheduling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://airflow.apache.org/docs/apache-airflow/stable/", "https://en.wikipedia.org/wiki/Apache_Airflow"]
---

# Airflow and Workflow Orchestration

## Summary

Apache Airflow orchestrates workflows as directed acyclic graphs (DAGs) defined in Python.
It schedules, retries, and visualizes dependencies between tasks.
Orchestration is the control plane that keeps pipelines running on time.
Orchestration is where pipelines get operational maturity: retries, alerts, and SLAs.

## Details

- DAGs declare task dependencies; the scheduler executes them.
- Operators wrap actions: SQL, Spark, transfers, and custom logic.
- Sensors and hooks handle waiting and external systems.
- Retries, backfills, and catch-up manage operational recovery.
- Alternatives: Dagster, Prefect, and managed schedulers.
- Idempotent tasks make retries and backfills safe.
- Keep DAGs thin: logic in libraries, orchestration in the graph.
- Orchestration platforms are control planes: their health determines the health of every pipeline they run.

## Related

- [[wiki/data-storage/pipelines|Pipelines]] — what gets orchestrated
- [[wiki/data-storage/data-pipeline-testing|Data Pipeline Testing]] — testing DAGs
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — monitoring runs
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — existing note
- [[wiki/infrastructure/pipeline-sla-and-latency-budgets|Pipeline Sla And Latency Budgets]] — SLAs
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

