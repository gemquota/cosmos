---
type: "concept"
title: "Bayesian Networks"
description: "Directed graphical models of probabilistic dependencies"
tags: ["bayesian-networks", "probability", "inference", "graphical-models"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Bayesian Networks

## Summary
Bayesian networks represent joint probability distributions as directed acyclic graphs: nodes are variables, edges are dependencies, and each node has a conditional distribution given its parents. They matter because they make probabilistic inference tractable and interpretable. They are the classic tool for belief modeling under uncertainty.

## Details
- Inference: compute posteriors given evidence (exact or approximate).
- Learning: structure and parameters from data.
- Agent use: diagnosis, risk assessment, belief states.
- Open questions: LLM-guided structure learning.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — uncertainty for safety decisions
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — the programming embodiment
- [[wiki/concepts/belief-states|Belief States]] — posteriors over world state
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — sequential belief updating
- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]] — the probabilistic variant
