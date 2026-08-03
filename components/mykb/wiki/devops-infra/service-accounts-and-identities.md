---
type: "concept"
title: "Service Accounts & Identities"
description: "Machine identities for workloads: tokens, keys, and cloud roles"
tags: ["service-accounts", "identity", "kubernetes", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Service Accounts & Identities

## Summary
Service accounts and workload identities give machine workloads an identity for authentication: Kubernetes ServiceAccounts for in-cluster operations, and workload identity federation (AWS IRSA, GCP Workload Identity, Azure AD Pod Identity) for cloud API access. The principle is the same as for humans — least privilege, short-lived credentials, audited usage — applied to code.

## Details
- Kubernetes mechanics: a ServiceAccount exists per namespace; pods mount its token; RBAC binds roles to service accounts; tokens authenticate to the API server; projected service account tokens are short-lived and audience-scoped, avoiding the pitfalls of long-lived static tokens.
- Cloud identity mechanics: workload identity binds a Kubernetes service account to a cloud IAM role — the cloud issues short-lived credentials only to pods with the right service account; no static keys live in the cluster.
- Concrete example: a pod running the wiki daemon uses a service account with a role allowing only reads from the store bucket and writes to the backup bucket; the cloud role is scoped to those actions; rotation happens automatically as tokens expire.
- Failure modes: using the default service account with over-broad cluster-admin RBAC; static cloud keys committed or mounted as fallback when workload identity misconfigures; token expiry breaking long-running jobs that do not renew; audience mismatches where a token minted for one purpose authenticates elsewhere; identity sprawl — one service account per concern multiplied into unmanageable policy.
- Tradeoffs: workload identity removes static secrets — a major security win — but adds federation and RBAC complexity; the alternative, static keys, is simpler and leaks; the mature pattern is least-privilege service accounts per workload, short-lived tokens, and audited cloud roles.
- Operational notes: audit service accounts and role bindings periodically, monitor token expiry and usage, and treat identity changes like code changes.
- RSIS3 relevance: cosmos's daemon and dashboard need identities, not passwords — workload identity keeps cloud access short-lived and scoped, matching the least-privilege discipline RSIS3 applies to its own state.

## Related
- [[wiki/devops-infra/service-mesh-sidecars|Service Mesh Sidecars]]
- [[wiki/devops-infra/service-meshes-istio-linkerd|Service Meshes: Istio & Linkerd]]
- [[wiki/cloud-infra/service-discovery-dns-based|DNS-Based Service Discovery]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
