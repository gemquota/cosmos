---
type: "concept"
title: "Dense vs Sparse Models"
description: "Trade-offs between dense models that use all parameters per token and sparse MoE models"
tags: ["dense-sparse", "architecture", "comparison", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dense vs Sparse Models

## Summary
Trade-offs between dense models that use all parameters per token and sparse MoE models

## Details
- Dense models are simpler to serve and reason about.
- Sparse models get more capacity for similar active compute.
- Memory, batch behavior, and latency differ substantially.
- Choice depends on serving hardware and traffic patterns.

## Related
- [[wiki/ml-frameworks/moe-architectures|Mixture-of-Experts Architectures]] — sparse family
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — dense niche
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — serving implications
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — cost comparison
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — selection impact
