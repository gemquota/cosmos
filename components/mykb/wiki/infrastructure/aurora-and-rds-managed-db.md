---
type: "concept"
title: "Aurora and RDS Managed Databases"
description: "AWS managed relational databases with replication, failover, and scaling"
tags: ["aurora", "rds", "aws", "managed-db"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Aurora and RDS Managed Databases

## Summary

AWS RDS and Aurora are managed relational database services that remove the operational burden of running databases yourself. The core value proposition is the same for both — provisioning, patching, backups, and failover are automated — but Aurora adds a distributed storage architecture designed to solve the scaling and availability ceilings of a single-instance database.

## Details

- RDS automates provisioning, patching, backups, and failover for MySQL, Postgres, SQL Server, and more. The operator picks an engine and instance class; the service handles the rest: automatic backups with point-in-time recovery, maintenance windows for patching, Multi-AZ replication for failover, and managed monitoring. The tradeoff is control: you get the database, not the host — no SSH to the server, no custom kernel modules, and performance tuning is limited to what the service exposes. RDS is the right answer when the database is a dependency, not the product.
- Aurora uses a distributed storage layer replicated six ways across AZs with fast failover. The architectural break with RDS: Aurora separates compute from storage. The storage tier is a cluster of nodes that replicate each 10GB segment six times across three availability zones, and the database engine writes only to the cluster's quorum — so a writer failure fails over in tens of seconds without crash recovery or log replay, because the storage layer already holds the durable state. This is why Aurora's failover is dramatically faster than RDS Multi-AZ's standby promotion: there is no cold standby to promote, just a new writer attaching to the same storage.
- Aurora Serverless v2 scales capacity in fractional increments for variable workloads. Where provisioned Aurora has fixed instance sizes, Serverless v2 adjusts capacity continuously (in fractions of an ACU) based on load, which fits spiky or unpredictable workloads that would otherwise pay for idle capacity. The tradeoff: capacity changes take tens of seconds, and you pay a premium per unit of capacity versus provisioned instances, so the choice is a cost-modeling decision.
- Managed services trade some control for operational simplicity and built-in high availability. The decision framework: if you need exotic engine features, kernel-level control, or maximum cost optimization, self-managed or raw RDS may fit; if you need reliability without the operations team, Aurora's storage-replicated design is hard to beat.
- For mykb: this is the reference node for the managed-db branch of the data-storage cluster, connecting replication, backup, and migration concepts to a concrete AWS implementation.


## Related
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — replication under the hood
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — automated backups
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — Aurora read scaling
- [[wiki/data-storage/zero-downtime-migrations|Zero Downtime Migrations]] — moving workloads onto RDS
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
