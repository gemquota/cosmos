---
type: "concept"
title: "emptyDir & ConfigMap Volumes"
description: "Ephemeral and configuration volumes injected into pods"
tags: ["emptydir", "configmap", "volumes", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# emptyDir & ConfigMap Volumes

## Summary
emptyDir and ConfigMap volumes cover the ephemeral and configuration storage needs of pods: emptyDir gives a per-pod scratch volume that lives and dies with the pod, and ConfigMap volumes mount configuration as files that update when the ConfigMap changes. Together they cover most non-persistent storage needs without PVCs.

## Details
- emptyDir mechanics: a node-local directory created when the pod is scheduled, shared by all containers in the pod; medium: Memory backs it with tmpfs (fast, counts against memory limits, lost on restart); it dies with the pod — ideal for scratch space, caches, and inter-container handoff.
- ConfigMap mechanics: a ConfigMap volume mounts each key as a file; updates to the ConfigMap propagate to mounted files (with a kubelet sync delay); env-from and projected volumes extend the pattern; secrets use the same mechanism with more access controls.
- Concrete example: a pod with an app container and a log-shipper sidecar sharing an emptyDir for logs; an app mounting config.yaml from a ConfigMap and reacting to file changes (reload on inotify); a temporary render directory in tmpfs for fast disk.
- Failure modes: relying on emptyDir for anything that must survive restarts — it is per-pod, so node loss and pod deletion lose it; tmpfs usage exceeding memory limits causing OOM kills; ConfigMap updates not propagating to subPath mounts (bind-mounted once); expecting the filesystem to update instantly when kubelet syncs on a delay; large ConfigMaps (1MB default limit) or many mounts adding API overhead.
- Tradeoffs: emptyDir is simple and fast but ephemeral; ConfigMap volumes are declarative and updateable but eventual-consistency and limited in size; the alternative for durable data is PVCs, which trade complexity for persistence.
- Operational notes: choose the right storage class of ephemerality per need, and know the propagation semantics of each mount type.
- RSIS3 relevance: the wiki daemon's scratch and config needs map directly — ephemeral caches in emptyDir, config in ConfigMaps, durable data in PVCs.

## Related
- [[wiki/devops-infra/local-persistent-volumes|Local Persistent Volumes]]
- [[wiki/devops-infra/configmaps-and-secrets-rotation|ConfigMaps & Secrets Rotation]]
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
