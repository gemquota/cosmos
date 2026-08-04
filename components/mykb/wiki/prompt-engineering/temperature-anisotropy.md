---
type: "concept"
title: "Temperature Anisotropy"
description: "Phenomenon where model context and probability distributions are directionally biased in embedding space"
tags: ["temperature-anisotropy", "embeddings", "theory", "context"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Temperature Anisotropy

## Summary

Temperature anisotropy is the phenomenon in which language model representations are distributed unevenly in embedding space, concentrated in a narrow cone rather than spread across dimensions. This bias distorts similarity computations and degrades retrieval and clustering quality. The concept matters because many practical systems assume embeddings behave like well-behaved vector spaces, and anisotropy breaks that assumption. Anisotropy is invisible in individual examples and shows up only in aggregate quality metrics, which is why it is often missed.

## Details

- **Definition** — anisotropy means token and sentence embeddings cluster along a few directions, so pairwise distances are dominated by a common component.
- **Causes** — model training objectives and residual stream properties encourage representations to drift toward a shared mean direction.
- **Impact on similarity** — cosine similarity becomes less informative because nearly all vectors share the same dominant orientation.
- **Impact on retrieval** — dense retrieval quality drops when high-frequency tokens and unrelated sentences score as similar.
- **Mitigations** — mean-centering, whitening, and removing the top principal components restore useful geometry.
- **Training-side fixes** — contrastive learning and regularization during training reduce anisotropy at the source.
- **Worked example** — a semantic-search index returns topically unrelated results until the embeddings are mean-centered, after which precision improves sharply.
- **Failure modes** — ignoring anisotropy leads to silent quality degradation that is invisible in single-example inspection.
- **Practical relevance** — the concept guides embedding pipeline design for search, clustering, and RAG systems.
- **Relation to calibration** — like model calibration, anisotropy is a subtle distributional property that must be measured rather than assumed.
- **Diagnostic checks** — measuring the mean vector and variance across an embedding corpus reveals anisotropy before retrieval quality visibly degrades.


## Related

- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — the impacted systems
- [[wiki/ai-ml/embeddings-alignment|Embeddings Alignment]] — the alignment solutions
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the distorted metric
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — metric choice detail
- [[wiki/ai-ml/dense-passage-retrieval|Dense Passage Retrieval]] — the affected models
- [[wiki/data-storage/embeddings|Embeddings]] — the vector storage layer

