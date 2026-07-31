---
type: "entity"
title: "LLM Inference Tools"
tags: ["ml", "llm", "inference", "gguf", "ollama", "quantization"]
source: ["session-019ebdb9.md", "session-89e039d9.md"]
---

# LLM Inference Tools

Tools and frameworks for running LLM inference, researched across multiple sessions.

## Tool Stack

- **Ollama** — Local GGUF model runner, used for Gemma 2/3/4 deployment
- **GGUF Quantization** — Model compression format for consumer GPUs (q4_k_m, q5_k_m, q8_0)
- **Transformers (Python)** — Full-precision inference via HuggingFace Transformers
- **Petals** — Distributed inference across network nodes
- **exo** — Community-run distributed inference

## VRAM Requirements (Researched)

| Model | FP16 | Q8 | Q4 |
|-------|------|-----|-----|
| Gemma 4 12B | 24GB | 12GB | 6GB |
| Gemma 4 26B MoE | 52GB | 26GB | 13GB |
| Gemma 3 27B | 54GB | 27GB | 13.5GB |

## Colab-Based Deployment

The most practical path identified: Colab T4 (16GB) + Q4 quantized Gemma 4 12B via Ollama-Colab.

See also: [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/colab-gpu|Colab GPU]], [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/gemma-models|Gemma Models]]
