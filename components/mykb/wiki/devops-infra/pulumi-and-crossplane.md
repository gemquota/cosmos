---
type: "concept"
title: "Pulumi & Crossplane"
description: "Infrastructure as code in general-purpose languages and control planes"
tags: ["pulumi", "crossplane", "iac", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Pulumi & Crossplane

## Summary
Pulumi and Crossplane represent the next generation of infrastructure-as-code: Pulumi replaces HCL with real programming languages (TypeScript, Python, Go) and per-stateful resource graphs, while Crossplane runs infrastructure provisioning inside Kubernetes as declarative custom resources, enabling a control-plane model where platform teams expose infrastructure APIs to app teams.

## Details
- Pulumi mechanics: infrastructure is code in a general-purpose language — loops, conditionals, functions, and sharing via packages; the CLI computes diffs against state and applies; the state is a resource graph (not just text files), enabling previews and accurate dependency ordering; works with many clouds and Kubernetes.
- Crossplane mechanics: provider CRDs (AWS, GCP, Azure, Kubernetes) represent cloud resources; a Composition defines how a higher-level claim (PostgreSQLInstance) renders into lower-level resources; platform teams publish APIs, and app teams create claims without touching cloud credentials.
- Concrete example: a Pulumi program in TypeScript creating a VPC, RDS, and EKS cluster with loops over environments; a Crossplane claim `PostgreSQLInstance v2` that the platform composition turns into an RDS instance plus secrets, provisioned when the app team applies it.
- Failure modes: language power inviting imperative complexity — programs that are hard to review (treat as code with tests); Pulumi state corruption or drift handling; Crossplane compositions becoming hard to debug as providers lag cloud APIs; provider credential sprawl; a composition bug provisioning (or deleting) the wrong resources at scale.
- Tradeoffs: programming languages give expressiveness and reuse at the cost of review and debugging weight; Crossplane moves IaC into the cluster, giving app teams self-service, but adds a control plane to operate; both replace — rather than wrap — the Terraform workflow, so migration means re-implementing existing state.
- Operational notes: version programs/claims, test plans in CI, pin providers, and keep credentials least-privileged.
- RSIS3 relevance: cosmos's infra-as-code choice affects how quickly loop experiments get environments — a programmable or claim-based model makes disposable test environments cheap.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
