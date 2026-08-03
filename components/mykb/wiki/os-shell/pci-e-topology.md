---
type: "concept"
title: "PCIe Topology"
description: "The bus hierarchy linking CPUs, memory, and devices"
tags: ["pcie", "topology", "hardware", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# PCIe Topology

## Summary
PCIe (Peripheral Component Interconnect Express) is the serial bus hierarchy that links CPUs, memory, and virtually every high-speed device — GPUs, NVMe drives, network cards, and USB controllers. Its topology — root complexes, switches, bridges, and endpoints, connected by lanes of varying width and generation — determines device bandwidth, latency, and which NUMA node a device is "closest" to.

## Details
- Mechanism: PCIe is a point-to-point packet network of links, each composed of lanes (1, 2, 4, 8, or 16 per link, with each lane carrying one bit per direction per cycle). Devices attach to a root complex (in the CPU) directly or through switches that fan out to multiple devices; each device is addressed by bus:device.function, and Linux exposes the tree via `lspci -tv` and sysfs (`/sys/bus/pci/devices/`). Bandwidth is a function of generation and lanes: PCIe 3.0 x16 delivers ~16 GB/s, PCIe 4.0 x16 ~32 GB/s, PCIe 5.0 x16 ~64 GB/s. Devices negotiate the highest common link speed/width; a card rated 4.0 x16 in a 3.0 x8 slot runs at 3.0 x8 (~8 GB/s) — a common silent performance cap. Modern CPUs attach devices via a hierarchy of PCIe root ports, with peer-to-peer traffic (GPU to GPU, GPU to NVMe) able to bypass the CPU when the platform supports it.
- Concrete examples: `lspci -v` shows a GPU on `01:00.0` behind root port `00:01.1` with a link width of x16; an NVMe drive behind a chipset (PCH) shares the DMI link with other chipset devices, so two fast drives on chipset ports contend; a dual-GPU workstation places each GPU on a different root port for better peer-to-peer and NUMA locality; `nvidia-smi topo -m` shows the P2P connectivity matrix; servers check `lspci -tv` before installing a 4th GPU because the last slots share bandwidth.
- Failure modes: the classic failures are bandwidth contention (multiple devices behind one switch sharing link capacity — video capture + GPU on the same chipset link starves both), AER (Advanced Error Reporting) storms from a flaky card flooding the logs with corrected/uncorrectable errors, and resizable BAR/`ACS` issues that break SR-IOV passthrough in VMs. Physical causes dominate too: an x16 card in an x8 slot, a riser with insufficient lanes, and power/thermal limits under sustained load.
- Operational tradeoffs: topology knowledge buys performance: placing high-bandwidth devices on direct root-port links, spreading devices across root ports for parallel traffic, and matching generation/width expectations. The tradeoffs are motherboard cost (more root ports/switches) and the complexity of verifying negotiated speeds (`lspci -vv`, `lspci -nnk`) versus rated speeds. The practice rules: check `lspci -tv` and negotiated link stats before performance troubleshooting, keep peer-to-peer workloads (GPU training, NVMe caching) on the same hierarchy, and treat shared-chipset devices as contended by design. RSIS3/mykb relevance: the daemon's storage and GPU-adjacent workloads benefit from topology awareness — placing hot data and compute on the same bus hierarchy mirrors the locality discipline RSIS3 applies to memory and cache.

## Related
- [[wiki/os-shell/numa-and-cpu-topology|NUMA & CPU Topology]]
- [[wiki/devops-infra/topology-spread-constraints|Topology Spread Constraints]]
- [[wiki/infrastructure/network-topology-design|Network Topology Design]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
