---
type: "entity"
title: "Llama, Mistral, and DeepSeek"
description: "Leading open-weights model families that anchor the open model ecosystem"
tags: ["models", "open-weights", "comparison"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Llama, Mistral, and DeepSeek

## Summary
Llama, Mistral, and DeepSeek are leading open-weights model families that anchor the open model ecosystem. They matter because they let organizations self-host, fine-tune, and research with frontier-adjacent capability instead of renting closed APIs. Their ongoing releases keep pressure on the gap between open and closed models. Open-weight families are the substrate for private, adaptable AI.

## Details
- **Definition** — these families release model checkpoints with open weights that can be downloaded, served, and adapted by anyone.
- **Capability spread** — the families span small, efficient models to large frontier-scale checkpoints, covering deployment niches from edge to datacenter.
- **Self-hosting** — open weights enable running models on private infrastructure, which matters for privacy, cost control, and data residency.
- **Adaptation** — open checkpoints are the substrate for fine-tuning and instruction tuning, letting teams specialize behavior.
- **Licensing** — license terms differ across and within families and affect commercial use; license review is a prerequisite for adoption.
- **Serving** — open models run on engines like vllm and llama-cpp, with deployment choices depending on hardware and latency targets.
- **Worked example** — a company fine-tunes a small Llama variant for ticket routing on-premises, cutting API cost while keeping data in-house.
- **Failure modes** — capability gaps versus closed models, license surprises, and deployment complexity are the main adoption risks.
- **Practical relevance** — open-weights models define the self-hosted tier of the model economy and the competitive context for closed-model moats.
- **Community** — active ecosystems around these families provide tooling, adapters, and recipes.
- **Hardware** — deployment cost depends heavily on quantization and serving choices.
- **Failure example** — picking a family on headline benchmarks without testing on the actual workload leads to disappointment.

## Related
- [[wiki/ai-ml/open-weights-models|Open-Weight Models]] — the ecosystem category
- [[wiki/ml-frameworks/vllm|vLLM]] — a common serving engine
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — edge deployment
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — adapting open models
- [[wiki/ai-ml/closed-models-moat|The Closed-Model Moat]] — competitive context
