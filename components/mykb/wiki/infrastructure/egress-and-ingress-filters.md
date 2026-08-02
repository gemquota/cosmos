---
type: "concept"
title: "Egress & Ingress Filters"
description: "Directional access control at network boundaries"
tags: ["ingress", "egress", "firewall", "filtering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc2827",
  "https://www.rfc-editor.org/rfc/rfc3704",
]
---

# Egress & Ingress Filters

## Summary
Egress and ingress filters control traffic direction at network boundaries, implementing the principle of least privilege for the network. Ingress rules decide what can enter; egress rules decide what can leave. Both are enforced by firewalls, security groups, and ACLs.

## Details
- Ingress filtering protects services by allowing only expected protocols and sources, as recommended by BCP 38 for spoofing prevention.
- Egress filtering limits what compromised hosts can reach: C2 domains, data exfiltration, and lateral movement all depend on outbound freedom.
- RFC 2827 and RFC 3704 document anti-spoofing ingress filtering that rejects packets with source addresses not routable from the interface.
- Cloud security groups are stateful: return traffic is allowed automatically, while ACLs are stateless and need explicit rules.
- Egress proxies add an application-aware choke point on top of IP-level filtering.
- A practical pattern is default-deny with explicit allow lists, tested during game days so legitimate flows are not broken.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.

## Related
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/infrastructure/egress-proxies-and-filters|Egress Proxies & Filters]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
