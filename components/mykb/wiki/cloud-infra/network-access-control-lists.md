---
type: "concept"
title: "Network Access Control Lists"
description: "Stateless subnet-level filtering rules on cloud networks"
tags: ["acl", "networking", "firewall", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Network Access Control Lists

## Summary

Network ACLs (NACLs) are stateless, subnet-level filters — in AWS they evaluate rules by priority for both directions; GCP firewall rules and Azure NSGs fill similar roles with different semantics. They are the coarse second layer under security groups, not the primary control.

## Details
- Mechanism: AWS NACLs are stateless: inbound and outbound rules are evaluated independently, so responses need explicit allow rules (ephemeral ports); rules have a priority (lowest number wins, default deny at 65535); GCP firewall rules are stateful with priority and can target tags/service accounts; Azure NSGs are stateful with priority and apply per subnet/NIC.
- Concrete example: a subnet-level NACL denies inbound 22 from 0.0.0.0/0 while the instance security group allows 22 only from a bastion — defense in depth; a GCP firewall rule allows egress to the internet only from tagged instances, blocking others even if their SG allows it; ephemeral-port ranges (1024-65535) must be allowed for outbound responses on stateless NACLs.
- Failure modes: forgetting ephemeral-port allows on stateless NACLs (connections fail one way); rule ordering mistakes where a broad allow shadows a deny; NACL/SG contradictions that are hard to debug (check both when traffic fails); and drifting rule sets from manual edits that diverge from IaC.
- Operational tradeoffs: NACLs give subnet-wide control and DDoS-baseline filtering, but statelessness makes them error-prone; security groups remain the primary per-instance control. Keep NACLs minimal and stable, and remember that with stateful alternatives (GCP, Azure NSG), the ephemeral-port burden disappears.
- RSIS3/mykb relevance: the wiki's subnet baselines use minimal NACLs plus group references; this note records the ephemeral-port rules the loop's IaC templates must preserve.
- Change review: route NACL edits through the same review as security groups; stateless rules are easier to get wrong and harder to notice when wrong. On AWS, pair every stateless NACL change with a security-group check so the two layers agree.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/cloud-infra/congestion-control-algorithms|Congestion Control Algorithms]]
- [[wiki/cloud-infra/flow-control|Flow Control]]
