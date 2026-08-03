---
type: "concept"
title: "Dot Product"
description: "Scalar sum of element-wise vector products, the raw score behind cosine similarity"
tags: ["dot-product", "similarity", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Dot Product

## Summary
The dot product a·b = sum(a_i * b_i) is the simplest vector similarity: high when vectors are large and aligned. It is used directly for retrieval when vectors are normalized or when magnitude carries meaning — the raw score behind cosine similarity.

## Details
- Relation to cosine: cosine is the dot product of unit-normalized vectors; many systems normalize embeddings once at write time and then use the dot product, since the two are identical for unit vectors; this is why vector databases expose inner-product distance as an option.
- When to use: fast inner-product search, recommendation-style scoring, and models trained with dot-product objectives (many matrix-factorization and dense-retrieval models); magnitude carries real signal in such domains.
- Caveat: unnormalized dot products reward long vectors — a large-but-unrelated vector can outscore a small-but-relevant one; if the model's training objective was cosine or normalized dot product, applying raw dot product biases results.
- Worked example: two normalized embedding vectors at 0.91 cosine have a 0.91 dot product; without normalization, a long vector of mostly noise can score higher; normalizing before indexing removes the bias.
- Failure modes: mixing metrics — cosine-trained vectors searched with raw inner product; normalization applied at query time but not write time (or vice versa), making scores inconsistent; dot product compared against cosine thresholds, misranking results.
- Tradeoffs: the dot product is the cheapest similarity score (one pass, no division) and is index-friendly, at the cost of magnitude sensitivity; the alternative, cosine, normalizes that away at the price of an extra normalization step; the mature pattern is normalize at write and query, then use dot product consistently.
- Operational notes: verify the index metric matches the model's objective, normalize consistently, and calibrate thresholds per model.
- RSIS3 relevance: mykb's semantic search over article embeddings uses dot product over normalized vectors — the same score behind cosine retrieval.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — dot product after normalization
- [[wiki/data-storage/euclidean-distance|Euclidean Distance]] — the geometric distance alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors being multiplied
- [[wiki/data-storage/vector-databases|Vector Databases]] — metric choice happens at index creation
- [[wiki/data-storage/index|Data Storage]] — similarity metrics
