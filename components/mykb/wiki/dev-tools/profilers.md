---
type: "concept"
title: "Profilers"
description: "Tools that measure where a program spends time, memory, or I/O to guide optimization"
tags: ["profiling", "performance", "debugging", "tools"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Profiling_(computer_programming)", "https://docs.python.org/3/library/profile.html"]
---

# Profilers

## Summary
A profiler observes a running program and reports where resources go: CPU hotspots, allocation graphs, syscall waits. Optimization without profiling is guesswork; profiling makes the guess an observation.

## Details
- Sampling profilers trade precision for low overhead; instrumenting profilers give exact counts.
- Profile in production-like conditions — benchmarks on toy inputs mislead.
- RSIS3 relevance: agent loop latency can be profiled per phase (perception, planning, action).
- Profilers measure where a program spends time or memory — CPU sampling, tracing, heap and allocation profiling — to direct optimization effort.
- The data they produce (flame graphs, call trees, allocation sites) shows the actual hot spots instead of guesses.
- Profiling is a loop: measure, hypothesize, change, re-measure; the profiler keeps the loop honest.
- Sampling profilers are cheap and safe for production; tracing profilers give exact detail at higher overhead.
- **Worked example / comparison** — Worked example — a wiki daemon is slow; a CPU profiler shows 60% of time in embedding recalculation, so the fix targets caching instead of random micro-optimization.
- For mykb, profilers are documented as the evidence tool for the wiki's own daemon and search performance work.

## Related
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/concepts/telemetry|Workspace Telemetry]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
