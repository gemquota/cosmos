---
type: "concept"
title: "Euclidean Distance"
description: "Straight-line distance between vectors, sensitive to both direction and magnitude"
tags: ["euclidean", "distance", "metrics", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Euclidean Distance

## Summary
Euclidean (L2) distance measures the straight-line gap between two vectors. It is the natural metric when absolute position matters, and for normalized embeddings it orders results similarly to cosine.

## Details
- **Formula** — `|a-b| = sqrt(sum((a_i - b_i)^2))`; smaller is more similar.
- **Relation to cosine** — for unit-normalized vectors, minimizing L2 is equivalent to maximizing cosine.
- **When to use** — clustering, anomaly detection, and domains where magnitude is meaningful (e.g., timestamps, counts).

## Related
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the angle-based alternative
- [[wiki/data-storage/dot-product|Dot Product]] — the score-based alternative
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors distance is computed over
- [[wiki/data-storage/vector-databases|Vector Databases]] — selectable as the index metric
- [[wiki/data-storage/index|Data Storage]] — similarity metrics
