---
type: "concept"
title: "Curriculum Learning for LLMs"
description: "Ordering training examples from easy to hard to improve learning efficiency and final quality"
tags: ["curriculum", "training", "learning", "ordering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.14165", "https://arxiv.org/abs/2108.07258"]
---

# Curriculum Learning for LLMs

## Summary
Curriculum learning structures training data so models first learn simple patterns and gradually face harder ones. It matters because naive random ordering can slow convergence and yield weaker fine-tuned models. For LLMs, curricula appear in instruction tuning and reasoning training.

## Details
- **Design** — difficulty metrics (length, noise, reasoning steps) schedule when examples appear.
- **LLM specifics** — start with well-formed instruction data, then add reasoning-heavy and edge-case examples.
- **Worked example** — math SFT: arithmetic first, then multi-step word problems, then competition problems.
- **Risks** — poorly chosen curricula can reinforce biases; pacing must be monitored with eval curves.
- **mykb relevance** — fine-tuning on personal knowledge can be scheduled from familiar to novel domains.
- **Monitoring** — track eval curves per difficulty band so pacing problems are visible before training ends.
- **Risks** — poorly chosen curricula can bake in biases; keep distributional checks on the final dataset.
- **Worked example** — math SFT: arithmetic first, then multi-step word problems, then competition problems, each stage checkpointed and evaluated.

## Related
- [[wiki/ai-ml/supervised-fine-tuning|Supervised Fine-Tuning]] — training context
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — fine-tuning family
- [[wiki/prompt-engineering/least-to-most-prompting|Least-to-Most Prompting]] — prompting analog
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — monitoring curricula
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — data source
- [[wiki/ai-ml/continual-learning|Continual Learning]] — sibling paradigm
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — instruction tuning
