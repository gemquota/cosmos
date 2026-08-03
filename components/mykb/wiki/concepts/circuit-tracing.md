---
type: "concept"
title: "Circuit Tracing"
description: "Identifying the specific components implementing a behavior"
tags: ["circuit-tracing", "interpretability", "mechanistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Circuit Tracing

## Summary
Circuit tracing locates the attention heads, MLPs, and connections that implement a given behavior. It is the method half of circuit analysis: given a behavior you want to explain, tracing produces the specific causal path — which components, in which order, carrying which information — that implements it.

## Details
- The standard toolkit combines three families of evidence. Attribution methods (gradient-based or attention-based) generate candidate components cheaply and at scale, ranking heads and neurons by how much they influence the output. Causal interventions then test the candidates: activation patching, ablation, and path patching perturb each component and measure whether the behavior survives. The final circuit is the set of components that survive causal verification together — the minimum subgraph whose removal breaks the behavior.
- Tracing is iterative and human-in-the-loop in practice. The researcher starts with a hypothesis about where information enters (for example, an attention head that reads a particular token position), follows the propagation of that information through layers, and uses interventions to confirm each hop. Tools like TransformerLens and circuits-visualization libraries make the cache-and-patch loop routine for small models.
- The output is a causal path, not a complete map: tracing answers "how does this behavior work on these inputs" rather than "what does this model do generally". The same behavior can have different circuits on different input distributions, and circuits found in small models may not transfer to larger ones, so results must be scoped carefully.
- Failure modes include attribution noise (gradient methods flag components that correlate with but do not cause the output), intervention artifacts (patched states are out-of-distribution, so a behavior change can reflect the model reacting to an impossible input), and premature termination — stopping the trace at the first component that breaks the behavior can miss parallel pathways that would compensate if it were truly removed.
- RSIS3 relevance: tracing how a query becomes an answer is the retrieval-side analogue. Which index pages, link hops, and synthesis rules carry the decisive evidence for a given answer? Applying trace-and-verify to the retrieval graph tells the system which parts of its memory are genuinely load-bearing.

## Related
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — the research program
- [[wiki/concepts/activation-patching|Activation Patching]] — the main tool
- [[wiki/concepts/mechanistic-locality|Mechanistic Locality]] — what makes tracing tractable
- [[wiki/concepts/induction-heads|Induction Heads]] — a traced circuit
- [[wiki/concepts/grokking|Grokking]]
- [[wiki/ai-ml/probing|Probing]]
