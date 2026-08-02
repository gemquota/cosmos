---
type: "concept"
title: "Data Versioning"
description: "Tracking changes to datasets so states are reproducible and reversible"
tags: ["versioning", "data-management", "reproducibility", "history"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://dvc.org/doc/start/data-management/data-versioning", "https://delta.io/"]
---

# Data Versioning

## Summary
Data versioning records every state of a dataset — schema, content, and transformations — so any past state can be restored or compared. It is the data-science analogue of source control and a precondition for reproducible pipelines.

## Details
- **Forms** — file snapshots, git-style commit graphs, and database temporal tables (valid-time, transaction-time).
- **Why it matters** — models and analyses are only reproducible if the data they consumed is pinned.
- **Agent relevance** — versioned wiki exports let RSIS3 compare knowledge states across improvement cycles.
- Data versioning tracks the evolution of datasets and artifacts so every state can be named, compared, and reproduced.
- Version control for data is harder than for code because data is large, binary, and often produced by pipelines rather than edited by hand.
- Content-addressed storage plus manifest files give reproducible dataset versions; tools like DVC and lakeFS make this practical.
- Versioning is the prerequisite for reproducibility, rollback, and auditing — knowing which input produced which output.
- **Worked example / comparison** — Worked example — a wiki export pipeline tags each bundle with a manifest of article hashes; a regression is traced to the exact input snapshot it was built from.
- For mykb, data versioning is documented as the layer that makes the bundle's releases reproducible and auditable.

## Related
- [[wiki/memory/git-for-notes|Git for Notes]]
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/sources/README|Sources]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/deep-dives|Deep Dives]]
