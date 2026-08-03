---
type: "concept"
title: "Registry GC & Retention"
description: "Reclaiming space and enforcing image retention policies"
tags: ["registry", "gc", "retention", "containers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Registry GC & Retention

## Summary
Registry garbage collection and retention manage the lifecycle of stored container images: GC removes unreferenced blobs from the registry store, and retention policies decide which tags and digests survive. Together they control disk cost, compliance, and the availability of old images for rollback.

## Details
- Mechanism: registries store images as manifests plus content-addressed blobs; GC scans for blobs not referenced by any manifest and deletes them (registry GC runs on a schedule or on demand); retention policies (Harbor, Nexus, ECR lifecycle rules) expire old tags by age, count, or regex, optionally keeping the most recent N per repository.
- Concrete example: a Harbor retention rule keeps the latest 10 production tags and 30 days of staging tags; nightly GC reclaims blobs orphaned by expired tags; an ECR lifecycle rule expires untagged images after 14 days; the rollback story depends on retention — a 30-day window means you can revert to any release in the last month.
- Failure modes: GC deleting blobs still referenced by in-flight pushes or by manifests in other repos (race conditions — GC during push); retention rules that delete the image a rollback needs; retention that keeps everything, ballooning cost; orphaned blobs accumulating when GC is misconfigured or disabled; deleting tags that security tooling or CI still references.
- Tradeoffs: aggressive retention cuts cost but shortens the rollback and forensic window; generous retention is cheap insurance but grows storage; the tradeoff should be explicit per repository tier — prod images retained longest, ephemeral builds pruned fast; GC and retention need the same discipline as database cleanup, not a one-time setup.
- Operational notes: schedule GC off-peak, monitor repository size, test rollback from the retention window, and audit retention rules as images change.
- RSIS3 relevance: cosmos's own image retention should keep enough history for rollback of the dashboard and daemon — the same rule as for any production artifact.

## Related
- [[wiki/cloud-infra/storage-locks-and-retention|Storage Locks & Retention]]
- [[wiki/infrastructure/confluent-cloud-and-schema-registry|Confluent Cloud And Schema Registry]]
- [[wiki/infrastructure/glue-schema-registry|Glue Schema Registry]]
- [[wiki/infrastructure/nacos-and-service-registry|Nacos And Service Registry]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
