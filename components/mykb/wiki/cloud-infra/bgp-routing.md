---
type: "concept"
title: "BGP Routing"
description: "The path-vector protocol that interconnects autonomous systems"
tags: ["bgp", "routing", "internet", "asn"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc4271",
  "https://www.rfc-editor.org/rfc/rfc7454",
]
---

# BGP Routing

## Summary
BGP is the path-vector protocol that interconnects autonomous systems on the Internet, exchanging reachability for millions of prefixes. It is policy-driven rather than metric-driven: operators choose paths based on business relationships. BGP failures and hijacks make it the most operationally consequential routing protocol.

## Details
- RFC 4271 defines BGP-4: neighbors exchange UPDATE messages advertising network-layer reachability information with path attributes.
- Routes are selected by attributes such as local preference, AS path length, origin, and MED, then installed into the forwarding table.
- Peering happens over TCP port 179, which is why BGP sessions are often pinned or monitored separately.
- eBGP runs between autonomous systems; iBGP distributes learned routes inside an AS, often via route reflectors for scale.
- Route flaps, slow convergence, and prefix hijacking are the classic failure modes, mitigated by filtering, RPKI, and dampening.
- In cloud networking, BGP also appears inside SDN fabrics and with dynamic routing gateways, connecting the Internet and VPC worlds.

## Related
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/infrastructure/evpn-bgp-evpn|EVPN & BGP-EVPN]]
- [[wiki/infrastructure/eventbridge-and-routing|Eventbridge And Routing]]
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]]
