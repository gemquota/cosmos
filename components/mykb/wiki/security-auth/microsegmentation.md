---
type: "concept"
title: "Microsegmentation"
description: "Per-workload, per-service segmentation enforced by policy rather than physical topology"
tags: ["microsegmentation", "zero-trust", "workloads", "policy"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Microsegmentation"]
---

# Microsegmentation

- Microsegmentation applies identity-aware policy to individual workloads — containers, VMs, pods — instead of broad network zones.
- It pairs with service meshes and cloud network policies to enforce least privilege between services.
- The policy model is per-connection: which service may talk to which, on which ports, with which identities.
- For mykb: microsegmentation would let the memory service accept calls only from authorized agent runtimes.

## Related

- [[wiki/security-auth/network-segmentation|Network Segmentation]] — the coarser ancestor
- [[wiki/security/zero-trust|Zero Trust Architecture]] — per-request trust decisions
- [[wiki/api-services/kubernetes-security|Kubernetes Security]] — network policies per pod
- [[wiki/devops-infra/istio|Istio]] — mesh-based policy enforcement
- [[wiki/security-auth/least-privilege|Least Privilege]] — per-connection policy is network least privilege
