---
type: "concept"
title: "Hot and Cold Data Tiering"
description: "Matching storage cost to data temperature"
tags: ["tiering", "storage", "lifecycle", "cost"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html", "https://en.wikipedia.org/wiki/Data_retention"]
---

# Hot and Cold Data Tiering

## Summary

Tiering moves data between hot, warm, and cold storage by access frequency.
Hot data is fast and expensive; cold data is cheap and slow.
Lifecycle policies automate the transitions.
Tiering is a cost optimization that must respect access SLAs.

## Details

- Tiers: memory, SSD, object storage, archive, tape.
- Lifecycle rules age data automatically (S3 lifecycle, Glacier).
- Access patterns determine tier boundaries.
- Cold reads have retrieval latency; plan SLAs accordingly.
- Tiering cuts storage cost dramatically for aging data.
- Lifecycle rules need review when access patterns change.
- Cold tiers should still be queryable when required.
- Tiering is lifecycle management made automatic, cutting cost without cutting access.

## Related

- [[wiki/data-storage/data-retention-and-lifecycle|Data Retention and Lifecycle]] — lifecycle
- [[wiki/data-storage/downsampling-and-retention-policies|Downsampling And Retention Policies]] — time-series aging
- [[wiki/data-storage/data-compression-techniques|Data Compression Techniques]] — compression
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — existing note
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — lifecycle
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

