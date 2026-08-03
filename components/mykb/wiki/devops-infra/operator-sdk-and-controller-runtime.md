---
type: "concept"
title: "Operator SDK & Controller Runtime"
description: "Tooling for scaffolding operators and reconciling resources"
tags: ["operator-sdk", "controller-runtime", "kubernetes", "operators"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Operator SDK & Controller Runtime

## Summary
Operator SDK and controller-runtime are the standard frameworks for building Kubernetes operators in Go: controller-runtime provides the reconciliation loop, client, cache, and manager; Operator SDK adds scaffolding, CRD generation, and packaging (scorecard, bundle formats). They turn the operator pattern into a well-trodden development path.

## Details
- Mechanism: a controller reconciles a custom resource — the manager wires informers and caches; Reconcile functions receive a request and return (result, error), and controller-runtime requeues on error or on specified intervals; kubebuilder/operator-sdk generate CRD Go types, deepcopy methods, and manifests from markers; webhooks (mutating/validating) register with the manager.
- Concrete example: a Postgres operator with a Cluster CRD; the controller creates a StatefulSet when the CR appears, updates status with conditions, and reconciles drift; admission webhooks validate spec changes; the bundle is packaged for OLM with scorecard tests.
- Failure modes: reconciliation that is not idempotent — re-running must converge, or retries stack resources; hot loops from status updates triggering more reconcile calls (requeue storms); caches going stale, acting on outdated cluster state; RBAC gaps where the operator lacks permission for the resources it manages, failing silently; CRD schema and code drift between versions.
- Tradeoffs: the frameworks handle the hard plumbing (watches, caches, leader election) so builders focus on logic, but they embed Go and controller patterns that are heavy for small teams; alternatives (Kopf for Python, Java operator SDK, shell operators) trade ecosystem for simplicity; the payoff is a production-grade operator with testing conventions.
- Operational notes: use envtest for integration tests, generate manifests in CI, and follow the rule of small reconcile loops with explicit requeue.
- RSIS3 relevance: if cosmos builds operator-style automation for its stateful services, controller-runtime discipline — idempotent reconcile, status reporting — is the same loop discipline RSIS3 applies to its own L1 action loop.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
