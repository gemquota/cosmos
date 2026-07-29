---
type: "entity"
title: "Google Colab for GPU"
tags: ["ml", "colab", "gpu", "t4", "cloud"]
source: ["session-019ebdb9.md", "session-019f66ba.md"]
---

# Google Colab for GPU

Google Colab as a free-tier GPU compute platform for ML model inference and development.

## Key Findings from Sessions

- **T4 GPU (16GB VRAM)** — Available on free tier, sufficient for Gemma 4 12B with GGUF quantization
- **Session Time Limits** — Free tier sessions limited; need checkpointing/keepalive strategies
- **colab-ssh** — SSH access to Colab runtimes for persistent connections
- **colab-ollama-server** — Ollama on Colab for running GGUF models
- **Colab CLI tools** — Automating Colab session startup via CLI

## Automation Patterns

```
colab-cli → start session → SSH tunnel → load GGUF → serve API
```

This enables using Colab as a headless GPU server for local agent integration.

See also: [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/gemma-models|Gemma Models]], [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/model-sharding|Model Sharding]]
