---
type: "concept"
title: "World Models"
description: "Internal representations that let agents simulate and predict their environment"
tags: ["world-models", "simulation", "prediction", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# World Models

## Summary
World models are the agent's internal representation of how its environment works, used to predict outcomes and plan. They matter because an agent that can simulate consequences can plan without executing. They range from learned latent spaces to explicit domain simulations.

## Details
- Predictive power is the test: can the model anticipate the result of an action?
- World models enable mental rehearsal before risky actions.
- RSIS3 relevance: its domain knowledge in mykb acts as a lightweight world model.
- Open questions: when to trust the model vs. reality, and keeping it current.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — planning requires a world model
- [[wiki/concepts/belief-states|Belief States]] — the current-situation slice of the model
- [[wiki/concepts/active-inference|Active Inference]] — perception-action unified via models
- [[wiki/concepts/free-energy-principle|Free Energy Principle]] — theoretical grounding
- [[wiki/concepts/perception-loop|Perception Loop]] — how the model is kept updated
