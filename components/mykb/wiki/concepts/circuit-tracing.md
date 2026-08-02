---
type: "concept"
title: "Circuit Tracing"
description: "Identifying the specific components implementing a behavior"
tags: ["circuit-tracing", "interpretability", "mechanistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Circuit Tracing

## Summary
Circuit tracing locates the attention heads, MLPs, and connections that implement a given behavior.

## Details
- Circuit tracing locates the attention heads, MLPs, and connections that implement a given behavior.
- Methods combine activation patching, ablations, and attribution to build a causal path.
- Traced circuits are the strongest evidence about how a behavior is computed.
- RSIS3 relevance: tracing how a query becomes an answer is the retrieval-side analogue.

## Related
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — the research program
- [[wiki/concepts/activation-patching|Activation Patching]] — the main tool
- [[wiki/concepts/mechanistic-locality|Mechanistic Locality]] — what makes tracing tractable
- [[wiki/concepts/induction-heads|Induction Heads]] — a traced circuit
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ai-ml/probing|Probing]] — existing graph context
