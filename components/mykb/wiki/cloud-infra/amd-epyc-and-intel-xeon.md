---
type: "concept"
title: "AMD EPYC & Intel Xeon"
description: "Serving as the x86 workhorses of modern cloud instances"
tags: ["epyc", "xeon", "cpu", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# AMD EPYC & Intel Xeon

## Summary

Cloud instance families are built on AMD EPYC and Intel Xeon generations, each with different clock speeds, core counts, memory bandwidth, and per-core licensing implications. The choice shows up in price-performance and software licensing, not just benchmarks.

## Details
- Mechanism: providers expose CPU-generation-aware families (AWS M6a AMD vs M6i Intel, GCP AMD Milan vs Ice Lake, Azure D-family variants); AMD EPYC typically offers more cores per socket and often lower price per core, while Xeon historically carries better AVX-512/AMX support and single-thread clock for some generations.
- Concrete example: a compute-heavy batch job that scales with cores runs cheaper on AMD EPYC families at equal vCPU count; a workload relying on AVX-512 (some ML inference, scientific codes) may run faster per-core on matching Intel families, changing the cost equation despite higher list price.
- Failure modes: benchmarking one generation and assuming the vendor line holds; licensing by core/socket (Oracle, SQL Server, Windows Server) making AMD's higher core counts costlier in software than in compute; ignoring memory bandwidth differences for data-heavy jobs; and spot/commit pricing varying by CPU family.
- Operational tradeoffs: standardize on one family per workload tier to keep golden images and capacity simple, but benchmark your actual workload — CPU generation differences (2-4x in some generations) dwarf micro-architectural marketing. Use family flexibility in savings plans only where licensing permits, and keep a per-tier golden image per family so capacity swaps are mechanical.
- RSIS3/mykb relevance: benchmark results per CPU family are stored in the wiki so the loop's experiment planner picks the cheapest adequate family instead of the default.
- Procurement note: reserved/commit pricing differs per CPU family; a savings plan that spans families preserves flexibility only if licensing allows running anywhere.
- Measurement: publish a per-workload benchmark matrix (cores, memory bandwidth, price) in the wiki and re-run it after CPU generation launches, since two generations can change the recommendation. Record the compiler or runtime version in every row — a toolchain update can flip the winner.
