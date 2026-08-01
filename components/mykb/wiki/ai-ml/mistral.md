---
type: "concept"
title: "Mistral"
description: "Mistral AI's open-weight and commercial LLM family, known for efficiency and strong small models"
tags: ["mistral", "llm", "open-weights", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Mistral

## Summary
Mistral's models (Mistral 7B, Mixtral, and successors) emphasize efficiency, strong small-model performance, and permissive open weights. They are a popular middle ground between frontier APIs and fully local stacks.

## Details
- Mistral 7B demonstrated near-Llama-2-13B quality at 7B scale; Mixtral pioneered open MoE routing.
- Available via hosted API and open weights with commercial licensing.
- Good quantization behaviour makes them common in edge and on-device setups.
- RSIS3 relevance: Mistral-class models are strong candidates for RSIS3's local L2/L3 fine-tune experiments.

## Related
- [[wiki/ml-frameworks/ollama|Ollama]] — Serves Mistral weights locally
- [[wiki/ml-frameworks/vllm|vLLM]] — High-throughput serving for Mistral
- [[wiki/ai-ml/quantisation|Quantisation]] — Small-model deployment technique
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Open-model eval comparisons
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — MoE variant architecture
