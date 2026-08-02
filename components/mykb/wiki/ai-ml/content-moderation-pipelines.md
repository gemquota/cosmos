---
type: "concept"
title: "Content Moderation Pipelines"
description: "Automated pipelines that filter or flag unsafe model inputs and outputs"
tags: ["moderation", "safety", "pipelines", "filtering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/moderation", "https://arxiv.org/abs/2209.10282"]
---

# Content Moderation Pipelines

## Summary
Content moderation classifies text and images for policy violations before or after model generation. It matters because models can produce harmful content despite safety training. Pipelines combine classifiers, model-based judges, and human review queues.

## Details
- **Layers** — input filtering (blocked queries), output filtering (unsafe generations), and user reporting.
- **Classifiers** — trained moderation models score categories like hate, harassment, and self-harm; thresholds set the operating point.
- **Worked example** — a chatbot runs every output through a moderation classifier; above-threshold outputs are replaced with a refusal and logged.
- **Trade-off** — strict filters reduce harm but increase false positives that frustrate users.
- **mykb relevance** — personal knowledge systems should still filter injection attempts and unsafe retrieved content.
- **Queue design** — borderline scores route to human review with clear appeal paths, preventing both over-blocking and under-blocking.
- **Evaluation** — moderation accuracy is measured on labeled test sets with precision/recall tuned per harm category.
- **Worked example** — a chatbot runs every output through a moderation classifier; above-threshold outputs are replaced with a refusal and logged for review.

## Related
- [[wiki/ai-ml/llm-safety-policies|LLM Safety Policies]] — policy source
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — guardrail family
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — malicious inputs
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — testing filters
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — data-side filtering
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — related concept in this cluster
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — safety training
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — refusal behavior
