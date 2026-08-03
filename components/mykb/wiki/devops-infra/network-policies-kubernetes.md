---
type: "concept"
title: "Kubernetes Network Policies"
description: "L3/L4 allowlists between pods enforced by the CNI plugin"
tags: ["kubernetes", "network-policy", "security", "cni"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Kubernetes Network Policies

## Summary
Kubernetes NetworkPolicy is the built-in mechanism for segmenting pod traffic: it selects pods by label and declares which peers and ports may reach them (ingress) and which destinations they may reach (egress). With no policies, the cluster network is flat — every pod can talk to every pod — so policies are the difference between that and least-privilege networking.

## Details
- Mechanism: a NetworkPolicy has a podSelector (who the policy applies to), policyTypes (ingress, egress, or both), and rules with from/to selectors (pod labels, namespaces, IP blocks) and ports; policies are additive — if any policy selects a pod, only traffic permitted by the union of matching policies is allowed; absent a policy, everything is allowed.
- Concrete example: a default-deny policy per namespace with an ingress rule allowing only the frontend pods on port 8080; an egress rule allowing the API pods to reach only the database and the monitoring endpoint; policies expressed with namespace selectors to avoid enumerating pods.
- Failure modes: the classic default-deny rollout breaking every flow that was never enumerated — map actual traffic first (flow logs, service graphs); rules with IP blocks that drift as the cluster grows; namespace selectors matching unintended namespaces; the CNI not enforcing policies at all (each CNI implements NetworkPolicy differently, and some do not); policy bloat making rules unreadable and unverifiable.
- Tradeoffs: strict policies shrink blast radius and satisfy compliance but add a flow-mapping and debugging tax on every change; allow-all is cheapest to operate and worst for security; the practical path is default-deny in sensitive namespaces plus observability of denied traffic to iterate.
- Operational notes: test policies in staging, generate candidate rules from observed flows, and review new rules like code.
- RSIS3 relevance: if cosmos services share a cluster, NetworkPolicy bounds what a compromised wiki daemon could reach and what the loops can call — worth mapping before it matters.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
