---
type: "concept"
title: "Mixture-of-Experts Architectures"
description: "Model architecture that routes tokens through a subset of expert networks per layer"
tags: ["moe", "architecture", "sparse", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Mixture-of-Experts Architectures

## Summary
Model architecture that routes tokens through a subset of expert networks per layer

## Details
- Gating networks route each token to a few experts, keeping compute per token low.
- MoE scales parameters without scaling active FLOPs.
- Routing load imbalance and memory overhead are key challenges.
- Powers many frontier open models.

## Related
- [[wiki/ml-frameworks/sparse-experts|Sparse Experts]] — mechanism detail
- [[wiki/ml-frameworks/dense-vs-sparse-models|Dense vs Sparse Models]] — comparison
- [[wiki/ml-frameworks/routing-models|Routing Models]] — routing concept
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — serving MoE models
- [[wiki/ai-ml/model-capabilities-frontier|Model Capabilities Frontier]] — frontier role
