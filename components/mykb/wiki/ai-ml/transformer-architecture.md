---
type: "concept"
title: "Transformer Architecture"
description: "The attention-based neural network architecture that underlies virtually all modern LLMs"
tags: ["transformers", "architecture", "llm", "deep-learning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"]
---

# Transformer Architecture

## Summary
The transformer replaced recurrence with self-attention, enabling parallel training and long-range dependencies. 'Attention Is All You Need' introduced it in 2017 and every major LLM since descends from it.

## Details
- Core stack: token embeddings, positional encoding, stacked encoder/decoder (or decoder-only) blocks of attention plus feedforward layers.
- Decoder-only transformers are the standard LLM shape: predict next token, repeatedly.
- Parallelization made large-scale pretraining feasible for the first time.
- RSIS3 relevance: architecture choice constrains context windows, sampling, and cost — the constants RSIS3 plans around.
- The core stack is a token embedding plus positional information, followed by stacked blocks of multi-head self-attention and per-token feedforward layers, each wrapped in residual connections and layer normalization.
- Decoder-only transformers predict the next token autoregressively and are the standard LLM shape; encoders are used for representation tasks; encoder-decoders for sequence-to-sequence.
- Training parallelizes across tokens within a sequence because self-attention replaces recurrence, which is what made large-scale pretraining feasible.
- Practical costs scale with context length and parameter count, so architecture choice trades quality against memory, latency, and energy.
- **Worked example / comparison** — Worked example — an LLM generating an answer runs the same decoder blocks repeatedly; the KV cache keeps prior attention keys and values so each new token costs one forward pass, not a full re-run.
- For mykb, architecture knowledge is evergreen documentation: it is promoted once, then maintained on the longest freshness cadence because the fundamentals change slowly.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]]
- [[wiki/ai-ml/self-attention|Self-Attention]]
- [[wiki/ai-ml/positional-encoding|Positional Encoding]]
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]]
- [[wiki/ml-frameworks/pytorch|PyTorch]]
- [[wiki/ai-ml/quantisation|Quantisation]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
