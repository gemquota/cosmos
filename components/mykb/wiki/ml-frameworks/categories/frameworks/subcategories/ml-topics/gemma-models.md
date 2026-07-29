---
type: "entity"
title: "Gemma Models"
tags: ["ml", "google", "model", "llm", "open-source"]
source: ["session-019ebdb9.md"]
---

# Gemma Models

Google's Gemma family of open-source LLMs, extensively researched across multiple sessions. Gemma 4 includes 12B and 26B MoE (Mixture of Experts) variants.

## Model Variants

- **Gemma 4 12B** — Single GPU capable (T4 16GB VRAM with quantization)
- **Gemma 4 26B MoE** — Mixture of Experts architecture, requires model sharding or high-VRAM
- **Gemma 3 27B** — Previous generation, 27B parameters
- **Gemma 2 9B/27B** — Earlier generation, well-supported by GGUF/Ollama

## Deployment Patterns

Research from sessions shows exploration of:
- GGUF quantized formats for consumer GPUs (T4, RTX)
- Google Colab for free GPU access
- Model sharding across multiple Colab instances via Petals/exo
- Ollama for local deployment of smaller variants

## Key Resources

- HuggingFace: `google/gemma-4-12b-it`, `google/gemma-4-26b-moe-it`
- GGUF conversion for memory-constrained environments
- Colab notebooks for free-tier GPU inference

See also: [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/model-sharding|Model Sharding]], [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/colab-gpu|Colab GPU]]
