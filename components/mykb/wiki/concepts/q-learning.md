---
type: "concept"
title: "Q-Learning"
description: "Off-policy TD learning of action values for optimal policies"
tags: ["q-learning", "reinforcement-learning", "value", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Q-Learning

## Summary
Q-learning learns the value of taking each action in each state, Q(s, a), using off-policy TD updates. It matters because it converges to optimal policies without a model of the environment. Deep Q-networks extended it to large state spaces.

## Details
- The object of learning is the action-value function Q(s, a): the expected discounted return of taking action a in state s and then acting optimally. Once Q is correct, the optimal policy is trivial — always take the action with the highest Q. The learning problem is therefore entirely about estimating Q from experience, and Q-learning's update rule is the engine: after taking action a in state s, observing reward r and next state s', it updates Q(s, a) toward r + γ·max_a' Q(s', a').
- Update uses the max over next-state actions, making it off-policy. The key design choice is that the update targets the value of the best next action, regardless of the action the agent actually took — the learned Q function describes the optimal policy, not the exploratory policy that generated the data. This is what makes Q-learning off-policy: it can learn the optimal policy while behaving suboptimally (exploring), which is exactly the property needed for safe, curiosity-driven learning.
- Converges for tabular settings under exploration conditions. With a table of Q-values, infinite visits to every state-action pair, and a learning rate satisfying the Robbins-Monro conditions (sums to infinity, squares sum to finitely), Q-learning converges to the optimal Q function. The exploration condition is the practical content: the agent must keep trying all actions often enough, which is why epsilon-greedy and other exploration schedules are load-bearing rather than optional.
- DQN added experience replay and target networks. Deep Q-networks replaced the table with a neural network (needed for large state spaces like Atari pixels) and added two stabilizers: experience replay breaks the correlation between consecutive updates by sampling from a stored buffer of past transitions, and a target network (a frozen copy of Q updated periodically) prevents the instability of bootstrapping against a constantly moving target. These two ideas made value-based deep RL work for the first time.
- Failure modes: overestimation bias (the max operator systematically overestimates Q, which DQN variants like Double DQN correct), instability from the moving target, and the difficulty of applying value-based control to high-dimensional action spaces — which is why modern agent systems usually prefer policy-gradient methods.
- RSIS3 relevance: the loop's choice of which improvement to run next can be framed as Q-learning over pass types — state is the ecosystem's metrics, actions are pass types, and the reward is measured improvement — with off-policy learning as the natural fit, since the system must explore new pass types while exploiting known-good ones.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — value maximization can go wrong
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — the learning rule
- [[wiki/concepts/policy-gradient|Policy Gradient]] — the policy-based alternative
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — exploration during learning
