---
type: "concept"
title: "Data Lineage and Provenance"
description: "Tracing where data comes from and how it transforms"
tags: ["lineage", "provenance", "governance", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_lineage", "https://openlineage.io/docs/"]
---

# Data Lineage and Provenance

## Summary

Lineage maps the flow of data from sources through transformations to outputs.
It powers impact analysis, debugging, and compliance.
Automated extraction from SQL and pipeline code keeps it current.
Lineage turns 'who changed this number' from a rumor into a query.

## Details

- Table-level lineage shows dependencies; column-level shows field flows.
- Impact analysis answers: what breaks if this column changes?
- Provenance records origins for audit and reproducibility.
- OpenLineage standardizes lineage events across tools.
- Lineage depth should follow criticality to stay maintainable.
- Start with automated lineage for critical pipelines; manual maps rot.
- Use lineage to plan migrations and estimate blast radius.
- Lineage converts trust from a feeling into an artifact that can be queried and audited.

## Related

- [[wiki/data-storage/column-level-lineage|Column Level Lineage]] — column depth
- [[wiki/data-storage/data-catalogs-and-metadata|Data Catalogs and Metadata]] — catalog
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-lineage|Data Lineage]] — existing note
- [[wiki/infrastructure/data-rfc-process|Data Rfc Process]] — change governance
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

