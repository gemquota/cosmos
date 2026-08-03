---
type: "concept"
title: "NAT Variants"
description: "SNAT, DNAT, masquerade, and hairpin translation behaviors"
tags: ["nat", "networking", "routing", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# NAT Variants

## Summary

NAT variants — static (1:1), dynamic (many:few), NAPT/port address translation, destination NAT, and carrier-grade NAT — solve different problems: hiding private networks, sharing public IPs, and rewriting destinations. Choosing the wrong variant causes the classic "connects one way but not the other" failures.

## Details
- Mechanism: static NAT maps one private IP to one public IP (inbound-initiated services); dynamic NAT maps a pool without port translation; NAPT (most home/cloud NAT) maps many private addresses to one public IP using port numbers — outbound only unless port forwarding exists; DNAT rewrites destinations for inbound services; CGNAT sits at ISPs to share scarce IPv4 among many customers.
- Concrete example: a home network uses NAPT for thousands of devices behind one IP with port forwarding for a game server (DNAT); a company gives its mail server a static 1:1 mapping so MX records work; an ISP uses CGNAT, which breaks inbound VPNs and gaming — the reason IPv6 and port forwarding became customer issues.
- Failure modes: NAT types incompatible with protocols (FTP, SIP, IPSec embed IPs in payloads — ALGs exist but misfire); connection tracking table exhaustion under high churn; asymmetric routing when NAT is in the path of one direction only; and double NAT (router behind CGNAT) breaking inbound entirely.
- Operational tradeoffs: NAT conserves IPv4 and adds a security-ish boundary, but it breaks end-to-end connectivity and adds state; IPv6 removes the need; where NAT is unavoidable, document the variant per path (static for inbound services, NAPT for egress) and monitor connection tables.
- RSIS3/mykb relevance: the wiki's network diagrams label NAT variants per segment, so the loop's connectivity tests account for inbound restrictions before blaming applications.
- Connection tracking: monitor the NAT table size; exhaustion drops new connections silently while existing ones keep working, which is a confusing failure signature.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/network-function-virtualization|Network Function Virtualization]]
- [[wiki/infrastructure/network-policy|Network Policy]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
