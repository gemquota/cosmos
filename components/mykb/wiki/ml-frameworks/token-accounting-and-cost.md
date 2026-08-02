---
type: "concept"
title: "Token Accounting and Cost"
description: "Measuring token consumption and spend per request, user, and model"
tags: ["tokens", "cost", "accounting", "metering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/rate-limits", "https://github.com/openai/tiktoken"]
---

# Token Accounting and Cost

## Summary
Token accounting meters input, output, and cached tokens across every API call. It matters because LLM spend is per-token and grows fast. Accurate accounting drives budgets, routing decisions, and anomaly detection.

## Details
- **Metering** — count prompt tokens, completion tokens, and cache hits per call; attribute to user and feature.
- **Cost model** — price per token differs by model and tier; caching discounts matter.
- **Worked example** — a dashboard shows daily spend by model and user, flagging a key whose usage spiked 10x.
- **Controls** — budgets and quotas enforce limits surfaced by token-usage-tracking.
- **mykb relevance** — a personal KB must know its knowledge-loop cost per synthesis.
- **Worked example** — a dashboard shows daily spend by model and user, flagging a key whose usage spiked 10x.
- **Metering** — count prompt tokens, completion tokens, and cache hits per call; attribute to user and feature.
- **Controls** — budgets and quotas enforce the accounting, turning raw meter data into spending discipline.

## Related
- [[wiki/testing/token-usage-tracking|Token Usage Tracking]] — tracking layer
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — enforcement
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — trade-off analysis
- [[wiki/llm-agents/semantic-caching|Semantic Caching]] — cost reduction
- [[wiki/llm-agents/api-key-management-llm|API Key Management for LLMs]] — per-key accounting
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — cost-aware routing
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — the API surface it uses
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
