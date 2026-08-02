---
type: "concept"
title: "NFS & SMB (NAS)"
description: "Network filesystems for POSIX and Windows clients"
tags: ["nfs", "smb", "nas", "filesystem"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/filesystems/nfs/",
  "https://www.samba.org/samba/docs/",
]
---

# NFS & SMB (NAS)

## Summary
NFS and SMB are the network filesystem protocols behind NAS appliances and cloud file shares. NFS serves Unix clients with POSIX semantics; SMB serves Windows clients with rich locking and authentication. Both are essential for shared, multi-host storage.

## Details
- NFS exports directories over the network; clients mount them and see a normal filesystem, with versions NFSv3 and NFSv4 in use.
- SMB (Server Message Block) provides file sharing plus printer sharing, with ACLs and opportunistic locking for Windows workloads.
- The Linux kernel documentation covers NFS client and server implementation details.
- Performance tuning centers on cache, mount options, and network latency, since every operation crosses the wire.
- Security matters: NFS historically trusts client identities, so kerberized mounts and SMB signing are best practice.
- Cloud NAS services (EFS, Azure Files, Filestore) expose these protocols as managed offerings, tying NAS to the cloud cluster.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.

## Related
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/vxlan-overlays|VXLAN Overlays]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
