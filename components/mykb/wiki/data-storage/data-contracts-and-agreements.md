---
type: "concept"
title: "Data Contracts and Agreements"
description: "Formalizing producer-consumer expectations for data"
tags: ["data-contracts", "agreements", "governance", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_contract", "https://docs.greatexpectations.io/"]
---

# Data Contracts and Agreements

## Summary

A data contract defines what a dataset promises: schema, quality, freshness, and semantics.
Contracts make producer-consumer relationships explicit and testable.
They reduce breakage from silent schema and semantic drift.
Contracts make data consumption safe enough to decentralize ownership.

## Details

- Contract elements: schema, nullability, quality thresholds, SLA, and owner.
- Enforcement via schema registry checks and CI validation.
- Version contracts; breaking changes require consumer coordination.
- Contracts apply to tables, streams, and API payloads.
- Start small: contract critical datasets, then expand.
- Start with contracts on shared, high-traffic datasets.
- Automate contract checks so they are enforced, not aspirational.
- Contracts are how data teams borrow the reliability practices of API development.

## Related

- [[wiki/data-storage/contract-testing-data|Contract Testing for Data]] — testing contracts
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality terms
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — versioning
- [[wiki/data-storage/data-contracts|Data Contracts]] — existing note
- [[wiki/data-storage/data-lineage-and-provenance|Data Lineage And Provenance]] — impact
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

