---
type: "concept"
title: "Policy Engines: OPA & Kyverno"
description: "General-purpose and Kubernetes-native policy evaluation"
tags: ["opa", "kyverno", "policy", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Policy Engines: OPA & Kyverno

## Summary
OPA (Open Policy Agent) and Kyverno are the two dominant policy engines for Kubernetes: OPA evaluates Rego policies against admission requests and arbitrary data; Kyverno is Kubernetes-native, expressing policies as Kubernetes resources with YAML rules. Both implement policy-as-code: tested, versioned, reviewable guardrails instead of tribal rules.

## Details
- OPA mechanics: policies are Rego programs evaluated against inputs (admission review objects, configuration, live data); Gatekeeper integrates OPA with Kubernetes admission via ConstraintTemplates and Constraints; OPA also polices non-Kubernetes inputs (HTTP, Terraform, data); the engine is general, the Kubernetes integration is an add-on.
- Kyverno mechanics: a policy is a CRD with match/exclude selectors and rules; rules validate, mutate, generate, or clean up resources; cluster policies and namespaced policies share the same YAML model; policies can write status and send reports; no separate language — YAML plus JMESPath expressions.
- Concrete example: the same requirement — block `latest` image tags, require resource limits, enforce labels — is a Rego ConstraintTemplate under OPA and a YAML validate rule under Kyverno; both support audit mode to report violations without blocking.
- Failure modes: policy engines as a new single point of failure — a misconfigured engine can block the API path (always test and monitor admission latency); Rego's learning curve hiding bugs in policies; Kyverno's YAML expressiveness hitting its limits for complex logic; bypasses where resources escape policy scope (helm hooks, system controllers).
- Tradeoffs: OPA is more powerful and portable (one language for cluster, CI, and data); Kyverno is easier to adopt and maintain for pure-Kubernetes teams; the choice is complexity versus fit — most clusters with simple guardrails do fine with Kyverno, while OPA pays off for cross-platform policy.
- Operational notes: test policies in CI, roll out in audit mode, monitor denial rates, and version policies with the cluster.
- RSIS3 relevance: the same policy-as-code idea applies inside RSIS3 — encode registry invariants and state-guardrails as testable rules the loops must pass, with audit mode while new rules are unproven.

## Related
- [[wiki/devops-infra/gatekeeper-and-policy-as-code|Gatekeeper & Policy as Code]]
- [[wiki/infrastructure/network-policy|Network Policy]]
- [[wiki/os-shell/regex-engines|Regex Engines]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
