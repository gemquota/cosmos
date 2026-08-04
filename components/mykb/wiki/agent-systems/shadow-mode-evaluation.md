---
type: "concept"
title: "Shadow Mode Evaluation"
description: "Running new models or agents in parallel to production without affecting users"
tags: ["shadow-mode", "evaluation", "testing", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Shadow Mode Evaluation

## Summary
Shadow mode evaluation runs a new model or agent in parallel with production, observing its behavior without affecting real users. It matters because the safest way to measure a change is to let it act in a mirror before it acts for real. Shadow traffic reveals quality, cost, and latency differences before any rollout decision. Shadow mode is the cheapest way to learn what a change does before committing users to it.

## Details
- **Definition** — in shadow mode, production requests are copied to the candidate system, its outputs are recorded and scored, but its actions are discarded.
- **Measurement** — shadow runs measure quality against ground truth, cost per request, latency, and failure rates without user-visible risk.
- **Comparison** — paired shadow and production outputs enable direct side-by-side evaluation, often with llm-as-judge or rubric scoring.
- **Safe exploration** — shadow mode is a pre-rollout stage that pairs with canary-deployments-agents, where a small real-traffic slice is exposed only after shadow results look good.
- **Worked example** — a support team shadows a new summarization model for a week, comparing its summaries against the incumbent on accuracy and latency before enabling it for live tickets.
- **Failure modes** — shadow traffic that diverges from real conditions, unmeasured action costs, and drifting evaluation criteria undermine the signal.
- **Cost** — shadow mode doubles inference spend during the evaluation window, so sampling and budgets are used to control cost.
- **Practical relevance** — shadow evaluation is a standard stage in llmops-ci-cd pipelines and a precondition for trustworthy agent changes.
- **Sampling** — shadowing a sample of traffic controls cost while still measuring representative behavior.
- **Criteria** — pre-registered pass criteria prevent post-hoc rationalization of weak results.
- **Failure example** — shadowing only easy requests hides how the candidate behaves on hard ones.

## Related
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — the rollout stage after shadow mode
- [[wiki/agent-systems/a-b-testing-agents|A/B Testing Agents]] — the experimental stage after shadow mode
- [[wiki/agent-systems/offline-agent-testing|Offline Agent Testing]] — the earlier, fully offline stage
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — the pipeline shadow mode fits into
- [[wiki/agent-systems/agent-observability|Agent Observability]] — the measurement layer
