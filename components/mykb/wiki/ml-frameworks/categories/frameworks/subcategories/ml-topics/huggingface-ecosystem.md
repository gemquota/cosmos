---
type: "entity"
title: "HuggingFace Ecosystem"
tags: ["ml", "huggingface", "models", "transformers", "hub"]
source: ["session-019ebdb9.md"]
---

# HuggingFace Ecosystem

HuggingFace as the primary model hub and ecosystem for open-source ML models.

## Usage Patterns in Sessions

- **Model Discovery** — Searching for models by architecture, size, license via Hub API
- **Config Inspection** — Retrieving model configs (`google/gemma-4-12b-it`, `google/gemma-3-27b-it`) via `curl` to HuggingFace API
- **GGUF Quantized Models** — Finding quantization-ready versions on TheBloke and other community organizations
- **Transformers Library** — The primary SDK for loading and running HF models

## Key Endpoints Used

- `https://huggingface.co/api/models/{org}/{model}` — Config and metadata
- `https://huggingface.co/{org}/{model}/raw/main/config.json` — Raw config files

See also: [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/gemma-models|Gemma Models]], [[wiki/ml-frameworks/categories/frameworks/subcategories/ml-topics/llm-inference|LLM Inference]]
