---
type: "concept"
title: "Activation Analysis"
description: "Studying a model's internal activations to understand computation"
tags: ["activations", "interpretability", "analysis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Activation Analysis

## Summary
Activation analysis inspects the values flowing through a model during a forward pass: magnitude, patterns, and layer-wise structure. It is the raw observational layer of mechanistic interpretability: before asking what a component does, you must know what values it passes around and how those values change across inputs, layers, and training checkpoints.

## Details
- The residual stream is the shared highway every layer reads from and writes to; activation analysis tracks how representations accumulate across depth. A token's embedding moves through attention and MLP blocks, and the residual stream records the sum of all edits. That structure means "what is the model thinking" decomposes into "what has been added to the residual stream, where, and by whom".
- Standard measurements include per-layer norm growth, per-component output norms, activation sparsity, and cosine similarity between activations across inputs. Sudden norm jumps often flag numerical instabilities such as attention logit overflow or MLP dead zones, while unusually high similarity between two inputs can reveal a model collapsing onto a single internal template.
- Activations are the substrate for nearly every downstream technique: linear probes read classification structure off a chosen layer, sparse autoencoders (SAEs) factor the stream into features, and circuit tracers use activations as the medium for causal interventions. Choosing the right layer is itself an analytical decision, because earlier layers tend to encode syntax and surface form while later layers carry increasingly task-specific semantics.
- Activation statistics also serve safety monitoring. Anomaly detection on activation distributions can catch distribution shift, prompt injection triggers, or emergent behaviors that never surface in the final logits. Production systems often record rolling activation baselines so that deviations can be flagged before they corrupt downstream decisions.
- RSIS3 relevance: activation-style analysis of graph embeddings can reveal topic structure. In mykb, node embeddings produced from link structure can be scored for norm and cluster coherence the same way transformer activations are, turning retrieval diagnostics into the same quantitative discipline used in language-model interpretability.

## Related
- [[wiki/concepts/activation-patching|Activation Patching]] — intervention on activations
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — reading activations
- [[wiki/concepts/neuron-interpretation|Neuron Interpretation]] — unit-level view
- [[wiki/concepts/transformer-lens|TransformerLens]] — the tooling
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/activation-engineering|Activation Engineering]]
