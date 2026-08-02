---
type: "concept"
title: "Feature Stores and ML Features"
description: "Managing and serving features for machine learning"
tags: ["feature-store", "ml", "features", "mlops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Feature_store", "https://docs.feast.dev/"]
---

# Feature Stores and ML Features

## Summary

Feature stores centralize feature definition, computation, and serving.
They bridge batch and real-time feature pipelines for training and inference.
Consistency between offline training and online serving is the core value.
Feature stores exist to kill training-serving skew, the classic silent model killer.

## Details

- Feature definitions are code with versioning and metadata.
- Offline store serves historical features for training.
- Online store serves low-latency features for inference.
- Point-in-time correctness prevents label leakage.
- Feast, Tecton, and platform-native stores are common options.
- Feature definitions as code enable review and reuse.
- Monitor feature drift and freshness alongside model metrics.
- Feature stores make ML features reusable assets instead of duplicated notebook logic.

## Related

- [[wiki/data-storage/offline-vs-online-stores|Offline Vs Online Stores]] — store split
- [[wiki/data-storage/recommendation-data-pipelines|Recommendation Data Pipelines]] — use case
- [[wiki/data-storage/churn-prediction-features|Churn Prediction Features]] — features
- [[wiki/data-storage/data-versioning-models|Data Versioning Models]] — versioning
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-lake|Data Lake]] — lake reference

