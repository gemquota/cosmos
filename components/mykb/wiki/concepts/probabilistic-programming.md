---
type: "concept"
title: "Probabilistic Programming"
description: "Writing programs with random variables and performing inference over them"
tags: ["probabilistic-programming", "inference", "bayesian", "programming"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Probabilistic Programming

## Summary
Probabilistic programming languages let developers describe generative models as code with random choices, then run inference (e.g., MCMC, variational) to compute posterior distributions. They matter because they make probabilistic modeling composable and debuggable. Libraries like Pyro and Stan are the mainstream tools.

## Details
- Model = program with sample statements; inference = conditioning.
- Supports hierarchical, structured, and nonparametric models.
- Agent use: belief updates, active inference, risk estimation.
- Open questions: inference scalability for large models.

## Related

- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — the graphical model family
- [[wiki/concepts/constraint-logic-programming|Constraint Logic Programming]] — the logical sibling
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — sequential decision models
- [[wiki/concepts/active-inference|Active Inference]] — perception as probabilistic inference
- [[wiki/concepts/belief-states|Belief States]] — the posterior beliefs computed
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — the deterministic counterpart
