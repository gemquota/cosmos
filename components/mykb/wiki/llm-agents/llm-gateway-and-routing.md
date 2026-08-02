---
type: "concept"
title: "LLM Gateway and Routing"
description: "A central service for auth, routing, quotas, and observability across LLM providers"
tags: ["llm", "gateway", "routing", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/BerriAI/litellm", "https://github.com/Portkey-AI/gateway"]
---

# LLM Gateway and Routing

## Summary
An LLM gateway sits between applications and model providers, centralizing keys, routing, retries, caching, quotas, and observability. It turns per-application provider glue into a governed shared service. Gateways are the control plane for model spend, reliability, and policy.

## Details
- **Capabilities** — unified API surface, provider failover, model routing rules, semantic caching, rate limiting, and usage logging.
- **Routing** — route by task difficulty, cost budget, or latency target; fallback chains try the next provider on failure.
- **Policy enforcement** — content filtering, PII redaction, and key scoping happen in one place instead of every app.
- **Worked example** — a gateway routes summarization to a cheap model, routes reasoning to a frontier model, caches identical prompts, and logs every call with cost.
- **Open source options** — LiteLLM and Portkey provide gateway functionality on top of provider SDKs.
- **mykb relevance** — RSIS3's model routing rules and cost controls are gateway patterns applied at the agent level.

## Related
- [[wiki/ml-frameworks/litellm|LiteLLM]] — LiteLLM gateway implementation
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — routing decisions
- [[wiki/agent-systems/provider-failover|Provider Failover]] — failing over between providers
- [[wiki/agent-systems/rate-limiter-design|Rate Limiter Design]] — quotas at the gateway
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — fallback ordering
- [[wiki/ml-frameworks/openrouter-prompt-caching|OpenRouter and Prompt Caching]] — related concept in this cluster
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — the API surface it uses
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — embeddings access
