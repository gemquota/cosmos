---
type: "concept"
title: "Mechanistic Locality"
description: "The observation that circuits are localized in few components"
tags: ["locality", "circuits", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Mechanistic Locality

## Summary
Mechanistic locality is the empirical finding that behaviors are usually implemented by a small fraction of a model's components. When a transformer performs a behavior — copying a pattern, detecting a relation, following a rule — the computation tends to flow through a few specific attention heads and MLP units rather than being smeared across the whole network, and the small subgraph that does the work can be isolated.

## Details
- The evidence comes from the standard interpretability toolkit. Activation patching and ablation show that removing or altering a handful of components flips the behavior while ablating most of the network leaves it intact; attribution methods converge on the same few components; and fully traced circuits (the induction-head circuit being the canonical example) turn out to involve a handful of heads and connections, not the whole model. The pattern is consistent enough that it is treated as the working assumption of the field.
- It makes circuit analysis tractable: you can find the needle without reading the haystack. If computation were uniformly distributed, interpretability would require explaining every weight; locality means the search can be guided — look at the components that attribution ranks, verify the small candidate set causally, and you have the circuit. This is why the interpretability program scaled from small models to increasingly large ones: locality keeps the object of study small even as the model grows.
- Counterexamples exist; locality is a claim to verify per behavior, not an axiom. Some behaviors are genuinely distributed — certain language-model tasks involve many parallel heads contributing additively, and "society of minds" behaviors in large models are broad by design. The claim is therefore not "all computation is local" but "for many behaviors, a small subgraph is sufficient", and the methodologically correct stance is to test locality for each behavior before assuming it.
- The mechanism behind locality is debated: optimization tends to concentrate computation in specialized components because it is efficient, and specialization emerges naturally from the training objective — but nothing forces it, which is why counterexamples exist.
- RSIS3 relevance: locality in the graph means few links drive a synthesis; traceable and auditable. If a knowledge graph exhibits locality — a handful of pages and edges carry the retrieval weight for an answer — then auditing that answer is cheap and targeted; if it does not, attribution is expensive and the audit story weakens.

## Related
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — what locality enables
- [[wiki/concepts/activation-patching|Activation Patching]] — the evidence tool
- [[wiki/concepts/circuit-tracing|circuit-tracing]]
- [[wiki/syntheses/audit-frameworks-ai|AI Audit Frameworks]] — why locality aids auditing
- [[wiki/concepts/grokking|Grokking]]
- [[wiki/ai-ml/probing|Probing]]
