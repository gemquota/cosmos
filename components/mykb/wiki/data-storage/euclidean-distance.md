---
type: "concept"
title: "Euclidean Distance"
description: "Straight-line distance between vectors, sensitive to both direction and magnitude"
tags: ["euclidean", "distance", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Euclidean Distance

## Summary
Euclidean (L2) distance measures the straight-line gap between two vectors. It is the natural metric when absolute position matters, and for normalized embeddings it orders results similarly to cosine — smaller is more similar.

## Details
- Formula: |a-b| = sqrt(sum((a_i - b_i)^2)); it is sensitive to both direction and magnitude, so a vector that is longer but angled differently scores as far away.
- Relation to cosine: for unit-normalized vectors, minimizing L2 is equivalent to maximizing cosine — which is why many systems normalize and then use either metric interchangeably; without normalization, L2 punishes magnitude differences that cosine ignores.
- When to use: clustering, anomaly detection, and domains where magnitude is meaningful (timestamps, counts, raw feature vectors); for learned embeddings trained with cosine objectives, L2 on unnormalized vectors mixes in length noise.
- Worked example: two notes with similar content but very different lengths have a small cosine angle but a large L2 distance if unnormalized; after normalization the L2 ranking matches cosine; a cluster of activity timestamps compares naturally with L2.
- Failure modes: applying L2 to magnitude-noise embeddings, ranking by length instead of meaning; mixing metrics between index and query; thresholding L2 distances across models with different scales; ignoring the normalization state of stored vectors.
- Tradeoffs: L2 is intuitive and geometrically meaningful at the cost of magnitude sensitivity; cosine is scale-invariant and the better default for embeddings; the mature pattern is normalize embeddings and pick the metric that matches the model's training objective, applied consistently.
- Operational notes: normalize consistently, verify the metric at index creation, and calibrate distance thresholds per model.
- RSIS3 relevance: clustering wiki articles by embedding similarity uses L2 over normalized vectors — the metric choice shapes how mykb groups related knowledge.

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the angle-based alternative
- [[wiki/data-storage/dot-product|Dot Product]] — the score-based alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors distance is computed over
- [[wiki/data-storage/vector-databases|Vector Databases]] — selectable as the index metric
- [[wiki/data-storage/00-index|Data Storage]] — similarity metrics
