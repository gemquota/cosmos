---
type: "concept"
title: "Flame Graphs"
description: "Stack-trace visualizations that show where CPU time is concentrated"
tags: ["profiling", "visualization", "performance", "flame-graphs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Flame Graphs

## Summary
Flame graphs stack sampled call stacks so the widest bars show the hottest code paths. The x-axis is time share, the y-axis is call depth — the shape of a bottleneck becomes visible at a glance, and the widest top bars show where CPU time actually goes.

## Details
- Mechanism: a profiler samples the stack at intervals (perf record, py-spy, Go pprof); samples are folded into stacks and rendered as stacked rectangles; the width of a bar is inclusive time (self plus descendants), so a wide leaf at the top means that function itself is hot; inverted flame graphs show the ancestry of a hot leaf, and delta flame graphs compare before and after a change.
- Concrete example: a wiki build that takes 40 seconds — a flame graph shows 25 seconds in markdown parsing and 10 in link resolution; a delta graph after switching parsers shows the parsing block shrink; a Go pprof flame graph of an API server shows serialization dominating, pointing the optimization at JSON encoding.
- Failure modes: sampling too sparsely or briefly, missing the hot path; profiling the wrong workload (a micro-benchmark instead of real traffic); optimized builds with inlined frames distorting the tree; interpreting inclusive width as self time, blaming the wrong function; graphs from a single sample window misleading for variable workloads.
- Tradeoffs: flame graphs turn performance hunches into measurements at the cost of profiling overhead and interpretation skill; the alternative — guessing — wastes effort on cold paths; the mature pattern is profile first, optimize the widest bars, and re-profile to verify.
- Operational notes: collect profiles under representative load, keep symbol info, and automate profile capture during incidents.
- RSIS3 relevance: flame-graph the wiki build and link-check steps to find slow passes — the same measure-before-optimize discipline RSIS3 applies to its pipelines.

## Related
- [[wiki/dev-tools/profilers|Profilers]]
- [[wiki/dev-tools/profiling-tools|Profiling Tools]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/dev-tools/benchmark-frameworks|Benchmark Frameworks]]
