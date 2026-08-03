---
type: "concept"
title: "Superposition Research"
description: "Studying how networks pack many features into few dimensions"
tags: ["superposition", "features", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Superposition Research

## Summary
Superposition research studies how neural networks store more features than dimensions, exploiting sparsity and correlation structure. The phenomenon is the mathematical engine behind polysemanticity: a network with, say, 1000 dimensions but 5000 features to represent does not fail — it packs the features into nearly orthogonal directions, accepting small interference, because high-dimensional space has room for many approximately independent directions.

## Details
- The basic result: in high-dimensional spaces, you can represent many more directions than dimensions if the features are sparse (each input activates few features) and have correlation structure (features rarely co-occur). The network exploits this by assigning each feature a direction, accepting that directions are not perfectly orthogonal — the interference between features is small when they rarely co-occur, which is exactly the regime most real features live in. The packing is a tradeoff: the network could use dimensions inefficiently (one feature per dimension, wasteful) or pack densely (interference, but far more capacity), and it optimizes for the packing that best serves the training objective.
- It explains polysemanticity and motivates dictionary learning as the recovery tool. Because features share dimensions, a single unit (dimension) carries many features — the polysemantic neuron — and its response pattern is a mixture. The recovery implication: you cannot read features off individual units; you must decompose the activation space, which is precisely what dictionary learning and sparse autoencoders do. Superposition is why interpretability moved from "describe the unit" to "recover the features".
- The research program quantifies the phenomenon: toy models show when networks choose superposition over dense representation (it depends on feature sparsity, importance, and correlation), how interference scales, and what packing geometries emerge. Those toy results then guide interpretation of real networks — predicting where polysemanticity should appear and how much decomposition is needed.
- Understanding superposition bounds what can be read out of a model linearly. If features are packed with interference, a linear readout (a probe) sees the interference as noise or as spurious correlations — which is why probe results need control tasks and why feature recovery needs nonlinear decomposition rather than simple linear readout.
- RSIS3 relevance: superposition thinking applies to dense embedding spaces in the graph — if wiki topic embeddings pack many topics per dimension, then similarity scores are mixtures and retrieval needs the same decomposition discipline rather than raw cosine search.

## Related
- [[wiki/concepts/polysemanticity|Polysemanticity]] — the observable effect
- [[wiki/concepts/dictionary-learning-ai|Dictionary Learning for AI]] — the recovery method
- [[wiki/concepts/feature-double-counting|Feature Double-Counting]] — a failure mode
- [[wiki/concepts/sae-research|SAE Research]] — empirical side
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]]
