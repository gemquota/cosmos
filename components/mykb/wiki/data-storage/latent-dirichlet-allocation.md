---
type: "concept"
title: "Latent Dirichlet Allocation"
description: "Generative probabilistic topic model assigning documents mixtures of topics"
tags: ["lda", "topic-modeling", "probabilistic", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Latent Dirichlet Allocation

## Summary
Latent Dirichlet allocation (LDA) models each document as a mixture of topics and each topic as a distribution over words, inferred with Bayesian methods. It is the standard baseline for topic modeling — a way to label a corpus's themes without supervision.

## Details
- Generative story: for each document, draw a topic mixture from a Dirichlet prior; for each word, draw a topic then draw the word from that topic's distribution; inference (collapsed Gibbs sampling or variational methods) inverts the story to estimate the topic-word and document-topic distributions.
- Concrete example: a wiki corpus yields topics that look like devops, data-storage, and prompt-engineering — each an interpretable word distribution; a new article scores high on devops topics and low on others, giving a soft classification for clustering and navigation.
- Practicalities: preprocessing matters (tokenize, stopwords, lemmatize); the topic count K is chosen ahead of time and validated by interpretability; results need human labeling — the word lists are not labels.
- Failure modes: K chosen badly (too many topics fragment meaning, too few merge distinct themes); noisy preprocessing (stopwords dominating topics); topics that are not stable across runs (seed the RNG and validate); treating topic proportions as ground truth for ranking; corpora too small to infer meaningful topics.
- Tradeoffs: LDA is unsupervised, interpretable, and cheap compared to modern neural topic models, but its bag-of-words assumption misses word order and context; the alternative, embeddings-based clustering, captures semantics at the cost of interpretability; the mature pattern is LDA for broad theme labeling and embeddings for fine-grained similarity.
- Operational notes: fix the seed, evaluate topic coherence, and review topic labels before using them in curation.
- RSIS3 relevance: LDA topics over the wiki give RSIS3 a stable, interpretable map of what the knowledge base covers — a curation signal for gaps and duplicates.

## Related
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — the task LDA is the classic solution to
- [[wiki/data-storage/latent-semantic-analysis|Latent Semantic Analysis]] — the linear-algebra alternative
- [[wiki/data-storage/n-grams|N-grams]] — the features LDA consumes
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — LDA topics as curation signals
- [[wiki/data-storage/index|Data Storage]] — NLP analytics family
