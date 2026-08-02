---
type: "concept"
title: "Data Lake File Layouts"
description: "Organizing directories and files for scan efficiency"
tags: ["data-lake", "file-layout", "partitioning", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Lake File Layouts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Layout answers: partition columns, file sizes, compression, and directory depth.
- Hive-style partitions (date=2026-08-02) enable cheap pruning; hidden partitioning abstracts it.
- Target file sizes around 64-512MB to balance parallelism and metadata overhead.
- Table formats manage layout automatically, but physical partitioning still matters.

## Related

- [[wiki/data-storage/data-lake|Data Lake]] — lake fundamentals
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — partitioning
- [[wiki/data-storage/small-file-problem-and-compaction|Small File Problem And Compaction]] — file size management
- [[wiki/data-storage/data-lake-zones-and-layouts|Data Lake Zones And Layouts]] — zone layout
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
