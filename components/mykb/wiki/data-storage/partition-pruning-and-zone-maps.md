---
type: "concept"
title: "Partition Pruning and Zone Maps"
description: "Skipping irrelevant data before scanning"
tags: ["partition-pruning", "zone-maps", "query-performance", "columnar"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Partition Pruning and Zone Maps

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Partition pruning drops whole partitions based on partition-column predicates.
- Zone maps store per-file min/max stats so scans skip files that cannot match.
- Pruning works best when predicates align with physical layout.
- Iceberg/Delta manifests and parquet statistics enable file-level skipping.

## Related

- [[wiki/data-storage/partition-pruning|Partition Pruning]] — existing note
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — metadata-driven skipping
- [[wiki/data-storage/predicate-pushdown-and-projection|Predicate Pushdown And Projection]] — related pushdowns
- [[wiki/data-storage/z-ordering-and-data-skipping|Z Ordering And Data Skipping]] — layout for better skipping
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
