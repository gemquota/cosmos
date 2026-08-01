---
type: "concept"
title: "Deduplication"
description: "Removing or merging records that represent the same underlying thing"
tags: ["deduplication", "cleanup", "data-quality", "curation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Deduplication

## Summary
Deduplication finds and merges records that are the same entity or content, whether by exact hash, near-duplicate fingerprinting, or fuzzy matching. It is the hygiene step that keeps curated knowledge bases and databases trustworthy.

## Details
- **Levels** — exact (hash equality), near-duplicate (MinHash, SimHash), and semantic (embedding similarity plus confirmation).
- **Trade-off** — aggressive merging loses information and provenance; conservative merging leaves noise.
- **Agent relevance** — mykb's curation should dedupe concept pages created from different sessions about the same idea.

## Related
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]] — hash-based exact deduplication
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — merging records of the same real-world entity
- [[wiki/data-storage/minhash|MinHash]] — fingerprinting for near-duplicate detection
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — deduplication is a curation operation
- [[wiki/data-storage/index|Data Storage]] — storage hygiene concepts
