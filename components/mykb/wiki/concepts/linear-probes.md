---
type: "concept"
title: "Linear Probes"
description: "Linear classifiers over internal activations"
tags: ["probing", "linear", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Linear Probes

## Summary
Linear probes train a linear classifier on layer activations to test whether a concept is linearly separable there.

## Details
- Linear probes train a linear classifier on layer activations to test whether a concept is linearly separable there.
- Linearity matters because linear access suggests the feature is actually computed, not entangled.
- Probe accuracy across layers maps where information lives.
- RSIS3 relevance: embedding-level probing of the knowledge graph uses the same idea.

## Related
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — the general method
- [[wiki/concepts/monosemanticity|Monosemanticity]] — the ideal probe result
- [[wiki/concepts/feature-visualization|Feature Visualization]] — visual counterpart
- [[wiki/concepts/dictionary-learning-ai|Dictionary Learning for AI]] — feature decomposition
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/probing|Probing]] — existing graph context
