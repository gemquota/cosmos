---
type: "concept"
title: "MinHash"
description: "Fingerprint scheme estimating Jaccard similarity between sets"
tags: ["minhash", "jaccard", "deduplication", "fingerprint"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# MinHash

## Summary
MinHash estimates the Jaccard similarity of two sets from a few minimum-hash values, making near-duplicate detection feasible over millions of items. It is the classic approach for document deduplication — the probability that two sets share a minimum hash equals their Jaccard similarity.

## Details
- Idea: hash each element; the minimum hash of a set is a random sample biased toward overlap; the probability that two sets share a minimum hash equals their Jaccard similarity; k independent hashes give an unbiased estimate with variance shrinking as k grows.
- Pipeline: shingle text into n-gram sets, hash the shingles, keep the k minimum hashes as the set's signature; compare signatures (or band them with LSH) to find candidate near-duplicates; verify candidates exactly.
- Concrete example: two mykb notes that differ only in formatting produce nearly identical shingle sets and similar MinHash signatures; a signature threshold flags them as near-duplicates; over a million documents, LSH banding limits exact checks to a small candidate set.
- Failure modes: too few hashes, making estimates noisy and thresholds unreliable; shingle size mismatched to the text (tiny shingles over-match, large shingles miss paraphrases); signature comparison without LSH, still O(n^2); treating MinHash estimates as exact Jaccard.
- Tradeoffs: MinHash turns an expensive pairwise comparison into small-signature estimation at a tunable accuracy cost; the alternative, exact set intersection, is exact and infeasible at scale; the mature pattern is MinHash for candidate generation plus exact verification.
- Operational notes: choose k from the variance you can tolerate, band for scale, and calibrate thresholds on labeled duplicates.
- RSIS3 relevance: MinHash signatures would let mykb find near-duplicate notes across capture sources cheaply — dedup before curation.

## Related
- [[wiki/data-storage/locality-sensitive-hashing|Locality-Sensitive Hashing]] — MinHash is an LSH family
- [[wiki/data-storage/simhash|SimHash]] — the alternative text-fingerprint scheme
- [[wiki/data-storage/jaccard-similarity|Jaccard Similarity]] — the quantity MinHash estimates
- [[wiki/data-storage/deduplication|Deduplication]] — MinHash's main application
- [[wiki/data-storage/index|Data Storage]] — similarity techniques
- [[wiki/data-storage/embeddings|Embeddings]] — the vector-space alternative to set fingerprinting
