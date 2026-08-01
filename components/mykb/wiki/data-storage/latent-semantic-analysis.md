---
type: "concept"
title: "Latent Semantic Analysis"
description: "Matrix factorization over term-document counts to uncover latent word meanings"
tags: ["lsa", "svd", "semantics", "matrix-factorization"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Latent Semantic Analysis

## Summary
Latent semantic analysis (LSA) applies singular value decomposition to a term-document matrix, projecting words and documents into a lower-dimensional 'semantic' space where co-occurring terms are close. It is an early ancestor of modern embeddings.

## Details
- **Mechanism** — TF-weighted matrix → SVD → keep top-k singular vectors; documents and queries are projected into that space.
- **Legacy** — influenced word2vec and LDA; still useful for lightweight, interpretable semantic spaces.
- **Limits** — linear, bag-of-words, and sensitive to preprocessing; contextual models dominate today.

## Related
- [[wiki/data-storage/latent-dirichlet-allocation|Latent Dirichlet Allocation]] — the probabilistic successor to LSA
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — LSA as an early topic approach
- [[wiki/data-storage/tf-idf|TF-IDF]] — the weighting that feeds LSA
- [[wiki/data-storage/embeddings|Embeddings]] — the modern descendant of LSA spaces
- [[wiki/data-storage/index|Data Storage]] — semantic techniques
