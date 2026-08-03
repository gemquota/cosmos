---
type: "concept"
title: "OS Updates & Immutable Images"
description: "Replacing immutable images instead of mutating running systems"
tags: ["immutable", "os-updates", "images", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# OS Updates & Immutable Images

## Summary
OS update strategy is the decision between patching in place and rebuilding: mutable servers get incremental package updates, while immutable images are rebuilt and replaced wholesale. Immutable images trade update speed and flexibility for reproducibility, consistency, and the elimination of config drift.

## Details
- Mutable updates: package managers (apt, dnf) apply patches to running systems; fast and surgical but accumulate drift — servers differ by update history, and a patch can behave differently on each one; rollback is hard once packages are upgraded.
- Immutable updates: the image (golden image, container, CoreOS-style) is rebuilt with new packages, tested, and rolled out by replacing instances; every server is identical; rollback is redeploying the previous image; the cost is a rebuild cycle for every patch.
- Concrete example: a fleet of CoreOS nodes that never patch in place — the team bakes updates quarterly and rolls new images; a containerized workload updates by building a new image and rolling the Deployment; a mutable fleet scripts `apt upgrade` nightly, with drift checks.
- Failure modes: in-place patching breaking services because a library changed behavior; images that are never rebuilt, accumulating known CVEs (scan and alert on image age); the rebuild pipeline failing silently, stalling all updates; mutable servers that reboot into half-patched states; golden images so stale that new instances boot with old certificates or config.
- Tradeoffs: immutable is the modern default for workloads because it makes state reproducible, but stateful data must live outside the image; mutable remains pragmatic for pets and legacy; the hybrid pattern is immutable OS plus containerized workloads, patching only the host rarely.
- Operational notes: track image age and CVE exposure, test image builds in CI, and rehearse the rollback path.
- RSIS3 relevance: cosmos's dashboard and daemon should ship as immutable artifacts — rebuild, test, promote — so RSIS3 never debugs an instance whose state drifted from the build.

## Related
- [[wiki/devops-infra/container-images-oci|Container Images (OCI)]] — related coverage in the same cluster
- [[wiki/os-shell/immutable-filesystems|Immutable Filesystems]] — related coverage in the same cluster
- [[wiki/devops-infra/renovate-and-dependency-updates|Renovate & Dependency Updates]] — related coverage in the same cluster
- [[wiki/infrastructure/immutable-infrastructure|Immutable Infrastructure]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
