---
type: "concept"
title: "Embedding Alignment"
description: "Mapping embeddings from different spaces or languages into a shared coordinate frame"
tags: ["embedding-alignment", "embeddings", "mapping", "multilingual"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Embedding Alignment

## Summary
Embedding alignment learns a transformation between two embedding spaces — different models, languages, or modalities — so comparable items land near each other. It enables cross-lingual retrieval and model-agnostic vector search.

## Details
- **Approaches** — linear/procrustes alignment from known pairs, unsupervised adversarial alignment, and multilingual training.
- **Uses** — cross-lingual search, comparing embeddings from different models, and migrating indexes between embedders.
- **Caveat** — alignment quality depends on the spaces' compatibility; unrelated objectives may not align cleanly.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the spaces being aligned
- [[wiki/meta-learning/word2vec|Word2Vec]] — classic testbed for cross-lingual alignment
- [[wiki/meta-learning/graph-embeddings|Graph Embeddings]] — aligning graph and text spaces
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — alignment is a transfer mechanism
- [[wiki/meta-learning/index|Meta-Learning]] — representation learning family
