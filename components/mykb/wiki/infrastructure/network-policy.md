---
type: "concept"
title: "Network Policy"
description: "Declarative rules controlling which pods can talk to which, closing the east-west blast radius"
tags: ["network-policy", "kubernetes", "security", "segmentation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Network Policy

## Summary
Network policies are Kubernetes firewall rules that allow or deny traffic between pods and services. By default cluster networking is flat — policies bring segmentation to east-west traffic.

## Details
- Policies select pods by label and define ingress/egress rules by pod, namespace, or CIDR.
- Requires a CNI that enforces them (Calico, Cilium); default-deny is the strong baseline.
- Policy review belongs in the deploy pipeline like any other code.
- Open question: how network policy and service mesh policy should divide enforcement.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — L7 policy complement
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the outer network boundary
- [[wiki/security/zero-trust|Zero Trust Architecture]] — segmentation rationale
- [[wiki/devops-infra/kubernetes|Kubernetes]] — policies run in clusters
