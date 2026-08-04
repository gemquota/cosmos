---
type: "concept"
title: "Qwen and Gemma"
description: "Open-weight model families from Alibaba and Google with strong multilingual and small-model variants"
tags: ["models", "open-weights", "multilingual"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Qwen and Gemma

## Summary
Qwen and Gemma are open-weight model families from Alibaba and Google, offering strong multilingual and small-model variants. They matter because they expand the open model landscape beyond the dominant families, giving teams more choices for language coverage and deployment size. Their compact variants make capable models feasible on-device. Small and multilingual variants are where these families change deployment math.

## Details
- **Definition** — these families release open-weight checkpoints spanning multiple sizes, from efficient small models to large-scale dense and mixture-of-experts architectures.
- **Multilingual strength** — Qwen models emphasize broad language coverage, making them a default choice for multilingual deployments.
- **Size range** — both families include compact variants suited to on-device-llm and edge deployments with limited compute.
- **Serving** — open checkpoints run on standard engines, so deployment follows the same vllm and llama-cpp patterns as other open families.
- **Worked example** — a team deploys a small Gemma variant on-device for a translation feature and a larger Qwen model server-side for multilingual chat.
- **Failure modes** — capability gaps on complex reasoning, license considerations, and hardware requirements differ by variant and must be checked.
- **Ecosystem fit** — both families broaden the open-weights-models category and add pressure to model-family-comparisons.
- **Practical relevance** — Qwen and Gemma give practitioners flexible cost and language trade-offs that the flagship open families may not cover.
- **Quantization** — lower-precision versions cut memory and latency at some quality cost.
- **Licensing** — per-model license terms vary, so legal review belongs in the selection process.
- **Worked example** — an edge app selects a quantized small variant after testing that quality holds on its target language.
- **Failure example** — assuming all variants share one license or one quality profile causes integration surprises.

## Related
- [[wiki/ai-ml/open-weights-models|Open-Weight Models]] — the ecosystem category
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — the size niche
- [[wiki/prompt-engineering/multilingual-prompting|Multilingual Prompting]] — language coverage
- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — the deployment target for small variants
- [[wiki/ai-ml/model-family-comparisons|Model Family Comparisons]] — comparing across families
