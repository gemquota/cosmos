---
type: "concept"
title: "Provenance"
description: "Recorded origin and chain of custody for knowledge items, enabling trust and auditability"
tags: ["provenance", "trust", "sources", "metadata", "audit"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/TR/prov-overview/"]
---

# Provenance

## Summary
Provenance answers 'where did this come from and how did it get here?' — the source URL, capture time, transformation steps, and authorship of a knowledge item. It is what lets an agent trust or discard a claim and what makes knowledge bases auditable. W3C PROV standardizes such records, and mykb's `source:` fields are a lightweight version.

## Details
- **What to record** — origin URL, retrieved-at timestamp, extractor/author, transformations applied, and links to related items.
- **Why it matters** — LLM-written wikis otherwise drift into confident fabrication; provenance lets readers and agents trace every claim to evidence.
- **Worked example** — a mykb page states 'BM25 defaults are k1=1.2, b=0.75'; its frontmatter `source:` points at the Okapi BM25 reference, so RSIS3 can verify before reusing the claim.
- **Standards** — W3C PROV offers entities, activities, and agents; lightweight alternatives are YAML frontmatter fields and git history.
- **Trade-off** — detailed provenance costs capture effort; the trick is automating it at ingest time, not after the fact.

## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — the practical home for provenance fields
- [[wiki/data-storage/data-versioning|Data Versioning]] — keeps the history behind provenance
- [[wiki/memory/git-for-notes|Git for Notes]] — git history as a provenance layer
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — a format that makes provenance a first-class field
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — curation decisions deserve provenance too
- [[wiki/data-storage/record-linkage|Record Linkage]] — connecting records while preserving provenance
- [[wiki/sources/README|Sources]] — the namespace for raw material with origins
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the loop provenance makes auditable
