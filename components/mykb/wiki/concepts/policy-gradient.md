---
type: "concept"
title: "Policy Gradient"
description: "Learning policies directly by gradient ascent on expected reward"
tags: ["policy-gradient", "reinforcement-learning", "policy", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Policy Gradient

## Summary
Policy gradient methods optimize the policy directly: estimate the gradient of expected reward with respect to policy parameters and ascend it. They matter because they handle continuous and stochastic action spaces that value methods struggle with. Modern LLM alignment uses policy-gradient-style optimization.

## Details
- REINFORCE is the simplest estimator; actor-critic reduces variance.
- Natural gradients and PPO stabilize updates.
- RSIS3 relevance: parameter tuning from outcomes is a policy-gradient analogy.
- Open questions: credit assignment across long agent trajectories.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — the reward signal can be exploited
- [[wiki/concepts/q-learning|Q-Learning]] — the value-based alternative
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — critic learning
- [[wiki/concepts/utility-functions|Utility Functions]] — what is being maximized
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
