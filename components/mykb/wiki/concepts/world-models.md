---
type: "concept"
title: "World Models"
description: "Internal representations that let agents simulate and predict their environment"
tags: ["world-models", "simulation", "prediction", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1803.10122", "https://worldmodels.github.io/"]
---

# World Models

## Summary
World models are the agent's internal representation of how its environment works, used to predict outcomes and plan. They matter because an agent that can simulate consequences can plan without executing. They range from learned latent spaces to explicit domain simulations.

## Details
- Predictive power is the test: can the model anticipate the result of an action?
- World models enable mental rehearsal before risky actions.
- RSIS3 relevance: its domain knowledge in mykb acts as a lightweight world model.
- Open questions: when to trust the model vs. reality, and keeping it current.
- A world model is an internal representation an agent learns of how its environment behaves, used to predict outcomes and plan actions without acting.
- World models compress the environment: they must capture the dynamics that matter for the task while discarding irrelevant detail.
- They enable imagination-based planning — the agent simulates candidate actions and evaluates consequences before committing.
- The risk is model error: a world model that is confidently wrong sends the agent confidently off course, so planning must stay aware of model limits.
- **Worked example / comparison** — Worked example — an agent maintains a model of the wiki graph's link structure; it predicts which new stub links would raise graph density before adding them.
- For mykb, world models are documented as the predictive engine behind the perception loop and belief states.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]]
- [[wiki/concepts/belief-states|Belief States]]
- [[wiki/concepts/active-inference|Active Inference]]
- [[wiki/concepts/free-energy-principle|Free Energy Principle]]
- [[wiki/concepts/perception-loop|Perception Loop]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/deep-dives|Deep Dives]]
