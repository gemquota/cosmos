---
type: "concept"
title: "Network Policy"
description: "Declarative rules controlling which pods can talk to which, closing the east-west blast radius"
tags: ["network-policy", "kubernetes", "security", "segmentation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Network Policy

## Summary
Network policies are Kubernetes firewall rules that allow or deny traffic between pods and services. By default cluster networking is flat — every pod can reach every other pod — so policies are the mechanism that brings segmentation to east-west traffic: they define, per workload, exactly which peers may talk to it, and everything else is denied. They are microsegmentation's native Kubernetes expression.

## Details
- Policies select pods by label and define ingress/egress rules by pod, namespace, or CIDR. A NetworkPolicy has a podSelector (which pods it applies to) and a policyTypes list (ingress, egress, or both), plus rules: each rule has a from/to selector — another pod selector, a namespace selector, an IP block, or a combination — and optionally ports. The semantics: any policy applied to a pod adds allow rules; with no policy, traffic is allowed (flat default); the recommended strong baseline is a default-deny policy per namespace (a policy with no rules) so that everything not explicitly allowed is blocked. The combination logic (pod AND namespace selectors, or of IP blocks) gives expressive rules — "allow the frontend pods in the web namespace to reach the API on 443".
- Requires a CNI that enforces them (Calico, Cilium); default-deny is the strong baseline. The Kubernetes API defines the policy object, but enforcement lives in the CNI plugin: Calico programs iptables/eBPF rules per host, Cilium uses eBPF in the kernel, and the policy becomes per-endpoint firewall state — enforced at the pod's virtual interface, so policy follows the pod across nodes. The operational consequence: "I wrote a NetworkPolicy and nothing changed" means the CNI does not enforce it (some CNIs are policy-blind), and the safe migration is to verify the CNI's enforcement mode before trusting the policy.
- Policy review belongs in the deploy pipeline like any other code. Network policies are firewall rules written as YAML — they change the security posture on merge — so they need review, testing (a staging cluster where default-deny is enforced and traffic maps are verified), and versioning like any other security-relevant code. The failure modes: policies that drift from the application's real dependencies (a service's new dependency is not in the policy — the connection breaks in production, the classic "default-deny broke the app" incident), and the reverse — broad allow rules that were meant to be temporary and became permanent.
- Open question: how network policy and service mesh policy should divide enforcement — L3/L4 in the CNI, L7 (paths, methods, auth) in the mesh, with the split defined by the team's security model.
- For mykb: the node anchors the Kubernetes segmentation cluster — service mesh (L7), VPC (the outer boundary), and zero trust (the rationale) are its siblings.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — L7 policy complement
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the outer network boundary
- [[wiki/security/zero-trust|Zero Trust Architecture]] — segmentation rationale
- [[wiki/devops-infra/kubernetes|Kubernetes]] — policies run in clusters
