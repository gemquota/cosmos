---
type: "concept"
title: "Profilers"
description: "Tools that measure where a program spends time, memory, or I/O to guide optimization"
tags: ["profiling", "performance", "debugging", "tools"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Profilers

## Summary
A profiler observes a running program and reports where resources go: CPU hotspots, allocation graphs, syscall waits. Optimization without profiling is guesswork; profiling makes the guess an observation.

## Details
- Sampling profilers trade precision for low overhead; instrumenting profilers give exact counts.
- Profile in production-like conditions — benchmarks on toy inputs mislead.
- RSIS3 relevance: agent loop latency can be profiled per phase (perception, planning, action).

## Related
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — benchmarks set the stage profilers analyze
- [[wiki/dev-tools/debuggers|Debuggers]] — profilers find where; debuggers find why
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — browser profilers drive web tuning
- [[wiki/concepts/telemetry|Workspace Telemetry]] — system-wide profiling data for agents
- [[wiki/devops-infra/observability|Observability]] — profiling feeds observability pipelines
