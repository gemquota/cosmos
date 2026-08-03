---
type: "concept"
title: "Chinchilla Law"
description: "The compute-optimal scaling rule: model parameters and training tokens should grow at roughly equal rates"
tags: ["chinchilla-law", "scaling-laws", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Chinchilla Law

## Summary
Chinchilla (DeepMind, 2022) is the compute-optimal scaling result that showed most large language models were undertrained: for a fixed compute budget, the best loss comes from training larger models on proportionally more data than prior practice dictated. The headline finding — parameters and training tokens should scale at roughly equal rates — reshaped training runs toward data-heavy configurations across the industry.

## Details
- Mechanism: scaling laws model the loss as a power-law function of model size (parameters) and dataset size (tokens) under a fixed compute budget. Prior work (Kaplan et al., 2020) suggested growing parameters faster than data; Chinchilla re-derived the optimum empirically by training over 400 models of varying sizes and found the compute-optimal balance sits near a 1:1 ratio — for every doubling of parameters, roughly double the tokens. The practical consequence: for a fixed FLOPs budget, a smaller model trained on more data achieves lower loss than a larger model trained on less.
- Concrete examples: the Chinchilla model itself (70B parameters, 1.4T tokens) matched or beat much larger models (Gopher's 280B) at roughly the same compute budget; the result motivated the industry's shift to trillions of tokens for models like Llama (which published its data ratios and followed Chinchilla-style guidance) and the "scaling data is the bottleneck" framing of later training runs; a fine-tuning corollary is that more, well-curated tokens often beat a larger architecture for the same budget.
- Failure modes: the classic failure is treating Chinchilla as a universal law rather than a compute-budget optimum: if your constraint is inference cost or deployment memory (not training FLOPs), a larger model trained on fewer tokens may serve you better; if data is scarce or expensive (specialized domains), the data-side ratio is unreachable, and training beyond the compute-optimal point can still be rational. The result also applies to loss, not to downstream capability — two models at equal loss can differ on benchmarks.
- Operational tradeoffs: the rule reframes capacity planning: compute budget and data availability are joint decisions, and the guidance for small models is the same shape as for frontier ones — favor more tokens per parameter within your budget. The tradeoffs are data collection cost (curating millions of tokens is real work) versus training compute, and the inference-size tradeoff mentioned above. The practice rules: compute the Chinchilla-optimal point for your budget as a starting guess, weight data quality and decontamination when scaling data aggressively, and re-derive the balance when your constraint is inference rather than training. RSIS3 relevance: when fine-tuning small local models, Chinchilla-style guidance favors more, well-curated tokens — data quantity and curation are as strategic as architecture, which is exactly how RSIS3 treats corpus curation in its L2 loops.

## Related
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — The framework Chinchilla refines
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — Where data quantity guidance applies
- [[wiki/ai-ml/sft|SFT]] — Data-hungry supervised stage
- [[wiki/ai-ml/llama|Llama]] — Open families published with data ratios
- [[wiki/ai-ml/data-contamination|Data Contamination]] — A risk when scaling data aggressively
