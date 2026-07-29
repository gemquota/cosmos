---
type: "entity"
title: "Model Sharding"
tags: ["ml", "distributed", "inference", "petals", "exo"]
source: ["session-019ebdb9.md"]
---

# Model Sharding

Distributed LLM inference across multiple devices, explored extensively for running large models on free-tier hardware.

## Approaches Researched

- **Petals/Hivemind** — Distributed LLM inference across the internet. P2P model sharding where each node handles a portion of the transformer layers.
- **exo-explore/exo** — Active open-source project for distributed model execution. Well-starred on GitHub.
- **Manual Sharding** — Splitting model layers across multiple Colab instances manually.

## Use Case

Running Gemma 4 26B MoE across multiple free Google Colab T4 instances (each with 16GB VRAM) by sharding the model layers:

```
Instance 1: Layers 1-20 (12B parameters)
Instance 2: Layers 21-40 (12B parameters)
Coordinator: Orchestrates inference via gRPC
```

See also: [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/gemma-models|Gemma Models]], [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/colab-gpu|Colab GPU]]
