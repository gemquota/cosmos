---
type: "concept"
title: "Scaling Laws"
description: "Empirical power laws relating model performance to parameters, data, and compute"
tags: ["scaling-laws", "llm", "training", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Scaling Laws

## Summary
Scaling laws quantify how loss falls as models get bigger, trained on more data, with more compute. They turned model building into a predictable engineering discipline and drove the 'bigger is better' era.

## Details
- Kaplan et al. (2020) found smooth power-law improvements with parameters, data, and compute.
- Chinchilla (2022) revised the guidance: data should scale roughly equally with parameters.
- Frontier training budgets are now planned explicitly against these laws.
- RSIS3 relevance: capability expectations (and costs) for any chosen model size are forecast from scaling laws.

## Related
- [[wiki/ai-ml/chinchilla-law|Chinchilla Law]] — The compute-optimal refinement of scaling laws
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — Capability jumps attributed to scale
- [[wiki/ai-ml/gpt-4|GPT-4]] — A product of scaling-law planning
- [[wiki/prompt-engineering/context-windows|Context Windows]] — A capacity that scales with model size
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Scaling predictions are verified by evals
