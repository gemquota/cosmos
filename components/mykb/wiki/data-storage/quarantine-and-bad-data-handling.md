---
type: "concept"
title: "Quarantine and Bad Data Handling"
description: "Isolating records that fail quality checks"
tags: ["quarantine", "bad-data", "data-quality", "pipelines"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quarantine and Bad Data Handling

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Quarantine tables/topics hold records that fail validation but may be repairable.
- Separate quarantine reasons: schema mismatch, constraint violation, enrichment failure.
- Repair pipelines fix and re-ingest; quarantines age out by policy.
- Visible quarantine counts make data quality measurable.

## Related

- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — quality
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — pipeline DLQ analog
- [[wiki/data-storage/dead-letter-data-and-repair-pipelines|Dead Letter Data And Repair Pipelines]] — repair flows
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — visibility
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
