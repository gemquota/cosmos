---
type: "concept"
title: "Accelerator Observability"
description: "Metrics for GPU utilization, memory, and temperature in fleets"
tags: ["gpu", "observability", "metrics", "hpc"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Accelerator Observability

## Summary
Accelerator observability is the practice of collecting and acting on metrics for GPU utilization, memory, temperature, power, and interconnect health across fleets. It matters because accelerators are expensive, failure-prone, and opaque: a silent memory error, a hot HBM module, or a training job bottlenecked on PCIe transfers is invisible without the right telemetry, and each one wastes hours of expensive compute.

## Details
- The core metric set: utilization (SM/streaming-processor occupancy, achieved vs peak FLOPS), memory (used/total, bandwidth utilization, allocation stalls), temperature (per-module junction temps, throttling events), power draw and power capping, and interconnect activity (PCIe, NVLink/NVSwitch, or InfiniBand/RoCE traffic). The key insight is that each metric answers a different question: utilization says whether the accelerator is busy, memory bandwidth says whether it is productive, temperature says whether it is safe, and interconnect says whether the bottleneck is inside the node or between nodes.
- The failure modes are the reason the metrics exist. Thermal throttling silently cuts throughput — a GPU hitting its temperature ceiling drops clocks and the job slows with no error raised, so the only symptom is a utilization that looks high but a training throughput that fell. Memory errors (ECC corrections, then uncorrectable errors) corrupt training runs quietly; observability catches the ECC counter climbing before the run is lost. Memory leaks or allocation fragmentation produce OOM crashes after hours of useful work. And a job that is "utilizing the GPU" at 100% while waiting on data movement is burning money on bandwidth stalls — which utilization alone cannot distinguish from productive work.
- Operational tradeoffs: collecting per-second metrics on thousands of accelerators costs storage and tooling; the discipline is to keep a high-resolution window (recent hours) and downsample for history, and to derive alert thresholds from the physics (junction temp ceilings, ECC error rates) rather than from arbitrary percentages. Fleet-level aggregation hides node-level problems, so the dashboard must support per-accelerator drill-down.
- For RSIS3/mykb: accelerator observability is the GPU analog of the telemetry coverage the RSIS3 practices mandate — you cannot improve what you do not measure, and the same loop-closure logic (collect, detect, act, verify) applies to hardware fleets.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-observability|Storage Observability]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
