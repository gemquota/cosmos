---
type: "concept"
title: "hostPath & SubPath Volumes"
description: "Mounting host directories or volume subpaths into containers"
tags: ["hostpath", "subpath", "volumes", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# hostPath & SubPath Volumes

## Summary
hostPath mounts a node directory into a pod; subPath mounts a single file or directory from an existing volume. hostPath is powerful and dangerous — it breaks portability and can expose the node filesystem — while subPath solves the narrower problem of mounting one config file without hiding the rest of the volume.

## Details
- hostPath mechanics: `hostPath` volumes reference an absolute path on the node; types (DirectoryOrCreate, FileOrCreate) control creation; data persists on the node, so it survives pod restarts but not node loss; used for node agents, log directories, Docker sockets, and daemon-set workloads that genuinely need host access.
- subPath mechanics: with any volume (configMap, secret, PVC), `subPath` mounts one entry at a path instead of the whole volume, letting a pod mount e.g. `config.yaml` from a ConfigMap without the volume hiding an existing directory.
- Concrete example: a logging daemon-set mounts `/var/log` and `/var/lib/docker/containers` via hostPath; a web app mounts only `nginx.conf` from a ConfigMap with subPath so the container's other config files stay visible.
- Failure modes: hostPath with unrestricted node paths lets a compromised pod read the node's secrets (kubelet files, other containers' data) — never use it with untrusted workloads; node-affinity surprises — a pod using hostPath data lands on a different node and sees nothing; subPath mounts of ConfigMaps do not update on ConfigMap change (they are bind-mounted once), causing stale config; subPath with container-relative paths and ownership issues.
- Tradeoffs: hostPath gives low-latency, node-local storage and host access at the cost of portability, scheduler constraints, and security; subPath gives precise mounts but sacrifices the live-update behavior of full-volume ConfigMap mounts; prefer emptyDir and PVCs unless host access is genuinely required.
- Operational notes: restrict hostPath with policy (PodSecurity, OPA), document which nodes hold what data, and prefer FileOrCreate with explicit permissions.
- RSIS3 relevance: any host-mounted state in the cosmos deployment needs the same care — know which node owns it and what survives restarts.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
