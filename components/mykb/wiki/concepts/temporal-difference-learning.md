---
type: "concept"
title: "Temporal Difference Learning"
description: "Learning from the difference between successive value estimates"
tags: ["td-learning", "reinforcement-learning", "value", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Temporal Difference Learning

## Summary
Temporal difference (TD) learning updates value estimates from the difference between successive predictions, without waiting for the final outcome. It matters because it learns online, step by step. It is the backbone of modern reinforcement learning.

## Details
- TD(0) updates: V(s) ← V(s) + α(r + γV(s') − V(s)).
- Handles delayed reward by bootstrapping from the next state.
- Extends to TD(λ), Q-learning, and actor-critic methods.
- Open questions: TD-style credit assignment in agent trajectories.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — learning objectives can be gamed
- [[wiki/concepts/q-learning|Q-Learning]] — the off-policy TD method
- [[wiki/concepts/policy-gradient|Policy Gradient]] — the policy-based alternative
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — the single-step ancestor
