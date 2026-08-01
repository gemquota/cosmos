---
type: "concept"
title: "Q-Learning"
description: "Off-policy TD learning of action values for optimal policies"
tags: ["q-learning", "reinforcement-learning", "value", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Q-Learning

## Summary
Q-learning learns the value of taking each action in each state, Q(s, a), using off-policy TD updates. It matters because it converges to optimal policies without a model of the environment. Deep Q-networks extended it to large state spaces.

## Details
- Update uses the max over next-state actions, making it off-policy.
- Converges for tabular settings under exploration conditions.
- DQN added experience replay and target networks.
- Open questions: value-based control in LLM agent state spaces.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — value maximization can go wrong
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — the learning rule
- [[wiki/concepts/policy-gradient|Policy Gradient]] — the policy-based alternative
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — exploration during learning
