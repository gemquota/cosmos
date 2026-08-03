---
type: "concept"
title: "Gatekeeper & Policy as Code"
description: "OPA Gatekeeper admission policies stored as code"
tags: ["gatekeeper", "opa", "policy-as-code", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Gatekeeper & Policy as Code

## Summary
Gatekeeper (and OPA/Rego generally) enforces policy as code on Kubernetes: admission requests are evaluated against Rego policies, and violations block or mutate the request. Policy-as-code moves guardrails — who can do what, what images are allowed, what labels are required — out of tribal knowledge and into tested, versioned policies.

## Details
- Mechanism: OPA evaluates Rego queries; Gatekeeper integrates OPA with Kubernetes admission via ConstraintTemplates (policy logic) and Constraints (instantiated rules with parameters); a violation returns a denial with a message; audit mode reports violations without blocking, letting teams see impact before enforcing.
- Concrete example: a constraint requiring all pods to have resource limits; a constraint blocking `latest` image tags; a constraint enforcing namespace labels; policies are written in Rego, tested with `opa test`, and deployed through the same GitOps pipeline as everything else.
- Failure modes: policies that are too broad and block legitimate workloads, causing outage-style firefights (use audit mode and dry-run first); Rego that is hard to read, so bugs hide in the policy; the policy engine becoming the new bottleneck or single point of failure — a misconfigured Gatekeeper can take down the API path; bypasses via resources the constraints do not cover (cron jobs, helm hooks).
- Tradeoffs: policy-as-code gives consistent, reviewable, testable enforcement versus scattered admission hooks and human review; the costs are Rego's learning curve and the policy engine's operational weight; the payoff is that "why was this denied?" has a code answer.
- Operational notes: test policies in CI, run audit mode before enforce, version policies with the cluster, and monitor admission latency and denial rates.
- RSIS3 relevance: the same pattern applies to RSIS3's own workflows — encode guardrails (state invariants, telemetry coverage) as testable policies that the loops check, just as Gatekeeper checks cluster requests.

## Related
- [[wiki/devops-infra/infrastructure-as-code-revisited|Infrastructure as Code]]
- [[wiki/devops-infra/development-environments-as-code|Development Environments as Code]]
- [[wiki/devops-infra/configuration-as-data|Configuration as Data]]
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]]
