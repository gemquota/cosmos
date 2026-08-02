---
type: "concept"
title: "Metastore and Iceberg Catalog"
description: "Where table metadata lives in the lakehouse"
tags: ["metastore", "iceberg", "catalog", "metadata"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Metastore and Iceberg Catalog

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- The metastore/catalog maps table names to metadata locations and versions.
- Hive Metastore is the classic option; Iceberg catalogs (REST, Glue, Nessie) modernize it.
- Catalog operations (commit, snapshot, rollback) drive table evolution.
- Catalog choice affects multi-engine interoperability and governance.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — formats and catalogs
- [[wiki/data-storage/iceberg-table-format-and-versioning|Iceberg Table Format And Versioning]] — Iceberg internals
- [[wiki/data-storage/data-catalogs-and-metadata|Data Catalogs And Metadata]] — catalog ecosystem
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
