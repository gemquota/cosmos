---
type: "concept"
title: "Interpretability Tools"
description: "Tools for inspecting what models compute and why they behave as they do"
tags: ["interpretability", "mechanics", "inspection", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.01610", "https://arxiv.org/abs/2401.10020"]
---

# Interpretability Tools

## Summary
Interpretability tools expose the internal states and mechanisms of models: activations, attention patterns, circuits, and feature directions. They convert black-box behavior into inspectable evidence. Current tools are research-grade, but they already catch data issues, prompt-sensitivity, and some safety problems.

## Details
- **Tool families** — logit lens and probing read hidden states; sparse autoencoders isolate feature directions; attention visualization shows what tokens attend to; activation patching tests causal roles.
- **Uses** — debugging sycophancy, finding concept confusion, verifying safety-tuning effects, and monitoring for behavioral drift.
- **Worked example** — a logit-lens pass on a misbehaving model shows the refusal concept activating on benign inputs, tracing a data or tuning bug.
- **Limitations** — mechanistic findings are model-specific and rarely port across architectures; interpretability is slower than behavioral evals.
- **mykb relevance** — interpretability, mechanistic interpretability, logit lens, and sparse autoencoders are existing mykb topics.
- Worked example: a sparse autoencoder trained on layer activations isolates a feature that fires on praise; intervening on that feature shifts the model tone, demonstrating causal control.

## Related
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — mechanistic analysis
- [[wiki/ai-ml/logit-lens|Logit Lens]] — reading hidden states
- [[wiki/ai-ml/probing|Probing]] — probing classifiers
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — feature extraction
- [[wiki/ai-ml/interpretability|Interpretability]] — existing interpretability concept
- [[wiki/ai-ml/activation-engineering|Activation Engineering]] — steering activations
- [[wiki/testing/traces-spans|Traces and Spans]] — related concept in this cluster
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — related concept in this cluster
