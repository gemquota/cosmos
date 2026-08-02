---
type: "concept"
title: "A/B Testing Agents"
description: "Controlled experiments comparing agent versions on live traffic"
tags: ["ab-testing", "testing", "experiments", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# A/B Testing Agents

## Summary
Controlled experiments comparing agent versions on live traffic

## Details
- Randomize traffic across variants with consistent metrics.
- Statistical power requires sufficient sample size.
- Results drive rollout and rollback decisions.
- Pairs with shadow-mode-evaluation.

## Related
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — pre-experiment stage
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — rollout stage
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — control mechanism
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — metric design
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression baseline
