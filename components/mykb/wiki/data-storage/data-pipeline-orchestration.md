---
type: "concept"
title: "Data Pipeline Orchestration"
description: "DAG scheduling, retries, and dependency management"
tags: ["orchestration", "airflow", "dag", "data-pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html", "https://docs.getdbt.com/docs/build/jobs"]
---

# Data Pipeline Orchestration

## Summary
Orchestration coordinates the jobs that move and transform data: defining dependencies as a directed acyclic graph (DAG), scheduling runs, and handling retries, backfills, and failures. Airflow, Dagster, Prefect, and dbt Cloud jobs are the common tools, and the DAG is the contract between engineers and operations.

## Details
- **DAG semantics** — nodes are tasks, edges are dependencies; a task runs only when upstream tasks succeed, and the graph must stay acyclic or scheduling becomes impossible.
- **Scheduling** — cron-like or data-aware triggers (a sensor waiting for a file, a table checkpoint) decide when runs start; idempotent tasks let schedulers re-run safely.
- **Retries and backoff** — transient failures retry with exponential backoff; permanent failures alert and pause the downstream lineage so bad data does not propagate.
- **Backfills** — catch-up runs for historical dates re-execute the same DAG over past partitions; this only works when tasks are deterministic and idempotent.
- **Execution modes** — Airflow's scheduler + workers (Celery, Kubernetes) runs DAGs; dbt jobs run SQL models in dependency order; Dagster adds asset-aware materialization. All converge on the same ideas: state, observability, and lineage.
- **Operational practice** — every DAG should have an owner, SLAs with alerts, and tests (dag tests, pipeline checks); monitoring run duration, freshness, and failure rates is as important as the logic.

## Related
- [[wiki/data-storage/backfilling|Backfilling]] — reprocessing historical ranges
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — keeping scheduled runs cheap
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — making reruns safe
- [[wiki/data-storage/data-observability|Data Observability]] — monitoring pipeline health
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — what the DAG executes
