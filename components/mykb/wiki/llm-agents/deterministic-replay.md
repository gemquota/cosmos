---
type: "concept"
title: "Deterministic Replay"
description: "Re-running an agent's exact steps to reproduce and debug behavior"
tags: ["deterministic-replay", "debugging", "logs", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langfuse/langfuse", "https://github.com/openai/evals"]
---

# Deterministic Replay

## Summary
Deterministic replay re-executes a logged agent run with identical inputs and seeds to reproduce behavior exactly. It matters because agents are stochastic, and only replay can turn "it failed once" into a debuggable event. It requires complete, deterministic logs.

## Details
- **Requirements** — every input to every model call and tool must be logged, along with seeds, temperature, and timestamps.
- **Mechanisms** — fixed seeds, recorded model responses replayed from cache, and snapshotted tool results eliminate nondeterminism.
- **Uses** — reproducing failures, regression testing after agent changes, and auditing what actually happened.
- **Worked example** — a flaky agent test fails; replay with recorded responses shows the model chose the wrong tool at step 3, and the fix is a better tool description.
- **Limitations** — external side effects (emails, payments) cannot be replayed safely; those must be mocked or fenced.
- **mykb relevance** — deterministic replay is an existing mykb topic; RSIS3 checkpoints make its loops replayable.

## Related
- [[wiki/agent-systems/session-replay-agents|Session Replay for Agents]] — replaying sessions
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — the logs replay needs
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — replay-safe actions
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — replay against goldens
- [[wiki/agent-systems/agent-trace-visualization|Agent Trace Visualization]] — visualizing replayed runs
- [[wiki/testing/traces-spans|Traces and Spans]] — trace data for replay
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
