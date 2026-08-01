---
type: "concept"
title: "Word2Vec"
description: "Shallow neural models learning dense word vectors from local context"
tags: ["word2vec", "embeddings", "nlp", "representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Word2Vec

## Summary
Word2Vec learns dense word vectors from large corpora using either skip-gram (predict context from word) or CBOW (predict word from context). Its 2013 result — vectors capturing analogies like king - man + woman ≈ queen — launched modern representation learning.

## Details
- **Architectures** — skip-gram and CBOW with negative sampling or hierarchical softmax; trained on windowed co-occurrence.
- **Legacy** — static embeddings, one vector per word, no polysemy; superseded by contextual models but still fast and useful.
- **Agent relevance** — word-level vectors remain handy for glossary terms and lightweight similarity in mykb.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the general concept word2vec instantiates
- [[wiki/meta-learning/glove|GloVe]] — the matrix-factorization alternative
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — contextual successors
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — pretrained vectors transfer across tasks
- [[wiki/meta-learning/index|Meta-Learning]] — representation learning family
