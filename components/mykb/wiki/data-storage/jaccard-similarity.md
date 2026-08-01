---
type: "concept"
title: "Jaccard Similarity"
description: "Set-overlap metric defined as intersection size over union size"
tags: ["jaccard", "similarity", "sets", "metrics"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Jaccard Similarity

## Summary
Jaccard similarity scores two sets as `|A ∩ B| / |A ∪ B|`, from 0 (disjoint) to 1 (identical). It is the standard metric for token or shingle sets, where bag-of-words geometry does not apply.

## Details
- **Use cases** — document deduplication over shingles, tag overlap between notes, and graph neighbourhood similarity.
- **Estimation** — exact computation is expensive at scale; MinHash estimates it cheaply.
- **Worked example** — two mykb pages sharing 3 of 10 tags score 0.3 Jaccard — a lightweight relatedness signal.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the vector alternative to set overlap
- [[wiki/data-storage/minhash|MinHash]] — the estimator for large sets
- [[wiki/data-storage/edit-distance|Edit Distance]] — string-level closeness vs set overlap
- [[wiki/data-storage/semantic-search|Semantic Search]] — Jaccard is a lexical relatedness baseline
- [[wiki/data-storage/index|Data Storage]] — similarity metrics
