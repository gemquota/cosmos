---
type: "concept"
title: "Downsampling and Retention Policies"
description: "Reducing resolution and expiring old time-series data"
tags: ["downsampling", "retention", "time-series", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Downsampling and Retention Policies

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Downsampling coarsens resolution (1s to 1m) for long-term storage.
- Retention policies delete or archive data older than a horizon.
- Tiering keeps hot recent data fast and cold history cheap.
- Balance: keep enough resolution for audits and anomaly analysis.

## Related

- [[wiki/data-storage/storage-tiering|Storage Tiering]] — tiering
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — lifecycle
- [[wiki/data-storage/time-bucketing-and-rollups|Time Bucketing And Rollups]] — coarsening
- [[wiki/data-storage/data-retention-and-lifecycle|Data Retention And Lifecycle]] — retention
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
