---
type: "concept"
title: "Loopback vs Linux Bridge"
description: "The lo interface versus kernel bridges and veth plumbing"
tags: ["loopback", "bridge", "linux", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Loopback vs Linux Bridge

## Summary
The loopback interface (lo) and the Linux bridge are two different answers to the question "how do packets move without a physical NIC": lo is the host's own loopback — packets addressed to the machine itself — while the Linux bridge is a virtual L2 switch that connects network devices (veth pairs, physical NICs, tap interfaces) inside the kernel. Understanding the difference is prerequisite for reading any container or VM networking setup.

## Details
- The loopback interface: lo is the kernel's virtual interface with address 127.0.0.1/8 (and ::1). A packet sent to a loopback address never leaves the host — the kernel routes it back through lo, so it traverses the full network stack (which is why "localhost is fast but not free": every packet still pays the protocol-stack cost, and it is a real bottleneck for local IPC-heavy workloads). Its properties: it is always up (until you break it — a removed or downed lo breaks the machine's own networking assumptions), it carries the machine's identity (services that must be local-only bind to 127.0.0.1), and it is exempt from many of the rules applied to real interfaces. The failure mode that matters operationally: misconfiguring which interface a service binds to — a service bound to lo is reachable only from the host, a service bound to 0.0.0.0 is reachable from everywhere.
- The Linux bridge: a kernel virtual switch that forwards Ethernet frames between its member ports (physical NICs, veth ends, tap devices). It behaves like a physical switch — MAC learning, forwarding table, STP for loop prevention — entirely in software. Its role in containerization: each container gets a veth pair — one end inside the container's network namespace, the other attached to the bridge — so the bridge is the virtual L2 segment that connects containers to each other and (through a member physical NIC or a router) to the outside. Docker's default bridge (docker0), Kubernetes' pod networking (via CNI plugins that build on bridges), and VM networking (tap devices on a bridge) all use this mechanism.
- The relationship: containers typically have both — a lo inside each network namespace (so the container can address itself) and the bridge (so containers can address each other). The mental model: lo is "this machine's own traffic", the bridge is "the virtual LAN the machine's virtual interfaces plug into". The kernel also offers the L3 alternatives — the macvlan/ipvlan modes (which attach virtual interfaces directly to a physical NIC, bypassing the bridge) and veth-only point-to-point links (for pair connections without a switch).
- Failure modes: bridge loops (without STP, a looped bridge melts the network — the classic misconfiguration), MAC address conflicts (duplicate MACs on the bridge confuse its forwarding table), and the debugging trap of assuming lo traffic appears in packet captures on the physical interface (it does not — capture on lo).
- For mykb: the node anchors the Linux-virtual-networking cluster — namespaces, capabilities, and the container network stack all build on lo and the bridge.

## Related
- [[wiki/os-shell/linux-capabilities-and-selinux|Linux Capabilities & SELinux]]
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
