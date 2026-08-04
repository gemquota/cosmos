---
type: "concept"
title: "Embedding Alignment"
description: "Making embeddings from different sources or modalities comparable in one space"
tags: ["embedding-alignment", "embeddings", "alignment", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Embedding Alignment

## Summary
Embedding alignment makes vectors from different sources, models, or modalities comparable within one space. It matters because retrieval and similarity search assume a shared geometry, and mismatched embeddings silently break comparisons. Alignment is what lets one index serve text, images, and outputs from different encoders. Alignment makes embedding reuse possible across models and modalities.

## Details
- **Definition** — alignment transforms or trains embeddings so that semantically similar items from different origins sit close together in a common vector space.
- **Approaches** — shared training with paired data, learned linear projections, canonicalization into a fixed space, and cross-modal contrastive training are the main techniques.
- **Applications** — alignment enables cross-modal-retrieval, cross-model search, and unified knowledge bases where text and images are queried together.
- **Quality factors** — alignment quality depends on training pairs, the chosen metric, and the diversity of the data used to learn the mapping.
- **Drift** — aligned spaces drift as models update, so embedding-regression monitoring is needed to keep old and new vectors comparable.
- **Worked example** — a company aligns its text encoder and an image encoder so that a natural-language query retrieves matching product photos.
- **Failure modes** — spurious correlations in training pairs, metric mischoice, and unmonitored drift all degrade alignment silently.
- **Practical relevance** — alignment underpins hybrid search systems and is a prerequisite for treating multiple embedders as one index.
- **Evaluation** — alignment quality is measured with retrieval benchmarks on paired queries and targets.
- **Incremental updates** — re-aligning a subset of vectors avoids re-embedding entire corpora.
- **Worked example** — a new text encoder is projected into the existing image embedding space so both can be searched together.
- **Failure example** — aligning on one domain degrades retrieval in another, so eval sets must be domain-diverse.

## Related
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — the shared vector space
- [[wiki/llm-agents/cross-modal-retrieval|Cross-Modal Retrieval]] — the flagship application
- [[wiki/ai-ml/metric-space-cosine|Cosine Similarity]] — the metric used to compare aligned vectors
- [[wiki/ai-ml/embedding-regression|Embedding Regression]] — monitoring drift in aligned spaces
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — common tooling for aligned encoders
