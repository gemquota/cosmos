---
type: "concept"
title: "DPO"
description: "Direct Preference Optimization: aligning models from preference pairs with a simple classification loss, no reward model or RL"
tags: ["dpo", "preference-tuning", "alignment", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# DPO

## Summary
DPO reframes preference alignment as a supervised loss on preference pairs, eliminating the reward model and RL loop of RLHF. It is cheaper, more stable, and widely used for open-model alignment, though it trades some expressiveness for simplicity.

## Details
The core insight of DPO is that the optimal policy under a KL-constrained reward objective can be written directly in terms of the reference policy and the preference data, so the reward model disappears entirely. Training looks like SFT with a margin-based loss: for each pair of preferred and dispreferred completions, the loss pushes the model's probability of the preferred completion above the dispreferred one, scaled by a reference-policy ratio that prevents the model from drifting too far from its starting point.

The practical payoff is a dramatically simpler pipeline. RLHF requires training a reward model, running online sampling, and tuning PPO hyperparameters such as learning rate, KL coefficient, and advantage clipping — a notoriously brittle stack. DPO runs offline on a static preference dataset with a single classification loss, so it uses far less compute and has far fewer moving parts. For most tasks, quality is competitive with PPO-based RLHF, which is why DPO became the default alignment recipe for open-weight models.

The trade-offs are real. DPO is still sensitive to data quality: noisy or inconsistent preference pairs directly corrupt the loss, and duplicate or adversarial pairs can be memorized. It can overfit preferences, amplifying sycophancy if the data rewards agreeable answers over correct ones. Because it is offline, it cannot explore new behaviour the way online RL can, so tasks that need active exploration (such as reasoning with verifiable rewards) often still prefer PPO or GRPO-style methods. A common failure mode is divergence from the reference policy on out-of-distribution inputs, which shows up as degraded style or refusal behaviour after aggressive DPO runs.

RSIS3 relevance: DPO is the practical choice for aligning locally hosted RSIS3 models on mykb preference data, because preference pairs can be curated as a static, versioned dataset and replayed without a reward-model infrastructure.

## Related
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The family DPO belongs to
- [[wiki/ai-ml/rlhf|RLHF]] — The approach DPO simplifies
- [[wiki/ai-ml/reward-model|Reward Model]] — What DPO makes unnecessary
- [[wiki/ai-ml/sft|SFT]] — The starting checkpoint DPO adjusts
- [[wiki/ai-ml/ppo|PPO]] — The RL algorithm DPO replaces
