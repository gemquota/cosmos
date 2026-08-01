---
type: "concept"
title: "DPO"
description: "Direct Preference Optimization: aligning models from preference pairs with a simple classification loss, no reward model or RL"
tags: ["dpo", "preference-tuning", "alignment", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# DPO

## Summary
DPO reframes preference alignment as a supervised loss on preference pairs, eliminating the reward model and RL loop of RLHF. It is cheaper, more stable, and widely used for open-model alignment.

## Details
- Core insight: the optimal policy can be expressed directly from the reference policy and preference data.
- Training looks like SFT with a margin-based loss between preferred and dispreferred completions.
- Less compute and fewer moving parts than PPO; quality is competitive for most tasks.
- Still sensitive to data quality and can overfit preferences, including sycophancy.
- RSIS3 relevance: DPO is the practical choice for aligning locally hosted RSIS3 models on mykb preference data.

## Related
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The family DPO belongs to
- [[wiki/ai-ml/rlhf|RLHF]] — The approach DPO simplifies
- [[wiki/ai-ml/reward-model|Reward Model]] — What DPO makes unnecessary
- [[wiki/ai-ml/sft|SFT]] — The starting checkpoint DPO adjusts
- [[wiki/ai-ml/ppo|PPO]] — The RL algorithm DPO replaces
