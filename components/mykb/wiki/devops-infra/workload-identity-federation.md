---
type: "concept"
title: "Workload Identity Federation"
description: "Exchanging workload credentials for cloud roles without long-lived keys"
tags: ["identity", "federation", "oidc", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Workload Identity Federation

## Summary
Workload identity federation lets workloads authenticate to external services (cloud APIs, other platforms) using their platform identity instead of long-lived static keys: Kubernetes service accounts get cloud IAM roles, GitHub Actions get cloud credentials via OIDC, and short-lived tokens are issued per run. It removes the static-credential class of supply-chain risk.

## Details
- Mechanism: the workload presents its own identity (a Kubernetes service account token, a GitHub OIDC token); the target cloud validates it against a trust relationship (IAM OIDC provider, workload identity pool) and issues short-lived credentials scoped by the mapping; the workload uses those credentials and they expire automatically.
- Concrete example: GitHub Actions calls the cloud API with OIDC federation — no long-lived access key in secrets; the trust policy pins the repo and branch, and each job gets scoped, expiring credentials; a pod's service account maps to an IAM role allowing only its needed actions.
- Failure modes: trust policies too broad (any workflow or branch able to mint credentials); token replay where a stolen token is valid longer than intended (keep TTLs short); audience mismatches breaking issuance; fallback to static keys when federation misconfigures, quietly reintroducing the risk; identity mapping sprawl that is hard to audit.
- Tradeoffs: federation eliminates static secrets — the single biggest credential win — at the cost of trust-policy design and debugging; the alternative, static keys, is simpler until one leaks; the mature pattern is federation with pinned trust, short TTLs, and audit logs on issuance.
- Operational notes: review trust policies periodically, monitor credential issuance, and treat identity mappings as code.
- RSIS3 relevance: cosmos's CI and daemon should use federated identity for cloud access — no static keys in the repo means a repo leak does not become an account compromise.

## Related
- [[wiki/devops-infra/identity-aware-proxies|Identity-Aware Proxies]]
- [[wiki/devops-infra/cluster-federation-vs-hub-spoke|Federation vs Hub-Spoke]]
- [[wiki/infrastructure/workload-management-and-queues|Workload Management And Queues]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/identity-distribution|Identity Distribution]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
