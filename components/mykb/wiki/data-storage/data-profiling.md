---
type: "concept"
title: "Data Profiling"
description: "Discovering statistics and anomalies in datasets"
tags: ["data-profiling", "statistics", "exploration", "data-quality"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.greatexpectations.io/docs/", "https://en.wikipedia.org/wiki/Data_profiling"]
---

# Data Profiling

## Summary
Data profiling inspects a dataset to learn its shape: column types, null rates, cardinality, distributions, and outliers. It is the discovery phase before writing quality checks or building models — you cannot assert what you have not measured.

## Details
- **Column statistics** — type inference, distinct counts, min/max, mean/median, null percentage, and value frequency; database `ANALYZE`/statistics and tools like Great Expectations, Pandas Profiling (ydata-profiling), and Soda compute these per column.
- **Relationship discovery** — duplicate detection, cross-column correlations, and key inference (which columns look unique) hint at join keys and referential structure before schema design.
- **Anomaly hunting** — skewed distributions, negative values in "amount" fields, timestamps in the future, and mixed-format values (dates as strings) surface early, when fixing is cheapest.
- **Baselines** — profiling outputs become the thresholds for ongoing checks; a profile is a snapshot, and drift alerts compare new profiles to it.
- **Scale notes** — profiling full tables is expensive; sampling with a confidence bound is standard, and columnar engines profile via metadata (parquet statistics, zone maps) without scanning.
- **Workflow fit** — profile raw sources before contracting, re-profile after schema changes, and store profiles as versioned artifacts.

## Related
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — turning profiles into assertions
- [[wiki/data-storage/data-modeling|Data Modeling]] — design informed by measured data
- [[wiki/data-storage/record-linkage|Record Linkage]] — profile-driven duplicate resolution
- [[wiki/data-storage/data-observability|Data Observability]] — ongoing drift detection
- [[wiki/data-storage/data-contracts|Data Contracts]] — encoding profile findings
