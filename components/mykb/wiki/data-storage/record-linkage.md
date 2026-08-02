---
type: "concept"
title: "Record Linkage"
description: "Statistical techniques for matching records across datasets without shared identifiers"
tags: ["record-linkage", "matching", "data-integration", "statistics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Record_linkage", "https://github.com/J535D165/recordlinkage"]
---

# Record Linkage

## Summary
Record linkage (data matching) joins records across datasets using similarity over shared fields when no common key exists. It is the statistical machinery behind entity resolution and deduplication at scale.

## Details
- **Approaches** — deterministic rules, probabilistic scoring (Fellegi-Sunter), and learned matchers.
- **Fields** — names, dates, addresses; weights reflect how discriminating each field is.
- **Agent relevance** — linking wiki sources to the papers they cite is record linkage over bibliographic fields.
- Record linkage is the classic discipline of matching records across datasets that lack shared identifiers, using names, dates, and other fields.
- Probabilistic linkage assigns each field a match weight and combines them into a total score with a threshold decision.
- The tradeoff is precision versus recall: a low threshold merges too much, a high threshold misses true matches.
- Modern systems add machine-learned similarity models and human review queues for the uncertain band.
- **Worked example / comparison** — Worked example — two source records for the same paper differ in author order and title punctuation; field weights decide they match and the duplicates merge in the bibliography.
- For mykb, record linkage is documented as the statistical foundation that entity-resolution builds on.

## Related
- [[wiki/data-storage/entity-resolution|Entity Resolution]]
- [[wiki/data-storage/deduplication|Deduplication]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/questions/index|Open Questions]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
