---
type: "concept"
title: "Hugging Face"
description: "The hub, libraries, and community platform that standardizes model sharing and ML tooling"
tags: ["hugging-face", "transformers", "ecosystem", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Hugging Face

## Summary
Hugging Face is the central platform of the open ML ecosystem: model hub, tokenizers, datasets, and the transformers library. It is where most open models are published and consumed.

## Details
- Transformers library provides unified APIs across PyTorch/TensorFlow/JAX for thousands of models.
- Model Hub hosts weights, tokenizers, configs, and model cards with versioning.
- Datasets and evaluation tooling (leaderboards, eval harnesses) live in the same ecosystem.
- RSIS3 relevance: mykb's model telemetry can reference HF model IDs as canonical identifiers.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — What the transformers library implements
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The backend most HF models use
- [[wiki/ai-ml/model-cards|Model Cards]] — Hub documentation standard
- [[wiki/ai-ml/llama|Llama]] — Models distributed via the hub
- [[wiki/ai-ml/quantisation|Quantisation]] — Quantized artifacts shared on the hub
