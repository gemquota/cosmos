---
type: "concept"
title: "Data Versioning Models"
description: "Versioning datasets, schemas, and code together"
tags: ["data-versioning", "models", "reproducibility", "mlops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Versioning Models

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Version datasets, features, models, and code so results are reproducible.
- Options: copy-based (DVC), pointer-based (lakeFS), and table-snapshot (Delta/Iceberg).
- Version IDs should propagate into artifacts and metrics logs.
- Reproducibility is a continuum; choose depth by audit need.

## Related

- [[wiki/data-storage/data-versioning|Data Versioning]] — data versioning
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — snapshot formats
- [[wiki/data-storage/lakefs-and-git-for-data|Lakefs And Git For Data]] — lakeFS
- [[wiki/infrastructure/dataset-release-processes|Dataset Release Processes]] — release practice
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
