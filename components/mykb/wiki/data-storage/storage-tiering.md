---
type: "concept"
title: "Storage Tiering"
description: "Hot/warm/cold placement across storage media"
tags: ["storage-tiering", "tiered-storage", "cost-optimization", "data-lifecycle"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html", "https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview"]
---

# Storage Tiering

## Summary
Storage tiering places data on the medium that matches its access frequency: hot data on fast, expensive storage; warm and cold data on slower, cheaper tiers. Because storage cost scales steeply with performance, tiering is the main lever for keeping large datasets affordable without sacrificing hot-path latency.

## Details
- **The tier spectrum** — hot tiers (SSD/NVMe, in-memory) serve interactive traffic; warm tiers (HDD, standard object storage) hold monthly or quarterly data; cold/archive tiers (tape, Glacier-style object classes) store rarely read data at a fraction of the cost, with retrieval taking minutes to hours.
- **Object-storage tiering** — S3 storage classes and Azure Blob access tiers formalize the spectrum (Standard, Standard-IA, One Zone-IA, Glacier Instant/ Flexible/Deep Archive); lifecycle policies move objects automatically by age, and retrieval costs and minimum durations make each tier a real trade.
- **Database tiering** — databases tier by partition or tablespace: recent partitions on fast disks, old partitions on cheaper volume classes or archived entirely; engines like TimescaleDB and ClickHouse automate time-based tiering, and hybrid buffer pools (PostgreSQL, MySQL, SQL Server) extend cache with slower-but-cheaper memory.
- **Automatic vs manual** — automatic tiering (S3 Intelligent-Tiering, OS page migration between memory tiers) adapts to access patterns; manual tiering gives control but needs governance, or data lands in the wrong tier and costs spike.
- **Data lifecycle integration** — tiering pairs with retention: as data ages it moves down tiers, then expires; monitoring tier distribution and retrieval costs catches misclassification before it inflates the bill.
- **Design guidance** — classify data by access frequency and RPO/RTO needs before choosing tiers; keep metadata hot even when blobs are cold so catalogs stay fast.

## Related
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — policies that drive tier moves
- [[wiki/data-storage/object-storage|Object Storage]] — where tiering is native
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — the classic tiered workload
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — tiering by partition
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — archive tiers for copies
- [[wiki/data-storage/rpo-and-rto|RPO and RTO]] — cold-tier retrieval constraints
