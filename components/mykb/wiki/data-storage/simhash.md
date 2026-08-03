---
type: "concept"
title: "SimHash"
description: "Hashing technique producing fingerprints where similar documents have close hashes"
tags: ["simhash", "fingerprint", "deduplication", "hamming"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# SimHash

## Summary
SimHash converts a document into a fixed-size bit fingerprint such that similar documents have fingerprints with small Hamming distance. It is a fast, deterministic near-duplicate detector used in web-scale deduplication.

## Details
- Mechanism: each token is hashed to a bit vector (e.g. 64 bits); token weights accumulate per bit position (weighted votes); the fingerprint's bit i is the sign of the accumulated vote; similar documents share most bits, so their fingerprints have small Hamming distance.
- Search: fingerprints within a Hamming radius of the query are candidates; partitioning the fingerprint space or building an inverted index on bits speeds lookup beyond brute-force scans.
- Concrete example: two copies of the same article differing by a few words produce fingerprints within a Hamming distance of a handful of bits; a crawler flags them as near-duplicates; adding or removing a paragraph shifts only the bits its words vote on.
- Failure modes: choosing a radius too large, flooding candidates; short documents with too few tokens producing unstable fingerprints; weight distribution dominated by a few tokens, biasing the fingerprint; SimHash's bag-of-words blindness to order, missing reordered duplicates.
- Tradeoffs: SimHash is blazing fast and storage-light with deterministic fingerprints; MinHash is more principled for set overlap; the mature pattern is SimHash for text-similarity at scale, with exact verification of candidates.
- Operational notes: calibrate the Hamming threshold on labeled duplicates, and always verify candidates exactly before acting.
- RSIS3 relevance: SimHash fingerprints give mykb a fast, deterministic near-duplicate detector across capture sources — the first-pass filter before curation.

- Weight tokens by importance so content words, not stopwords, drive the fingerprint bits.
## Related
- [[wiki/data-storage/locality-sensitive-hashing|Locality-Sensitive Hashing]] — SimHash is an LSH-style scheme
- [[wiki/data-storage/minhash|MinHash]] — the set-similarity alternative
- [[wiki/data-storage/deduplication|Deduplication]] — the application SimHash serves
- [[wiki/data-storage/edit-distance|Edit Distance]] — a different notion of text closeness
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — near-duplicate detection serves curation
