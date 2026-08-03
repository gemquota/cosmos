---
type: "concept"
title: "Compute Shapes & SKUs"
description: "The family of instance sizes and their ratio tradeoffs"
tags: ["instance-types", "sku", "compute", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Compute Shapes & SKUs

## Summary

Compute shapes/SKUs are the instance catalog — CPU generation, vCPU count, memory, network, and storage attached per size. Choosing a shape is a constrained optimization over price, performance ceilings, and licensing; the catalog changes, so sizing must be revisited.

## Details
- Mechanism: providers publish families (general purpose, compute, memory, storage, GPU, accelerated) each with sizes that scale vCPU/memory in ratios; each size has network bandwidth and EBS/PD performance ceilings. SKU selection maps workload profile (CPU-bound, memory-bound, I/O-bound, GPU) to the family, and sizing maps observed utilization to the size.
- Concrete example: an in-memory cache selects a memory-optimized r-family shape where GB per vCPU is high; a batch renderer selects compute-optimized with high per-core clock; a database selects storage-optimized for disk throughput; and a bursty web tier standardizes on one general-purpose size with autoscaling rather than hand-tuning each box.
- Failure modes: sizing by checklist instead of utilization data (idle 4-vCPU boxes everywhere); ignoring per-size network/IOPS ceilings so the workload is network-bound before CPU is utilized; family staleness (older generations cheaper per dollar but slower); and SKU lock-in where the shape's licensing (per-core) makes a 64-core box costlier than two 32-cores.
- Operational tradeoffs: standardizing on a few shapes simplifies inventory, golden images, and capacity planning, at some cost in fit; right-size from percentile telemetry, re-check quarterly, and keep the family matrix in one place so upgrades are systematic.
- RSIS3/mykb relevance: the wiki keeps a per-workload shape matrix with utilization snapshots; the loop's capacity reviews propose shape changes from that data rather than folklore.
- Right-sizing loop: re-measure CPU/memory utilization quarterly and right-size with data; the 4-vCPU box chosen at launch is rarely still the right shape a year later.
- Family matrix: keep a one-page matrix of families vs workload profiles; the matrix turns instance selection from tribal knowledge into a lookup.

## Related
- [[wiki/cloud-infra/compute-autoscaling|Compute Autoscaling]]
- [[wiki/infrastructure/gpu-compute-infrastructure|GPU Compute Infrastructure]]
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]]
