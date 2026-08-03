---
type: "concept"
title: "Circuit Analysis"
description: "Mapping the computational circuits a network implements"
tags: ["circuits", "interpretability", "mechanistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Circuit Analysis

## Summary
Circuit analysis identifies the small subnetworks (circuits) that implement behaviors like induction, addition, or translation. It is the core of mechanistic interpretability: instead of treating the network as an opaque function, circuit analysis decomposes a behavior into the specific attention heads, MLP neurons, and connections that compute it, then verifies the decomposition causally.

## Details
- A circuit is a minimal, task-specific subgraph of the full network: a set of components and the connections between them that suffices to implement a behavior. The famous induction-head circuit, for example, consists of a few attention heads in early layers that copy previous-token patterns into the current position — a tiny fraction of the network's total parameters explains a large fraction of the behavior. Most behaviors studied so far turn out to be implemented by sparse circuits, not by diffuse whole-network computation.
- The workflow is iterative: hypothesize which components matter (guided by activation analysis and probing), trace the path of information with attribution methods, then verify with causal interventions — patch or ablate each candidate and confirm the behavior breaks or survives as predicted. A circuit claim is only as strong as its causal verification; correlation-based component importance is a hypothesis, not a result.
- The promise is a real science of model internals: known circuits can be inspected, monitored, and edited, which enables targeted interventions (fixing a specific failure mode, steering a behavior) and safety auditing. The practical constraint is scale: full-circuit mapping for frontier models is intractable today because the search space of components and paths is enormous, so progress is concentrated on small models, single behaviors, and narrow tasks, with the hope that discovered circuits and the methods themselves transfer.
- Failure modes: circuits are input-dependent and behavior-dependent, so a circuit mapped on one distribution may not hold on another; overclaiming (finding a circuit for a proxy behavior, not the real one); and the seductive completeness error of assuming that a verified small circuit is the whole story when other components contribute in parallel.
- RSIS3 relevance: circuit-style analysis of the knowledge loop would trace how queries flow through the graph — which retrieval steps, link hops, and synthesis rules are load-bearing for producing an answer, mirroring the same identify-trace-verify discipline.

## Related
- [[wiki/concepts/circuit-tracing|Circuit Tracing]] — the identification method
- [[wiki/concepts/induction-heads|Induction Heads]] — a famous circuit
- [[wiki/concepts/causal-interventions-ai|Causal Interventions in AI]] — the verification method
- [[wiki/concepts/mechanistic-locality|Mechanistic Locality]] — why circuits are local
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ai-ml/probing|Probing]] — existing graph context
