---
type: "concept"
title: "Custom Resource Definitions"
description: "Extending the Kubernetes API with typed resources"
tags: ["crd", "kubernetes", "api", "extensibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Custom Resource Definitions

## Summary
Custom Resource Definitions (CRDs) extend the Kubernetes API with domain-specific object types: a CRD defines the schema, and a controller (operator) reconciles instances toward desired state. This turns the Kubernetes API and controller pattern into a platform for building operational automation with built-in declarative semantics.

## Details
- Mechanism: a CRD declares group, version, kind, and an OpenAPI v3 schema for spec and status; the API server stores instances and validates them; an operator watches instances and reconciles — reading spec, comparing to reality, and acting; status surfaces outcomes and conditions back to users and other controllers.
- Concrete example: a `PostgresCluster` CRD with spec for version, replicas, and storage; the operator creates StatefulSets, PVCs, and backups, then reports Ready conditions in status; users interact only with the CRD, not the underlying resources.
- Failure modes: schemas without validation defaults — missing required fields surface only at runtime; status written by multiple controllers causing conflicts; conversion webhooks breaking when a new version is introduced — old instances must convert or you lose upgradeability; a controller that reconciles too fast (hot loop) or too slow (drift); name conflicts and API-group collisions; pruning and garbage collection of owned resources when an instance is deleted.
- Tradeoffs: CRDs are powerful but add maintenance — schema design, conversions, RBAC, and controller maturity all become your problem; the alternative (ConfigMaps plus scripts) is simpler but loses validation, watch semantics, and status. Use CRDs when the resource is truly declarative and long-lived, not for one-off jobs.
- Operational notes: follow API versioning conventions, write comprehensive schema defaults, set `preserveUnknownFields: false`, and test upgrades across versions in staging.
- RSIS3 relevance: RSIS3 could model loop configurations (strategy sets, pulse pipelines) as CRDs — the API server provides validation, versioning, and watch semantics for free.

## Related
- [[wiki/os-shell/resource-utilization-analysis|Resource Utilization Analysis]]
- [[wiki/cloud-infra/resource-tagging|Resource Tagging]]
- [[wiki/infrastructure/t-shirt-sizing-and-resource-models|T Shirt Sizing And Resource Models]]
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
