---
type: "concept"
title: "PyTorch"
description: "Meta's Python deep-learning framework, the de facto standard for training and serving LLMs"
tags: ["pytorch", "deep-learning", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# PyTorch

## Summary
PyTorch is the dominant framework for modern LLM work: dynamic computation graphs, a mature ecosystem, and near-universal support from model libraries. Most open models are released as PyTorch checkpoints.

## Details
- Dynamic graphs and eager execution make research iteration fast; torch.compile adds speedups.
- Distributed training (DDP, FSDP, tensor/pipeline parallelism) underpins frontier-scale runs.
- Ecosystem: HF transformers, LoRA libraries, vLLM, and countless tools build on it.
- RSIS3 relevance: RSIS3's fine-tune and inference tooling assumes PyTorch-compatible checkpoints.

## Related
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — The library ecosystem built on PyTorch
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — The main competing framework
- [[wiki/ml-frameworks/jax|JAX]] — The research-oriented alternative
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — PyTorch is where fine-tuning happens
- [[wiki/ml-frameworks/vllm|vLLM]] — PyTorch-based serving engine
