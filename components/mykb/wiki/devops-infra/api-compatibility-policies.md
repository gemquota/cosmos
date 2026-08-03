---
type: "concept"
title: "API Compatibility Policies"
description: "Rules for evolving APIs without breaking clients"
tags: ["api", "compatibility", "versioning", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# API Compatibility Policies

## Summary
API compatibility policies decide which changes to a service contract are allowed without a coordinated client rollout. The rule of thumb is additive-first: adding fields, endpoints, or enum values is usually safe, while removing, renaming, or changing semantics is breaking and must follow a documented deprecation cycle. The policy is what lets a team ship continuously while many clients upgrade at their own pace.

## Details
- Additive changes: new optional fields, new endpoints, new enum members, relaxed constraints. These are safe only if servers ignore unknown fields and clients tolerate them — enforce with JSON Schema `additionalProperties` handling and disciplined protobuf field numbering.
- Breaking changes: removing a field, changing a type, tightening validation, reordering protobuf field numbers, changing default behavior, or silently returning different data for the same request. Each needs a deprecation window (commonly 6-12 months), tracking of who still uses the old shape, and an enforced removal date.
- Mechanism: version the contract, not the client — URL path versions for REST, package/API versions for gRPC, schema `$id` for JSON Schema — and run compatibility diffs in CI so a breaking change fails the build before reaching production.
- Failure modes: dropping fields that clients still read yields silent nulls; reusing protobuf field numbers corrupts parsing; changing timestamp formats mis-orders events; "compatible" renames break reflection-based tooling. Silent failures are worst because data is corrupted before anyone notices.
- Tradeoffs: strict policies slow velocity and multiply versions; lax policies push breakage onto clients. A middle path is additive-only within a major version plus automated detection of accidental breaks, applied to internal consumers as strictly as external ones.
- RSIS3 relevance: RSIS3 loops exchange structured artifacts (registry entries, pulses, checkpoints); treating those schemas as versioned APIs with compatibility policies prevents old cached state from breaking new loop versions during L2/L3 evolution.

## Related
- [[wiki/devops-infra/api-gateways|API Gateways]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/api-gateway-patterns|API Gateway Patterns]]
