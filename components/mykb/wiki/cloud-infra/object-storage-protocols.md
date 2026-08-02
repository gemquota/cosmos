---
type: "concept"
title: "Object Storage Protocols"
description: "HTTP-based storage of immutable blobs with metadata"
tags: ["object-storage", "s3", "http", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html",
  "https://docs.ceph.com/en/latest/rados/",
]
---

# Object Storage Protocols

## Summary
Object storage stores immutable blobs addressed by key, with rich metadata and HTTP-based access. The S3 API became the de facto standard, implemented by AWS, GCP, MinIO, and Ceph. Object storage scales to exabytes and underpins data lakes and backups.

## Details
- Objects are stored flat in buckets; the key is the only addressing primitive, and listing is by key prefix.
- The S3 API defines GET/PUT/DELETE over HTTPS with ETags, multipart upload, and conditional requests.
- Durability comes from erasure coding or replication across devices and often across zones.
- Ceph's RADOS is the open-source foundation that object, block, and file protocols are built on.
- Lifecycle policies move objects to cheaper classes and expire old data automatically.
- In mykb, object storage connects to S3 lifecycle, archive classes, content hashing, and backup tooling.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/cloud-infra/object-storage|Object Storage]]
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
