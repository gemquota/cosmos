---
type: "concept"
title: "Feature Flags for Agents"
description: "Runtime toggles controlling agent behaviors and model choices without redeploys"
tags: ["feature-flags", "flags", "release", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Feature Flags for Agents

## Summary
Runtime toggles controlling agent behaviors and model choices without redeploys

## Details
- Enable progressive rollout and instant rollback.
- Flags cover prompts, tools, models, and pipeline stages.
- Flag state must be logged for debuggability.
- Support canary and a-b testing.

## Related
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — rollout method
- [[wiki/agent-systems/a-b-testing-agents|A/B Testing Agents]] — experiment method
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — version context
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — prompt flags
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — emergency toggles
