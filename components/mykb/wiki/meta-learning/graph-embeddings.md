---
type: "concept"
title: "Graph Embeddings"
description: "Low-dimensional vector representations of graph nodes, edges, or subgraphs"
tags: ["graph-embeddings", "node2vec", "representation", "graphs"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Graph Embeddings

## Summary
Graph embeddings map nodes (or whole graphs) into vector space so structural similarity becomes geometric proximity. They let standard vector machinery — clustering, similarity search — operate on relational data.

## Details
- **Approaches** — random-walk (node2vec, DeepWalk), matrix factorization (spectral), and message-passing (GNNs).
- **Uses** — link prediction, node classification, community detection, and graph retrieval.
- **Agent relevance** — embedding mykb's co-occurrence graph would surface structurally similar concepts, complementing text embeddings.

## Related
- [[wiki/meta-learning/node2vec|Node2Vec]] — the canonical random-walk method
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph structure being embedded
- [[wiki/data-storage/embeddings|Embeddings]] — the general representation concept
- [[wiki/data-storage/property-graph|Property Graph]] — an input graph type for embedding
- [[wiki/meta-learning/index|Meta-Learning]] — representation learning family
