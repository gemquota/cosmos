---
type: "concept"
title: "Model Fallback Chains"
description: "Ordered sequences of models tried when a primary model fails or degrades"
tags: ["fallback-chains", "routing", "reliability", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Fallback Chains

## Summary
Ordered sequences of models tried when a primary model fails or degrades

## Details
- Fallbacks trigger on errors, timeouts, or quality gates.
- Chains typically step down cost and capability.
- Fallback logic lives in llm-gateway-and-routing.
- Paired with model-routing-rules.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — primary routing
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — gateway layer
- [[wiki/agent-systems/provider-failover|Provider Failover]] — provider-level fallback
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — service degradation
- [[wiki/agent-systems/endpoint-health-checks|Endpoint Health Checks]] — trigger source
