---
type: "concept"
title: "Virtual Switches"
description: "Open vSwitch and kernel bridges forwarding between VMs and containers"
tags: ["ovs", "switch", "virtualization", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Virtual Switches

## Summary
Virtual switches are software switches that forward frames between virtual machines, containers, and physical NICs on the same host, replacing the wiring closet with configuration. The Linux bridge and Open vSwitch (OVS) are the two dominant implementations, and they sit underneath almost every cloud and container networking stack.

## Details
- Mechanism: a bridge or OVS creates a virtual L2 domain on the host; VM vNICs and container interfaces attach as ports, and the switch forwards frames between them and the physical uplink. OVS adds OpenFlow programmability, so a controller can install flows and the same switch logic can be virtualized for network virtualization.
- Linux bridge vs OVS: the kernel bridge is simple, fast for basic forwarding, and built into every kernel; OVS is feature-rich — OpenFlow, VXLAN/Geneve tunnels, QoS, bonding, and flow-based forwarding — but has more moving parts and a userspace datapath (mitigated by the kernel datapath module and DPDK).
- Concrete examples: KVM/libvirt default networking uses a bridge; OpenStack computes run OVS with tunnel endpoints to virtual networks; Kubernetes CNIs (Calico, Cilium, Flannel) build on bridge or OVS primitives under their eBPF/IPIP abstractions; and OVS-in-DPDK delivers millions of packets per second for NFV.
- Failure modes: misconfigured bridges that forward frames out the wrong uplink and loop; OVS flows that age out or mismatch after a controller restart; STP disabled on redundant bridge paths causing loops; and packet loss when the kernel datapath and userspace agent disagree on flow state.
- Tradeoffs: virtual switches make networking programmable and host-local, but they consume CPU (or need DPDK/SmartNIC offload), add a layer that must be debugged through `ovs-vsctl`/`ovs-ofctl` or `brctl`/`ip link`, and their failure semantics differ from hardware — a host problem is also a network problem.
- Operational practice: monitor the virtual switch as infrastructure (flow counts, drops, CPU), keep OVS and kernel versions aligned, prefer eBPF-native CNIs where features allow, and test what happens to traffic when the control agent restarts.
- RSIS3/mykb relevance: the virtual switch is the substrate for any distributed self-improvement system; this node keeps the bridge-vs-OVS tradeoff retrievable when reasoning about host-local networking.

## Related
- [[wiki/cloud-infra/virtual-private-clouds|Virtual Private Clouds]]
- [[wiki/cloud-infra/virtual-machines-hypervisors|Virtual Machines & Hypervisors]]
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]]
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]]
