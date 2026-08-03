---
type: "concept"
title: "Namespace Networking"
description: "Network namespaces as isolated network stacks for containers"
tags: ["namespaces", "networking", "containers", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Namespace Networking

## Summary
A network namespace is a kernel-isolated copy of the network stack: its own interfaces, routes, firewall rules, and socket tables. Containers are the famous consumer — each gets a namespace with its own loopback and a virtual Ethernet pair (veth) connecting it to the host — but network namespaces are also the mechanism behind VPNs, network testing labs, and multi-tenant isolation on a single host.

## Details
- Mechanism: `ip netns add ns1` creates a namespace with only loopback; `ip link add veth0 type veth peer name veth1` creates a veth pair, `ip link set veth1 netns ns1` moves one end into the namespace, and each side gets addresses and routes — a container's network is exactly this: one end in the host (attached to a bridge), one end inside the container. Bridges (`br0`) connect many veth host-ends so containers on one host share a subnet, while routing/NAT (`iptables`/nftables MASQUERADE) gives them outbound access. Each namespace carries independent state for interfaces, ARP, routing tables, netfilter rules, and socket options, so a firewall change or interface flap inside one namespace cannot touch another.
- Concrete examples: Docker's default bridge network creates one namespace per container with a veth into `docker0`; `ip netns exec ns1 ping 8.8.8.8` tests a namespace's connectivity; a network engineer builds a virtual lab of namespaces connected by veth pairs and bridges to test routing protocols without hardware; a service isolates tenants by putting each in its own namespace with its own egress policy; unprivileged users can create namespaces (`unshare -n`) to experiment without root.
- Failure modes: the classic failures are forgetting that the default namespace contains the physical NICs — moving a physical interface into a namespace removes it from the host, and if the namespace is deleted, the interface is destroyed; DNS and service discovery inside a namespace depend on the namespace's own resolv.conf and hosts file, so a fresh namespace has no DNS until configured; and nested namespaces multiply confusion (a container runtime inside a container needs its own veth setup and can run into `NET_ADMIN` capability limits).
- Operational tradeoffs: namespaces give hard isolation at near-zero performance cost — they are kernel objects, not VMs — but they complicate debugging (the `ss`, `tcpdump`, and `iptables` you run must target the right namespace with `ip netns exec`) and require deliberate plumbing (veth, bridge, NAT) that VM-style isolation provides out of the box. The practice rules: script namespace creation idempotently, never move a physical NIC you are not prepared to lose, use `ip netns exec` for all inspection commands, and pair namespaces with routing and firewall policy explicitly rather than assuming defaults. RSIS3/mykb relevance: namespace isolation is compartmentalization — each agent loop or service boundary gets its own network state, mirroring RSIS3's rule that one loop's traffic and failures must not leak into another's.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
