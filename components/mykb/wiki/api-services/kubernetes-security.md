---
type: "concept"
title: "Kubernetes Security"
description: "Securing clusters: RBAC, pod security, network policy, and secrets"
tags: ["kubernetes", "k8s", "security", "clusters"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://kubernetes.io/docs/concepts/security/"]
---

# Kubernetes Security

- Kubernetes security spans control-plane protection, workload isolation, RBAC, network policies, and secrets handling.
- Key practices: namespaces, least-privilege RBAC, pod security standards (restricted), no privileged containers, and TLS for all components.
- The Kubernetes documentation's security concepts page is the canonical starting map.
- For mykb: if the triad runs on k8s, a hardened cluster baseline protects the memory services.

## Related

- [[wiki/api-services/container-security|Container Security]] — the workload layer under k8s
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — network policies segment pods
- [[wiki/devops-infra/kubernetes|Kubernetes]] — existing article on the platform
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — cluster RBAC
