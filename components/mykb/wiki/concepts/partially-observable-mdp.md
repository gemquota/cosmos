---
type: "concept"
title: "Partially Observable MDP"
description: "Sequential decision making when the true state is hidden"
tags: ["pomdp", "decision-making", "belief", "uncertainty"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Partially Observable MDP

## Summary
A POMDP extends the MDP with observations: the agent never sees the true state, only noisy observations, so it acts on a belief distribution over states. It matters because real agents rarely see the full state. POMDP planning optimizes over belief space, which is harder but more realistic.

## Details
- The formal extension: a POMDP adds an observation function O(o | s', a) to the MDP tuple — after taking action a and transitioning to state s', the agent observes o with probability O(o | s', a). The agent does not know s'; it has only the history of its actions and observations, summarized in a belief — a probability distribution over states. The Markov property moves from state space to belief space: the belief is the sufficient statistic, and the agent's decision problem becomes an MDP whose states are beliefs.
- Belief updates via Bayesian filtering as observations arrive. Starting from a prior belief, the agent predicts the next belief by applying the transition model, then conditions on the actual observation with Bayes' rule: new belief ∝ observation likelihood × transitioned prior belief. This is the same machinery as the Kalman filter (for linear Gaussian models) and particle filters (for general models). The update is where the agent's world model earns its keep — the quality of the belief depends on the quality of the transition and observation models.
- Optimal policies are functions of belief, not raw state. Because the true state is unknown, the optimal action depends on the whole belief distribution — two histories that yield the same belief require the same action. This is both the theoretical elegance and the computational curse: belief space is continuous and high-dimensional, so exact POMDP planning (value iteration over belief space) is intractable beyond toy problems, and practical solvers use point-based methods, Monte Carlo sampling, or learned approximations.
- Agent use: world state inference from tool outputs. A language agent's context — what it believes about the task, the environment, and its own state — is exactly a belief, updated by each tool result; the POMDP frame makes explicit that the agent's context is a posterior, not ground truth, which is why confident agents acting on stale beliefs fail.
- The tradeoff: POMDPs are more realistic but harder to solve — the hidden state multiplies the problem's difficulty, and the common shortcut (pretend the observation is the state, as a plain MDP does) buys tractability at the cost of systematic errors from hidden variables.
- RSIS3 relevance: the loop operates on a partial view of its own ecosystem — the registry, wiki, and telemetry are observations, not the full state — and treating its beliefs as revisable posteriors rather than facts is the discipline that prevents confident wrong consolidation.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — acting under hidden risk
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the fully observable base
- [[wiki/concepts/belief-states|Belief States]] — the object being tracked
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — the belief representation
- [[wiki/concepts/active-inference|Active Inference]] — a unified perception-action theory
