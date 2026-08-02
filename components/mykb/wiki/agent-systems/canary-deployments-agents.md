---
type: "concept"
title: "Canary Deployments for Agents"
description: "Rolling out agent changes to a small traffic slice before full deployment"
tags: ["canary", "deployments", "agents", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Canary Deployments for Agents

## Summary
Rolling out agent changes to a small traffic slice before full deployment

## Details
- Compare canary and baseline on live metrics.
- Automated rollback on regression signals.
- Canaries need shadow-mode evaluation support.
- Part of agent-versioning practice.

## Related
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — parallel evaluation
- [[wiki/agent-systems/a-b-testing-agents|A/B Testing Agents]] — experimental comparison
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — release control
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — version management
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression gates
