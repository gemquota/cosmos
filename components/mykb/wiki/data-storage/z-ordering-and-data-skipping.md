---
type: "concept"
title: "Z-Ordering and Data Skipping"
description: "Multidimensional clustering that makes scans skip irrelevant files"
tags: ["z-ordering", "data-skipping", "clustering", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Z-Ordering and Data Skipping

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Z-ordering maps multiple sort columns onto a space-filling curve, clustering similar rows.
- Zone maps per file then let engines skip files that cannot match predicates.
- It helps most on correlated filter columns (e.g., region + date).
- Rewrite cost during clustering trades write overhead for read speed.

## Related

- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — metadata skipping
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — pruning fundamentals
- [[wiki/data-storage/bucketing-and-clustering-in-tables|Bucketing And Clustering In Tables]] — clustering family
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — zone maps
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
