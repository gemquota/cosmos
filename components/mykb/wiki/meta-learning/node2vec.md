---
type: "concept"
title: "Node2Vec"
description: "Random-walk method learning node embeddings that balance homophily and structural roles"
tags: ["node2vec", "graph-embeddings", "random-walk", "representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Node2Vec

## Summary
Node2Vec learns node embeddings by simulating biased random walks and feeding them to a word2vec-style model. Its two walk parameters, p (return) and q (in-out), let it interpolate between community-focused and role-focused embeddings.

## Details
- **Mechanism** — second-order random walks sample node neighborhoods: from each node, walkers take biased steps guided by p and q, generating sequences that act as 'sentences'; skip-gram with negative sampling learns vectors from these walk sequences, so nodes that appear in similar walk contexts land near each other.
- **Parameters** — p controls the likelihood of immediately returning to the previous node (low p keeps walkers local, emphasizing homophily — same-community closeness); q controls whether the walker moves outward or stays in a local region (low q favors breadth and structural equivalence — same-role closeness, e.g., both nodes being hubs or bridges); tuning p and q selects the notion of similarity the task needs.
- **Strengths** — scalable to large graphs (walks are cheap to generate and the skip-gram training is fast), unsupervised (no labels needed), and flexible (any graph that can be walked works, including knowledge graphs, code dependency graphs, and social networks).
- **Failure modes** — the random-walk distribution is sensitive to degree: high-degree nodes dominate the context distribution and skew embeddings; the method is transductive (new nodes require re-walking or inductive extensions); and node identity is learned without node features, so rich attributes are ignored unless concatenated separately.
- **Evaluation** — embeddings are judged by downstream tasks: link prediction (held-out edge recovery), node classification (label propagation), and clustering quality (community recovery); hyperparameters p, q, walk length, and embedding dimension need a small validation sweep per graph.
- **Uses** — link prediction and clustering over mykb-style concept graphs: embedding the wiki's wikilink graph would surface unlinked-but-related concepts (candidate [[wikilinks]]), and clustering the embeddings would expose thematic groups that page-level tags miss.

## Related
- [[wiki/meta-learning/graph-embeddings|Graph Embeddings]] — the category node2vec exemplifies
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph node2vec operates on
- [[wiki/data-storage/embeddings|Embeddings]] — the output representation type
- [[wiki/meta-learning/word2vec|Word2Vec]] — the learning machinery node2vec reuses
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — walk-based features transfer across graphs
- [[wiki/meta-learning/index|Meta-Learning]] — representation learning family
