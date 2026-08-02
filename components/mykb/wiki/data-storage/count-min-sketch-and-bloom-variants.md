---
type: "concept"
title: "Count-Min Sketch and Bloom Variants"
description: "Frequency and membership estimation with hashing"
tags: ["count-min-sketch", "bloom-filter", "sketches", "hashing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Count-Min Sketch and Bloom Variants

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Count-Min Sketch estimates frequencies with sublinear space and bounded overcount.
- Bloom filters answer membership with false positives but no false negatives.
- Variants: counting bloom, cuckoo, quotient filters trade space and operations.
- Both underpin caching, dedup, and analytics acceleration.

## Related

- [[wiki/data-storage/bloom-filters-and-skipping|Bloom Filters And Skipping]] — bloom fundamentals
- [[wiki/data-storage/bloom-filters-and-skipping|Bloom Filters And Skipping]] — bloom in query engines
- [[wiki/data-storage/sketch-based-analytics|Sketch Based Analytics]] — sketch family
- [[wiki/data-storage/probabilistic-data-structures|Probabilistic Data Structures]] — foundations
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
