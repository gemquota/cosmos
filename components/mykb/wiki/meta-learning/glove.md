---
type: "concept"
title: "GloVe"
description: "Word embeddings learned from global co-occurrence statistics via matrix factorization"
tags: ["glove", "embeddings", "nlp", "representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# GloVe

## Summary
GloVe (Global Vectors) learns word vectors by factorizing a word-word co-occurrence matrix so vector arithmetic reflects co-occurrence ratios. It combined the global statistics view with local-context efficiency.

## Details
- **Mechanism** — weighted least-squares fit over log co-occurrence counts; produces static word vectors.
- **Comparison** — word2vec (local windowed sampling) vs GloVe (global counts): similar quality, different training dynamics.
- **Legacy** — like word2vec, static and context-free; a baseline for evaluating contextual embeddings.

## Related
- [[wiki/meta-learning/word2vec|Word2Vec]] — the local-context counterpart
- [[wiki/data-storage/embeddings|Embeddings]] — the category GloVe belongs to
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — contextual successors
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — GloVe vectors as transferable features
- [[wiki/meta-learning/00-index|Meta-Learning]] — representation learning family
