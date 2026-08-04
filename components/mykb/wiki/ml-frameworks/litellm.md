---
type: "entity"
title: "LiteLLM"
description: "Proxy and SDK that normalizes hundreds of LLM providers behind one OpenAI-compatible interface"
tags: ["proxy", "routing", "multi-vendor"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# LiteLLM

## Summary
Proxy and SDK that normalizes hundreds of LLM providers behind one OpenAI-compatible interface

## Details
- Translates a single API shape to OpenAI, Anthropic, Gemini, Bedrock, and local engines.
- Adds routing, fallbacks, budgets, and logging at the proxy layer.
- Lets applications avoid vendor lock-in with minimal code change.
- Common choice for llm-gateway-and-routing deployments.

## Related
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — category it implements
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — failover behavior
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — policy-driven provider choice
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — budget controls it enforces
- [[wiki/ml-frameworks/openrouter-prompt-caching|OpenRouter and Prompt Caching]] — alternative gateway service
