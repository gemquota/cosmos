---
type: "concept"
title: "MinHash"
description: "Fingerprint scheme estimating Jaccard similarity between sets"
tags: ["minhash", "jaccard", "deduplication", "fingerprint"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# MinHash

## Summary
MinHash estimates the Jaccard similarity of two sets from a few minimum-hash values, making near-duplicate detection feasible over millions of items. It is the classic approach for document deduplication.

## Details
- **Idea** — the probability that two sets share a minimum hash equals their Jaccard similarity; k hashes give an unbiased estimate.
- **Pipeline** — shingle text into n-gram sets, hash, keep minima, compare signatures.
- **Agent relevance** — MinHash signatures would let mykb find near-duplicate notes across capture sources cheaply.

## Related
- [[wiki/data-storage/locality-sensitive-hashing|Locality-Sensitive Hashing]] — MinHash is an LSH family
- [[wiki/data-storage/simhash|SimHash]] — the alternative text-fingerprint scheme
- [[wiki/data-storage/jaccard-similarity|Jaccard Similarity]] — the quantity MinHash estimates
- [[wiki/data-storage/deduplication|Deduplication]] — MinHash's main application
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
- [[wiki/data-storage/embeddings|Embeddings]] — the vector-space alternative to set fingerprinting
