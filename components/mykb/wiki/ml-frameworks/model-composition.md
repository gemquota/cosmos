---
type: "concept"
title: "Model Composition"
description: "Building systems from multiple models or adapters rather than a single monolithic model"
tags: ["model-composition", "models", "composition", "routing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Composition

## Summary

Model composition is the practice of building an AI system from multiple models or adapters rather than relying on one monolithic model. Composition can happen at the routing layer, through weight merging, or via orchestrated multi-model pipelines. The approach matters because it lets systems combine specialized capabilities, control cost, and adapt without retraining a single giant model. Composition shifts the optimization problem from one giant model to the interaction between parts, which requires new evaluation and monitoring practices.

## Details

- **Definition** — model composition assembles capabilities from several model components, each chosen for a specific role.
- **Routing** — a router selects the best model per request based on task, cost, or quality, enabling specialization and fallback chains.
- **Merging** — model merging fuses weights so one checkpoint holds multiple skills, a form of composition at the parameter level.
- **Adapters** — parameter-efficient adapters attach modular capabilities to a shared base model, composing without full checkpoints.
- **Orchestration** — pipelines chain models: a planner, a generator, a verifier, and an editor each handle one stage of a task.
- **Benefits** — composition improves cost control, robustness through fallbacks, and specialization, and eases incremental updates.
- **Worked example** — a support system routes billing questions to a small fast model and complex legal queries to a large model, with a fallback chain if one fails.
- **Failure modes** — routing errors, inconsistent output styles across components, and added latency from multi-model calls degrade quality.
- **Practical relevance** — composition is central to LLM gateways, agent architectures, and cost engineering in production systems.
- **Design space** — choices include where to compose (weights, prompts, or orchestration), how to evaluate component interactions, and how to monitor drift.
- **Interaction testing** — each component should be evaluated alone and in combination, since a good model in a bad pipeline can still fail.


## Related

- [[wiki/ml-frameworks/routing-models|Routing Models]] — the selection mechanism
- [[wiki/ml-frameworks/model-merging|Model Merging]] — weight-level composition
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — agent-level combination
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — resilience pattern
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — the gateway layer
- [[wiki/ml-frameworks/peft-methods|PEFT Methods]] — adapter-level composition

