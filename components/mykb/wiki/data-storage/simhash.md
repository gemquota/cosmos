---
type: "concept"
title: "SimHash"
description: "Hashing technique producing fingerprints where similar documents have close hashes"
tags: ["simhash", "fingerprint", "deduplication", "hamming"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SimHash

## Summary
SimHash converts a document into a fixed-size bit fingerprint such that similar documents have fingerprints with small Hamming distance. It is a fast, deterministic near-duplicate detector used in web-scale dedup.

## Details
- **Mechanism** — token hashes are weighted and aggregated into a bit vector; the sign of each aggregated bit forms the fingerprint.
- **Search** — fingerprints near the query's Hamming radius are candidates; partitions or inverted bits speed lookup.
- **Trade-off** — blazing speed and small storage; less principled than MinHash for set overlap.

## Related
- [[wiki/data-storage/locality-sensitive-hashing|Locality-Sensitive Hashing]] — SimHash is an LSH-style scheme
- [[wiki/data-storage/minhash|MinHash]] — the set-similarity alternative
- [[wiki/data-storage/deduplication|Deduplication]] — the application SimHash serves
- [[wiki/data-storage/edit-distance|Edit Distance]] — a different notion of text closeness
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — near-duplicate detection serves curation
