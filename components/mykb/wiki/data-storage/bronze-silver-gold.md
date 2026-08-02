---
type: "concept"
title: "Bronze, Silver, Gold Layers"
description: "The three medallion layers of lakehouse data engineering"
tags: ["bronze", "silver", "gold", "medallion"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.databricks.com/glossary/medallion-architecture", "https://en.wikipedia.org/wiki/Data_lakehouse"]
---

# Bronze, Silver, Gold Layers

## Summary

Bronze, silver, and gold are the standard layers of medallion architecture, each answering a different need.
Bronze preserves truth, silver standardizes, and gold optimizes for consumption.
Keeping the layers physically separate makes reprocessing and governance tractable.
Layer boundaries are governance boundaries: access, quality, and ownership tighten as data moves from bronze to gold.

## Details

- Bronze mirrors sources closely, storing raw payloads for audit and re-processing.
- Silver applies typing, deduplication, and conforming to a canonical model.
- Gold holds star-schema marts, aggregates, and curated features.
- Quality gates at each boundary prevent bad data from propagating.
- Time travel in bronze/silver enables point-in-time debugging.
- Reprocessing a layer must be safe, so keep upstream layers immutable.
- Freshness SLAs usually apply to gold; bronze can lag.
- The layers are a pipeline discipline, not a storage taxonomy: the same table can serve different layers at different times.

## Related

- [[wiki/data-storage/medallion-architecture|Medallion Architecture]] — the pattern
- [[wiki/data-storage/raw-landing-and-curated-zones|Raw Landing And Curated Zones]] — zone equivalent
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality gates
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lakehouse
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — auditing layers
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

