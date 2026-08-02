---
type: "concept"
title: "LLM Evaluation, Serving, and LLMOps"
description: "Evaluating, serving, and operating LLM systems in production"
tags: ["llmops", "evaluation", "serving", "operations"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/openai/evals", "https://github.com/EleutherAI/lm-evaluation-harness"]
---

# LLM Evaluation, Serving, and LLMOps

## Summary
LLM evaluation and LLMOps is the discipline of measuring model quality and running it reliably in production — evals, monitoring, versioning, cost control, and serving infrastructure. It treats models as software artifacts with SLAs. The field is young, so most organizations assemble tooling from evals harnesses, gateways, and observability platforms.

## Details
- **Evaluation** — offline evals on golden sets, LLM-as-judge scoring, and online feedback; evaluations gate every prompt or model change.
- **Serving** — vLLM, TGI, and cloud APIs with continuous batching, autoscaling, and fallbacks.
- **Monitoring** — latency, cost, error rates, drift, and qualitative output sampling in production.
- **Versioning** — prompts, models, and configs are versioned and deployed through CI/CD with canaries.
- **Worked example** — a release pipeline runs regression evals on a candidate model, deploys to 5% of traffic, compares metrics, then rolls to 100%.
- **mykb relevance** — mykb's evaluation and ops documentation covers the same lifecycle for the knowledge system and its agents.

## Related
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — versioning models
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — the deployment pipeline
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — serving infrastructure
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judge-based evaluation
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — detecting drift
- [[wiki/ai-ml/llm-leaderboards|LLM Leaderboards]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
