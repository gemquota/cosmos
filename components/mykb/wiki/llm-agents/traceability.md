---
type: "concept"
title: "Traceability"
description: "The ability to link any outcome back to the actions that produced it"
tags: ["traceability", "audit", "accountability", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Traceability

## Summary
Traceability means every result can be traced to its inputs and steps: which prompt, tool call, and decision produced this outcome. It matters for accountability, debugging, and trust. It is the audit property built on agent logs and telemetry.

## Details
- Requires stable IDs linking outcome → trajectory → inputs.
- Enables 'why did this happen' investigations in minutes.
- Supports evaluation by attributing success and failure.
- Open questions: trace granularity vs. storage cost.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — evaluation needs attribution
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the raw material
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — traces make replay possible
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the trace structure
- [[wiki/agent-systems/crisis-monitoring|Crisis Monitoring]] — attributing incidents
