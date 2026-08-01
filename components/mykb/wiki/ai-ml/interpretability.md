---
type: "concept"
title: "Interpretability"
description: "Methods for understanding what models compute and why they produce the outputs they do"
tags: ["interpretability", "llm", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Interpretability

## Summary
Interpretability aims to open the black box: locating concepts in activations, tracing reasoning, and predicting failure modes. It is a research frontier with practical payoffs for debugging, safety, and eval design.

## Details
- Levels: behavioural (probing), mechanistic (circuits), and architectural (feature analysis).
- Practical uses: detecting hidden prompt injection, finding knowledge conflicts, auditing bias.
- Fast-moving field; findings transfer unevenly across model families.
- RSIS3 relevance: interpretability of RSIS3's own models could explain why certain prompts fail or drift.

## Related
- [[wiki/ai-ml/probing|Probing]] — Reading information from activations
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Reverse-engineering circuits
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Feature extraction from activations
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Reading predictions from intermediate layers
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Interpreting attention weights
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Interpretability informs eval design
