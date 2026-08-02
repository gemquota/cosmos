---
type: "concept"
title: "Provider Failover"
description: "Automatic switching between LLM providers when one becomes unavailable"
tags: ["failover", "providers", "reliability", "routing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Provider Failover

## Summary
Automatic switching between LLM providers when one becomes unavailable

## Details
- Health checks and error rates trigger failover.
- Failover must preserve request semantics and budgets.
- Multi-provider strategy reduces single-vendor risk.
- Operates inside llm-gateway-and-routing.

## Related
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — gateway layer
- [[wiki/agent-systems/endpoint-health-checks|Endpoint Health Checks]] — health source
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — model-level fallback
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — retry policy
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — fallback quality
