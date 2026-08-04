---
type: "concept"
title: "Agent Cancellation"
description: "Cleanly stopping a running agent when it is no longer needed or has gone off track"
tags: ["cancellation", "agents", "control", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Cancellation

## Summary
Agent cancellation cleanly stops a running agent when it is no longer needed or has gone off track, halting tools, freeing resources, and preserving state. It matters because agents act on the world, and stopping them is as important as starting them. A good cancellation path prevents wasted spend and unintended side effects. Cancellation is a lifecycle control as important as starting the run.

## Details
- **Definition** — cancellation is the controlled termination of an agent run, distinct from a timeout because it is initiated by an operator or policy rather than a limit.
- **Mechanism** — cancellation must halt in-flight tool calls, revoke delegated work, release resources, and record the final state.
- **Cooperative vs hard** — cooperative cancellation signals the agent to stop at a safe point; hard kills stop immediately but risk inconsistent state.
- **State handling** — checkpointing before cancellation lets a run resume later or abort cleanly, preserving work already completed.
- **Trigger sources** — humans, supervisors, policy engines, and task-scheduling-agents can all initiate cancellation when priorities change.
- **Worked example** — a user realizes a research task was submitted against the wrong project; cancelling the run stops the web calls and saves the partial findings.
- **Failure modes** — uncooperative tools ignore cancel signals, cancellation races with completion, and cascades cancel dependent work unexpectedly.
- **Idempotency** — clean re-runs depend on idempotent-agent-actions so partially completed work does not double-apply.
- **Practical relevance** — cancellation is a core lifecycle control alongside timeouts and supervision, making agent runs stoppable by design.
- **Propagation** — cancellation should cascade to child tasks, tools, and spawned processes.
- **Confirmation** — idempotent cancellation lets retried cancel signals be harmless.
- **Failure example** — cancelling a parent run while children keep executing leaves orphaned side effects.

## Related
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — the time-based stop mechanism
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — preserving state for resume or abort
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — clean re-runs after cancellation
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — who decides to cancel
