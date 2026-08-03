---
type: "concept"
title: "Word2Vec"
description: "Shallow neural models learning dense word vectors from local context"
tags: ["word2vec", "embeddings", "nlp", "representation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Word2Vec

## Summary
Word2Vec learns dense word vectors from large corpora using either skip-gram (predict context from word) or CBOW (predict word from context). Its 2013 result — vectors capturing analogies like king - man + woman ≈ queen — launched modern representation learning.

## Details
- **Architectures** — skip-gram predicts the surrounding context words from the center word; CBOW predicts the center word from the context; both train a shallow network whose hidden layer weights become the word vectors, with negative sampling or hierarchical softmax making training tractable on large corpora; the training signal is windowed co-occurrence, so words that appear in similar contexts get similar vectors.
- **Why it mattered** — the analogical structure (king - man + woman ≈ queen; Paris - France + Italy ≈ Rome) showed that vector arithmetic captures relational semantics, and the ability to pretrain embeddings on unlabeled text and reuse them in downstream models made word2vec the foundation of modern transfer learning.
- **Properties** — vectors capture both semantic similarity (synonyms cluster) and relational similarity (directions encode relationships); dimensions are not individually interpretable; frequency biases exist (rare words get worse vectors unless subword information is added); and each word has one static vector, so polysemy ('bank' as river vs financial) is conflated.
- **Legacy** — static embeddings were superseded by contextual models (ELMo, BERT, sentence-transformers) for most NLP, but word2vec remains fast to train, cheap to serve, and effective for domain-specific glossaries, sparse-data settings, and as an embedding layer for token features.
- **Failure modes** — garbage in, garbage out: vectors inherit corpus biases (gender stereotypes propagate through the analogies), small corpora produce unstable vectors, and out-of-vocabulary words have no representation without subword tricks.
- **Agent relevance** — word-level vectors remain handy for glossary terms and lightweight similarity in mykb: embedding the wiki's tag and title vocabulary with a small domain model is cheap, and word2vec-style training on the wiki corpus itself would produce a custom thesaurus for expanding search queries and detecting near-synonym concepts.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the general concept word2vec instantiates
- [[wiki/meta-learning/glove|GloVe]] — the matrix-factorization alternative
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — contextual successors
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — pretrained vectors transfer across tasks
- [[wiki/meta-learning/00-index|Meta-Learning]] — representation learning family
