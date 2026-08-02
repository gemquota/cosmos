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
Catastrophic forgetting is the collapse of previously learned capabilities when a model is fine-tuned on new data. It matters because SFT and RLHF can silently destroy skills a base model had. Mitigation keeps new and old capabilities alive simultaneously.

## Details
- **Symptoms** — drop in general reasoning or safety behavior after narrow fine-tuning; benchmark regression on old tasks.
- **Mitigations** — mixing general data into the fine-tune set, replay of old examples, low-rank adapters that limit weight change, and elastic weight consolidation.
- **Worked example** — before SFT on coding data, keep 10-20% general instruction data; measure general benchmarks before and after.
- **Evaluation** — continual-learning and regression suites catch forgetting before deployment.
- **mykb relevance** — mykb fine-tunes on personal knowledge; forgetting general capability would be a visible regression.
- **Order matters** — interleave new and old data rather than training new data in one long block, which amplifies forgetting.
- **Selection** — choose replay examples that cover the skill space (reasoning, code, safety) rather than random samples.

## Related
- [[wiki/ai-ml/supervised-fine-tuning|Supervised Fine-Tuning]] — source of forgetting
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — bounded weight updates
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression detectors
- [[wiki/testing/evals-harness|Evals Harness]] — running checks
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — rehearsal via distillation
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — related concept in this cluster
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — memory consolidation research
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — fine-tuning practice
