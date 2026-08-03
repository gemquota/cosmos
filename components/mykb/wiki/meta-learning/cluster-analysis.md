---
type: "concept"
title: "Cluster Analysis"
description: "Grouping items so similar ones share a cluster, revealing structure without labels"
tags: ["clustering", "unsupervised", "similarity", "groups"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Cluster Analysis

## Summary
Cluster analysis partitions a set of items — documents, embeddings, notes — so members of a cluster are more similar to each other than to outsiders. It is the unsupervised workhorse for organization, deduplication, and topic discovery.

## Details
- **Algorithms** — k-means (centroid, fast but assumes spherical clusters and needs k), hierarchical (agglomerative tree, gives a dendrogram and any cut), DBSCAN (density-based, finds arbitrary shapes and noise points), and spectral (graph-based, uses the eigenstructure of a similarity matrix); embeddings make vector clustering universal because any item becomes a fixed-length vector.
- **Choosing k** — the eternal question: the elbow method and silhouette score give heuristics, but the right k depends on the downstream use — broad topic groups need fewer clusters, deduplication needs many small tight ones — so cluster count should be validated against the task, not a statistic.
- **Evaluation** — internal metrics (silhouette, Davies-Bouldin) measure compactness and separation without ground truth; external metrics (purity, adjusted Rand index, NMI) compare against known labels; internal metrics can mislead when clusters are non-convex.
- **Failure modes** — high-dimensional embeddings make distance measures noisy (the curse of dimensionality), so normalization and dimensionality reduction often precede clustering; outliers distort k-means centroids; and cluster labels are only as meaningful as the feature space, so garbage embeddings yield garbage groupings.
- **Operational use** — clustering powers near-duplicate detection, topic discovery, anomaly spotting (small or isolated clusters), and recommendation; it is also the foundation of community detection when run on knowledge-graph structure rather than raw features.
- **Agent relevance** — clustering mykb pages by embedding would auto-suggest concept groups and detect duplication: running a periodic cluster pass over wiki notes can surface orphaned pages, overlapping coverage, and candidate cross-links that manual curation would miss.

## Related
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — the thematic cousin of clustering
- [[wiki/data-storage/embeddings|Embeddings]] — the features clustering usually consumes
- [[wiki/memory/folksonomy|Folksonomy]] — clusters can propose tag vocabularies
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — community detection is graph clustering
- [[wiki/meta-learning/index|Meta-Learning]] — unsupervised learning family
