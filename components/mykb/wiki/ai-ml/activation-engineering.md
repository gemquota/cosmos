---
type: "concept"
title: "Activation Engineering"
description: "Modifying hidden activations at inference time to steer behaviour — a lightweight alternative to fine-tuning"
tags: ["activation-engineering", "interpretability", "steering", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Activation Engineering

## Summary
Activation engineering adjusts internal activations (add or subtract steering vectors) during inference to shift behaviour without touching weights. It can steer refusal, persona, and style with surprising precision.

## Details
- Steering vectors are often computed as differences between activation states (e.g., honest vs. dishonest).
- Methods: activation addition, inference-time intervention, and representation engineering (RepE).
- Cheaper than fine-tuning and reversible per request; less robust to distribution shift.
- RSIS3 relevance: steering could implement per-task persona shifts in RSIS3's L1 loop without retraining.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The field that motivates interventions
- [[wiki/ai-ml/probing|Probing]] — Finding the directions to steer along
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Feature directions for steering
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — A behaviour steering targets
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Understanding the mechanism behind steering
- [[wiki/ai-ml/guardrails|Guardrails]] — Steering as a runtime control layer
