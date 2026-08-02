---
type: "concept"
title: "Idempotent Agent Actions"
description: "Designing agent operations so repeating them has the same effect as doing them once"
tags: ["agents", "idempotency", "reliability", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://github.com/langchain-ai/langgraph"]
---

# Idempotent Agent Actions

## Summary
An action is idempotent if executing it multiple times produces the same final state as executing it once. Idempotency makes retries, replays, and parallel execution safe. Without it, a retried agent action can double-charge, double-write, or corrupt state.

## Details
- **Mechanisms** — idempotency keys on API calls, upserts instead of inserts, and natural idempotency (e.g. setting a value) instead of stateful ones (e.g. incrementing).
- **Agent implications** — every tool the agent calls should declare whether it is idempotent; the planner should prefer idempotent tools for retryable steps.
- **Verification** — replaying a run must not change outcome; golden tests can assert idempotency of critical paths.
- **Worked example** — a file-write tool writes to a content-addressed path, so re-running the agent overwrites with identical bytes instead of duplicating.
- **Failure modes** — non-idempotent payment or email actions repeated by a retry loop are the classic incident.
- **mykb relevance** — RSIS3 checkpoint-rollback semantics assume actions can be replayed, which requires idempotent writes.

## Related
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — declaring idempotency in tool schemas
- [[wiki/llm-agents/api-key-management-llm|API Key Management for LLMs]] — credentials for retried calls
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — stopping unsafe retries
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — undo depends on repeatability
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — idempotency under partial failure
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — related concept in this cluster
