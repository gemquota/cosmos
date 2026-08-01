---
type: "concept"
title: "Node2Vec"
description: "Random-walk method learning node embeddings that balance homophily and structural roles"
tags: ["node2vec", "graph-embeddings", "random-walk", "representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Node2Vec

## Summary
Node2Vec learns node embeddings by simulating biased random walks and feeding them to a word2vec-style model. Its two walk parameters, p (return) and q (in-out), let it interpolate between community-focused and role-focused embeddings.

## Details
- **Mechanism** — second-order random walks sample node neighborhoods; skip-gram learns vectors from walk sequences.
- **Parameters** — p favors homophily (same-community closeness), q favors structural equivalence (same-role closeness).
- **Uses** — link prediction and clustering over mykb-style concept graphs.

## Related
- [[wiki/meta-learning/graph-embeddings|Graph Embeddings]] — the category node2vec exemplifies
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph node2vec operates on
- [[wiki/data-storage/embeddings|Embeddings]] — the output representation type
- [[wiki/meta-learning/word2vec|Word2Vec]] — the learning machinery node2vec reuses
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — walk-based features transfer across graphs
- [[wiki/meta-learning/index|Meta-Learning]] — representation learning family
