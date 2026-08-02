---
type: "concept"
title: "Routing Models"
description: "Systems that dispatch each request to the most suitable model or adapter"
tags: ["routing-models", "routing", "models", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Routing Models

## Summary
Systems that dispatch each request to the most suitable model or adapter

## Details
- Routers use classifiers, embeddings, or cost heuristics.
- Routing cuts cost by matching difficulty to model tier.
- Quality risk: misrouting hard tasks to weak models.
- Operationalized in model-routing-rules.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — policy layer
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — failure path
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — cheap tier
- [[wiki/ai-ml/semantic-operator-similarity|Semantic Operator Similarity]] — semantic routing
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — economic driver
