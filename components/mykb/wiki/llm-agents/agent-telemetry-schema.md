---
type: "concept"
title: "Agent Telemetry Schema"
description: "The field-level contract for structured agent telemetry events"
tags: ["telemetry", "schema", "observability", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Agent Telemetry Schema

## Summary

An agent telemetry schema defines the structured fields every agent run emits — events, metrics, spans, and metadata — so runs across components compare, aggregate, and alert consistently. Without a schema, agent observability is a pile of incompatible JSON.

## Details
- Mechanism: a schema specifies event types (run_started, tool_called, model_response, error, run_completed), required fields (run_id, agent_id, timestamp, step), metrics (tokens, latency, cost), and spans for tracing; it is versioned so producers and dashboards evolve compatibly; enforcers validate events at emit time (JSON schema, protobuf) and fail fast on drift.
- Concrete example: every agent in the wiki's fleet emits the same run/step/tool events with trace ids, letting one dashboard compare a RAG agent against a reflexion agent on cost, latency, and success; a regression in tool-call success rate alerts on a shared metric rather than requiring per-agent custom code.
- Failure modes: schema drift across versions breaking dashboards (validate and version); fields that are optional in practice but required in policy (reliability leaks); PII sneaking into metadata fields; and telemetry that is rich but unreviewed — a schema is only as good as the alerting and dashboards built on it.
- Operational tradeoffs: a schema costs design time and validation plumbing; it pays in shared observability, comparative analysis, and cheaper onboarding of new agents. Start small (run/step/tool/error), version explicitly, and extend with additive fields.
- RSIS3/mykb relevance: the wiki's telemetry schema is the contract every loop agent emits against, feeding the rack's unified dashboards and improvement analysis.
- Cost fields: include token usage and estimated cost per event so dashboards can compare agent economics; cost is a first-class telemetry dimension for loops.
- Redaction policy: define which fields are redacted before storage (prompts, tool payloads) and where, so the schema never becomes a PII leak.

## Related
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — the practice this schema serves
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the log events conforming to it
- [[wiki/llm-agents/traceability|Traceability]] — IDs that enable tracing
- [[wiki/agent-systems/crisis-monitoring|Crisis Monitoring]] — the signals it structures
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — metrics built on the schema
