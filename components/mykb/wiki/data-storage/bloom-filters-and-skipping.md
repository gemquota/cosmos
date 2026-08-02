---
type: "concept"
title: "Bloom Filters and Skipping"
description: "Probabilistic filters that skip irrelevant data"
tags: ["bloom-filter", "skipping", "query-performance", "probabilistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bloom_filter", "https://parquet.apache.org/docs/file-format/"]
---

# Bloom Filters and Skipping

## Summary

Bloom filters answer membership questions with small memory and no false negatives.
Query engines use them to skip files or rows that cannot match.
They convert full scans into index-like lookups.
Skipping is the quiet hero of columnar query performance.

## Details

- A bloom filter never says 'no' incorrectly, so skipping is safe.
- False positives only cost a little extra IO.
- Parquet and ORC store per-file/row-group bloom filters.
- Databases use them in LSM read paths.
- Tune bits-per-element for the false-positive budget.
- Bloom filters pay off on high-cardinality, rarely-matching predicates.
- Combine with zone maps for defense in depth.
- Skipping structures are what let engines read megabytes instead of terabytes.

## Related

- [[wiki/data-storage/count-min-sketch-and-bloom-variants|Count Min Sketch And Bloom Variants]] — variants
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — pruning
- [[wiki/data-storage/b-tree-and-lsm-trees|B-Trees and LSM Trees]] — LSM reads
- [[wiki/data-storage/bitmap-indexes|Bitmap Indexes]] — index family
- [[wiki/data-storage/probabilistic-data-structures|Probabilistic Data Structures]] — family
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

