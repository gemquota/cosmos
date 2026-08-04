---
type: "concept"
title: "Small Language Models"
description: "Compact models tuned for efficiency, speed, and on-device deployment"
tags: ["slm", "models", "efficiency", "edge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Small Language Models

## Summary

Small language models (SLMs) are compact language models tuned for efficiency, speed, and deployment on constrained hardware such as laptops, phones, and edge servers. They trade raw capability for lower latency, cost, and memory footprint. SLMs matter because they make AI features practical where large models are too slow, too expensive, or too privacy-sensitive. The right comparison for an SLM is not against the largest model but against the task requirements and deployment constraints of the application.

## Details

- **Definition** — an SLM is a language model with relatively few parameters, designed to run within tight compute and memory budgets.
- **Capability gap** — small models underperform large ones on complex reasoning, but match them on focused, well-specified tasks.
- **Compression sources** — SLMs are trained from scratch, distilled from larger models, or pruned and quantized from existing checkpoints.
- **Deployment profile** — SLMs enable low latency, offline use, local privacy, and lower per-token cost, at the price of reduced generality.
- **Task fit** — they excel at classification, extraction, structured output, and tool-calling patterns where narrow competence suffices.
- **Worked example** — a phone assistant uses an on-device SLM for dictation and quick replies, reserving a large cloud model for complex requests.
- **Routing strategies** — serving systems often route simple queries to SLMs and escalate hard ones to large models, cutting average cost.
- **Failure modes** — small models hallucinate more on open-ended questions and are brittle on out-of-distribution inputs.
- **Practical relevance** — SLMs are central to edge inference and on-device deployment, and to cost engineering in high-volume APIs.
- **Evaluation** — choosing an SLM requires benchmarking the specific task mix, since aggregate leaderboard scores misrepresent narrow use cases.
- **Cost modeling** — at high request volumes, the per-token savings of small models can fund more capable infrastructure or features overall.


## Related

- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — the deployment target
- [[wiki/ml-frameworks/distillation-vs-quantization|Distillation vs Quantization]] — the compression routes
- [[wiki/ai-ml/model-quantization|Model Quantization]] — weight compression
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — the computing context
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — escalation policies
- [[wiki/ml-frameworks/routing-models|Routing Models]] — the router mechanism

