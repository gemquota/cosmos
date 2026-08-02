---
type: "concept"
title: "RLHF Stages"
description: "The pipeline of supervised tuning, reward modeling, and reinforcement learning used to align models"
tags: ["rlhf", "alignment", "pipeline"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# RLHF Stages

## Summary
The pipeline of supervised tuning, reward modeling, and reinforcement learning used to align models

## Details
- Stage one: SFT on curated demonstrations. Stage two: reward model from preferences. Stage three: RL against the reward model.
- Each stage needs distinct data and evaluation.
- Methods vary: PPO, DPO, GRPO, and variants.
- Failure points: reward hacking and distribution shift.

## Related
- [[wiki/ai-ml/supervised-fine-tuning|Supervised Fine-Tuning]] — first stage
- [[wiki/ai-ml/reward-model-training|Reward Model Training]] — second stage
- [[wiki/ai-ml/preference-optimization|Preference Optimization]] — third stage family
- [[wiki/ai-ml/reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]] — umbrella
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — risk management
