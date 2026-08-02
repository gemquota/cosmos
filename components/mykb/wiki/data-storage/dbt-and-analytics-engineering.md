---
type: "concept"
title: "dbt and Analytics Engineering"
description: "SQL-first transformation workflows with testing and docs"
tags: ["dbt", "analytics-engineering", "sql", "transformation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.getdbt.com/docs/introduction", "https://docs.getdbt.com/docs/build/tests"]
---

# dbt and Analytics Engineering

## Summary

dbt lets analytics engineers transform data with versioned, testable SQL models.
It compiles Jinja-templated SQL into runnable transformations in the warehouse.
dbt brought software engineering practices to analytics.
dbt made transformations reviewable and versioned, closing the gap between code and analytics.

## Details

- Models are SELECT statements materialized as tables, views, or incremental builds.
- Tests (unique, not_null, custom SQL) gate data quality.
- Sources and docs produce an auto-generated catalog and lineage graph.
- Environments and CI run models per branch or deployment.
- Semantic models and metrics extend dbt toward a metrics layer.
- Documentation and lineage come free with every model.
- Incremental models and tests keep warehouse costs and confidence in check.
- dbt's model is now the community standard for transformation-layer engineering.

## Related

- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/infrastructure/dbt-environments-and-jobs|Dbt Environments And Jobs]] — environments
- [[wiki/data-storage/semantic-layers-and-metrics|Semantic Layers And Metrics]] — metrics
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — ELT model
- [[wiki/data-storage/data-lineage-and-provenance|Data Lineage and Provenance]] — lineage
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

