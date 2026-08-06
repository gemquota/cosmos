---
type: "concept"
title: "Telemetry for Agents"
description: "Structured logs, metrics, and traces that make agent behavior observable"
tags: ["telemetry", "observability", "logging", "metrics", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://opentelemetry.io/docs/"]
---

# Telemetry for Agents

## Summary
Agent telemetry is the practice of emitting structured, queryable data about what an agent did: tool calls, model turns, retries, timings, and outcomes. It matters because agents are complex and stochastic; without telemetry, failures are opaque and improvements are guesses. OpenTelemetry provides the standard vocabulary (traces, metrics, logs) that agent systems can adopt.

## Details
- **Three pillars**: traces (one run's full path), metrics (aggregate counters like pulse success rate), logs (individual events).
- **Event granularity**: each tool call and model turn gets an id, timestamp, inputs hash, and outcome.
- **The dashboard is the consumer**: RSIS3 reads telemetry to render pulses, layers, and success rates.
- Telemetry enables replay: with the inputs logged, a bad run can be replayed deterministically.
- Privacy and cost require sampling and redaction, especially for prompt content.
- Worked example: a spike in retry-rate is traced to a single tool whose schema changed — found in minutes, not days.

- **Correlation** — a trace id threaded through tool calls, model turns, and sub-agent spawns links the whole run; without correlation, logs are uninterpretable fragments.
- **Alerting** — thresholds on retry rates, failure rates, and latency turn telemetry into operational signals rather than post-mortem records.
- **Privacy and cost** — sampling and redaction keep telemetry affordable and compliant; logging full prompts at full volume is usually neither.
- **Retention** — define what is kept and for how long; telemetry is the evidentiary base for audits and incident review, so retention policy is a governance decision.

- **Incident response** — with good telemetry, an incident becomes a query (find the run, replay the trace, inspect the failing step); without it, an incident becomes an argument about what happened.

## Related

- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the field-level contract for telemetry
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the log pillar of telemetry
- [[wiki/llm-agents/traceability|Traceability]] — what telemetry enables
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — metrics telemetry feeds into
- [[wiki/ops/gap-report|Gap Analysis Report]] — telemetry-driven gap analysis
