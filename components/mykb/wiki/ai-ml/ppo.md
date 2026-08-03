---
type: "concept"
title: "PPO"
description: "Proximal Policy Optimization: a stable policy-gradient RL algorithm used in the RLHF training stage"
tags: ["ppo", "reinforcement-learning", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# PPO

## Summary
PPO is the RL algorithm of choice in classic RLHF: it optimizes the language-model policy against the reward model while clipping updates to stay near the reference policy. Its stability made large-scale RL fine-tuning feasible.

## Details
- **Mechanism** — PPO is an on-policy actor-critic method: it samples rollouts from the current policy, computes advantages with a learned value model plus generalized advantage estimation, and updates the policy with a clipped surrogate objective that bounds how far a single update can move the policy in probability space.
- **Clip objective** — the surrogate takes the minimum of the importance-ratio objective and its clipped variant, preventing destructive policy updates when ratios spike; a KL penalty (or adaptive KL controller) additionally keeps outputs close to the SFT model so generations do not drift into reward-model exploitation.
- **Infrastructure** — PPO requires a reward model, a value model, rollout generation across many workers, and a reference policy for the KL term; this heavy machinery is why RLHF is far more expensive than the preference-tuning alternatives.
- **Failure modes** — reward hacking (the policy finds loopholes the reward model misses), KL collapse or entropy collapse (loss of diversity), and distribution drift away from the human-preference distribution; each needs monitoring of per-token KL, entropy, and reward distribution during training.
- **Alternatives** — DPO eliminates RL by optimizing a closed-form loss over preference pairs; GRPO drops the value model by using group-relative baselines; RLOO uses a leave-one-out baseline; all trade PPO's generality for simplicity and stability.
- **RSIS3 relevance** — understanding PPO's data appetite clarifies why preference data curation matters for alignment: PPO consumes sampled generations and their rewards, so the quality, diversity, and label agreement of the preference set bound what the policy can learn, and reward-model drift is the primary thing to monitor in any RLHF-style loop.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The framework PPO powers
- [[wiki/ai-ml/reward-model|Reward Model]] — The signal PPO optimizes against
- [[wiki/ai-ml/dpo|DPO]] — The simpler alternative
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The umbrella family
- [[wiki/ai-ml/sft|SFT]] — The initialization PPO starts from
