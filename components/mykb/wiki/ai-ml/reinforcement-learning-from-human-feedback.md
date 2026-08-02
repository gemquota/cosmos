---
type: "concept"
title: "Reinforcement Learning from Human Feedback"
description: "Using human preferences as rewards to align model behavior"
tags: ["rlhf", "alignment", "reward", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2212.03551", "https://arxiv.org/abs/2305.18290"]
---

# Reinforcement Learning from Human Feedback

## Summary
RLHF trains models to produce outputs humans prefer: a reward model learns from human comparisons, and the policy is optimized against it with reinforcement learning. It is the standard alignment technique behind instruction-following chat models. RLHF is expensive, sensitive to reward overoptimization, and increasingly supplemented by direct methods.

## Details
- **Pipeline** — collect human preference comparisons → train a reward model → run RL (typically PPO) to maximize predicted reward while a KL penalty anchors the policy.
- **Preference data** — pairwise comparisons are more reliable than absolute ratings; datasets like Anthropic Helpful-Harmless and Chatbot Arena inform collection.
- **Risks** — reward hacking, where the policy exploits reward-model quirks; KL and constraint tuning mitigate but do not eliminate it.
- **Alternatives** — DPO optimizes the same preferences without a separate RL loop; KTO and GRPO adjust the objective further.
- **Worked example** — a support model's candidate responses are ranked by humans; the reward model learns the ranking, and a PPO pass increases the probability of preferred responses.
- **mykb relevance** — RLHF, reward models, and PPO are existing mykb topics; RSIS3's preference-driven refinement mirrors the loop at system level.

## Related
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — learning the reward signal
- [[wiki/ai-ml/preference-optimization|Preference Optimization]] — optimizing preferences
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — the direct alternative
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — the pipeline stages
- [[wiki/ai-ml/rlhf|RLHF]] — existing RLHF concept
- [[wiki/ai-ml/ppo|PPO]] — PPO algorithm
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — failure mode control
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — collecting the data
