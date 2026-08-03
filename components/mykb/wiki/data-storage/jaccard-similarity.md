---
type: "concept"
title: "Jaccard Similarity"
description: "Set-overlap metric defined as intersection size over union size"
tags: ["jaccard", "similarity", "sets", "metrics"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Jaccard Similarity

## Summary
Jaccard similarity scores two sets as |A ∩ B| / |A ∪ B|, from 0 (disjoint) to 1 (identical). It is the standard metric for token or shingle sets, where bag-of-words geometry does not apply — exact overlap, not vector angles, is what matters.

## Details
- Use cases: document deduplication over shingles (n-gram sets), tag overlap between notes, graph neighbourhood similarity, and lexical relatedness baselines; it is scale-invariant in the sense that it depends on relative overlap, not size.
- Estimation: exact computation is expensive at scale (pairwise set intersections); MinHash estimates Jaccard from small signatures cheaply, which is why large-scale deduplication pipelines use it.
- Worked example: two mykb pages sharing 3 of 10 tags score 0.3 Jaccard — a lightweight relatedness signal for suggestions; two articles with disjoint shingle sets score 0 regardless of length.
- Failure modes: applying Jaccard where semantics, not overlap, matter (synonyms share no tokens); thresholds set too low, flooding near-duplicate candidates; shingle size chosen badly (too small gives trivial matches, too large misses paraphrases); comparing sets of different granularity (characters versus words).
- Tradeoffs: Jaccard is exact, interpretable, and cheap for small sets; the alternative, cosine over embeddings, captures semantics but costs model inference; the mature pattern is Jaccard over shingles for exact-overlap detection and embeddings for semantic similarity.
- Operational notes: choose shingle size per language, calibrate thresholds, and use MinHash when the corpus outgrows exact computation.
- RSIS3 relevance: Jaccard over tags and shingles gives mykb a cheap lexical relatedness and duplicate-detection signal alongside semantic search.

## Practice
- Interpret it as a fraction of shared content: 0.5 means half of the combined elements are shared, which maps intuitively to review thresholds.
## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the vector alternative to set overlap
- [[wiki/data-storage/minhash|MinHash]] — the estimator for large sets
- [[wiki/data-storage/edit-distance|Edit Distance]] — string-level closeness vs set overlap
- [[wiki/data-storage/semantic-search|Semantic Search]] — Jaccard is a lexical relatedness baseline
- [[wiki/data-storage/00-index|Data Storage]] — similarity metrics
