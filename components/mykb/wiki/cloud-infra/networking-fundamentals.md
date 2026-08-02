---
type: "concept"
title: "Networking Fundamentals"
description: "The layered model, addressing, and packet flow that underpin all networked systems"
tags: ["networking", "fundamentals", "tcp-ip", "osi"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc1122",
  "https://www.rfc-editor.org/rfc/rfc1180",
]
---

# Networking Fundamentals

## Summary
Networking fundamentals cover the layered model, addressing, and packet flow that let applications communicate across hosts. Everything from a phone to a datacenter relies on the same core ideas: encapsulation, addressing, and routing. This node is the anchor of the mykb Systems & Infrastructure cluster.

## Details
- The OSI and TCP/IP models organize protocols into layers; each layer encapsulates the one above it, adding headers as data travels down the stack.
- Addressing has two scales: MAC addresses identify a link-local interface, while IP addresses identify a host on an internetwork and enable routing between networks.
- Packet flow is a pipeline: application data becomes segments, then packets, then frames, each step adding the information the next hop needs.
- RFC 1122 defines the host requirements that make interoperable implementations possible, and RFC 1180 remains the clearest short tutorial on the whole stack.
- Failure modes are layered too: link loss, routing loops, and transport retransmission each surface at a different level, which is why debugging starts at the physical layer and moves up.
- In the mykb graph this node feeds the protocol-specific pages such as TCP/IP, DNS, and HTTP, and links to the OS and cloud-infra clusters.

## Related
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/cloud-infra/vpc-networking|VPC Networking]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
