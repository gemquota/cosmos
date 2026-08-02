---
type: "concept"
title: "Bucketing and Clustering in Tables"
description: "Physical grouping of rows to speed joins and aggregations"
tags: ["bucketing", "clustering", "table-design", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Bucketing and Clustering in Tables

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Bucketing hash-partitions rows by key into fixed buckets, enabling shuffle-free joins.
- Clustering (Delta liquid clustering, Iceberg sort order) co-locates similar values.
- Both improve pruning and reduce scan volume for keyed queries.
- Buckets are static; clustering adapts as data changes.

## Related

- [[wiki/data-storage/clustered-tables|Clustered Tables]] — clustering concept
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — partitioning
- [[wiki/data-storage/broadcast-joins-and-bucketing|Broadcast Joins and Bucketing]] — join benefits
- [[wiki/data-storage/z-ordering-and-data-skipping|Z Ordering And Data Skipping]] — related co-location
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
