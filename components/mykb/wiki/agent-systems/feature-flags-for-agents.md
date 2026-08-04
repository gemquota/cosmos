---
type: "concept"
title: "Feature Flags for Agents"
description: "Runtime toggles controlling agent behaviors and model choices without redeploys"
tags: ["feature-flags", "flags", "release", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Feature Flags for Agents

## Summary
Feature flags are runtime toggles that control agent behaviors and model choices without redeploying, enabling progressive rollout and instant rollback. They matter because agent changes are risky and hard to predict, and flags put a kill switch on every behavior change. Flagged deployments make releases reversible. Flags are a governance tool, not just a release convenience.

## Details
- **Definition** — a feature flag is a configuration value read at runtime that switches prompts, tools, models, or pipeline stages on and off.
- **Use cases** — flags enable progressive rollout, instant rollback, emergency degradation, and per-tenant or per-user variation.
- **Coverage** — flags can control prompts, tool allowlists, model routing, retry policies, and entire pipeline stages.
- **Logging** — flag state must be logged with each run so behavior can be reconstructed and debugging is not confused by unrecorded toggles.
- **Integration** — flags support canary-deployments-agents and a-b-testing-agents by providing the control mechanism for variants.
- **Worked example** — a team ships a new summarization prompt behind a flag, enables it for ten percent of users, and disables it within minutes when a quality regression appears.
- **Failure modes** — flag drift, stale flags, and flags that change mid-request create inconsistent behavior and hard-to-debug systems.
- **Practical relevance** — feature flags are the operational layer of agent-versioning and prompt-versioning, making deployment decisions cheap to reverse.
- **Ownership** — every flag should have an owner and an expiry so stale toggles do not accumulate.
- **Consistency** — flags should be read once per request so behavior does not change mid-run.
- **Worked example** — an emergency flag disables a misbehaving tool across the fleet in under a minute.
- **Failure example** — a flag left on for a year silently locks everyone into an old behavior.

## Related
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — the rollout method flags enable
- [[wiki/agent-systems/a-b-testing-agents|A/B Testing Agents]] — experiments built on flags
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — version management context
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — versioning the prompts flags toggle
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — emergency toggles
