---
type: "concept"
title: "Activation Engineering"
description: "Modifying hidden activations at inference time to steer behaviour — a lightweight alternative to fine-tuning"
tags: ["activation-engineering", "interpretability", "steering", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Activation Engineering

## Summary
Activation engineering adjusts a model's hidden activations during inference — adding or subtracting "steering vectors" at chosen layers — to shift behavior without touching weights. Unlike fine-tuning, it is per-request reversible, needs no training run, and can steer refusal behavior, persona, style, and even factual tendencies with surprising precision.

## Details
- Mechanism: the core primitive is the steering vector. A direction is computed from activation differences — for example, averaging the residual-stream activations at a layer over "honest" examples and subtracting those over "dishonest" examples gives a vector that, when added during decoding, shifts outputs toward honesty. Methods range from simple activation addition (`h + λv`) and inference-time interventions to representation engineering (RepE), which reads and writes "reading vectors" identified via contrastive datasets. Because the intervention happens in the forward pass only, it is trivially reversible per request and does not permanently alter the model.
- Concrete examples: adding a refusal-steering vector at the last few layers makes a model decline harmful requests it would otherwise answer, without a safety fine-tune; a persona vector shifts a code assistant toward a terse, senior-engineer style; a "truthfulness" vector measurably raises performance on honesty benchmarks; RepE-style probes can also *detect* internal states (deception, sycophancy) at runtime. The technique is popular in the open-source community precisely because it works on consumer hardware in a few lines of code.
- Failure modes: the classic failures are brittleness and overshoot: a steering strength (λ) that is too large produces incoherent or degenerate outputs, and the same vector that steers one model version may do nothing (or distort) on a fine-tuned successor because the representation space shifted. Steering is also not a guarantee — it is a soft intervention, so it can fail on adversarial or out-of-distribution inputs, and it does not remove the underlying capability, only biases its expression.
- Operational tradeoffs: activation engineering trades the durability of fine-tuning for speed and reversibility: no training data, no checkpoint, per-request control, and easy A/B testing of steering vectors in production. The tradeoffs are fragility across model versions, the need to recompute vectors when the model changes, and weaker guarantees than a trained behavior change. The practice rule: use steering for cheap, reversible behavior nudges; use fine-tuning when the behavior must be stable and general. RSIS3 relevance: steering could implement per-task persona shifts in RSIS3's L1 loop without retraining — a fast, reversible control layer, while durable behavior changes stay in the L2 fine-tune loop with the usual forgetting gates.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The field that motivates interventions
- [[wiki/ai-ml/probing|Probing]] — Finding the directions to steer along
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Feature directions for steering
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — A behaviour steering targets
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Understanding the mechanism behind steering
- [[wiki/ai-ml/guardrails|Guardrails]] — Steering as a runtime control layer
