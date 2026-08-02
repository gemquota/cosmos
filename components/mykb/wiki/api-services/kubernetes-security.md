---
type: "concept"
title: "Kubernetes Security"
description: "Securing clusters: RBAC, pod security, network policy, and secrets"
tags: ["kubernetes", "k8s", "security", "clusters"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kubernetes.io/docs/concepts/security/overview/", "https://kubernetes.io/docs/concepts/security/security-checklist/"]
---

# Kubernetes Security

## Summary


## Details
- Kubernetes security is defense in depth across the cluster: authentication, authorization, admission control, network policy, and workload isolation.
- RBAC bounds what identities can do; admission controllers (including Pod Security) enforce policy before workloads run.
- Network policies segment traffic, and security contexts, seccomp, and AppArmor profiles restrict what containers can do.
- The attack surface includes the API server, etcd, kubelets, image registries, and the supply chain of everything they pull.
- **Worked example / comparison** — Worked example — a cluster enforces: no privileged pods, a default-deny network policy, RBAC scoped per namespace, and image scanning blocking vulnerable tags at admission. This layered posture means a single compromise — a leaked kubeconfig, an over-permissioned pod, a malicious image — does not automatically give an attacker the whole cluster.
- For mykb, kubernetes-security is the cluster-level capstone of the container-security cluster.

## Related
- [[wiki/api-services/container-security|Container Security]]
- [[wiki/security-auth/network-segmentation|Network Segmentation]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
