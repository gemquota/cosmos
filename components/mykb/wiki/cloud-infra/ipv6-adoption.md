---
type: "concept"
title: "IPv6 Adoption"
description: "Address exhaustion, transition mechanisms, and the state of IPv6 rollout"
tags: ["ipv6", "addressing", "adoption", "internet"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc8200",
  "https://www.rfc-editor.org/rfc/rfc4291",
]
---

# IPv6 Adoption

## Summary
IPv6 replaces IPv4's 32-bit addresses with 128-bit addresses, solving exhaustion while adding mandatory security and simpler configuration. Adoption has been gradual: the Internet is dual-stacked today, with IPv6 traffic dominating in several regions. Infrastructure engineers must understand both stacks.

## Details
- RFC 8200 defines IPv6; RFC 4291 covers addressing architecture including link-local addresses and global unicast assignments.
- IPv6 removes NAT as a default requirement, restoring end-to-end connectivity and simplifying some security models.
- Transition mechanisms such as dual-stack, tunneling (6in4), and translation (NAT64) let IPv4 and IPv6 coexist.
- Stateless address autoconfiguration (SLAAC) and DHCPv6 assign addresses without a central server.
- The expanded address space also enables simpler subnetting: 64-bit interface identifiers make subnet planning uniform.
- Practical adoption drivers include cloud provider defaults, mobile networks, and CDNs, while legacy equipment and monitoring remain the main blockers.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/ipv6-link-local-addresses|IPv6 Link-Local Addresses]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
