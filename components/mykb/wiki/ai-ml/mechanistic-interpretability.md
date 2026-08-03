---
type: "concept"
title: "Mechanistic Interpretability"
description: "Reverse-engineering the internal circuits of a model — how features and computations compose into behaviour"
tags: ["mechanistic-interpretability", "interpretability", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Mechanistic Interpretability

## Summary
Mechanistic interpretability seeks to explain a model's behaviour by identifying the actual circuits: which features, heads, and layers compute what. It is the most rigorous — and hardest — branch of interpretability, aiming for causal understanding rather than correlation.

## Details
The working objects are concrete: induction heads that copy patterns from context, feature circuits that detect concepts in activations, and attention-head specialization where particular heads implement particular subtasks. The field's ambition is a full reverse-engineered map of how these pieces compose into observable behaviour, at which point predictions about failure modes would be derived from structure rather than guessed from outputs.

The method is experimental, not just observational. Findings from activation analysis are validated with interventions — patching activations from one input into another, ablating heads, or steering features — and a circuit claim only holds when the intervention produces the predicted behaviour change. That discipline is what separates mechanistic work from correlation-based probing, but it is also what makes it slow: every claim requires a controlled experiment.

Scaling is the field's central obstacle. Hand-reverse-engineering works on small toy models where circuits are small enough to enumerate, but LLM-scale work is partial and contested: discovered circuits are often incomplete, model-family-specific, and expensive to reproduce. Sparse autoencoders made feature extraction tractable at scale, yet the resulting features are themselves a learned approximation whose boundaries are fuzzy. The honest state of the art is that we have islands of mechanistic understanding, not a full map.

The payoff would be genuine causal understanding that predicts jailbreaks and knowledge errors before they happen, rather than after. RSIS3 relevance: mechanistic findings such as sycophancy circuits inform which behaviours mykb should regression-test, and storing the specific circuit claims alongside eval results keeps the causal story attached to the behaviour it predicts.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella discipline
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — The current feature-extraction tool
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Circuit evidence in attention
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — The interventionist sibling
- [[wiki/ai-ml/probing|Probing]] — The lighter-weight predecessor
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Understanding circuits behind attack susceptibility
