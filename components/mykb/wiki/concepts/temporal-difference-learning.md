---
type: "concept"
title: "Temporal Difference Learning"
description: "Learning from the difference between successive value estimates"
tags: ["td-learning", "reinforcement-learning", "value", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Temporal Difference Learning

## Summary
Temporal difference (TD) learning updates value estimates from the difference between successive predictions, without waiting for the final outcome. It matters because it learns online, step by step. It is the backbone of modern reinforcement learning.

## Details
- The insight that made TD learning revolutionary: you do not need the final outcome to learn. After taking a step from state s to s', the agent receives reward r and can immediately compare its prediction for s (V(s)) with its updated prediction for s' (r + γV(s')). The difference between them — the temporal difference error — is a learning signal available at every step, so the agent learns continuously during an episode rather than only at its end. This is the structural difference from Monte Carlo methods, which must wait for episode completion to use the true return.
- TD(0) updates: V(s) ← V(s) + α(r + γV(s') − V(s)). The update moves the old prediction toward a better estimate built from the immediate reward plus the next state's value — bootstrapping. The parenthetical is the TD error: positive, the prediction was too low and rises; negative, it falls. The learning rate α controls step size, and the discount γ weights future value. Because every step generates an update, TD learning is sample-efficient and works in continuing (non-episodic) tasks where Monte Carlo cannot.
- Handles delayed reward by bootstrapping from the next state. The mechanism by which TD learns long-horizon tasks from immediate signals: the value of the final state, learned from the terminal reward, propagates backward one step at a time as the estimate of each earlier state is updated toward the next state's estimate. The propagation is the reason delayed reward becomes learnable — no reward needs to arrive at the current step for the current estimate to improve.
- Extends to TD(λ), Q-learning, and actor-critic methods. TD(λ) interpolates between one-step TD and Monte Carlo by propagating eligibility traces across multiple steps; Q-learning applies the TD idea to action values with an off-policy max target; actor-critic methods pair a TD-learned critic (the value estimate) with a policy actor. Every modern deep RL algorithm, from DQN to PPO, is a TD-style method under the hood — the TD error is the learning signal.
- The failure modes: bootstrapping introduces bias from the value estimate's own errors, TD updates are correlated along trajectories (needing experience replay to stabilize), and the learning signal is only as good as the reward — TD learns whatever the reward encodes, including reward hacking.
- Open question: TD-style credit assignment in agent trajectories — attributing a sparse final outcome back across long chains of actions remains the field's hardest practical problem.
- RSIS3 relevance: the loop's outcome-based learning is TD-like — each pass's metric delta is a step signal that updates the system's estimate of which practices work, learned continuously rather than waiting for a final verdict.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — learning objectives can be gamed
- [[wiki/concepts/q-learning|Q-Learning]] — the off-policy TD method
- [[wiki/concepts/policy-gradient|Policy Gradient]] — the policy-based alternative
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — the single-step ancestor
