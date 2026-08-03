---
type: "concept"
title: "Polysemanticity"
description: "Neurons or features that respond to many unrelated concepts"
tags: ["polysemanticity", "interpretability", "features"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Polysemanticity

## Summary
Polysemanticity is the phenomenon where a single unit responds to many unrelated inputs, complicating interpretation. A neuron that fires on cat faces, car wheels, and mathematical notation is not a "cat face neuron" with an explanation problem — it is a unit shared across concepts, and unit-level description systematically misleads until the shared structure is understood.

## Details
- The empirical signature is documented across models and scales: detailed studies of trained networks find that most neurons respond to heterogeneous, semantically unrelated inputs, and the exceptions (clean monosemantic units) are the minority. The phenomenon is not an implementation accident; it is a consequence of how the network represents information, which is why it appears so reliably.
- It arises from superposition: the network packs features densely and shares units. A network with fewer units than the concepts it must represent uses the geometry of high-dimensional space to pack multiple features into nearly orthogonal directions, with interference kept small but nonzero. The unit fires for whichever features happen to activate it, so its response pattern is a blend — the mathematical consequence of representing more features than units. Superposition is efficient (that is why networks do it), and its price is interpretability.
- The consequence for interpretability is that the unit is the wrong level of analysis. Describing a neuron by its strongest activation describes only one feature among the several it carries, and claims like "this neuron detects X" are systematically incomplete. The field's response is to change the unit of analysis: dictionary learning recovers the underlying features, making polysemantic units readable — a sparse autoencoder decomposes a polysemantic neuron's activations into the features it participates in, and the features, not the neurons, are the interpretable objects.
- The practical discipline this imposes: never trust a unit-level description without checking for polysemanticity, and prefer feature-level or causal analysis when drawing conclusions about what a model computes.
- RSIS3 relevance: graph nodes that mix topics are polysemantic; splitting them improves retrieval. A wiki page covering several distinct concepts behaves like a polysemantic neuron — it fires (surfaces) for unrelated queries, diluting precision — and the fix is the same: decompose into cleaner units (separate pages), or at least label the page so retrieval can distinguish the concepts it mixes.

## Related
- [[wiki/concepts/monosemanticity|Monosemanticity]] — the opposite ideal
- [[wiki/concepts/superposition-research|Superposition Research]] — the cause
- [[wiki/concepts/dictionary-learning-ai|Dictionary Learning for AI]] — the fix
- [[wiki/concepts/neuron-interpretation|Neuron Interpretation]] — the level that misleads
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/activation-engineering|Activation Engineering]]
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]]
