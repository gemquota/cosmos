---
type: "concept"
title: "Preference Optimization"
description: "Updating models so their outputs rank higher on human preferences"
tags: ["preference-optimization", "alignment", "training", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.18290", "https://arxiv.org/abs/2212.03551"]
---

# Preference Optimization

## Summary
Preference optimization adjusts a model so its outputs are more likely to be preferred by humans, given preference data. RLHF is the classic route; direct methods like DPO skip the separate reward model and RL loop. The choice between them balances complexity, stability, and data efficiency.

## Details
- **RLHF route** — train reward model, then optimize the policy with RL (PPO) while staying near a reference policy.
- **Direct route** — DPO reparameterizes the preference objective into a classification loss on the policy itself; simpler and more stable, slightly less flexible.
- **Data** — preference pairs with diverse coverage; data quality and coverage drive most of the outcome.
- **Worked example** — a writing assistant collects pairwise preference judgments on its drafts and applies DPO, improving judged win rate from 52% to 61%.
- **Evaluation** — hold-out preference accuracy, arena-style comparisons, and task evals all guard against over-optimization.
- **mykb relevance** — preference tuning and DPO are existing mykb topics; the preference loop mirrors RSIS3's refinement cycles.

## Related
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — the direct method
- [[wiki/ai-ml/reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]] — the RL method
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — the data
- [[wiki/ai-ml/kto-grpo-contextual-rl|KTO, GRPO, and Contextual RL]] — other preference objectives
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — existing preference tuning concept
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — over-optimization
- [[wiki/ai-ml/dpo|DPO]] — existing DPO concept
- [[wiki/ai-ml/arena-ranking|Arena Ranking]] — measuring preferences at scale
