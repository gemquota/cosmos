---
type: "concept"
title: "TensorFlow"
description: "Google's ML framework with production serving focus, used across Google's model stack"
tags: ["tensorflow", "deep-learning", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# TensorFlow

## Summary
TensorFlow pioneered large-scale ML deployment with static graphs, TF Serving, and mobile support. Its LLM presence has faded relative to PyTorch, but it remains important for production and on-device stacks.

## Details
- Keras is the high-level API; TF Serving handles production inference.
- TPU tooling integrates deeply with Google Cloud and Gemini infrastructure.
- Legacy ecosystem: many production systems still run TF checkpoints.
- RSIS3 relevance: mostly relevant when integrating with Google-hosted models and TPU-scale training.

## Related
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The dominant competitor
- [[wiki/ml-frameworks/jax|JAX]] — Google's research successor
- [[wiki/ml-frameworks/google-gemini|Google Gemini]] — Google's model family built on its stack
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — Implemented across frameworks
- [[wiki/ml-frameworks/onnx|ONNX]] — Interop format spanning frameworks
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — TF checkpoints still fine-tuned in production
