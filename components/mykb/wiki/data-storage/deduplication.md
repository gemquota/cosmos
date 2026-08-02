---
type: "concept"
title: "Deduplication"
description: "Removing or merging records that represent the same underlying thing"
tags: ["deduplication", "cleanup", "data-quality", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_deduplication", "https://learn.microsoft.com/en-us/windows-server/storage/data-deduplication/overview"]
---

# Deduplication

## Summary
Deduplication finds and merges records that are the same entity or content, whether by exact hash, near-duplicate fingerprinting, or fuzzy matching. It is the hygiene step that keeps curated knowledge bases and databases trustworthy.

## Details
- **Levels** — exact (hash equality), near-duplicate (MinHash, SimHash), and semantic (embedding similarity plus confirmation).
- **Trade-off** — aggressive merging loses information and provenance; conservative merging leaves noise.
- **Agent relevance** — mykb's curation should dedupe concept pages created from different sessions about the same idea.
- Deduplication eliminates redundant data by storing one copy of identical content and referencing it from everywhere it appears.
- It works at multiple granularities — files, blocks, chunks — and pays off most where repeated copies are common: backups, container layers, and archives.
- The savings are offset by hash-computation cost and the complexity of tracking references and reclaiming unreferenced storage.
- Deduplication is distinct from compression: compression shrinks a single stream, deduplication removes cross-stream copies.
- **Worked example / comparison** — Worked example — weekly wiki backups deduplicate at chunk level, so only the changed markdown chunks consume new storage each week.
- For mykb, deduplication is documented as the storage practice behind content-addressable-storage and the wiki's archive strategy.

## Related
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]]
- [[wiki/data-storage/entity-resolution|Entity Resolution]]
- [[wiki/data-storage/minhash|MinHash]]
- [[wiki/memory/knowledge-curation|Knowledge Curation]]
- [[wiki/data-storage/index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
