---
type: "concept"
title: "Flame Graphs"
description: "Stack-trace visualizations that show where CPU time is concentrated"
tags: ["profiling", "visualization", "performance", "flame-graphs"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Flame Graphs

## Summary
Flame graphs stack sampled call stacks so the widest bars show the hottest code paths. The x-axis is time share, the y-axis is call depth, making the shape of a bottleneck visible at a glance.

## Details
- Built from stack samples: perf record, py-spy dump, or profiler exports, then folded and rendered.
- Inverted flame graphs show the full ancestry of a hot leaf; delta flame graphs compare before/after a change.
- Bars represent inclusive time, so a wide bar at the top means the leaf itself is hot, not just its callers.
- mykb relevance: flame-graph the wiki build and link-check steps to find slow passes.

## Related
- [[wiki/dev-tools/profilers|Profilers]]
- [[wiki/dev-tools/profiling-tools|Profiling Tools]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/dev-tools/benchmark-frameworks|Benchmark Frameworks]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
