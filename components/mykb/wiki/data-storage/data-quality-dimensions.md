---
type: "concept"
title: "Data Quality Dimensions"
description: "The measurable aspects of data fitness for use"
tags: ["data-quality", "dimensions", "metrics", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_quality", "https://docs.greatexpectations.io/"]
---

# Data Quality Dimensions

## Summary

Data quality dimensions are the categories used to assess fitness: completeness, accuracy, consistency, timeliness, and more.
Each dimension maps to concrete, automated checks.
Quality is contextual: the bar depends on how data is used.
Quality requirements differ by use case: a field acceptable for trends may be fatal for billing.

## Details

- Completeness: how much expected data is present.
- Accuracy: how well data reflects reality.
- Consistency: agreement across sources and definitions.
- Timeliness: freshness relative to need.
- Uniqueness, validity, and integrity round out the standard set.
- Attach quality SLAs to data contracts, not just to teams.
- Measure dimensions continuously; spot checks miss drift.
- Quality dimensions give teams a shared vocabulary for what 'good' means for a dataset.

## Related

- [[wiki/data-storage/data-profiling-and-validation|Data Profiling and Validation]] — measuring
- [[wiki/data-storage/table-health-and-quality-metrics|Table Health And Quality Metrics]] — scorecards
- [[wiki/data-storage/dq-frameworks-and-great-expectations|Dq Frameworks And Great Expectations]] — tooling
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — existing note
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — monitoring
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

