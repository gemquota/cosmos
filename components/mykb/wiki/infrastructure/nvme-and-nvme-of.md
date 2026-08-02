---
type: "concept"
title: "NVMe & NVMe-oF"
description: "The NVMe command set and its transport across fabrics"
tags: ["nvme", "nvme-of", "storage", "ssd"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://nvmexpress.org/",
  "https://en.wikipedia.org/wiki/NVM_Express",
]
---

# NVMe & NVMe-oF

## Summary
NVMe is the command set designed for flash storage, replacing SCSI's aging assumptions with parallel queues and low latency. NVMe-oF extends it across fabrics for shared, networked flash. It is the dominant storage interface in modern datacenters.

## Details
- NVMe exposes multiple hardware queues, each capable of many outstanding commands, unlocking flash parallelism.
- The NVM Express organization maintains the specifications for the base command set and transports.
- NVMe-oF runs the same command set over fabrics such as RDMA, Fibre Channel, and TCP.
- NVMe over TCP brings NVMe benefits to standard Ethernet without special hardware.
- Latency drops to tens of microseconds, changing application and database architecture assumptions.
- In mykb, NVMe connects to storage systems, PCIe topology, multipath, and kernel storage articles.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.
- Capacity and redundancy tradeoffs for this topic are covered in the datacenter redundancy and power articles.

## Related
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]
- [[wiki/infrastructure/nvme-multipath|NVMe Multipath]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
