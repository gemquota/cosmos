---
type: "concept"
title: "Probabilistic Programming"
description: "Writing programs with random variables and performing inference over them"
tags: ["probabilistic-programming", "inference", "bayesian", "programming"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Probabilistic Programming

## Summary
Probabilistic programming languages let developers describe generative models as code with random choices, then run inference (e.g., MCMC, variational) to compute posterior distributions. They matter because they make probabilistic modeling composable and debuggable. Libraries like Pyro and Stan are the mainstream tools.

## Details
- Model = program with sample statements; inference = conditioning. The programmer writes a normal program in which some variables are drawn from distributions — `x ~ Normal(0, 1)` — and then conditions on observed data — `observe(y, x + Normal(0, 0.1))`. The language's inference engine automatically computes the posterior distribution over the random variables given the observations. This separation is the key win: the model is expressed as a program (composable, structured, debuggable), and the inference machinery is a generic library rather than hand-derived math per model.
- The engine options trade generality against efficiency. MCMC methods (Hamiltonian Monte Carlo in Stan, NUTS) are general and produce asymptotically exact posteriors but are slow and scale poorly with model size. Variational inference (Pyro, PyMC) approximates the posterior with a tractable distribution and optimizes it by gradient descent — much faster and scalable to large models, but biased by the approximation family. Sequential Monte Carlo handles state-space models; the choice of engine is a modeling decision, not a detail.
- Supports hierarchical, structured, and nonparametric models. Probabilistic programs express hierarchical models (group-level and individual-level parameters), structured models with loops and recursion, and nonparametric models (Dirichlet processes) that grow with the data — modeling patterns that are painful in closed-form probability and natural in code. This expressiveness is why probabilistic programming became the standard tool for Bayesian data analysis.
- Agent use: belief updates, active inference, risk estimation. An agent's belief about the world is a posterior over hidden state, updated as observations arrive; active inference agents compute the expected free energy of policies using probabilistic models; risk estimation computes posterior distributions over outcomes rather than point estimates. In each case the probabilistic program is the agent's world model, and the inference engine is its reasoning.
- Open question: inference scalability for large models — current engines struggle with the deep, large models that agent systems need, which is why agent world models are often approximated with neural networks rather than exact posteriors.
- RSIS3 relevance: the system's own estimates — "will this pass improve the metric?", "is this synthesis sound?" — are probabilistic claims, and a probabilistic-programming frame makes them explicit posteriors with uncertainty rather than confident point estimates.


## Related
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — the graphical model family
- [[wiki/concepts/constraint-logic-programming|Constraint Logic Programming]] — the logical sibling
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — sequential decision models
- [[wiki/concepts/active-inference|Active Inference]] — perception as probabilistic inference
- [[wiki/concepts/belief-states|Belief States]] — the posterior beliefs computed
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — the deterministic counterpart
