---
type: "concept"
title: "Canary Deployments for Agents"
description: "Rolling out agent changes to a small traffic slice before full deployment"
tags: ["canary", "deployments", "agents", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Canary Deployments for Agents

## Summary
Canary deployments roll agent changes out to a small traffic slice before full deployment, comparing the canary against the baseline on live metrics. They matter because agent changes can pass offline tests and still fail in production, and a canary contains that risk to a small, measurable fraction. Automated rollback on regression signals makes the process safe. Canaries make releases reversible and measurable.

## Details
- **Definition** — a canary deployment routes a small percentage of live traffic to the new version while the rest stays on the baseline.
- **Metrics** — canary and baseline are compared on quality, latency, cost, and error rates using pre-defined thresholds for rollback.
- **Automation** — regression signals trigger automated rollback, removing the new version before most users are affected.
- **Progression** — canary traffic share grows in stages, such as one, five, and twenty percent, as confidence accumulates.
- **Relationship to other stages** — canaries follow shadow-mode-evaluation and A/B testing in the release pipeline and rely on feature-flags for instant control.
- **Worked example** — a support team deploys a new prompt to five percent of tickets, watches resolution rate for a day, then scales to fifty percent before full rollout.
- **Failure modes** — insufficient sample sizes, metrics that lag real impact, and canary traffic that differs from the general population all weaken the signal.
- **Practical relevance** — canaries are part of agent-versioning practice, making model and prompt changes reversible and measurable.
- **Duration** — canary windows must be long enough to observe delayed failures.
- **Segments** — canarying per tenant or per traffic type isolates risky populations.
- **Failure example** — a canary compared against itself after full rollout produces a misleading success signal.

## Related
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — the parallel evaluation stage before canaries
- [[wiki/agent-systems/a-b-testing-agents|A/B Testing Agents]] — controlled experiments in the same pipeline
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — the release control mechanism
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — managing agent versions across releases
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — offline regression gates before canary
