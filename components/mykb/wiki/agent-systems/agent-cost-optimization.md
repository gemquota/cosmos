---
type: "concept"
title: "Agent Cost Optimization"
description: "Reducing token, latency, and operational costs of agent systems without losing quality"
tags: ["agents", "cost", "optimization", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://openrouter.ai/docs", "https://platform.openai.com/docs/guides/prompt-caching"]
---

# Agent Cost Optimization

## Summary
Agent cost optimization reduces the dominant expense of agent systems — tokens — by spending them where they matter: fewer calls, smaller contexts, cached inputs, and cheaper models for easy steps. Cost is a design constraint that shapes architecture. Optimization must be measured against quality, not just spend.

## Details
- **Levers** — prompt caching, semantic caching of identical calls, model routing (small model for classification, large for reasoning), and context compression.
- **Architectural levers** — fewer agent hops, summary-of-context instead of full history, and batching independent calls.
- **Measurement** — token accounting per run and per step; latency budgets connect cost to user experience.
- **Worked example** — a triage flow routes 80% of requests to a small model with a rubric, reserving the frontier model for 20% that need reasoning.
- **Tradeoffs** — aggressive optimization raises regression risk; shadow evaluation keeps quality gates on optimized paths.
- **mykb relevance** — RSIS3's token budgets and model routing rules are the same optimization discipline applied to recursive self-improvement.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — routing to cheaper models
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — unit economics
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — caching prompt prefixes
- [[wiki/prompt-engineering/context-compression|Context Compression]] — shrinking context cost
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency and cost together
- [[wiki/testing/token-usage-tracking|Token Usage Tracking]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — the API surface it uses
