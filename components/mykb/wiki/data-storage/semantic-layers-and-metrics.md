---
type: "concept"
title: "Semantic Layers and Metrics"
description: "One definition of metrics, served everywhere"
tags: ["semantic-layer", "metrics", "bi", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/build/metrics", "https://cloud.google.com/looker/docs"]
---

# Semantic Layers and Metrics

## Summary

A semantic layer defines business metrics once and serves them to any tool.
It decouples metric definitions from dashboard implementation.
Consistent definitions end metric disagreements across teams.
The semantic layer is where business language meets SQL, and governance lives in between.

## Details

- Define metrics: name, formula, grain, filters, and owner.
- Serve via SQL, REST, or BI integrations.
- Tools: dbt metrics, Looker LookML, Cube, and semantic-layer servers.
- Versioning and review keep definitions trustworthy.
- Semantic layers underpin self-serve analytics safely.
- Review metric changes like code changes.
- Expose metrics through one API to keep every tool consistent.
- One metric definition, many surfaces: the semantic layer is the single source of truth.

## Related

- [[wiki/infrastructure/metric-definition-catalog|Metric Definition Catalog]] — catalog
- [[wiki/infrastructure/self-serve-analytics|Self Serve Analytics]] — consumers
- [[wiki/data-storage/business-intelligence-dashboards|Business Intelligence Dashboards]] — BI
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse
- [[wiki/infrastructure/kpi-definition-and-alignment|Kpi Definition And Alignment]] — KPIs
- [[wiki/data-storage/data-lake|Data Lake]] — lake reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions

