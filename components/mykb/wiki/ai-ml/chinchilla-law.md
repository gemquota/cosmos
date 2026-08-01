---
type: "concept"
title: "Chinchilla Law"
description: "The compute-optimal scaling rule: model parameters and training tokens should grow at roughly equal rates"
tags: ["chinchilla-law", "scaling-laws", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Chinchilla Law

## Summary
Chinchilla (DeepMind, 2022) showed most LLMs were undertrained: for a given compute budget, the best loss comes from training larger models on proportionally more data than prior practice. The result reshaped training runs toward data-heavy configurations.

## Details
- Key result: parameters and tokens scale roughly 1:1 for compute-optimal training.
- Chinchilla (70B, 1.4T tokens) beat much larger models at the same compute budget.
- Implication: data collection is as strategic as model size for frontier training.
- RSIS3 relevance: when fine-tuning small local models, Chinchilla-style guidance favors more, well-curated tokens.

## Related
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — The framework Chinchilla refines
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — Where data quantity guidance applies
- [[wiki/ai-ml/sft|SFT]] — Data-hungry supervised stage
- [[wiki/ai-ml/llama|Llama]] — Open families published with data ratios
- [[wiki/ai-ml/data-contamination|Data Contamination]] — A risk when scaling data aggressively
