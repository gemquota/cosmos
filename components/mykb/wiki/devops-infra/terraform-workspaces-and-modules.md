---
type: "concept"
title: "Terraform Workspaces & Modules"
description: "Reusable module composition and isolated state workspaces"
tags: ["terraform", "modules", "workspaces", "iac"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Terraform Workspaces & Modules

## Summary
Terraform workspaces and modules are the two main structures for organizing infrastructure code: modules package reusable, parameterized resource groups (a VPC module, a database module), and workspaces (or environments with separate state) isolate state for dev, staging, and prod. Modules give reuse and consistency; workspaces give separation.

## Details
- Modules: a directory of Terraform with input variables and outputs; modules are versioned (registry, git tags) and called with arguments; they enforce patterns (naming, tagging, security defaults) consistently across every use.
- Workspaces: named state instances within one backend — each workspace has its own state and variables; the common alternative is directory-per-environment with separate state files, which avoids shared-module coupling; both isolate environments so a change in dev cannot affect prod.
- Concrete example: a `network` module creates VPC, subnets, and security groups; dev, staging, and prod each call it in their own directory with different CIDRs and tags; a database module versions its schema and settings; CI runs plan on every workspace and applies with approvals.
- Failure modes: workspace drift — variables or state diverging between environments; module version skew where environments run different module versions; state lock contention blocking parallel applies; module interfaces that grow too large or too rigid; accidentally applying the wrong workspace, changing prod from a dev session.
- Tradeoffs: modules reduce duplication but add an abstraction layer that must be versioned and tested; workspaces share a backend and can cause cross-environment mistakes, while separate state directories are safer and clearer at the cost of duplication; the mature pattern is versioned modules plus directory-per-environment state and a promotion pipeline.
- Operational notes: test modules in CI, pin module versions, separate state backends per environment, and gate applies by environment.
- RSIS3 relevance: cosmos's infrastructure should follow the same structure — reusable modules for the wiki stack, separate state per environment — so promoting a change is a reviewed diff.

## Related
- [[wiki/devops-infra/terraform-state-management|Terraform State Management]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/devops-infra/terraform|Terraform]]
- [[wiki/os-shell/kernel-modules|Kernel Modules]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
