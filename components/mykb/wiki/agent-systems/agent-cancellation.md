---
type: "concept"
title: "Agent Cancellation"
description: "Cleanly stopping a running agent when it is no longer needed or has gone off track"
tags: ["cancellation", "agents", "control", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Agent Cancellation

## Summary
Cleanly stopping a running agent when it is no longer needed or has gone off track

## Details
- Cancellation must halt tools, free resources, and record state.
- Cooperative cancellation beats hard kills for stateful agents.
- Checkpointing enables resume or abort decisions.
- Governed by task-scheduling-agents.

## Related
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — time-based stop
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — resume support
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — clean re-runs
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — who cancels
