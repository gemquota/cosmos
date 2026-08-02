---
type: "concept"
title: "OpenRouter and Prompt Caching"
description: "Multi-provider API gateway plus automatic caching of shared prompt prefixes to cut cost and latency"
tags: ["caching", "routing", "cost"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# OpenRouter and Prompt Caching

## Summary
Multi-provider API gateway plus automatic caching of shared prompt prefixes to cut cost and latency

## Details
- OpenRouter exposes many models through one API with per-model pricing and credits.
- Prompt caching stores common prefixes so repeated calls bill less and answer faster.
- Caches are typically automatic for stable prefixes like system prompts.
- Gateways can surface cache hit rates for cost accounting.

## Related
- [[wiki/llm-agents/semantic-caching|Semantic Caching]] — semantic analog of prefix caching
- [[wiki/llm-agents/inference-caching|Inference Caching]] — caching family
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — gateway category
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — how cache savings show up
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — gateway routing behavior
