---
type: "concept"
title: "Cosine Similarity"
description: "Similarity of two vectors measured by the cosine of the angle between them"
tags: ["cosine", "similarity", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Cosine Similarity

## Summary
Cosine similarity scores vectors by the angle between them, ignoring magnitude — `cos(theta) = dot(a,b) / (|a||b|)`. It is the default metric for embeddings because it is scale-invariant and cheap.

## Details
- **Properties** — range -1..1 for real vectors (0..1 for non-negative); 1 means same direction, 0 orthogonal.
- **Why default** — embedding models trained with cosine objectives produce direction-meaningful vectors; magnitude is often noise.
- **Worked example** — two notes about RAG may differ in length but score 0.91 cosine on their sentence embeddings.

## Related
- [[wiki/data-storage/dot-product|Dot Product]] — the numerator of cosine similarity
- [[wiki/data-storage/euclidean-distance|Euclidean Distance]] — magnitude-sensitive alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors cosine compares
- [[wiki/data-storage/semantic-search|Semantic Search]] — ranking by cosine is the core operation
- [[wiki/data-storage/vector-databases|Vector Databases]] — stores vectors under a chosen metric
- [[wiki/data-storage/index|Data Storage]] — similarity metrics
