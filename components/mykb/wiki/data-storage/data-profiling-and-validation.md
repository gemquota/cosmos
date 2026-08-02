---
type: "concept"
title: "Data Profiling and Validation"
description: "Understanding data before you trust it"
tags: ["profiling", "validation", "data-quality", "analysis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_profiling", "https://docs.greatexpectations.io/"]
---

# Data Profiling and Validation

## Summary

Profiling examines data to learn its shape: types, distributions, nulls, and anomalies.
Validation checks data against declared expectations.
Together they catch surprises before they reach consumers.
Profiling before modeling catches the surprises that otherwise become production incidents.

## Details

- Profile new sources: schema, cardinality, null rates, and ranges.
- Validation rules encode expectations: uniqueness, allowed values, freshness.
- Automate profiling in pipelines to detect drift.
- Results feed quality scorecards and data contracts.
- Profiling is cheap insurance against bad joins and broken marts.
- Pair profiling with anomaly detection for ongoing drift alerts.
- Share profile results in the catalog for self-serve trust.
- Profiling is cheap insurance: an hour of profiling prevents a week of debugging.

## Related

- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — dimensions
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — frameworks
- [[wiki/data-storage/data-validation-before-promotion|Data Validation Before Promotion]] — gates
- [[wiki/data-storage/data-profiling|Data Profiling]] — existing note
- [[wiki/data-storage/quarantine-and-bad-data-handling|Quarantine And Bad Data Handling]] — bad data
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

