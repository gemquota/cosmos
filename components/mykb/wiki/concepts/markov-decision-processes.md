---
type: "concept"
title: "Markov Decision Processes"
description: "The formal framework for sequential decisions under uncertainty"
tags: ["mdp", "decision-making", "reinforcement-learning", "planning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Markov Decision Processes

## Summary
An MDP is a tuple of states, actions, transition probabilities, rewards, and discount: the agent chooses actions to maximize expected cumulative reward, and the future depends only on the current state. It matters because it is the canonical model for sequential decision making. Planning in MDPs is solved by dynamic programming or search.

## Details
- Policies map states to actions; value functions score states.
- RL methods (TD, Q-learning, policy gradient) solve unknown MDPs.
- Agent tasks become MDPs with tool calls as actions.
- Open questions: MDP abstraction for open-ended agent tasks.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — planning in MDPs
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — belief over hidden states
- [[wiki/concepts/q-learning|Q-Learning]] — model-free solving
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — value learning
- [[wiki/concepts/utility-functions|Utility Functions]] — the reward specification
