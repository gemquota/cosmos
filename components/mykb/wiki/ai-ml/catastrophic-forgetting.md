---
type: "concept"
title: "Catastrophic Forgetting"
description: "The loss of previously learned capabilities when a model is fine-tuned on a new task or distribution"
tags: ["catastrophic-forgetting", "fine-tuning", "continual-learning"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Catastrophic Forgetting

## Summary
Catastrophic forgetting is the tendency of neural networks to overwrite previously learned knowledge when trained on new data: gradient updates that fit the new task also destroy weights that encoded old tasks. For LLMs it appears as degraded general ability — worse coding, reasoning, or instruction following — after aggressive fine-tuning on a narrow domain.

## Details
- Mechanism: neural networks share weights across tasks, so updating weights for task B necessarily perturbs the representations that solved task A; because the new data contains no examples of A, nothing prevents the perturbation from being destructive. Severity is driven by the training regime: high learning rates and many epochs on a small, repetitive dataset overwrite more; narrow domains (e.g., only legal text) collapse the general distribution the base model was trained on. The loss is often silent — the model still passes the target task while degrading everywhere else.
- Concrete examples: a model fine-tuned on 100k medical QA pairs still answers medical questions well but loses math ability; an instruction-tuned model fine-tuned on a single style becomes terse and refuses to elaborate; a code model fine-tuned on one framework produces worse generic Python; replay-style methods (mixing in general corpora during fine-tuning) are the standard fix, and LoRA/adapters confine updates to a low-rank subspace so the base weights are barely perturbed.
- Failure modes: the classic failure is evaluating only the target task after fine-tuning — the forgetting is invisible because nobody ran the general benchmarks. The subtler failure is assuming adapters eliminate forgetting entirely: LoRA reduces but does not eliminate it, and adapter merging back into the base weights can reintroduce it. Data mixing ratios that are too small (1% general) still forget; too large (50% general) dilute the target task's learning.
- Operational tradeoffs: the mitigations — lower learning rates, fewer epochs, data mixing with general corpora, LoRA, and rehearsal/replay — trade target-task fidelity for retained generality. The practice rules: always run a fixed general eval set before and after fine-tuning (the before/after delta is the forgetting measurement); gate fine-tune acceptance on that delta, not just the target metric; and prefer adapters for narrow tasks. RSIS3 relevance: L2 fine-tune loops must gate against forgetting with a fixed general eval set — exactly the regression gate RSIS3 uses for loop improvements, where an optimization that helps one task must not degrade the rest.

## Related
- [[wiki/ai-ml/continual-learning|Continual Learning]] — The research area studying the problem
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The activity that triggers it
- [[wiki/ai-ml/sft|SFT]] — The training regime at risk
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The measurement that catches it
- [[wiki/ai-ml/dpo|DPO]] — Preference tuning can also forget
