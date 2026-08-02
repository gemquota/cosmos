---
type: "concept"
title: "Storage Tiering Automation"
description: "Moving data between hot, warm, and cold tiers automatically"
tags: ["tiering", "automation", "storage", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
  "https://cloud.google.com/storage/docs/storage-classes",
]
---

# Storage Tiering Automation

## Summary
Storage tiering moves data between hot, warm, and cold storage classes automatically as access patterns change. Lifecycle policies make the process declarative and auditable. Tiering is how object storage keeps costs proportional to access frequency.

## Details
- AWS S3 lifecycle rules transition objects between storage classes and expire them automatically after configured ages.
- Google Cloud defines storage classes with per-class pricing for access and retrieval.
- Tier transitions trade latency for cost: cold classes charge for retrieval and have slower first-byte times.
- Policy design should model real access patterns: recent data hot, quarterly snapshots warm, and compliance archives cold.
- Monitoring tier distribution reveals whether policies match real usage.
- In mykb, tiering connects to archive classes, lifecycle, and cost-of-storage articles in the cloud-infra cluster.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]]
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
