---
type: "concept"
title: "Data License Issues"
description: "Legal problems from training data terms"
tags: ["data", "licenses", "legal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data License Issues

## Summary
Data license issues arise when training data is used beyond its license terms — scraping, redistribution, or derived models. Web-scale training makes provenance murky and disputes frequent; mitigations include documented provenance, licenses recorded at ingestion, and filtering.

## Details
- Mechanism: each dataset carries terms (public domain, permissive, restrictive, no-derivatives, no-commercial); using data beyond those terms creates legal exposure; ingestion pipelines should record license metadata at collection time, because provenance is unrecoverable later; derived models inherit questions about the data they were trained on.
- Concrete example: a scraper collects web pages with mixed licenses; one source prohibits commercial use; a commercial model trained on the corpus creates exposure; the fix is license-tagged ingestion, filtering restricted sources, and a provenance manifest for the training set.
- Failure modes: provenance lost at ingestion, making compliance impossible later; licenses assumed permissive without checking; no-derivative and share-alike terms missed; datasets re-shared without their license metadata; terms changing after collection.
- Tradeoffs: strict license filtering shrinks usable data and may bias the corpus; ignoring licenses maximizes data and creates risk; the mature pattern is documented provenance, license-aware ingestion, and periodic audits.
- Operational notes: record licenses at ingestion, keep a provenance manifest, and audit high-risk sources.
- RSIS3 relevance: raw captures in the bundle should record their source licenses — the same provenance discipline applied to the wiki's sources.

- Treat license metadata as a first-class field in the data model, not an afterthought added during audits.
- Re-verify high-risk sources on a schedule, because terms and sources change even when your own pipeline does not.
- Prefer clearly licensed sources for anything that may be redistributed, and document the license of every raw capture at ingestion time.
## Related
- [[wiki/decisions/copyright-and-ai|Copyright and AI]] — the headline issue
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — note
- [[wiki/decisions/model-license-risks|Model License Risks]] — the model side
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — the wiki practice
- [[wiki/syntheses/knowledge-synthesis-pipelines|Knowledge Synthesis Pipelines]] — the full treatment of this theme
