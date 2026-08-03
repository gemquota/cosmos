---
type: "concept"
title: "Probing"
description: "Training small classifiers on model activations to test what information is linearly available at each layer"
tags: ["probing", "interpretability", "activations"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Probing

## Summary
Probing trains lightweight classifiers on hidden representations to see whether a property (e.g., part-of-speech, truthfulness) is encoded. High probe accuracy means the information is linearly accessible.

## Details
- **Mechanism** — a probe is a small model (typically logistic regression or a shallow MLP) trained on frozen activations at one or more layers to predict a target label; high held-out accuracy indicates the representation contains the information in a form the probe can read.
- **Probe families** — linear classifiers answer the cleanest question ('is this linearly separable?'); logistic probes and contrastive probes trade flexibility for interpretability; MLP probes detect non-linear structure but blur the distinction between 'encoded' and 'computable from the representation'.
- **Measurement, not causation** — a probe finding a feature does not prove the model uses it: the information could be a by-product of other computations, and probes can achieve high accuracy using spurious or low-frequency directions. Causal follow-ups (activation patching, feature ablation) are needed to show the feature matters.
- **Control baselines** — modern practice controls for probe artefacts with baselines such as control tasks (random labels), held-out-language checks, and comparing against representations from unrelated models, because probes will happily learn noise.
- **Layer trends** — accuracy trajectories across layers reveal where information enters and transforms: early-layer accuracy for syntactic properties, later layers for semantic ones, with information often being linearly decodable long before it is behaviourally used.
- **RSIS3 relevance** — probing could detect whether RSIS3's models encode wiki context reliably: train probes for 'is this claim grounded in the retrieved note?' on the model's activations during generation, giving a cheap early-warning signal for hallucinated or context-free outputs before they reach the knowledge graph.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella field
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — Intervening where probes read
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — The modern successor to simple probing
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Layer-wise prediction reading
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — The deeper cousin of probing
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Probes as an evaluation instrument
