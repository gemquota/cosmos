---
type: "concept"
title: "Transformer Architecture"
description: "The attention-based neural network architecture that underlies virtually all modern LLMs"
tags: ["transformers", "architecture", "llm", "deep-learning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Transformer Architecture

## Summary
The transformer replaced recurrence with self-attention, enabling parallel training and long-range dependencies. 'Attention Is All You Need' introduced it in 2017 and every major LLM since descends from it.

## Details
- Core stack: token embeddings, positional encoding, stacked encoder/decoder (or decoder-only) blocks of attention plus feedforward layers.
- Decoder-only transformers are the standard LLM shape: predict next token, repeatedly.
- Parallelization made large-scale pretraining feasible for the first time.
- RSIS3 relevance: architecture choice constrains context windows, sampling, and cost — the constants RSIS3 plans around.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — The core operation of the transformer
- [[wiki/ai-ml/self-attention|Self-Attention]] — The variant transformers use internally
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — How order is injected into attention
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]] — The per-token transformation in each block
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The framework most transformers are built in
- [[wiki/ai-ml/quantisation|Quantisation]] — How transformer models get deployed at scale
