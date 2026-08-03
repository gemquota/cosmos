---
type: "concept"
title: "Dictionary Learning for AI"
description: "Decomposing activations into sparse feature dictionaries"
tags: ["dictionary-learning", "features", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dictionary Learning for AI

## Summary
Dictionary learning finds a sparse decomposition of a vector space: each activation is a few features from a large dictionary. In interpretability, the goal is to factor the dense, unreadable activation space of a neural network into a sparse set of features — directions that correspond to human-understandable concepts — so the model's internals can be described in terms of what they represent rather than raw coordinates.

## Details
- The mathematical setup: given a matrix of activation vectors, learn an overcomplete dictionary (many more basis directions than dimensions) such that every activation is approximately a sparse linear combination of a few dictionary elements. Sparsity is the load-bearing assumption — it is what forces the decomposition to find meaningful structure, because a dense decomposition has infinitely many equally valid factorizations and no reason to pick interpretable ones.
- In interpretability it recovers interpretable features from model activations; sparse autoencoders are the current implementation. An SAE is a neural network with a wide, sparsely activated bottleneck trained to reconstruct activations; the bottleneck units are the candidate features. Training involves three competing objectives — reconstruction fidelity, sparsity, and the interpretability of the resulting features — and the practical art is balancing them: too much sparsity pressure produces dead or duplicated features, too little reproduces the dense, polysemantic mess the method was meant to dissolve.
- Dictionary quality is judged by sparsity, reconstruction error, and feature interpretability. The first two are measurable; the third requires human evaluation or automated proxies (does the feature fire on coherent, nameable contexts?). A feature is only useful if its activation pattern is stable across inputs and models — features that appear in one training run and vanish in the next are not facts about the model family, they are artifacts of the decomposition.
- The central motivation is polysemanticity: individual neurons in real models fire for many unrelated concepts, so neuron-level analysis cannot find clean units of meaning. Dictionary learning dissolves polysemantic neurons into a larger set of monosemantic features, at the cost of far more units to study — the known scaling problem where frontier models need enormous dictionaries.
- RSIS3 relevance: sparse semantic features could improve graph search and deduplication — representing wiki topics as sparse feature vectors would make near-duplicate detection and retrieval ranking more robust than raw embedding similarity.

## Related
- [[wiki/concepts/sae-research|SAE Research]] — the implementation
- [[wiki/concepts/superposition-research|Superposition Research]] — why decomposition is needed
- [[wiki/concepts/linear-probes|Linear Probes]] — the simpler cousin
- [[wiki/concepts/polysemanticity|Polysemanticity]] — the motivation
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]]
