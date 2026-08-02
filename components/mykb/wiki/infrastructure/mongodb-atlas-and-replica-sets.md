---
type: "concept"
title: "MongoDB Atlas and Replica Sets"
description: "Managed document database with automatic replication and failover"
tags: ["mongodb", "atlas", "replica-sets", "nosql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# MongoDB Atlas and Replica Sets

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A replica set is a primary plus secondaries; the primary takes writes and secondaries replicate via oplog.
- Atlas manages replica sets across AZs/regions, backups, monitoring, and scaling.
- Reads can be routed to secondaries for horizontal read scaling (with eventual-consistency caveats).
- Schema design (embedded vs referenced) drives performance more than cluster size.

## Related

- [[wiki/data-storage/document-stores|Document Stores]] — document model
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — replica set topology roots
- [[wiki/data-storage/mongodb-data-modeling|Mongodb Data Modeling]] — modeling for MongoDB
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — secondary reads
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
