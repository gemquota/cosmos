---
type: "concept"
title: "JAX"
description: "Google's numerical library with autodiff and XLA compilation, popular for ML research and TPU training"
tags: ["jax", "deep-learning", "framework", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# JAX

## Summary

JAX is a numerical computing library for high-performance ML research: NumPy-like API, automatic differentiation, JIT compilation to accelerators, and composable transforms (grad, jit, vmap, pmap). It powers much of the modern LLM research stack.

## Details
- Mechanism: functions are pure and compiled with jit; grad differentiates, vmap vectorizes, pmap/shard_map parallelize across devices; XLA compiles to TPU/GPU/CPU; immutability and functional style make transformations composable — the same function can be jitted, vmapped, and differentiated in any combination.
- Concrete example: a transformer trainer defines a forward pass, wraps it in grad + jit, and shards across TPUs with pmap/shard_map; an RL experiment vectorizes 1024 environments with vmap; a research prototype composes checkpointing and parallel data loading around a pure update function.
- Failure modes: JIT compilation errors that only surface at trace time (dynamic shapes break compilation); device-memory management (arrays must be placed explicitly); ecosystem friction (some libraries are TF/PyTorch-only); and the steeper learning curve for imperative-style programmers.
- Operational tradeoffs: JAX's performance and composability suit research and large-scale training; PyTorch's ease and ecosystem suit iterative development; the pragmatic pattern is research in JAX where transformations and TPU scale matter, with interop (jax2tf, safetensors) to the rest of the stack.
- RSIS3/mykb relevance: the wiki's training experiments record the framework choice and its reasoning, so the loop reuses proven stacks instead of re-litigating them.
- Debugging: jit obscures eager stack traces — use jax.debug and eager fallback for tracing issues, and keep shapes static where possible.
- Checkpointing: prefer orbax-style checkpoints with explicit device placement; JAX's async transfers make naive save/load races easy to hit.

## Related
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The mainstream alternative
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — The production sibling
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — JAX powers the training runs that test them
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — HF supports JAX for many models
- [[wiki/ai-ml/gemini|Gemini]] — Google models trained with JAX-scale tooling
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — JAX powers research-scale fine-tuning
