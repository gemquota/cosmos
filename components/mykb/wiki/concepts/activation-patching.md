---
type: "concept"
title: "Activation Patching"
description: "Replacing activations from one input with another to test causal roles"
tags: ["patching", "activations", "causality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Activation Patching

## Summary
Activation patching runs a model on input A, then replays activations from input B at chosen layers to see what changes.

## Details
- Activation patching runs a model on input A, then replays activations from input B at chosen layers to see what changes.
- It localizes where information is processed and which components matter.
- Zero- and mean-ablation variants give cheaper estimates of component importance.
- RSIS3 relevance: patching-style A/B tests on graph retrieval isolate which links drive answers.

## Related
- [[wiki/concepts/causal-interventions-ai|Causal Interventions in AI]] — the family
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — what it builds
- [[wiki/concepts/causal-interventions-ai|causal-interventions-ai]] — related tool
- [[wiki/concepts/transformer-lens|TransformerLens]] — tooling support
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — existing graph context
