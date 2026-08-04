---
type: "concept"
title: "Model Routing Rules"
description: "Policy rules deciding which model handles which request"
tags: ["routing-rules", "routing", "models", "policy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Routing Rules

## Summary
Model routing rules are policies deciding which model handles which request, matching task type, difficulty, cost, and latency needs. They matter because model choices dominate both quality and cost, and a static pick wastes money or underdelivers. Routing turns model selection into an explicit, testable policy. Routing is a policy decision that should be versioned like any other code.

## Details
- **Definition** — routing rules map request characteristics to model assignments, evaluated at the gateway before inference.
- **Signal dimensions** — rules match on task type, expected difficulty, data sensitivity, latency budget, and cost tolerance.
- **Mechanism** — routing-models and deterministic rule engines implement the policy inside llm-gateway-and-routing.
- **Cost leverage** — routing is a primary cost-control lever: easy requests go to cheap models, hard ones escalate to expensive models.
- **Testing** — rules need evaluation against representative sets, because mis-routed requests degrade quality invisibly.
- **Worked example** — a support system routes simple FAQ queries to a small fast model and complex troubleshooting to a frontier model, with a classifier deciding the split.
- **Failure modes** — stale rules, misclassification at boundaries, and routing to models with different behaviors cause inconsistent quality.
- **Relation to fallbacks** — routing picks the default model; model-fallback-chains handle what happens when that model fails.
- **Practical relevance** — routing rules sit at the intersection of cost, quality, and reliability and are a standard feature of production gateways.
- **Versioning** — routing rules change behavior, so they need versioning and rollback like code.
- **Telemetry** — tracking per-route quality and cost shows whether the policy is delivering its intent.
- **Worked example** — a routing classifier sends short factual queries to a cheap model and defers complex reasoning to a stronger one.
- **Failure example** — a rule that routes all traffic to the cheapest model quietly drops quality across the board.

## Related
- [[wiki/ml-frameworks/routing-models|Routing Models]] — the routing mechanism
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — the failure path after routing
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — the execution layer
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — the cost logic behind rules
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — choosing models in the first place
