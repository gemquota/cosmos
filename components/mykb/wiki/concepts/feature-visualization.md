---
type: "concept"
title: "Feature Visualization"
description: "Visualizing what network features detect"
tags: ["visualization", "features", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Feature Visualization

## Summary
Feature visualization optimizes inputs that maximally activate a neuron or feature, producing images of what it detects. It is the oldest intuitive tool of interpretability: if you want to know what a unit responds to, search input space for the pattern that lights it up most, and the resulting image is the unit's "preferred stimulus" made visible.

## Details
- The method: take the model's weights, pick a target unit (a neuron, channel, or dictionary feature), and run gradient ascent on a synthetic input to maximize that unit's activation — optionally with regularization to keep the result naturalistic. Early work used random noise and produced recognizable, eerily evocative images: a neuron that fires on cat faces visualizes as a field of cat faces; a curve detector visualizes as curves. The technique made early mechanistic interpretation vivid, exactly as the classic images show.
- Modern practice adds crucial refinements because naive optimization produces adversarial-looking artifacts. Regularization (total variation, frequency penalties, deep-feature priors from generative models) keeps optima in the natural image manifold; feature inversion, where you reconstruct the input that produces a given activation pattern, complements maximization; and optimization ensembles or multiple restarts reveal which visual patterns are robust features versus local optima.
- Results can be misleading: optima show the detector's inputs, not its role in computation. A neuron that fires on "cat faces" is not necessarily the "cat face recognizer" in the circuit — it may be a small part of a larger computation, or fire on cat faces only as a side effect of what it really does. Visualization shows what excites a unit, and excitation alone says nothing about causal importance, which is why visualization findings are hypotheses for activation patching and circuit analysis to verify, not conclusions.
- Polysemanticity compounds the problem: a single neuron fires for many unrelated inputs, so its "preferred stimulus" image is a blend of unrelated concepts and describes none of them precisely.
- RSIS3 relevance: visualization analogies help explain graph communities to humans — projecting wiki link clusters into a visual layout is the graph analog of feature visualization — as long as the same caveat is remembered: the projection shows structure, not causal role.

## Related
- [[wiki/concepts/neuron-interpretation|Neuron Interpretation]] — the target
- [[wiki/concepts/activation-analysis|Activation Analysis]] — the substrate
- [[wiki/concepts/polysemanticity|Polysemanticity]] — why visuals mislead
- [[wiki/concepts/superposition-research|superposition-research]] — note
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — existing graph context
