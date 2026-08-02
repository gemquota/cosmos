---
type: "concept"
title: "lakeFS and Git for Data"
description: "Git-like versioning and branching for data lakes"
tags: ["lakefs", "git-for-data", "versioning", "data-lake"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.lakefs.io/", "https://dvc.org/doc"]
---

# lakeFS and Git for Data

## Summary

lakeFS brings Git semantics to object storage: branches, commits, and merges.
It enables isolated experiments and reproducible lake states.
Data versioning at lake scale changes how teams develop pipelines.
Git semantics on lakes change development workflow: review, test, merge, promote.

## Details

- Branches create zero-copy table versions via metadata.
- Commits snapshot table states; merges reconcile changes.
- CI hooks validate branches before promotion.
- Rollback restores a lake state instantly.
- Nessie and DVC are complementary approaches.
- Zero-copy branches make parallel experimentation cheap.
- Hooks enforce validation before merges.
- Git semantics for data bring review, branching, and rollback to the lake.

## Related

- [[wiki/data-storage/data-versioning-and-branching|Data Versioning and Branching]] — concepts
- [[wiki/infrastructure/ci-cd-for-data|Ci Cd For Data]] — validation
- [[wiki/infrastructure/data-deployment-strategies|Data Deployment Strategies]] — deploy
- [[wiki/data-storage/data-lake|Data Lake]] — lake
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]] — environments
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability

