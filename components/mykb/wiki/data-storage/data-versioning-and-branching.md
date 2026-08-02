---
type: "concept"
title: "Data Versioning and Branching"
description: "Versioning datasets and branching experiments"
tags: ["data-versioning", "branching", "dvc", "lakefs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_versioning", "https://dvc.org/doc"]
---

# Data Versioning and Branching

## Summary

Data versioning snapshots datasets so results are reproducible.
Branching lets teams experiment without touching production data.
Tooling ranges from DVC to lakeFS and Nessie.
Versioning data makes 'what did we ship last quarter' a lookup, not a reconstruction.

## Details

- Version datasets alongside code and models.
- Branch/merge data like code for safe experiments.
- Reproduce any past state from versioned pointers.
- Snapshot-based versioning costs storage; pointer-based costs metadata.
- Combine with CI to validate branches before merge.
- Branch experiments on data to de-risk changes.
- Retention of versions balances cost against audit need.
- Versioned data makes 'what changed and when' answerable in minutes.

## Related

- [[wiki/data-storage/lakefs-and-git-for-data|Lakefs And Git For Data]] — lakeFS
- [[wiki/data-storage/data-versioning-models|Data Versioning Models]] — models
- [[wiki/infrastructure/dataset-release-processes|Dataset Release Processes]] — releases
- [[wiki/data-storage/data-versioning|Data Versioning]] — existing note
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — table versioning
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability

