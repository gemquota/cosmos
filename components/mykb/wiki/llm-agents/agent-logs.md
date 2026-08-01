---
type: "concept"
title: "Agent Logs"
description: "Chronological records of agent actions, decisions, and outcomes"
tags: ["agent-logs", "logging", "observability", "traceability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agent Logs

## Summary
Agent logs are the timestamped record of everything the agent did: thoughts, tool calls, observations, retries, and results. They matter because they are the raw material for debugging, audit, evaluation, and replay. Good logs are structured, complete, and safe.

## Details
- Include request/response hashes, tool inputs, outcomes, and timings.
- Privacy: prompts and data may need redaction.
- Logs feed telemetry metrics and traceability.
- Open questions: retention policy and searchability at scale.

## Related
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — logs as the telemetry substrate
- [[wiki/llm-agents/traceability|Traceability]] — what logs enable
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the field contract
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replaying logged runs
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — the retry events logged
