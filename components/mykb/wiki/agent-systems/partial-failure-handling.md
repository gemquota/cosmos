---
type: "concept"
title: "Partial Failure Handling"
description: "Graceful recovery when some components of a request fail"
tags: ["partial-failure", "reliability", "failure", "systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Partial Failure Handling

## Summary
Partial failure handling is the set of techniques for recovering gracefully when only some components of a request fail: one tool call times out, one sub-agent errors, one shard of a response is stale. The goal is to degrade predictably — deliver what can be delivered, retry what can be retried, and report the rest — instead of collapsing the whole operation.

## Details
- **Scope of failure** — in agent systems a single step rarely fails alone; the question is whether the failure is isolated (one tool) or cascading (downstream steps depend on the failed output).
- **Decomposition** — handling partial failure starts with structure: separate the request into independent units so one failure does not invalidate the rest.
- **Graceful degradation** — when a component fails, the system either substitutes (cached or approximate result), skips (marks the item incomplete), or escalates (routes to a human or a different strategy).
- **Retry boundaries** — partial failures use bounded retry with backoff for transient errors; permanent component failures should not be retried but should be reported precisely.
- **State consistency** — the danger of partial success is inconsistent state: some writes applied, others not; idempotent actions and checkpoints make the partial state safe to resume from.
- **Reporting** — a good partial-failure response tells the user what succeeded, what failed, and what was done about it; silent partial success is the worst outcome.
- **mykb relevance** — multi-file wiki operations degrade component-wise: per-file results are reported with per-file status rather than an all-or-nothing verdict.

- **Testing partial failure** — the handling logic should be exercised deliberately: fault-injection tests (kill one sub-agent, timeout one tool call) reveal whether the degradation path actually works before production needs it.

## Related
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — safe retries under partial failure
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — isolating repeated failures
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — the retry policy
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — reduced-quality continuation
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — reporting failures well
