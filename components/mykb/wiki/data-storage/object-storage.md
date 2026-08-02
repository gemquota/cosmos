---
type: "concept"
title: "Object Storage"
description: "S3-style blob stores with flat namespaces and metadata"
tags: ["object-storage", "s3", "blob-storage", "cloud-storage"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html", "https://min.io/docs/minio/container/index.html"]
---

# Object Storage

## Summary
Object storage stores data as discrete objects — a blob of bytes plus metadata and a unique key — in a flat namespace addressed over HTTP. Amazon S3, Azure Blob, Google Cloud Storage, and self-hosted MinIO provide the near-unlimited, durable, cheap storage that backs data lakes, backups, media, and application artifacts.

## Details
- **Objects, buckets, keys** — an object is the data plus system metadata (size, ETag, timestamps) and user metadata; objects live in buckets and are addressed by key, often a pseudo-path like `logs/2026/08/app.log`, with no real directory hierarchy.
- **The flat namespace** — there are no directories or filesystem semantics; clients use list and prefix operations to emulate folders, which keeps the namespace simple, massively parallel, and horizontally scalable.
- **Consistency and durability** — S3 now offers strong read-after-write consistency for all operations; durability comes from replication and erasure coding across devices (S3's 11 nines design, MinIO's erasure sets), not from filesystem RAID.
- **Features** — versioning, lifecycle transitions between storage classes, server-side encryption, bucket policies for access control, multipart uploads for large objects, and event notifications that feed downstream pipelines.
- **Access patterns** — REST/S3 API is the standard; range reads and multipart download serve media; direct-to-object uploads avoid app servers; object stores are the foundation of data lakes and the archive tier of database backups.
- **Trade-offs** — first-byte latency is higher than local disks or block storage, there is no in-place update (rewrite the object), and strong consistency historically lagged; for random-access OLTP, block or database storage remains better.

## Related
- [[wiki/data-storage/data-lake|Data Lake]] — object storage as the raw layer
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — durable off-site copies
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — hot/warm/cold classes
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — native lifecycle rules
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — query engines over objects
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event-driven object processing
