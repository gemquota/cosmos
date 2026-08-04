---
type: "concept"
title: "Simulation Laws"
description: "The rules and invariants that govern a simulation's behavior"
tags: ["entity", "simulation", "rules", "models", "fidelity"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Simulation Laws

## Summary

Simulation laws are the rules and invariants that define how a simulation behaves — the physics, equations, and constraints that map state changes over time. They matter because a simulation is only as credible as its laws: wrong rules produce confidently wrong results. Choosing, implementing, and validating laws is the core modeling work.

## Details

- **Definition** — Simulation laws are the formal rules — equations, state machines, or agent policies — that determine the next state from the current one.
- **Fidelity** — Laws range from idealized approximations to detailed physical models; fidelity trades against compute and calibration effort.
- **Validation** — Laws are validated against real observations, analytic solutions, or expert review; unvalidated laws quietly mislead.
- **Worked example** — A traffic simulation models car-following with an acceleration law; tuning its parameters reproduces observed flow-density curves.
- **Common failure modes** — Instability at small timesteps, laws that conserve nothing when they should, and hard-coded constants tuned to one scenario.
- **Practical relevance** — Agent sandboxes and digital twins inherit this discipline: the environment's laws define what agents can learn.
- **Variants** — Discrete-event laws advance by events; continuous laws integrate over time; hybrid systems mix both.
- **Telemetry note** — The stub mis-tags Simulation Laws to AWS; the simulation-rules reading matches the modeling sessions where it appeared.
- **Documentation** — Laws should be documented with their assumptions and validity ranges, so users know when the model stops being trustworthy.
- **Parameters** — Calibration fits law parameters to data; sensitivity analysis shows which parameters most affect outcomes.
- **Worked example** — An epidemic model's laws reproduce historical curves after calibration; the team documents the parameter ranges outside which results are unreliable.
- **Versioning** — Changing laws changes simulation results, so laws should be versioned and runs labeled with the law set used.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/live-simulation|Live Simulation]] — running laws in real time
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — law-driven agent sandboxes
- [[wiki/concepts/forward-models|Forward Models]] — laws used for prediction
- [[wiki/testing/stress-testing|Stress Testing]] — pushing laws to limits
- [[wiki/concepts/predictive-processing|Predictive Processing]] — internal models of laws
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — documenting laws as knowledge
