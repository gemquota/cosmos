---
type: "concept"
title: "PyTorch"
description: "Meta's Python deep-learning framework, the de facto standard for training and serving LLMs"
tags: ["pytorch", "deep-learning", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# PyTorch

## Summary

PyTorch is the dominant ML framework: eager-by-default tensors with autograd, a mature ecosystem (transformers, torchvision, Lightning), and production paths via torch.compile, TorchScript, and ONNX export. It is the framework most models in the wiki's stack are trained and fine-tuned with.

## Details
- Mechanism: tensors execute eagerly (easy debugging), autograd records operations for backprop, modules organize parameters, DataLoader pipelines data, and torch.compile (TorchInductor) JIT-optimizes for speed; distributed (DDP, FSDP, DTensor) scales training; export paths (script, ONNX, eager mode) move models to inference.
- Concrete example: a fine-tuning run loads a transformers model, wraps it in FSDP for multi-GPU, trains with AMP, and checkpoints with the optimizer state; a serving pipeline exports to ONNX or serves the eager model behind an engine; a research prototype iterates eagerly and compiles only the hot path.
- Failure modes: device management (CPU/GPU tensor mismatches); nondeterminism across runs without seeding; checkpoint incompatibilities across versions; and eager-mode performance that hides until torch.compile or export is applied.
- Operational tradeoffs: PyTorch's ecosystem and debuggability dominate research and fine-tuning; the trade is performance work (compile/export) before production; the discipline is seeding for reproducibility, pinned versions, and a benchmark between eager, compiled, and exported paths.
- RSIS3/mykb relevance: the wiki's training recipes standardize on PyTorch with pinned versions and seed policies, so the loop's experiments reproduce across runs.
- DataLoader pitfalls: worker count, pin_memory, and prefetch factor dominate throughput; profile the data path before blaming the model.
- Determinism: set seeds and torch.use_deterministic_algorithms where supported; full determinism has a performance cost, so choose the level your reproducibility needs.
- Checkpointing: save optimizer state and RNG state alongside weights so a resumed run reproduces; partial checkpoints are the common source of "resume drift".
- Ecosystem leverage: prefer well-maintained libraries (transformers, PEFT, Lightning) over hand-rolled training loops; the framework's value is the ecosystem, not the tensor API.

## Related
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — The library ecosystem built on PyTorch
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — The main competing framework
- [[wiki/ml-frameworks/jax|JAX]] — The research-oriented alternative
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — PyTorch is where fine-tuning happens
- [[wiki/ml-frameworks/vllm|vLLM]] — PyTorch-based serving engine
