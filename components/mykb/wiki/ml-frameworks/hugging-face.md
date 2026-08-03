---
type: "concept"
title: "Hugging Face"
description: "The hub, libraries, and community platform that standardizes model sharing and ML tooling"
tags: ["hugging-face", "transformers", "ecosystem", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Hugging Face

## Summary

Hugging Face is the open-model ecosystem: Hub (datasets, models, spaces), transformers/diffusers libraries, and safetensors weights. It is how teams adopt and fine-tune open models instead of being locked to hosted APIs.

## Details
- Mechanism: the Hub stores model weights, tokenizers, configs, and datasets with versioning and metadata; transformers loads them into PyTorch/JAX/TF pipelines; safetensors provides safe, fast weight serialization; inference can run locally or via Inference Endpoints; datasets and spaces (demo apps) complete the loop from data to deployment.
- Concrete example: a team pulls a small instruction-tuned model for local serving via llama.cpp/transformers, fine-tunes it on wiki-style notes with PEFT/LoRA, and pushes the adapter back to the Hub; an eval suite runs a set of leaderboard tasks before adopting a new base model.
- Failure modes: supply-chain risk — model weights are code-adjacent (pickle payloads; prefer safetensors and pinned revisions); license confusion (weights licenses vary from permissive to restrictive — check before commercial use); cache/dedup issues across team machines; and local-vs-hosted quality gaps when models are quantized too aggressively.
- Operational tradeoffs: open models buy control, privacy, and cost predictability at the cost of infrastructure and expertise; the discipline is pinned revisions, safetensors, license review, and a reproducible local serving stack.
- RSIS3/mykb relevance: the wiki's local runtimes source pinned open models from the Hub, with license and revision recorded per experiment.
- Reproducibility: pin the full commit revision (not just the model name) in training and eval configs; Hub revisions change and silent weight updates invalidate experiments.
- Offline practice: mirror required models/datasets to internal storage for air-gapped or unreliable-network runs, and verify checksums before load.
- Storage hygiene: model caches grow fast (multi-GB per model); manage HF_HOME with a shared cache policy so teams do not re-download or fill disks.
- Fine-tuning stack: transformers + PEFT (LoRA/QLoRA) is the standard adaptation path; record the base revision and adapter config for reproducible fine-tunes.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — What the transformers library implements
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The backend most HF models use
- [[wiki/ai-ml/model-cards|Model Cards]] — Hub documentation standard
- [[wiki/ai-ml/llama|Llama]] — Models distributed via the hub
- [[wiki/ai-ml/quantisation|Quantisation]] — Quantized artifacts shared on the hub
