---
type: "concept"
title: "Model Fallback Chains"
description: "Ordered sequences of models tried when a primary model fails or degrades"
tags: ["fallback-chains", "routing", "reliability", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Fallback Chains

## Summary
Model fallback chains are ordered sequences of models tried when a primary model fails or degrades, stepping down in cost and capability as needed. They matter because no model is always available, and a graceful downgrade beats a failed request. Chains make degradation predictable and automatic. A fallback chain is a degradation contract written in advance.

## Details
- **Definition** — a fallback chain is a prioritized list of models, tried in order until one returns an acceptable result.
- **Triggers** — chains activate on errors, timeouts, rate-limit responses, or quality gates such as schema validation failures.
- **Direction** — chains typically step down in cost and capability, but can also step up when quality gates reject cheap output.
- **Placement** — fallback logic lives in llm-gateway-and-routing, where routing rules select the primary and chains handle the rest.
- **Worked example** — a request to a frontier model times out; the gateway retries with a mid-tier model, then serves a cached answer as the last resort.
- **Failure modes** — cascading timeouts across the whole chain, fallbacks with incompatible outputs, and silent quality drops are the main risks.
- **Pairing** — chains pair with model-routing-rules for primary selection and provider-failover for provider-level issues.
- **Practical relevance** — fallback chains are how agent platforms deliver availability commitments and feed degraded-mode-operations.
- **Output compatibility** — fallback models should produce compatible output shapes or the chain must transform them.
- **Quality gates** — schema and content checks decide whether a fallback result is acceptable or the chain should continue.
- **Worked example** — a chain tries a frontier model, then a mid-tier model, then a cached response, each gated by validation.
- **Failure example** — a chain that silently falls back on every request hides a primary outage from operators.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — picking the primary model
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — where chains execute
- [[wiki/agent-systems/provider-failover|Provider Failover]] — provider-level fallback
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — the reduced-service state chains support
- [[wiki/agent-systems/endpoint-health-checks|Endpoint Health Checks]] — the signal that triggers fallback
