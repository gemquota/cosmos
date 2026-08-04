---
type: "concept"
title: "A/B Testing Agents"
description: "Controlled experiments comparing agent versions on live traffic"
tags: ["ab-testing", "testing", "experiments", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# A/B Testing Agents

## Summary
A/B testing agents run controlled experiments that compare agent versions on live traffic, using consistent metrics and statistical rigor. They matter because agent changes can improve some behaviors while silently degrading others, and only a controlled experiment separates signal from noise. Results from A/B tests drive rollout and rollback decisions. Experiments replace opinions with evidence when they are designed before they start.

## Details
- **Definition** — an A/B test randomly assigns incoming traffic to a control variant and one or more treatment variants, then compares outcomes.
- **Assignment** — randomization must be stable per user or session to avoid interference, typically via hashed user IDs rather than per-request coin flips.
- **Metrics** — experiments need pre-registered metrics covering quality, cost, latency, and safety, because measuring everything after the fact invites bias.
- **Statistical power** — small effects need large samples; teams must estimate sample size before the experiment instead of stopping when results look good.
- **Worked example** — a support team tests a new summarization prompt on ten percent of tickets for two weeks, comparing resolution rate and user satisfaction.
- **Failure modes** — peeking at results, imbalanced groups, and novelty effects produce wrong conclusions; guardrails and fixed horizons prevent them.
- **Rollout connection** — A/B testing pairs with shadow-mode-evaluation before it and canary-deployments-agents after it in the release pipeline.
- **Practical relevance** — A/B testing turns deployment from a gamble into an evidence-based decision for agent systems.
- **Pre-registration** — metrics, sample sizes, and decision rules should be fixed before the experiment begins.
- **Guardrail metrics** — safety and latency metrics are tracked even when they are not the primary outcome.
- **Interference** — user-level randomization prevents one variant's behavior from contaminating the other's results.
- **Failure example** — stopping an experiment early because the trend looks good produces unreliable conclusions.

## Related
- [[wiki/agent-systems/shadow-mode-evaluation|Shadow Mode Evaluation]] — the pre-experiment stage
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — the rollout stage after experiments
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — the control mechanism behind variants
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — designing the metrics
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — offline regression baselines
