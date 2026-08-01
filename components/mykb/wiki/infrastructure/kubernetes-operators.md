---
type: "concept"
title: "Kubernetes Operators"
description: "Controllers that encode application-specific operational knowledge as custom Kubernetes resources"
tags: ["kubernetes", "operators", "controllers", "crds", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kubernetes.io/docs/concepts/extend-kubernetes/operator/"]
---

# Kubernetes Operators

## Summary
A Kubernetes operator is a controller that encodes operational knowledge about an application as code, exposed through custom resources. It watches the cluster state and takes actions to converge reality toward the declared desired state — handling backups, upgrades, scaling, and failure recovery that humans used to do by hand. Operators are the standard way to run stateful software like databases on Kubernetes.

## Details
- Operators extend the Kubernetes API with Custom Resource Definitions (CRDs); users declare desired state in a custom resource, and the operator's control loop reconciles it.
- The pattern comes from CoreOS's 2016 work: combine the controller pattern with domain expertise about an application's lifecycle.
- Typical managed concerns: safe version upgrades, backup and restore, storage provisioning, certificate rotation, and day-2 failure recovery.
- Examples: Prometheus Operator manages scrape configs; etcd and database operators handle quorum and backups; cert-manager automates TLS certificates.
- Comparison with Helm: Helm installs and upgrades packaged resources, while an operator continuously reacts to state changes — they complement each other.
- Cost of adoption: operators are real software with versioning, RBAC, and upgrade paths; operators should be reused before being written, and written only for complex stateful applications.
- Relevance to mykb: an operator-style loop (desired state + reconcile + self-heal) mirrors the agent-loop pattern used in the agent systems cluster.

## Related
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]] — the primary use case for operators
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — the lifecycle primitives operators orchestrate
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the platform operators extend
- [[wiki/devops-infra/helm|Helm]] — packaging that complements operators
- [[wiki/security/rbac|RBAC]] — permissions operators need to reconcile
- [[wiki/security/secrets-management|Secrets Management]] — secret rotation often handled by operators
