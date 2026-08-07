---
type: "concept"
title: "Catastrophic Forgetting Mitigation"
description: "Techniques that prevent fine-tuned or continually trained models from losing prior knowledge"
tags: ["forgetting", "fine-tuning", "continual-learning", "stability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1902.10407", "https://arxiv.org/abs/2212.04839"]
---

# Catastrophic Forgetting Mitigation

## Summary
Catastrophic forgetting is the collapse of previously learned capabilities when a model is fine-tuned on new data. It matters because supervised fine-tuning and RLHF can silently destroy skills a base model had. Mitigation keeps new and old capabilities alive simultaneously, and it is a routine part of any continual-learning pipeline.

## Details
- **Symptoms** — a drop in general reasoning or safety behavior after narrow fine-tuning, or benchmark regression on old tasks; the damage is silent until the old task is tested again.
- **Data mixing** — mixing general data into the fine-tune set keeps the model practiced on old distributions; a common rule of thumb is 10-20% general instruction data before task-specific data.
- **Replay** — rehearse old examples during training; replay sets should cover the skill space (reasoning, code, safety) rather than random samples, because random replay over-represents easy examples.
- **Bounded updates** — low-rank adapters limit the weight-change surface; elastic weight consolidation and other regularization methods penalize movement on parameters important to old tasks.
- **Order matters** — interleave new and old data rather than training new data in one long block, which amplifies forgetting; curriculum order is a cheap and effective lever.
- **Evaluation** — continual-learning and regression suites catch forgetting before deployment; golden test sets of old capabilities are the minimal guard.
- **Worked example** — before supervised fine-tuning on coding data, keep general instruction data in the mix and run general benchmarks before and after; any regression on the general suite blocks the release until mixing is adjusted.

- **For mykb** — the wiki fine-tunes on personal knowledge; forgetting general capability would be a visible regression, so mitigations are part of the continual-learning practice rather than a one-off fix.
## Related
- [[wiki/ai-ml/catastrophic-forgetting|Catastrophic Forgetting]] — the failure being mitigated
- [[wiki/ai-ml/continual-learning|Continual Learning]] — the umbrella discipline
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — bounded weight updates
- [[wiki/ai-ml/supervised-fine-tuning|Supervised Fine-Tuning]] — a source of forgetting
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression detectors
- [[wiki/concepts/regularization-practice|Regularization Practice]] — stability mechanisms
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — rehearsal via distillation
