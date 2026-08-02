---
type: "concept"
title: "Local Persistent Volumes"
description: "Node-local storage with static binding for low-latency workloads"
tags: ["local-pv", "storage", "kubernetes", "node"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Local Persistent Volumes

## Summary
Node-local storage with static binding for low-latency workloads. This stub frames the concept and its place in the mykb Systems & Infrastructure cluster; expand it into a full article with worked examples, failure modes, and verified sources.

## Details
- Definition anchor: Node-local storage with static binding for low-latency workloads.
- Open questions: how this interacts with adjacent delivery, reliability, and Kubernetes operations topics, the failure modes that matter, and the operational tradeoffs to document.
- Ties to RSIS3/mykb: keeping this node discoverable makes it easier to surface from related protocols and tooling during retrieval.
- Next step: verify sources and promote to a growing article with protocol or configuration detail.

## Related
- [[wiki/cloud-infra/ipv6-link-local-addresses|IPv6 Link-Local Addresses]] — related coverage in the same cluster
- [[wiki/devops-infra/persistent-volume-claims|Persistent Volume Claims]] — related coverage in the same cluster
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]] — related coverage in the same cluster
- [[wiki/devops-infra/volumes-emptydir-and-configmaps|emptyDir & ConfigMap Volumes]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
