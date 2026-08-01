---
type: "concept"
title: "Record Linkage"
description: "Statistical techniques for matching records across datasets without shared identifiers"
tags: ["record-linkage", "matching", "data-integration", "statistics"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Record Linkage

## Summary
Record linkage (data matching) joins records across datasets using similarity over shared fields when no common key exists. It is the statistical machinery behind entity resolution and deduplication at scale.

## Details
- **Approaches** — deterministic rules, probabilistic scoring (Fellegi-Sunter), and learned matchers.
- **Fields** — names, dates, addresses; weights reflect how discriminating each field is.
- **Agent relevance** — linking wiki sources to the papers they cite is record linkage over bibliographic fields.

## Related
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — the goal record linkage serves
- [[wiki/data-storage/deduplication|Deduplication]] — linkage applied within one dataset
- [[wiki/memory/provenance|Provenance]] — linked records must keep their origins
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — cross-source linkage grows the graph
- [[wiki/questions/index|Open Questions]] — open questions on linkage quality
