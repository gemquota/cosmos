---
type: "concept"
title: "Token Usage Tracking"
description: "Metering token consumption per user, request, and model for cost and quota management"
tags: ["token-tracking", "tokens", "cost", "metering"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Token Usage Tracking

## Summary
Metering token consumption per user, request, and model for cost and quota management

## Details
- Track input, output, and cache tokens across calls.
- Usage feeds budgets, billing, and anomaly detection.
- Dashboards expose cost per feature and user.
- Core to token-accounting-and-cost.

## Related
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — accounting layer
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — quota enforcement
- [[wiki/llm-agents/api-key-management-llm|API Key Management for LLMs]] — per-key metering
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — cost analysis
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — operational metrics
