---
type: "concept"
title: "Causal Interventions in AI"
description: "Perturbing internals to test causal roles"
tags: ["causal", "interventions", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Causal Interventions in AI

## Summary
Causal interventions edit a model's internal state (activations, weights, tokens) and observe output changes, testing whether a component is causally load-bearing.

## Details
- Causal interventions edit a model's internal state (activations, weights, tokens) and observe output changes, testing whether a component is causally load-bearing.
- Activation patching is the standard intervention tool.
- Causal claims are stronger than correlational probe claims, which is why safety analysis prefers them.
- RSIS3 relevance: interventions on graph state (deleting a node) test its causal role in retrieval.

## Related
- [[wiki/concepts/activation-patching|Activation Patching]] — the main method
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — what interventions verify
- [[wiki/concepts/activation-patching|activation-patching]] — the framing
- [[wiki/concepts/causal-interventions-ai|causal-interventions-ai]] — statistical basis
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — existing graph context
