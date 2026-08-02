---
type: "concept"
title: "Model Routing Rules"
description: "Policy rules deciding which model handles which request"
tags: ["routing-rules", "routing", "models", "policy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Routing Rules

## Summary
Policy rules deciding which model handles which request

## Details
- Rules match on task type, difficulty, cost, and latency needs.
- Implement routing-models at the gateway.
- Rules need testing against eval sets.
- A primary cost-control lever.

## Related
- [[wiki/ml-frameworks/routing-models|Routing Models]] — routing mechanism
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — failure path
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — execution layer
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — cost logic
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — selection policy
