---
type: "concept"
title: "Probing"
description: "Training small classifiers on model activations to test what information is linearly available at each layer"
tags: ["probing", "interpretability", "activations"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Probing

## Summary
Probing trains lightweight classifiers on hidden representations to see whether a property (e.g., part-of-speech, truthfulness) is encoded. High probe accuracy means the information is linearly accessible.

## Details
- Probes measure representation, not causation: a probe finding a feature does not prove the model uses it.
- Common probe families: linear classifiers, logistic probes, and contrastive probes.
- Modern practice controls for probe artefacts with careful baselines.
- RSIS3 relevance: probing could detect whether RSIS3's models encode wiki context reliably.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella field
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — Intervening where probes read
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — The modern successor to simple probing
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Layer-wise prediction reading
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — The deeper cousin of probing
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Probes as an evaluation instrument
