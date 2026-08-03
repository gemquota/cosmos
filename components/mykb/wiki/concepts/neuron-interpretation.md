---
type: "concept"
title: "Neuron Interpretation"
description: "Attributing meaning to individual units in a network"
tags: ["neurons", "interpretability", "mechanistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Neuron Interpretation

## Summary
Neuron interpretation studies what individual neurons or attention heads respond to. It is the oldest unit-level project of interpretability: find a neuron, characterize its selectivity, and thereby explain part of what the network computes. The field's history is a lesson in how that project had to be revised — the clean "one neuron, one concept" picture gave way to a far messier reality.

## Details
- The method: identify a unit (a channel, neuron, or attention head), find the inputs that activate it most (feature visualization, dataset search for maximum-activation examples), and describe the common pattern — "this neuron fires on cat faces", "this head copies the previous token". The resulting catalog of unit descriptions was the first intuitive vocabulary for model internals and remains the entry point for many analyses.
- Early claims of clean 'feature neurons' gave way to polysemantic units that fire for many unrelated inputs. Detailed study found that individual neurons in trained networks regularly fire on heterogeneous, unrelated inputs — a neuron that responds to cat faces, car wheels, and mathematical notation — because the network uses superposition to pack more features than it has neurons, sharing units across concepts. This shattered the interpretability promise of unit-level analysis: a neuron is not a word in the model's vocabulary but a mixed bag of concepts, and describing it by its strongest activation is describing only part of what it does.
- Interpretation is now done at the feature level (via dictionary learning) rather than the neuron level. Sparse autoencoders decompose activations into a larger set of sparse features, each of which is (ideally) monosemantic — the feature-level counterpart of the old neuron-level dream. The shift is profound: the unit of analysis moved from the network's physical units to the learned feature directions that the network's computation actually uses, at the cost of many more units to characterize.
- The enduring caveats: interpretation of a unit's inputs does not explain its causal role (a neuron that fires on cat faces may be a small part of the cat-recognition circuit or a side effect), and unit-level findings are input-dependent — the same neuron's role can differ across distributions.
- RSIS3 relevance: interpretability practice informs how graph nodes are labeled and merged. A wiki topic is the "neuron" of the knowledge graph — it may be polysemantic (one page covering several distinct concepts), and the discipline of checking selectivity before merging or labeling is the same discipline the interpretability field learned.

## Related
- [[wiki/concepts/polysemanticity|Polysemanticity]] — why neurons are ambiguous
- [[wiki/concepts/monosemanticity|Monosemanticity]] — the clean ideal
- [[wiki/concepts/feature-visualization|Feature Visualization]] — visualizing selectivity
- [[wiki/concepts/sae-research|SAE Research]] — the modern method
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/activation-engineering|Activation Engineering]]
