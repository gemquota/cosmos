---
type: "concept"
title: "NUMA & CPU Topology"
description: "Non-uniform memory access and topology-aware scheduling"
tags: ["numa", "cpu", "topology", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NUMA & CPU Topology

## Summary
NUMA (Non-Uniform Memory Access) describes multi-socket and many-core machines where memory access time depends on which CPU touches which memory: each node (socket) owns a portion of RAM, and remote-node access is slower than local access. The kernel's topology-aware scheduling — keeping threads and their memory on the same node — is often the difference between a server that scales and one that stalls on cross-socket traffic.

## Details
- Mechanism: the kernel represents topology as a hierarchy of domains: hyperthreads share a core, cores share a cache group (L2/L3), and groups of cores form NUMA nodes, each with local memory. The scheduler uses these domains to make wakeup and load-balancing decisions (prefer an idle core sharing a cache; avoid pulling a task across a node boundary), and the page allocator implements NUMA-aware policies (local allocation first, `numa_balancing` automatic migration). Memory policy is controllable via `numactl`: `--cpunodebind`, `--membind`, `--interleave`, and `--preferred` override the defaults, and `numastat`/`numactl --hardware` show node distances and distribution.
- Concrete examples: a two-socket database server where `numastat` shows most allocations on node 0 while threads run on node 1 — a classic "remote memory" trap; `numactl --interleave=all` for memory-bandwidth-bound HPC jobs that span nodes; `taskset` pinning a latency-critical worker to one core group; Kubernetes `topologySpreadConstraints` (the cluster-level echo of this) spreading pods across zones; a VM host pinning vCPUs per NUMA node so guest memory stays local (`-numa node` in QEMU).
- Failure modes: the classic failures are accidental remote access: the kernel allocates a thread on node 0 while its working set is on node 1 (fixable with `numactl` or auto-balancing), and the "first-touch" rule — memory is allocated to the node of the thread that first touches it, so initialization order silently determines locality. Overcommit and cgroup limits can force allocation to remote nodes; and pinning mistakes (a task bound to a CPU whose local memory is exhausted) can deadlock under memory pressure. Benchmarks on NUMA machines are notoriously misleading without `--interleave` or consistent pinning.
- Operational tradeoffs: topology-aware scheduling is mostly automatic and beneficial — the kernel's defaults (sched domains, local allocation, automatic NUMA balancing) are right for most workloads — and the operational lever is *verification*: check `numactl --hardware`, `lstopo`, and `numastat` before assuming locality, and pin or interleave only when measurements justify it. The tradeoff for aggressive manual pinning is reduced load-balancing flexibility and complexity under cgroup/migration. RSIS3/mykb relevance: parallel loop workers on a big host benefit from the same locality discipline — keep a worker's memory, cache, and node together — mirroring how the wiki's batch jobs should pin work to the data they process.

## Related
- [[wiki/os-shell/cpu-governors-and-frequency-scaling|CPU Governors & Frequency Scaling]] — related coverage in the same cluster
- [[wiki/devops-infra/topology-spread-constraints|Topology Spread Constraints]] — related coverage in the same cluster
- [[wiki/infrastructure/network-topology-design|Network Topology Design]] — related coverage in the same cluster
- [[wiki/os-shell/pci-e-topology|PCIe Topology]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
