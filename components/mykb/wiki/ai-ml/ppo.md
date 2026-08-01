---
type: "concept"
title: "PPO"
description: "Proximal Policy Optimization: a stable policy-gradient RL algorithm used in the RLHF training stage"
tags: ["ppo", "reinforcement-learning", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# PPO

## Summary
PPO is the RL algorithm of choice in classic RLHF: it optimizes the language-model policy against the reward model while clipping updates to stay near the reference policy. Its stability made large-scale RL fine-tuning feasible.

## Details
- Clip objective prevents destructive policy updates; a KL penalty keeps outputs close to the SFT model.
- Requires reward model, value model, and rollout machinery — heavy infrastructure.
- Alternatives (DPO, GRPO, RLOO) simplify or replace parts of the stack.
- RSIS3 relevance: understanding PPO's data appetite clarifies why preference data curation matters for alignment.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The framework PPO powers
- [[wiki/ai-ml/reward-model|Reward Model]] — The signal PPO optimizes against
- [[wiki/ai-ml/dpo|DPO]] — The simpler alternative
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The umbrella family
- [[wiki/ai-ml/sft|SFT]] — The initialization PPO starts from
