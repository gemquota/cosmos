---
type: "concept"
title: "NAT & Port Forwarding"
description: "Address translation and forwarding rules"
tags: ["nat", "port-forwarding", "networking", "masquerade"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc3022", "https://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO.html"]
---

# NAT & Port Forwarding

## Summary
Network address translation rewrites addresses (and often ports) as packets cross a boundary, letting many private hosts share one public IP and letting inbound traffic reach services inside. Connection tracking makes the translation stateful.

## Details
- SNAT/masquerade rewrites the source address of outbound traffic; masquerade picks the egress address automatically, ideal for dynamic WAN IPs.
- DNAT rewrites the destination, the basis of port forwarding: a router forwards WAN:8080 to a LAN host's port 80.
- Port forwarding rules pair a public port with a private destination and are the standard way to expose home servers and lab machines.
- Connection tracking (conntrack) remembers the mapping so return traffic is translated back; /proc/net/nf_conntrack shows the table.
- PAT (port address translation) maps many internal connections to different ports on one public IP, multiplying capacity.
- Limitations: inbound connections to private hosts fail without rules, and some protocols (FTP, SIP) embed addresses and need helpers.
- Modern tools: nftables nat chains replace iptables -t nat; cloud NAT gateways do the same at the VPC edge.

## Related
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]] — the path traffic takes before translation
- [[wiki/os-shell/firewalls-and-netfilter|Firewalls & netfilter]] — the framework NAT rules run in
- [[wiki/cloud-infra/nat-gateways|NAT Gateways]] — managed NAT in the cloud
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the subnets NAT connects
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — the port numbers forwarding rewrites
