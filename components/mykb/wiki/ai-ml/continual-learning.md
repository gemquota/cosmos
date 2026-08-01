---
type: "concept"
title: "Continual Learning"
description: "Methods for updating models on new data without destroying old capabilities — lifelong learning"
tags: ["continual-learning", "catastrophic-forgetting", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Continual Learning

## Summary
Continual learning asks how a model keeps learning across a stream of tasks without forgetting. It is the training-side counterpart to retrieval: instead of re-fetching knowledge, the model retains it.

## Details
- Families: regularization, replay/rehearsal, parameter isolation, and adapters.
- Replay from a stored corpus (e.g., a wiki) is the most practical approach for LLMs.
- Evaluation uses backward transfer (old tasks) and forward transfer (new tasks) metrics.
- RSIS3 relevance: L3 evolution is a continual-learning loop — each improvement must not regress prior capabilities.

## Related
- [[wiki/ai-ml/catastrophic-forgetting|Catastrophic Forgetting]] — The failure continual learning prevents
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The base mechanism being made continual
- [[wiki/ai-ml/sft|SFT]] — The update regime
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — A wiki is a natural replay store
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Backward-transfer evals
