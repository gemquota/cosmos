---
type: "concept"
title: "Microsegmentation"
description: "Fine-grained isolation between workloads down to the service level"
tags: ["microsegmentation", "security", "networking", "zero-trust"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Microsegmentation

## Summary
Microsegmentation is fine-grained isolation between workloads — down to the individual service or pod, rather than the subnet or network segment. It exists because the perimeter model failed: once east-west traffic (service-to-service) dominates and attackers move laterally inside the network, the question "who can talk to whom" must be answered at every connection, not at the edge. Microsegmentation is the network-level implementation of zero trust.

## Details
- The problem it solves: traditional segmentation divides the network into a few big zones (DMZ, app tier, data tier) with firewalls between them. The zones are coarse — everything in the app tier can reach everything else — so a compromise of one service gives the attacker free lateral movement across all its zone-mates, which is exactly where the sensitive data usually lives (the attacker hops app → database in one allowed connection). Microsegmentation replaces "same zone = trusted" with per-workload policy: each service gets the smallest set of allowed peers, enforced per connection.
- The mechanisms: in virtualized/cloud environments, the enforcement points are the hypervisor or host — policies attached to workloads (VMs, pods, containers) rather than to network segments. Kubernetes network policies are the canonical expression (select pods by label, allow specific ingress/egress); Calico, Cilium, and cloud-native security platforms (NSX, Illumio, etc.) enforce at the workload's virtual interface, so policy travels with the workload — a pod moving to a new node keeps its policy. Because enforcement is L3/L4 (and increasingly L7, in Cilium's case), the policy language is "service A may talk to service B on port X", not "10.0.0.0/8 may talk to 10.1.0.0/8".
- The tradeoffs: the fine granularity is the security win and the operational cost. Every policy is a rule to write, review, and debug, and the default-deny posture (the strong baseline) breaks applications whose dependencies were never documented — the reason microsegmentation projects fail is not the technology but the discovery phase (mapping actual service-to-service dependencies) and the cultural change of making every connection intentional. The mitigations: policy from observed traffic (analyze flows, generate the allow-list, review, enforce), label-driven policy that survives workload churn, and staged rollout (observe → warn → enforce).
- The failure modes: policies that drift from reality (dependencies change, policy does not), the all-allow escape hatch ("we'll tighten it later" — which is the same as no segmentation), and the enforcement gap (a workload type the CNI/firewall does not cover becomes a free path).
- For mykb: microsegmentation is the security story behind the network-policy and service-mesh nodes — the same east-west isolation logic implemented at different layers.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
