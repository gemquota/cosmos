---
type: "concept"
title: "GPU Compute Infrastructure"
description: "GPUs as schedulable compute resources in clusters and clouds"
tags: ["gpu", "compute", "infrastructure", "hpc"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# GPU Compute Infrastructure
## Summary
GPU compute infrastructure is the practice of treating GPUs as schedulable, shared compute resources in clusters and clouds — provisioning them, partitioning them, scheduling workloads onto them, and managing their lifecycle the way CPUs have been managed for decades. The discipline exists because GPUs are scarce, expensive, and indivisible in ways that CPU compute is not, so naive provisioning wastes money and naive sharing causes interference.

## Details
- The provisioning stack: GPU nodes are assembled from the accelerator, its host CPU/memory, the interconnects (PCIe, NVLink, or the fabric for multi-node training), and the software layer (drivers, container runtime, orchestration plugin). The Kubernetes pattern is the standard: nodes are labeled with GPU type and count, the device plugin advertises GPUs as allocatable resources, and workloads request them (`nvidia.com/gpu: 1`) — the scheduler treats each GPU as a schedulable unit. The operational consequence: GPU allocation granularity matters. A workload that needs a quarter of a GPU either wastes the rest (if GPUs are allocated whole) or requires MIG/time-slicing (if partial allocation is supported), and each option trades utilization against isolation.
- The sharing mechanisms, in order of isolation quality: whole-GPU allocation (simplest, most isolated, most wasteful), MIG (Multi-Instance GPU — hardware partitioning of the GPU into isolated instances with dedicated memory and compute slices; the enterprise standard for A100/H100-class sharing), time-slicing (software sharing — flexible but no memory isolation and higher interference), and vGPU (virtualization with fair scheduling — the VDI path). The choice is a utilization-vs-interference decision, and the failure mode is the opposite of the CPU world: GPUs shared carelessly produce throughput collapse (one workload's memory or SM pressure starving another) with no clean error, just slower jobs.
- The fleet operations: GPU nodes fail differently from CPU nodes — thermal events, ECC errors, driver hangs (which require node reboots, killing running jobs), and HBM degradation. Observability (the accelerator-observability node) is load-bearing: utilization and memory per GPU, temperature, ECC counters, and power. The scheduling reality: training jobs want whole nodes and long durations, so the scheduler must support gang scheduling (all-or-nothing placement) and preemption policies, and the cost model must distinguish "GPU busy" from "GPU productive" — a GPU waiting on data is expensive idle.
- Failure modes: over-provisioning (GPUs idle, capital wasted), under-provisioning (jobs queue, researchers wait), and the shared-GPU tragedy (nobody's job is isolated, everyone's is slow).
- For mykb: the node anchors the GPU cluster — drivers/CUDA, observability, and container tooling all plug into this scheduling story.

## Related
- [[wiki/devops-infra/infrastructure-as-code-revisited|Infrastructure as Code]] — related coverage in the same cluster
- [[wiki/cloud-infra/compute-autoscaling|Compute Autoscaling]] — related coverage in the same cluster
- [[wiki/infrastructure/gpu-drivers-and-cuda|GPU Drivers & CUDA]] — related coverage in the same cluster
- [[wiki/devops-infra/infrastructure-drift-detection|Infrastructure Drift Detection]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
