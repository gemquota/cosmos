---
type: "concept"
title: "Offline vs Online Stores"
description: "Training-time and serving-time feature infrastructure"
tags: ["feature-store", "offline", "online", "mlops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.feast.dev/", "https://en.wikipedia.org/wiki/Feature_store"]
---

# Offline vs Online Stores

## Summary

Offline stores serve historical feature data for training; online stores serve current features for inference.
The two must be computed consistently or models degrade in production.
Serving latency and freshness requirements differ sharply.
The gap between stores is a pipeline, not just a configuration; keep definitions in one place.

## Details

- Offline: batch-computed, columnar, large volumes, point-in-time queries.
- Online: low-latency lookups, often cached key-value access.
- Consistency requires shared feature definitions and dual writes.
- Training-serving skew is the classic failure mode.
- Feature stores operationalize the bridge between the two.
- Log serving features to close the feedback loop.
- Point-in-time correctness prevents leakage in training data.
- Consistency between offline and online features is the difference between a model that works and one that doesn't.

## Related

- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — feature stores
- [[wiki/data-storage/real-time-personalization|Real Time Personalization]] — online use
- [[wiki/data-storage/cache-aside-and-write-through|Cache-Aside and Write-Through]] — caching
- [[wiki/data-storage/offline-vs-online-stores|Offline vs Online Stores]] — overview
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-lake|Data Lake]] — lake reference

