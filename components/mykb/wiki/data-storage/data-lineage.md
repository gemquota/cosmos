---
type: "concept"
title: "Data Lineage"
description: "Tracing data flow across pipelines, tables, and reports"
tags: ["data-lineage", "metadata", "governance", "observability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://openlineage.io/docs/", "https://docs.getdbt.com/docs/collaborate/explore-projects"]
---

# Data Lineage

## Summary
Data lineage records how data flows: source systems to raw tables, through transformations, into marts and dashboards. Column-level lineage answers "where did this number come from?", making debugging, impact analysis, and governance possible at scale.

## Details
- **Levels** — table-level lineage shows job dependencies; column-level lineage traces individual fields through SQL; full lineage includes the actual data pipeline graph from source to report.
- **How it is captured** — dbt generates lineage from model dependencies; OpenLineage standardizes events from orchestrators and engines; databases' system catalogs (information_schema) give baseline table dependencies.
- **Why teams need it** — impact analysis (which dashboards break if I change this column?), root-cause debugging (why is this metric wrong?), and compliance (prove where PII flowed) all require lineage.
- **Automated vs manual** — SQL parsing can infer column lineage automatically but misses dynamic SQL and stored procedures; manual annotations fill the gaps but rot without enforcement.
- **Operational practice** — lineage is a metadata artifact: store it, render it, and diff it in reviews; link it to data-quality checks so a failing check shows its downstream blast radius.

## Related
- [[wiki/data-storage/data-observability|Data Observability]] — monitoring the flows lineage maps
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — failures with lineage context
- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — where lineage is born
- [[wiki/data-storage/data-contracts|Data Contracts]] — formal producer/consumer edges
- [[wiki/concepts/project-lineage|Project Lineage]] — lineage ideas beyond data pipelines
