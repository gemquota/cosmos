---
type: "concept"
title: "Free Energy Principle"
description: "A theory that self-organizing systems minimize surprise about their world"
tags: ["free-energy-principle", "theory", "cognition", "bayesian"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Free Energy Principle

## Summary
The free energy principle (FEP) proposes that adaptive systems act and perceive to minimize variational free energy — a bound on surprise about their sensory world. It matters as an organizing theory for why agents explore, learn, and maintain models. It underpins active inference and predictive processing.

## Details
- The mathematical core: an agent that survives must keep its sensory states within a small set of viable states, which means keeping them unsurprising under its generative model. Since exact surprise is intractable, the agent minimizes variational free energy, an upper bound on surprise that decomposes into accuracy (how well the model predicts observations) and complexity (how much the model must stretch to fit them). Minimizing it by updating beliefs is perception; minimizing it by sampling new observations is action.
- Surprise minimization via perception (fit the model) and action (fit the world). Perception adjusts the model's beliefs to explain what is sensed — prediction-error minimization, the engine of predictive processing accounts of the brain. Action selects policies that are expected to realize preferred outcomes — and because preferences are priors over outcomes, the agent treats its goals as expectations to fulfill rather than utilities to maximize. The same free-energy quantity drives both, which is the theory's elegance: one objective, two modes.
- Markov blankets define the system-environment boundary. Every system is conditionally independent of its environment given its blanket states — the boundary states that mediate interaction — which formalizes what it means to be an agent with an inside and an outside. The blanket concept has become central to debates about how far FEP generalizes: every particle, cell, and brain has a blanket, so the principle applies at every scale, which is either its great unifying power or the sign that it explains too much.
- Debated as a grand theory; practically inspires model-based agents. Critics argue FEP is unfalsifiable in its broadest form because free energy can always be defined after the fact; defenders point to testable predictions in neuroscience (prediction-error responses, precision weighting). The practical payoff for AI is the architecture: agents with generative models, precision-weighted error signals, and action selection by expected free energy — the blueprint behind active inference agents that explore and exploit without a separate reward signal.
- RSIS3 relevance: the knowledge loop is a free-energy system in miniature — mykb is the generative model, retrieval is perception, and an improvement pass is action that tries to make the next session's predictions come true.

## Related
- [[wiki/concepts/active-inference|Active Inference]] — the applied framework
- [[wiki/concepts/world-models|World Models]] — the model being fitted
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — the probabilistic machinery
- [[wiki/concepts/belief-states|Belief States]] — beliefs that minimize surprise
- [[wiki/agent-systems/planning-systems|Planning Systems]] — acting to reduce expected surprise
