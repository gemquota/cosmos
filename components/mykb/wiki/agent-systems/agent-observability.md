---
type: "concept"
title: "Agent Observability"
description: "Instrumentation that exposes what an agent did, why, and at what cost"
tags: ["agents", "observability", "telemetry", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langfuse/langfuse", "https://github.com/open-telemetry/opentelemetry-python"]
---

# Agent Observability

## Summary
Agent observability captures traces of every decision, tool call, token, and state transition so behavior can be inspected, debugged, and audited. Agents are stochastic and long-running, so without observability failures are unreproducible. Observability is the foundation for evaluation, replay, and trust.

## Details
- **What to record** — inputs, outputs, tool calls with arguments and results, model IDs, latency, token counts, and confidence scores.
- **Formats** — structured logs, traces and spans, and run records that can be replayed deterministically.
- **Tools** — LangSmith, Langfuse, Helicone, and OpenTelemetry-based agents instrumentation provide dashboards and trace explorers.
- **Worked example** — a failed finance agent run: the trace shows it called the balance tool with stale credentials, and replay reproduces the exact call sequence.
- **Cost** — observability adds latency and storage; sampling and redaction balance fidelity with cost and privacy.
- **mykb relevance** — RSIS3 telemetry, checkpoint commits, and pulse evaluation logs are exactly this pattern applied to a self-modifying system.

## Related
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — structured records for review
- [[wiki/testing/traces-spans|Traces and Spans]] — the tracing model
- [[wiki/agent-systems/agent-trace-visualization|Agent Trace Visualization]] — making traces inspectable
- [[wiki/agent-systems/agent-run-inspectors|Agent Run Inspectors]] — inspecting individual runs
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — existing telemetry concepts in mykb
- [[wiki/testing/runtime-observability-agent|Runtime Observability for Agents]] — runtime monitoring of agents
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
