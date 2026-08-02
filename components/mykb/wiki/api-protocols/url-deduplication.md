---
type: "concept"
title: "URL Deduplication"
description: "Detecting and merging repeated source URLs across the wiki"
tags: ["urls", "deduplication", "references", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# URL Deduplication

## Summary
URL deduplication finds the same source cited from multiple articles and detects both exact duplicates and near-duplicates that differ only in parameters or case.

## Details
- Duplicate citations are not always wrong — two articles can legitimately cite one source — but the reference records should agree on the canonical URL.
- Near-duplicate detection depends on url-normalization; without it, the report is full of false alarms.
- For mykb, URL deduplication output feeds the dedup review queue and keeps the source graph clean.

## Related
- [[wiki/api-protocols/url-normalization-wiki|URL Normalization]]
- [[wiki/api-protocols/url-formatting|URL Formatting]]
- [[wiki/data-storage/deduplication|Deduplication]]
- [[wiki/data-storage/reference-blocks|Reference Blocks]]
- [[wiki/data-storage/source-formatting|Source Formatting]]
- [[wiki/api-services/source-monitoring|Source Monitoring]]
