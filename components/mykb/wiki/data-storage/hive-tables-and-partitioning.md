---
type: "concept"
title: "Hive Tables and Partitioning"
description: "The legacy SQL-on-files model with static partitioning"
tags: ["hive", "partitioning", "table-format", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hive Tables and Partitioning

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Hive tables map directories to tables with partition columns as directory levels.
- Hive Metastore catalogs schemas; static partitions require explicit partition management.
- Problems: small files, strict schema evolution, and no ACID historically.
- Iceberg/Delta supersede it on lakes; Hive remains the compatibility baseline.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — modern successors
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — schema evolution limits
- [[wiki/data-storage/metastore-and-catalog-iceberg|Metastore And Catalog Iceberg]] — metastore role
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — partitioning practice
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
