---
type: "concept"
title: "Pipelines"
description: "The chains of steps that move and transform data"
tags: ["pipelines", "etl", "orchestration", "data-engineering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_pipeline", "https://en.wikipedia.org/wiki/Workflow_automation"]
---

# Pipelines

## Summary

A pipeline is an ordered chain of steps that extracts data from sources, transforms it, and loads it into a destination.
Pipelines are the backbone of analytics: every dashboard, model, and report depends on them running correctly and on time.
The design space spans batch vs streaming, orchestration, error handling, and testing.
The hardest pipeline bugs are data bugs, not code bugs: schema drift, duplicates, and semantic changes pass tests that only check syntax.

## Details

- Pipeline anatomy: source connectors, transformation steps, quality checks, and sink writers.
- Idempotency and retries make pipelines safe to rerun after partial failure.
- Monitoring covers run status, data volume, latency, and freshness per stage.
- Orchestrators (Airflow, Dagster, dbt) schedule, retry, and visualize dependencies.
- Pipeline-as-code with tests in CI is the modern standard.
- Pipeline observability should expose per-stage row counts and latency, not just pass/fail.
- Version pipelines as code so every run is reproducible and reviewable.
- Design pipelines so that any step can fail and be resumed, and so that reruns converge on the same result as the original run.

## Related

- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — foundation
- [[wiki/data-storage/airflow-and-workflow-orchestration|Airflow and Workflow Orchestration]] — orchestration
- [[wiki/data-storage/bulk-vs-streaming-ingestion|Bulk vs Streaming Ingestion]] — ingestion modes
- [[wiki/data-storage/data-pipeline-testing|Data Pipeline Testing]] — testing
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — existing orchestration notes
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — pipeline shape
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

