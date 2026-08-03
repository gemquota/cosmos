---
type: "concept"
title: "Sparse Autoencoders"
description: "SAEs: unsupervised models that decompose activations into sparse, interpretable feature directions"
tags: ["sparse-autoencoders", "interpretability", "sae"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Sparse Autoencoders

## Summary
Sparse autoencoders learn to reconstruct activations as sparse combinations of feature directions, revealing interpretable concepts (e.g., 'Python code', 'flattery', 'dates'). They are the leading tool for dictionary-learning-style interpretability of LLMs.

## Details
- **Training setup** — an encoder maps an activation vector to a much wider sparse feature space, a decoder reconstructs the original vector, and training minimizes reconstruction error plus an L1 sparsity penalty on the features; the dictionary is learned without any labels, so features emerge purely from the statistics of the activations.
- **What emerges** — features are interpretable directions that fire on specific concepts or contexts — code syntax, flattery, dates, persona switches — and the same feature can reappear across layers and models, suggesting shared structure in how LLMs represent knowledge.
- **Interpretability caveats** — many features are polysemantic (mixing several concepts) or dead (never firing), and automated interpretability scoring and human audits disagree on what counts as 'interpretable'; a named feature is a hypothesis, not a proof, and needs causal validation.
- **Use cases** — features have been used to steer behaviour (amplifying or suppressing a direction changes outputs), to detect concepts like deception or refusal, and to locate where facts are stored; these levers turn SAEs from descriptive tools into intervention tools.
- **Cost** — training SAEs on large models is a research-scale undertaking: millions of feature dimensions, careful hyperparameter sweeps over sparsity and learning rate, and large activation datasets; the compute budget must be justified by a concrete downstream use.
- **RSIS3 relevance** — SAE-style analysis could surface why prompts misbehave, feeding mykb's gap reports: if a recurring failure mode (e.g., flattery or sycophantic agreement in RSIS3's self-critique loop) maps to a consistent feature, the loop can detect and correct the pattern at the representation level rather than chasing symptoms in output text.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The field SAEs serve
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — SAEs are its core instrument
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — Features give directions to steer
- [[wiki/ai-ml/probing|Probing]] — The predecessor approach
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Companion layer-reading technique
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Feature detection for attack identification
