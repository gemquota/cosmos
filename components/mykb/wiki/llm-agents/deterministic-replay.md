---
type: "concept"
title: "Deterministic Replay"
description: "Re-running an agent's exact steps to reproduce and debug behavior"
tags: ["deterministic-replay", "debugging", "logs", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Deterministic Replay

## Summary
Deterministic replay re-executes a logged agent run with identical inputs and seeds to reproduce behavior exactly. It matters because agents are stochastic, and only replay can turn 'it failed once' into a debuggable event. It requires complete, deterministic logs.

## Details
- Needs logged tool inputs, model responses, and random seeds.
- Enables bisecting where a run went wrong.
- Complements rollback: understand before retrying.
- Open questions: replay fidelity with non-deterministic tools.

## Related
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — replay before retry
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the replay source
- [[wiki/llm-agents/traceability|Traceability]] — the linking property
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — replay across versions
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — replaying retried steps
