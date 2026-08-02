---
type: "concept"
title: "Kimball vs Inmon"
description: "Two philosophies for architecting the data warehouse"
tags: ["kimball", "inmon", "methodology", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/", "https://en.wikipedia.org/wiki/Data_warehouse"]
---

# Kimball vs Inmon

## Summary

Kimball's bottom-up approach builds dimensional marts first and combines them into a conformed bus architecture.
Inmon's top-down approach builds a normalized enterprise data warehouse first, then derives marts.
The choice shapes schema style, team workflow, and time-to-value.
Many teams adopt a pragmatic hybrid: Kimball-style marts over a lightly normalized integration layer.

## Details

- Kimball: star schemas, conformed dimensions, faster first marts, iterative delivery.
- Inmon: 3NF enterprise model, single source of truth, slower start, stronger consistency.
- Hybrids are common: vault or lake staging with dimensional presentation layers.
- Data vault modeling separates hubs, links, and satellites for audit-friendly history.
- Pick by governance needs, team maturity, and delivery pressure.
- The bus matrix (processes x dimensions) is Kimball's planning tool for conformed marts.
- Document the chosen approach; mixed philosophies without a documented standard create drift.
- Whatever philosophy you choose, publish it as a standard and enforce it in reviews so new models do not silently diverge.

## Related

- [[wiki/data-storage/data-modeling-star-schema|Data Modeling: Star Schema]] — Kimball's tool
- [[wiki/data-storage/data-vault-modeling|Data Vault Modeling]] — the third approach
- [[wiki/data-storage/methodology|Methodology]] — methodology comparison
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — modeling
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

