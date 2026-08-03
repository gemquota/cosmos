---
type: "concept"
title: "Latent Semantic Analysis"
description: "Matrix factorization over term-document counts to uncover latent word meanings"
tags: ["lsa", "svd", "semantics", "matrix-factorization"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Latent Semantic Analysis

## Summary
Latent semantic analysis (LSA) applies singular value decomposition to a term-document matrix, projecting words and documents into a lower-dimensional semantic space where co-occurring terms are close. It is an early ancestor of modern embeddings and still useful for lightweight, interpretable semantic spaces.

## Details
- Mechanism: build a term-document matrix weighted by TF or TF-IDF; apply SVD and keep the top-k singular vectors; words and documents become vectors in the reduced space where dot products approximate semantic relatedness; queries are projected into the same space for retrieval.
- Concrete example: terms like car and automobile that rarely co-occur in the same document still land near each other because they co-occur with shared words (engine, road); a query about cars retrieves documents containing automobile — the classic synonym effect that exact lexical search misses.
- Failure modes: raw counts without weighting, letting frequent words dominate; k chosen badly (too small loses structure, too large keeps noise); sensitivity to preprocessing — stemming and stopword choice change the space; the linear, bag-of-words model missing word order and polysemy.
- Tradeoffs: LSA is fast, deterministic, and interpretable (the dimensions are linear combinations), at the cost of linearity and context blindness; the alternative, neural embeddings, captures nonlinear semantics but needs training data and is less inspectable; the mature pattern is LSA for small, transparent semantic spaces and neural embeddings for scale.
- Operational notes: weight with TF-IDF, validate k on a held-out task, and rebuild when the corpus changes.
- RSIS3 relevance: LSA gives mykb a cheap, interpretable semantic space over the wiki — a baseline that modern embeddings can be compared against.

## Practice
- Prefer TF-IDF weighting over raw counts so frequent words do not dominate the singular vectors.
## Related
- [[wiki/data-storage/latent-dirichlet-allocation|Latent Dirichlet Allocation]] — the probabilistic successor to LSA
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — LSA as an early topic approach
- [[wiki/data-storage/tf-idf|TF-IDF]] — the weighting that feeds LSA
- [[wiki/data-storage/embeddings|Embeddings]] — the modern descendant of LSA spaces
- [[wiki/data-storage/index|Data Storage]] — semantic techniques
