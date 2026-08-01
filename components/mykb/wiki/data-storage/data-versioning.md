---
type: "concept"
title: "Data Versioning"
description: "Tracking changes to datasets so states are reproducible and reversible"
tags: ["versioning", "data-management", "reproducibility", "history"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Data Versioning

## Summary
Data versioning records every state of a dataset — schema, content, and transformations — so any past state can be restored or compared. It is the data-science analogue of source control and a precondition for reproducible pipelines.

## Details
- **Forms** — file snapshots, git-style commit graphs, and database temporal tables (valid-time, transaction-time).
- **Why it matters** — models and analyses are only reproducible if the data they consumed is pinned.
- **Agent relevance** — versioned wiki exports let RSIS3 compare knowledge states across improvement cycles.

## Related
- [[wiki/memory/git-for-notes|Git for Notes]] — git as a practical versioning layer
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]] — hash-addressing underlies version stores
- [[wiki/memory/provenance|Provenance]] — version history complements provenance
- [[wiki/sources/README|Sources]] — versioned raw material for the wiki
