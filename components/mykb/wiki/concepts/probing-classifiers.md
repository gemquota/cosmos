---
type: "concept"
title: "Probing Classifiers"
description: "Classifiers trained on internal representations to test what is encoded"
tags: ["probing", "interpretability", "representations"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Probing Classifiers

## Summary
Probing classifiers are small models trained on a model's internal activations to test whether features are linearly accessible.

## Details
- Probing classifiers are small models trained on a model's internal activations to test whether features are linearly accessible.
- Good probe performance suggests the feature is encoded; the technique is the workhorse of representational analysis.
- Probes can mistake shallow correlations for deep knowledge; control tasks are essential.
- RSIS3 relevance: probe-style analysis informs how the graph's embeddings are inspected.

## Related
- [[wiki/concepts/linear-probes|Linear Probes]] — the simplest probe
- [[wiki/concepts/activation-analysis|Activation Analysis]] — the data being probed
- [[wiki/concepts/polysemanticity|Polysemanticity]] — why probes mislead
- [[wiki/concepts/feature-double-counting|Feature Double-Counting]] — probe confound
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/probing|Probing]] — existing graph context
