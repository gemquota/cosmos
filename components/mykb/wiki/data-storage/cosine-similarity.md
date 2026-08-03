---
type: "concept"
title: "Cosine Similarity"
description: "Similarity of two vectors measured by the cosine of the angle between them"
tags: ["cosine", "similarity", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Cosine Similarity

## Summary
Cosine similarity scores vectors by the angle between them, ignoring magnitude — cos(theta) = dot(a,b) / (|a||b|). It is the default metric for embeddings because it is scale-invariant and cheap: direction carries the meaning in models trained with cosine objectives, and magnitude is usually noise.

## Details
- Properties: range -1..1 for real vectors (0..1 for non-negative embeddings); 1 means same direction, 0 orthogonal, -1 opposite; it measures orientation, not distance, so a short and a long vector with the same direction score identically.
- Why default: embedding models trained with cosine objectives (many sentence and doc encoders) produce direction-meaningful vectors; normalizing vectors makes cosine equivalent to the dot product, which vector databases can index efficiently.
- Worked example: two notes about RAG may differ in length but score 0.91 cosine on their sentence embeddings; a note about PostgreSQL scores lower against them because the direction differs; thresholding at 0.8 separates related from unrelated.
- Failure modes: using cosine where magnitude matters (pricing, counts, frequencies) throws information away; unnormalized vectors compared by dot product instead of cosine, conflating magnitude with similarity; threshold drift — a fixed cosine threshold behaves differently across embedding models; comparing vectors from different embedding spaces entirely.
- Tradeoffs: cosine's scale-invariance is a strength for embeddings and a weakness for magnitude-sensitive data; the alternative, euclidean distance, is sensitive to scale and length; the mature pattern is normalize embeddings at write time and use dot product or cosine consistently at query time.
- Operational notes: normalize vectors before storing, verify the metric matches the model's training objective, and calibrate thresholds per model.
- RSIS3 relevance: wiki retrieval by cosine over article embeddings is the core of semantic search in mykb — the default metric choice for the knowledge graph.

## Related
- [[wiki/data-storage/dot-product|Dot Product]] — the numerator of cosine similarity
- [[wiki/data-storage/euclidean-distance|Euclidean Distance]] — magnitude-sensitive alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors cosine compares
- [[wiki/data-storage/semantic-search|Semantic Search]] — ranking by cosine is the core operation
- [[wiki/data-storage/vector-databases|Vector Databases]] — stores vectors under a chosen metric
- [[wiki/data-storage/00-index|Data Storage]] — similarity metrics
