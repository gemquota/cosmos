---
type: "concept"
title: "Dictionary Learning for AI"
description: "Decomposing activations into sparse feature dictionaries"
tags: ["dictionary-learning", "features", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dictionary Learning for AI

## Summary
Dictionary learning finds a sparse decomposition of a vector space: each activation is a few features from a large dictionary.

## Details
- Dictionary learning finds a sparse decomposition of a vector space: each activation is a few features from a large dictionary.
- In interpretability it recovers interpretable features from model activations; sparse autoencoders are the current implementation.
- Dictionary quality is judged by sparsity, reconstruction error, and feature interpretability.
- RSIS3 relevance: sparse semantic features could improve graph search and deduplication.

## Related
- [[wiki/concepts/sae-research|SAE Research]] — the implementation
- [[wiki/concepts/superposition-research|Superposition Research]] — why decomposition is needed
- [[wiki/concepts/linear-probes|Linear Probes]] — the simpler cousin
- [[wiki/concepts/polysemanticity|Polysemanticity]] — the motivation
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — existing graph context
