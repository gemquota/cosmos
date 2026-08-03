---
type: "concept"
title: "Linear Probes"
description: "Linear classifiers over internal activations"
tags: ["probing", "linear", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Linear Probes

## Summary
Linear probes train a linear classifier on layer activations to test whether a concept is linearly separable there. If a simple linear boundary can read "this input is toxic" or "this token is the subject of the sentence" from a layer's activations, the concept is present in that layer in a directly usable form — the representation itself has been organized to make the distinction easy.

## Details
- The procedure: freeze the model, cache activations from a chosen layer over a labeled dataset, train a logistic regression (or linear SVM) on those activations, and measure its accuracy on held-out labels. The probe is deliberately simple — no hidden layers — so that high accuracy is evidence the information is linearly accessible in the representation, not evidence that a powerful classifier can extract anything from anything.
- Linearity matters because linear access suggests the feature is actually computed, not entangled. Neural networks are believed to organize concepts into directions in activation space, and a linear probe tests exactly that hypothesis: if the concept is linearly separable, it exists as a clean direction; if only a nonlinear probe can find it, the concept is entangled with other features or present only in raw form. This distinction is what separates "the model represents the concept" from "the model's internals can be decoded into the concept".
- Probe accuracy across layers maps where information lives. Probing every layer produces a "probe curve": accuracy typically rises through early and middle layers as the representation matures, peaks near the task-relevant layers, and sometimes declines at the output where information is compressed into prediction logits. Curves that stay low until the final layer suggest the model never builds the concept as an explicit representation, which is itself a finding.
- The known pitfalls: probes can be fooled by input information that leaks through the residual stream (the "probe cannot distinguish representation from input" problem), and high probe accuracy does not mean the model uses the concept causally — probing shows presence, not participation, which is why probe results are hypotheses for causal-intervention confirmation.
- RSIS3 relevance: embedding-level probing of the knowledge graph uses the same idea — training a linear readout on node embeddings to test whether a topic distinction (e.g., "infrastructure" vs "memory") is linearly present, telling the system whether its embeddings have organized the concepts it wants to retrieve on.

## Related
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — the general method
- [[wiki/concepts/monosemanticity|Monosemanticity]] — the ideal probe result
- [[wiki/concepts/feature-visualization|Feature Visualization]] — visual counterpart
- [[wiki/concepts/dictionary-learning-ai|Dictionary Learning for AI]] — feature decomposition
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/probing|Probing]] — existing graph context
