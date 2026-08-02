---
type: "concept"
title: "Traces and Spans"
description: "Telemetry primitives that record execution trees and per-operation timing for LLM and agent systems"
tags: ["traces-spans", "observability", "telemetry", "llmops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Traces and Spans

## Summary
Telemetry primitives that record execution trees and per-operation timing for LLM and agent systems

## Details
- A trace is a tree of spans covering one request lifecycle.
- Spans capture model calls, retrieval, tools, and sub-agents.
- Trace analysis finds latency, cost, and correctness issues.
- Standardized by OpenTelemetry-inspired conventions.

## Related
- [[wiki/testing/runtime-observability-agent|Runtime Observability for Agents]] — consumer of traces
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — trace in pipelines
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — metrics companion
- [[wiki/agent-systems/agent-run-inspectors|Agent Run Inspectors]] — trace inspection
- [[wiki/testing/latency-budgets-throughput-calibration|Latency Budgets and Throughput Calibration]] — trace-based tuning
