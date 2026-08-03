---
type: "concept"
title: "Topic Modeling"
description: "Unsupervised discovery of latent themes that explain a document collection"
tags: ["topic-modeling", "lda", "nlp", "unsupervised"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Topic Modeling

## Summary
Topic modeling learns a small set of latent topics — distributions over words — and assigns each document a mixture of them. It turns a corpus into a thematic map without labels, useful for overview, organization, and tagging suggestions.

## Details
- Models: LDA (generative, Dirichlet priors) is the canonical approach; LSA (matrix factorization) is the linear ancestor; neural variants (embedding-based clustering, BERTopic) capture semantics at more cost.
- Output: per-topic word lists give interpretable theme labels; per-document topic weights drive clustering, tagging suggestions, and navigation; coherence scores and human review validate the topics.
- Concrete example: a topic model over mykb pages surfaces themes that match the repo's clusters (devops, data-storage, prompt-engineering); a page scoring high on devops topics but low elsewhere suggests a taxonomy branch; a page fitting no topic flags a gap or an outlier for curation.
- Failure modes: topic count chosen badly, fragmenting or merging themes; stopword and preprocessing noise dominating topics; unstable topics across runs (fix the seed); treating soft weights as hard labels; small or skewed corpora producing meaningless topics.
- Tradeoffs: topic modeling is unsupervised and interpretable, cheap relative to deep alternatives, at the cost of bag-of-words blindness and tuning; the alternative, embedding-based clustering, captures semantics but is less inspectable; the mature pattern is LDA or BERTopic for broad thematic overview, with human-labeled validation.
- Operational notes: evaluate topic coherence, seed runs for reproducibility, and review topic labels before they drive curation.
- RSIS3 relevance: topic models over mykb pages could propose taxonomy branches or flag pages that fit no topic — the thematic map RSIS3 uses for gap analysis.

- Combine topic weights with human review before using them to reorganize taxonomy.
## Related
- [[wiki/data-storage/latent-dirichlet-allocation|Latent Dirichlet Allocation]] — the canonical topic model
- [[wiki/data-storage/latent-semantic-analysis|Latent Semantic Analysis]] — the matrix-factorization alternative
- [[wiki/meta-learning/cluster-analysis|Cluster Analysis]] — groups documents using topic vectors
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — topic modeling as a curation aid
- [[wiki/data-storage/index|Data Storage]] — NLP analytics family
