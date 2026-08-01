---
type: "concept"
title: "Object Storage"
description: "Scalable storage for unstructured data addressed by keys, with high durability and S3-compatible APIs"
tags: ["object-storage", "s3", "storage", "data", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"]
---

# Object Storage

## Summary
Object storage keeps unstructured data — files, backups, media, model artifacts — as objects in flat namespaces with metadata, designed for massive scale and extreme durability. The S3 API became the de facto standard, with compatible implementations across clouds and self-hosted systems like MinIO. It is the default home for backups, archives, and content in cloud architectures.

## Details
- Model: buckets hold objects addressed by keys; each object carries content, metadata, and an ETag; there is no in-place editing, so updates replace objects.
- Durability and availability: object stores are engineered for 11-nines durability through replication and erasure coding across devices and facilities.
- Features: versioning (undo and protection), lifecycle policies (transition to cheaper tiers, expire), multipart upload for large objects, and server-side encryption.
- Presigned URLs grant time-limited access without exposing credentials — useful for uploads from browsers or agents.
- Comparison: block storage (attached disks, low latency, filesystems) and file storage (shared filesystems, NFS) differ from object storage's key-based model, high latency, and unlimited scale.
- Worked example: mykb can version its wiki JSON exports to an S3-compatible bucket with a 30-day retention and lifecycle transition to cold storage for archives.
- S3-compatible self-hosting (MinIO, Ceph RGW) provides the same API inside a private network for data-residency reasons.

## Related
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]] — moving objects between hot and cold tiers
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — cheap long-term object retention
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]] — point-in-time copies of data
- [[wiki/devops-infra/backups|Backups]] — object stores as the backup target
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — recovery semantics layered on storage
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]] — keying data by content hash
