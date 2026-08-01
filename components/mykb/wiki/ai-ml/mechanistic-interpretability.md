---
type: "concept"
title: "Mechanistic Interpretability"
description: "Reverse-engineering the internal circuits of a model — how features and computations compose into behaviour"
tags: ["mechanistic-interpretability", "interpretability", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Mechanistic Interpretability

## Summary
Mechanistic interpretability seeks to explain a model's behaviour by identifying the actual circuits: which features, heads, and layers compute what. It is the most rigorous — and hardest — branch of interpretability.

## Details
- Working objects: induction heads, feature circuits, and attention head specialization.
- Scales poorly: hand-reverse-engineering works on small models; LLM-scale work is partial and contested.
- Payoff: genuine causal understanding could predict jailbreaks and knowledge errors before they happen.
- RSIS3 relevance: mechanistic findings (e.g., sycophancy circuits) inform which behaviours mykb should regression-test.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella discipline
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — The current feature-extraction tool
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Circuit evidence in attention
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — The interventionist sibling
- [[wiki/ai-ml/probing|Probing]] — The lighter-weight predecessor
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Understanding circuits behind attack susceptibility
