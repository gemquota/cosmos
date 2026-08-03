---
type: "concept"
title: "Crisis Monitoring"
description: "Detecting degradation or dangerous behavior and triggering recovery"
tags: ["monitoring", "crisis", "safety", "telemetry", "rsis3"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1606.06565"]
---

# Crisis Monitoring

## Summary
Crisis monitoring watches an agent's runtime signals for conditions that mean something is wrong: failure cascades, budget blowouts, constraint violations, or behavior outside policy. It matters because detection speed determines whether an incident is a log line or a catastrophe. RSIS3 runs a crisis monitor inside its pulse engine that can interrupt normal flow and trigger recovery.

## Details
- **Signals**: error rates, retry storms, latency anomalies, constraint violations, unexpected state transitions.
- **Thresholds and escalation**: soft warnings first, then automatic actions like pausing or rollback.
- **Heartbeats** prove the loop is alive; a missed heartbeat triggers restart or alert.
- Recovery integration: the monitor hands off to rollback-and-recovery rather than letting the agent thrash.
- RSIS3 surfaces crisis state on the dashboard so humans can see the system's own assessment.
- Worked example: three consecutive test failures on a mutation trip the monitor, which reverts the change before it ships.

## Related

- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — the signals the monitor reads
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the raw material for anomaly detection
- [[wiki/llm-agents/traceability|Traceability]] — attributing crises to specific actions
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — the recovery path crises trigger
- [[wiki/ops/gap-report|Gap Analysis Report]] — anomalies feed gap analysis
- [[wiki/questions/open-questions|Open Questions]] — open questions on crisis detection