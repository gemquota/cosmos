---
type: "concept"
title: "Cluster Analysis"
description: "Grouping items so similar ones share a cluster, revealing structure without labels"
tags: ["clustering", "unsupervised", "similarity", "groups"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Cluster Analysis

## Summary
Cluster analysis partitions a set of items — documents, embeddings, notes — so members of a cluster are more similar to each other than to outsiders. It is the unsupervised workhorse for organization, deduplication, and topic discovery.

## Details
- **Algorithms** — k-means (centroid), hierarchical (tree), DBSCAN (density), and spectral (graph); embeddings make vector clustering universal.
- **Evaluation** — internal (silhouette) and external (purity) metrics; choosing k is the eternal question.
- **Agent relevance** — clustering mykb pages by embedding would auto-suggest concept groups and detect duplication.

## Related
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — the thematic cousin of clustering
- [[wiki/data-storage/embeddings|Embeddings]] — the features clustering usually consumes
- [[wiki/memory/folksonomy|Folksonomy]] — clusters can propose tag vocabularies
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — community detection is graph clustering
- [[wiki/meta-learning/index|Meta-Learning]] — unsupervised learning family
