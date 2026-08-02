---
type: "concept"
title: "RAID Levels"
description: "Striping, mirroring, and parity combinations for storage"
tags: ["raid", "storage", "parity", "redundancy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/admin-guide/md.html",
  "https://en.wikipedia.org/wiki/RAID",
]
---

# RAID Levels

## Summary
RAID combines disks into arrays that survive disk failure, trading capacity and performance for redundancy. Levels range from pure striping to mirroring to parity schemes. Modern systems layer RAID concepts into filesystems and cloud storage.

## Details
- RAID 0 stripes data with no redundancy; RAID 1 mirrors; RAID 5/6 use distributed parity to survive one or two disk failures.
- The kernel's md documentation covers software RAID administration on Linux.
- RAID 10 (mirrored stripes) is the common high-performance choice for databases.
- Rebuild time and failure risk grow with disk size, pushing many systems to erasure coding instead.
- Hardware RAID offloads computation but adds controller dependence; software RAID is simpler to operate.
- In mykb, RAID levels connect to mdadm, hardware vs software RAID, and erasure coding articles.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/infrastructure/hardware-raid-vs-software-raid|Hardware RAID vs Software RAID]]
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/devops-infra/isolation-levels|Isolation Levels]]
- [[wiki/devops-infra/severity-levels|Severity Levels]]
