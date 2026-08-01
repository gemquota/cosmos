---
type: "concept"
title: "JAX"
description: "Google's numerical library with autodiff and XLA compilation, popular for ML research and TPU training"
tags: ["jax", "deep-learning", "framework", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# JAX

## Summary
JAX combines NumPy-style API with automatic differentiation, JIT compilation, and hardware portability. It powers much frontier research (DeepMind, Google) and increasingly efficient LLM training.

## Details
- Function transformations (jit, grad, vmap, pmap) make research code concise and fast.
- XLA compilation targets TPU/GPU efficiently; used by PaLM- and Gemini-scale training.
- Steeper learning curve than PyTorch; ecosystem is smaller but research-forward.
- RSIS3 relevance: relevant when replicating research methods (e.g., DeepSeek-style training) on TPUs.

## Related
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The mainstream alternative
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — The production sibling
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — JAX powers the training runs that test them
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — HF supports JAX for many models
- [[wiki/ai-ml/gemini|Gemini]] — Google models trained with JAX-scale tooling
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — JAX powers research-scale fine-tuning
