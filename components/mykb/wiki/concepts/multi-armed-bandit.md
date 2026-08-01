---
type: "concept"
title: "Multi-Armed Bandit"
description: "The problem of choosing among options with unknown rewards"
tags: ["bandit", "decision-making", "exploration", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Multi-Armed Bandit

## Summary
The multi-armed bandit is the sequential decision problem where each pull of an arm yields reward from an unknown distribution, and the agent must balance learning and earning. It matters because it is the cleanest model of exploration-exploitation. Many agent choices reduce to bandits.

## Details
- Regret measures how far the agent is from always picking the best arm.
- Algorithms: epsilon-greedy, UCB1, Thompson sampling.
- Contextual bandits add features per decision.
- Open questions: bandits over LLM-generated action spaces.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — bandits as a planning simplification
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — the core trade-off
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — bandits inside tree search
- [[wiki/concepts/q-learning|Q-Learning]] — the full RL generalization
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — learning from delayed reward
