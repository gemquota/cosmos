---
type: "concept"
title: "Multi-Armed Bandit"
description: "The problem of choosing among options with unknown rewards"
tags: ["bandit", "decision-making", "exploration", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Multi-Armed Bandit

## Summary
The multi-armed bandit is the sequential decision problem where each pull of an arm yields reward from an unknown distribution, and the agent must balance learning and earning. It matters because it is the cleanest model of exploration-exploitation. Many agent choices reduce to bandits.

## Details
- The setup: there are K arms (slot machines), each with an unknown reward distribution. At each time step the agent pulls one arm and observes its reward. The agent faces the fundamental tension: it should exploit the arm with the best estimated mean, but it must explore other arms to learn whether their means are actually better. The best arm is unknown, so every pull is simultaneously a decision and an experiment.
- Regret measures how far the agent is from always picking the best arm. Regret is the cumulative difference between the reward of the optimal arm and the reward actually collected — in expectation, the price of not knowing which arm is best. Regret is the standard yardstick because it captures the tradeoff directly: algorithms that explore too much pay regret on missed exploitation, algorithms that explore too little pay regret on wrong choices. The theory's landmark results characterize optimal regret rates (logarithmic in time, with a constant that depends on the gaps between arm means) — and the algorithms that achieve them.
- Algorithms: epsilon-greedy, UCB1, Thompson sampling. Epsilon-greedy explores with fixed probability ε and exploits otherwise — simple, but wastes exploration on bad arms. UCB1 (Upper Confidence Bound) computes an optimistic estimate for each arm (mean plus an uncertainty bonus) and pulls the arm with the highest bound; it is the canonical near-optimal algorithm. Thompson sampling pulls each arm according to its posterior probability of being best, and despite (or because of) its Bayesian randomness, it matches or beats UCB in practice. The design question across all of them is how exploration is allocated: uniformly, optimistically, or probability-matched.
- Contextual bandits add features per decision: the agent observes context (user, situation) before choosing, learns which arm is best given the context, and generalizes across contexts — the model behind personalized recommendation and ad placement. This is the middle ground between the pure bandit and full RL: there is no long-horizon state, only context → action → reward.
- The failure mode: distribution change — the arms' reward distributions drift, and a bandit tuned to static arms collects regret while the world moves.
- RSIS3 relevance: choosing which improvement experiment to run next is a bandit problem — each candidate pass type is an arm with unknown payoff, and the loop should explore new pass types while exploiting the ones that have historically improved metrics.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — bandits as a planning simplification
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — the core trade-off
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — bandits inside tree search
- [[wiki/concepts/q-learning|Q-Learning]] — the full RL generalization
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — learning from delayed reward
