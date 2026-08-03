---
type: "concept"
title: "Mutating & Validating Policies"
description: "Admission policies that change or reject resource requests"
tags: ["admission", "policies", "kubernetes", "validation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Mutating & Validating Policies

## Summary
Kubernetes admission policies come in two kinds: mutating policies rewrite requests before they are stored (defaults, label injection, sidecar injection), and validating policies accept or reject requests (security constraints, naming rules). Mutating webhooks and ValidatingAdmissionPolicies (CEL-based) implement them; running in order — mutations first, validation last — they are the enforcement layer for cluster governance.

## Details
- Mechanism: the kube-apiserver calls admission controllers during CREATE/UPDATE; mutating policies (MutatingWebhookConfiguration or mutating policies) transform the object; validating policies (ValidatingWebhookConfiguration, or the built-in ValidatingAdmissionPolicy with CEL expressions) then check the final state; failures block the request; audit mode logs violations without blocking.
- Concrete example: a mutating policy that injects sidecars into selected pods or defaults resource requests; a validating policy requiring all deployments to have three replicas in prod or forbidding `latest` image tags; Kyverno policies implement both kinds declaratively.
- Failure modes: mutation order surprises — a later policy sees an earlier one's changes and rejects them; infinite loops when a mutating policy touches its own webhook config; validation gaps when resources are created by controllers bypassing admission (kubelet, system controllers); overly broad policies blocking legitimate workloads, causing firefights — use audit mode before enforcing.
- Tradeoffs: policy-based enforcement gives consistent, code-reviewed guardrails versus scattered hooks and human review; the cost is policy-authoring complexity (CEL, Rego, Kyverno syntax) and admission latency; the payoff is that every request is checked against the same rules, including ones from automation.
- Operational notes: test policies in CI, roll out in audit mode first, monitor admission latency and denial rates, and keep policies in git.
- RSIS3 relevance: RSIS3's loop pipelines can use the same pattern — mutate (default) and validate (guardrail) each artifact against invariants before persisting, with audit mode while rules are new.

## Related
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
