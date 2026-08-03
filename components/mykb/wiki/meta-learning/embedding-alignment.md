---
type: "concept"
title: "Embedding Alignment"
description: "Mapping embeddings from different spaces or languages into a shared coordinate frame"
tags: ["embedding-alignment", "embeddings", "mapping", "multilingual"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Embedding Alignment

## Summary
Embedding alignment learns a transformation between two embedding spaces — different models, languages, or modalities — so comparable items land near each other. It enables cross-lingual retrieval and model-agnostic vector search.

## Details
- **Approaches** — (1) linear/procrustes alignment from known pairs: given anchor pairs, fit an orthogonal transformation that maps one space onto the other; (2) unsupervised adversarial alignment: train a discriminator to confuse the two spaces without paired anchors; (3) multilingual training: train a single encoder on many languages so alignment is baked in rather than learned post hoc.
- **Why it works** — embedding spaces for the same kind of data tend to share geometric structure: word2vec spaces across languages are approximately isomorphic, so a linear map found on a few hundred anchors generalizes to the whole vocabulary; the same trick works between different models trained on similar data.
- **Uses** — cross-lingual search (query in one language, retrieve documents in another), comparing embeddings from different models (migrating an index between embedders without re-embedding), and multimodal alignment (images and text into one space).
- **Caveats** — alignment quality depends on the spaces' compatibility: unrelated objectives may not align cleanly, anchor quality dominates the result (a few bad pairs wreck the map), and the transformation is only meaningful for items in the shared semantic domain; out-of-domain items land arbitrarily.
- **Evaluation** — alignment is measured by retrieval accuracy on a held-out bilingual test set, by nearest-neighbour agreement across spaces, or by the residual error of the map on anchor pairs; retrieval metrics matter more than map error because a low-error map can still misrank.
- **mykb relevance** — if the wiki ever migrates its embedding model, alignment makes the transition smooth: a fitted map lets the old index stay queryable during the swap, and bilingual alignment could let RSIS3 retrieve across the English wiki and translated or code-domain content in one vector store.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — the spaces being aligned
- [[wiki/meta-learning/word2vec|Word2Vec]] — classic testbed for cross-lingual alignment
- [[wiki/meta-learning/graph-embeddings|Graph Embeddings]] — aligning graph and text spaces
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — alignment is a transfer mechanism
- [[wiki/meta-learning/00-index|Meta-Learning]] — representation learning family
