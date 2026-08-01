---
type: "concept"
title: "Sparse Autoencoders"
description: "SAEs: unsupervised models that decompose activations into sparse, interpretable feature directions"
tags: ["sparse-autoencoders", "interpretability", "sae"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Sparse Autoencoders

## Summary
Sparse autoencoders learn to reconstruct activations as sparse combinations of feature directions, revealing interpretable concepts (e.g., 'Python code', 'flattery', 'dates'). They are the leading tool for dictionary-learning-style interpretability of LLMs.

## Details
- Training: reconstruct the activation with an L1 penalty to force sparsity; features emerge without labels.
- Feature interpretability is evaluated by automated and human audits; many features are polysemantic or hard to name.
- SAE features have been used to steer behaviour and to detect concepts like deception.
- Compute-heavy: SAE training on large models is a research-scale undertaking.
- RSIS3 relevance: SAE-style analysis could surface why prompts misbehave, feeding mykb's gap reports.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The field SAEs serve
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — SAEs are its core instrument
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — Features give directions to steer
- [[wiki/ai-ml/probing|Probing]] — The predecessor approach
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Companion layer-reading technique
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Feature detection for attack identification
