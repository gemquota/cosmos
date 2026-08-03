---
type: "concept"
title: "OpenTofu & Forks"
description: "The open-source Terraform fork and ecosystem compatibility"
tags: ["opentofu", "terraform", "iac", "open-source"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# OpenTofu & Forks

## Summary
OpenTofu is the open-source fork of Terraform created after HashiCorp's license change: a drop-in-compatible IaC tool implementing the Terraform workflow and provider ecosystem under MPL-2.0. Teams adopt it to keep Terraform-style workflows on an open license with community governance.

## Details
- Mechanism: OpenTofu reimplements the Terraform CLI, state format, HCL, and provider protocol; existing Terraform configurations and providers run without code changes in most cases; the registry and provider ecosystem are shared via the provider protocol; development is community-governed with feature proposals and releases.
- Concrete example: a team migrates by swapping the binary in CI (terraform -> tofu) and running plan/apply; state files remain compatible; modules and providers work unchanged; the fork adds its own features (encrypted state, provider-defined functions) while tracking the upstream language.
- Failure modes: feature drift — a Terraform feature or provider that depends on proprietary behavior breaks on the fork; version skew in state format between tools; ecosystem confusion where some CI tools assume terraform binary names; providers pinning to upstream-only behaviors; migration cutovers that mix tofu and terraform in one pipeline, splitting state.
- Tradeoffs: OpenTofu buys license freedom and community governance but introduces a second ecosystem to track; the compatibility promise is strong but not absolute — test every provider and feature before committing; staying on Terraform means accepting its license terms; both are viable for most teams, and the split is more about governance than capability.
- Operational notes: pin versions, test plan diffs in CI with both tools during migration, and keep state migration rehearsed.
- Migration path: run both binaries in CI during the transition, compare `tofu plan` against the same state, and switch the pipeline only when plans match — never let both tools apply in the same window.
- RSIS3 relevance: cosmos's infra-as-code choice (OpenTofu vs Terraform) is a governance decision with operational consequences — the wiki's infrastructure definitions should record which toolchain they target.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
