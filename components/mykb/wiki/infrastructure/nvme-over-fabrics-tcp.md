---
type: "concept"
title: "NVMe over Fabrics (TCP)"
description: "NVMe commands carried over TCP for remote block storage"
tags: ["nvme-of", "tcp", "storage", "fabrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NVMe over Fabrics (TCP)

## Summary
NVMe over Fabrics (NVMe-oF) carries NVMe commands over a network fabric instead of the local PCIe bus; the TCP transport variant runs those commands over ordinary TCP/IP networks. The significance: it extends NVMe's low-overhead command model to remote storage — so a host can use a remote NVMe drive (or array) as if it were local, over the datacenter's standard Ethernet, without special fabrics like Fibre Channel or InfiniBand.

## Details
- The protocol structure: NVMe-oF splits the NVMe command set from the transport. The command/queue model stays (admin and I/O queues, submission/completion, 64-byte commands), and a transport binding (the "fabrics" layer) carries those commands over a chosen medium — RDMA (InfiniBand or RoCE), FC (Fibre Channel), or TCP. The TCP transport defines how NVMe queue pairs map onto TCP connections: each NVMe queue pair maps to a TCP connection (with optional connection pooling), commands and data are encapsulated in capsules, and the target processes them against its namespaces. Because it is TCP, it works on any existing IP network with standard switches and NICs — no special hardware — which is the adoption story.
- The performance reality: TCP NVMe-oF delivers remote block storage with CPU cost higher than RDMA (the kernel TCP stack processes the traffic; the NIC offloads checksums and segmentation but not the protocol), so the latency/throughput lands between local NVMe and iSCSI — typically closer to local than iSCSI was, and with the huge advantage of running everywhere. The operational knob is tuning: large MTU, proper queue depths, NIC offloads enabled, and CPU/NUMA placement for the target and initiator — an untuned TCP NVMe-oF setup underperforms iSCSI; a tuned one beats it.
- The use cases: remote boot and shared storage for stateless hosts, disaggregated storage (the NVMe drives live in storage servers; compute servers attach over fabric), and the Kubernetes persistent-volume path (NVMe-oF as a CSI backend). The tradeoff versus local NVMe: fabric latency (tens of microseconds versus single-digit) and the network as a dependency — but the gain is pooling (storage utilization, easier failover, no wasted local capacity).
- The failure modes: network congestion (TCP NVMe-oF is sensitive to fabric saturation — the storage traffic competes with everything else; priority queuing for storage traffic is the fix), path loss (mitigated by multipath), and the silent performance cliff: a fabric problem that does not fail the connection but degrades it, showing up as mysterious latency.
- For mykb: the node anchors the remote-block-storage branch — it connects the TCP stack, the RDMA alternatives, and the multipath reliability layer.

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/cloud-infra/udp-vs-tcp|UDP vs TCP]]
- [[wiki/infrastructure/roce-and-rdma-over-tcp|RoCE & RDMA over TCP]]
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
