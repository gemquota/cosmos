---
type: "concept"
title: "Direct Preference Optimization"
description: "Optimizing a policy directly on preference data without RL"
tags: ["dpo", "preference-optimization", "alignment", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.18290", "https://arxiv.org/abs/2210.11610"]
---

# Direct Preference Optimization

## Summary
Direct preference optimization (DPO) fine-tunes a model on preference pairs using a simple classification loss, removing the reward model and RL loop from RLHF. It is simpler, more stable, and cheaper to run. Its main limitation is a narrower optimization surface than RLHF.

## Details
- **Idea** — DPO shows the RLHF objective can be written as a loss on the policy itself, implicitly defining the reward.
- **Practical benefits** — no reward-model training, no PPO instability, and lower compute; works with any preference dataset.
- **Variants** — KTO handles unpaired data, GRPO samples advantages inside the loop, and other objectives adjust the reference or weighting.
- **Worked example** — a chat model is DPO-tuned on 20k preference pairs and improves judged helpfulness without a separate reward model.
- **When RLHF still wins** — tasks needing complex rewards, iterative data collection, or long-horizon objectives.
- **mykb relevance** — DPO and preference tuning are existing mykb topics; the method is a practical default for preference alignment.

## Related
- [[wiki/ai-ml/dpo|DPO]] — existing DPO concept
- [[wiki/ai-ml/kto-grpo-contextual-rl|KTO, GRPO, and Contextual RL]] — related objectives
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — data for DPO
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — skipped reward model
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — where DPO fits
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — over-optimization risk
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — preference learning
- [[wiki/ai-ml/reward-model|Reward Model]] — reward learning
