---
type: "concept"
title: "Agent Telemetry Schema"
description: "The field-level contract for structured agent telemetry events"
tags: ["telemetry", "schema", "observability", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agent Telemetry Schema

## Summary
An agent telemetry schema is the agreed structure for telemetry events: event types, fields, IDs, and timestamps. It matters because structured, consistent data is what makes dashboards, alerting, and replay possible. Schema drift breaks the whole observability stack.

## Details
- Core fields: event id, type, agent id, run id, timestamp, inputs hash, outcome.
- Versioned so consumers can migrate gradually.
- Extensible per event type (tool call, model turn, retry, handoff).
- Open questions: schema stability vs. evolving agent features.

## Related
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — the practice this schema serves
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the log events conforming to it
- [[wiki/llm-agents/traceability|Traceability]] — IDs that enable tracing
- [[wiki/agent-systems/crisis-monitoring|Crisis Monitoring]] — the signals it structures
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — metrics built on the schema
