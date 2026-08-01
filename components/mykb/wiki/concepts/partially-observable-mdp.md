---
type: "concept"
title: "Partially Observable MDP"
description: "Sequential decision making when the true state is hidden"
tags: ["pomdp", "decision-making", "belief", "uncertainty"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Partially Observable MDP

## Summary
A POMDP extends the MDP with observations: the agent never sees the true state, only noisy observations, so it acts on a belief distribution over states. It matters because real agents rarely see the full state. POMDP planning optimizes over belief space, which is harder but more realistic.

## Details
- Belief updates via Bayesian filtering as observations arrive.
- Optimal policies are functions of belief, not raw state.
- Agent use: world state inference from tool outputs.
- Open questions: scalable POMDP policies with learned models.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — acting under hidden risk
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the fully observable base
- [[wiki/concepts/belief-states|Belief States]] — the object being tracked
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — the belief representation
- [[wiki/concepts/active-inference|Active Inference]] — a unified perception-action theory
