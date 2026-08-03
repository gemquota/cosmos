---
type: "concept"
title: "Markov Decision Processes"
description: "The formal framework for sequential decisions under uncertainty"
tags: ["mdp", "decision-making", "reinforcement-learning", "planning"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Markov Decision Processes

## Summary
An MDP is a tuple of states, actions, transition probabilities, rewards, and discount: the agent chooses actions to maximize expected cumulative reward, and the future depends only on the current state. It matters because it is the canonical model for sequential decision making. Planning in MDPs is solved by dynamic programming or search.

## Details
- The formal tuple: (S, A, P, R, γ). S is the state set, A the action set, P(s' | s, a) the transition distribution, R(s, a, s') the reward, and γ ∈ [0,1) the discount factor that prices future reward against present reward and, critically, keeps the cumulative sum finite. The Markov property — the transition depends only on the current state and action, not on history — is what makes the model tractable: the past matters only through the state, which is why state design (what information to include) is the single most consequential modeling decision.
- Policies map states to actions; value functions score states. A policy π(a|s) is the agent's decision rule; the state-value V^π(s) is the expected discounted cumulative reward from s following π; the action-value Q^π(s,a) is the same for taking action a first. The optimal value function satisfies the Bellman equation — the value of a state is the best immediate reward plus the discounted value of where you land — and dynamic programming (value iteration, policy iteration) exploits that recursive structure to solve known MDPs exactly.
- RL methods (TD, Q-learning, policy gradient) solve unknown MDPs. When the transition and reward functions are unknown, the agent learns from experience: temporal-difference learning bootstraps value estimates from sampled transitions, Q-learning learns the optimal action-value directly, and policy-gradient methods optimize the policy by gradient ascent on expected reward. The family spans model-based (learn the model, then plan) and model-free (learn values or policies directly) approaches with different sample-efficiency and bias profiles.
- Agent tasks become MDPs with tool calls as actions. Any agent loop — observe, decide, act, get feedback — is an MDP in structure, which is why the framework generalizes from grid worlds to language-agent tool use: the state is the context plus tool results, actions are tool calls and outputs, rewards are task completion signals.
- The limitation: the Markov assumption and the state space. Real tasks have hidden state (hence POMDPs) and enormous action spaces (hence hierarchical and learned abstractions). Open question: MDP abstraction for open-ended agent tasks.
- RSIS3 relevance: each loop pass is an MDP in miniature — the registry and wiki state is the state, the proposed changes are actions, and the metric deltas are rewards; modeling it formally makes the discount (how much to value future passes) and the state design (what the loop must track) explicit.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — planning in MDPs
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — belief over hidden states
- [[wiki/concepts/q-learning|Q-Learning]] — model-free solving
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — value learning
- [[wiki/concepts/utility-functions|Utility Functions]] — the reward specification
