---
type: "concept"
title: "ConfigMaps & Secrets Rotation"
description: "Injecting and rotating Kubernetes configuration and secrets"
tags: ["configmap", "secrets", "rotation", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ConfigMaps & Secrets Rotation

## Summary
Kubernetes ConfigMaps and Secrets deliver configuration and sensitive data to pods; rotation is the process of replacing values, or the whole object, safely. The hard part is that pods hold mounted values in memory, so rotation must trigger a reload or restart — and secret rotation has the extra failure mode of breaking running workloads when keys change unexpectedly.

## Details
- Mechanisms: update the object and rely on mounted-volume updates — files mounted under `subPath` update only on restart while regular files update in place; or use a reloader (Stakater Reloader, Reloader) that watches ConfigMap and Secret changes and rolls the Deployment; or bake config into images, which is worst for secrets.
- Concrete example: a credentials Secret mounted as a volume; rotation updates the Secret with a new API key; the reloader detects the change and triggers a rolling restart so pods pick up the new value. A safer variant writes a new Secret under a new name, flips the Deployment reference, then deletes the old object.
- Failure modes: partial rollout — old and new pods run different keys during a rolling restart, so consumers must tolerate both briefly; a race between secret update and pod restart leaving pods with tokens that invalidate mid-request; `secretKeyRef` environment values never update without restart, so an operator who only edits the object thinks rotation worked while pods keep the old value; deleting a Secret still referenced by pods breaks them with confusing errors.
- Tradeoffs: restart-based rotation is simple and robust but causes availability blips and connection churn; name-versioned secrets avoid restarts but accumulate objects and need cleanup; external secret operators (External Secrets Operator, Vault agent) keep secrets in one place and push rotations with controlled timing.
- Operational notes: rotate on a schedule and after compromise, test in staging first, keep a rollback path where the previous key remains valid for a grace window, and audit secret metadata without ever logging values.
- RSIS3 relevance: MyKB daemon credentials and API tokens follow the same lifecycle — rotation planning belongs in the operational playbook and the policy notes belong in mykb.

## Related
- [[wiki/devops-infra/secrets-management-revisited|Secrets Management]]
- [[wiki/devops-infra/volumes-emptydir-and-configmaps|emptyDir & ConfigMap Volumes]]
- [[wiki/infrastructure/secret-rotation|Secret Rotation]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
