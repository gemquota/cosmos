---
type: "concept"
title: "Catastrophic Forgetting"
description: "The loss of previously learned capabilities when a model is fine-tuned on a new task or distribution"
tags: ["catastrophic-forgetting", "fine-tuning", "continual-learning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Catastrophic Forgetting

## Summary
Catastrophic forgetting is the tendency of neural networks to overwrite old knowledge when trained on new data. For LLMs it shows up as degraded general ability after aggressive fine-tuning.

## Details
- More severe with high learning rates, repeated data, and narrow domains.
- Mitigations: lower learning rate, data mixing with general corpora, LoRA adapters, and rehearsal.
- Detected by running general benchmarks before/after fine-tuning, not just the target task.
- RSIS3 relevance: L2 fine-tune loops must gate against forgetting with a fixed general eval set.

## Related
- [[wiki/ai-ml/continual-learning|Continual Learning]] — The research area studying the problem
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The activity that triggers it
- [[wiki/ai-ml/sft|SFT]] — The training regime at risk
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The measurement that catches it
- [[wiki/ai-ml/dpo|DPO]] — Preference tuning can also forget
