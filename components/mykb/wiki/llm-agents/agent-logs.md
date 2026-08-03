---
type: "concept"
title: "Agent Logs"
description: "Chronological records of agent actions, decisions, and outcomes"
tags: ["agent-logs", "logging", "observability", "traceability"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Agent Logs

## Summary

Agent logs capture what an agent did and why — prompts, tool calls, decisions, and outcomes — in a replayable, auditable form. They are the difference between an agent that can be debugged and one that can only be trusted on vibes.

## Details
- Mechanism: structured logging records each step: request id, timestamp, model/messages sent, tool calls with inputs and outputs, token counts, latency, and the decision that led to each action; logs must be correlated (trace ids), stored durably, and queryable; replayability requires logging enough state to reconstruct the loop (or storing deterministic inputs) without logging secrets.
- Concrete example: a RAG agent logs the query, the retrieved chunks (with ids and scores), the assembled context, and the final answer — a bad answer is diagnosable by checking which chunks were retrieved; a tool-calling agent logs each tool invocation and result, so a wrong side effect traces to the call that caused it. The failure pattern: logging only final outputs, leaving the interesting failures opaque.
- Failure modes: logging prompts verbatim when they contain PII/secrets; unbounded log growth from tool outputs and token payloads (truncate and summarize); correlation breaks across retries and parallel steps; and logs that lie — recording intent but not the actual execution path (log the real calls).
- Operational tradeoffs: thorough logging costs storage and careful redaction; it pays in debugging, audit, and safety analysis. The standard is trace-id correlation, structured JSON, redaction by default, and retention aligned with audit needs.
- RSIS3/mykb relevance: the wiki's loop sessions would log every pass as structured events, so post-run analysis and the synthesis pipeline work from the actual trace, not memory.

## Related
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — logs as the telemetry substrate
- [[wiki/llm-agents/traceability|Traceability]] — what logs enable
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the field contract
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replaying logged runs
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — the retry events logged
