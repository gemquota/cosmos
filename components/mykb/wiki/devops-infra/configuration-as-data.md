---
type: "concept"
title: "Configuration as Data"
description: "Storing config in versioned data formats, not code"
tags: ["config", "data", "versioning", "iac"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Configuration as Data

## Summary
Configuration as data treats configuration as versionable, reviewable, machine-validated data rather than imperative setup scripts or dashboard clicks. It is the shared foundation of GitOps, infrastructure-as-code, and twelve-factor config: everything defining system behavior lives in a repo, is reviewed in PRs, and is applied by an automated reconciler.

## Details
- Mechanism: configuration lives in YAML, JSON, HCL, or TOML files (values, policies, manifests); schemas validate shape (JSON Schema, kubeconform, cue); a diff shows exactly what changes; a reconciler or pipeline applies it. Environments are data too — promotion moves the same config through dev, staging, and prod without drift.
- Concrete example: an Argo CD repository containing every manifest; a PR that bumps a version produces a rendered diff in the pipeline, an approval, and an automated sync; secrets are excluded from the repo and injected from a store, keeping the data layer auditable without exposing values.
- Failure modes: config drift — hand edits on servers the repo never learns about; validation gaps — config that parses but is semantically wrong, such as a typo'd field name silently ignored; ambient config — values present in only one environment, discovered during promotion; default divergence where local defaults differ from production data.
- Tradeoffs: config-as-data shifts effort to schemas and review but pays off in reproducibility and auditability; the cost is ceremony — every small change needs a PR, so teams batch low-risk changes or use automated approvals. Imperative hotfixes are allowed but should be exceptions followed by re-sync.
- Operational notes: validate schemas in CI, run config linters, keep secrets out of the data layer, and reconcile drift continuously (GitOps) rather than on demand.
- RSIS3 relevance: RSIS3's loop parameters and dashboard config are exactly this — storing them as versioned data lets L4/L5 experiments review, roll back, and reproduce parameter changes.

## Related
- [[wiki/devops-infra/infrastructure-as-code-revisited|Infrastructure as Code]]
- [[wiki/devops-infra/configuration-management-revisited|Configuration Management]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
