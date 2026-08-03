---
type: "concept"
title: "Re-platforming"
description: "Migrating with targeted upgrades to managed services without rewriting application code"
tags: ["migration", "replatform", "managed-services", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Re-platforming

## Summary

Re-platforming (lift-and-reshape) moves workloads with moderate changes to exploit cloud-native services — managed databases instead of self-hosted, containers instead of VMs, serverless where fits — capturing cost and operational benefits without a full rewrite. It is the migration sweet spot between lift-and-shift and refactor.

## Details
- Mechanism: per-component decisions replace infrastructure with managed equivalents: RDS/Aurora for self-managed MySQL, EKS/Fargate for EC2 fleets, S3 for NFS shares, queues for point-to-point integration, autoscaling for fixed capacity. Each swap changes failure modes, licensing, and operational surface.
- Concrete example: a self-hosted Postgres on a big VM becomes RDS with automated backups and failover — same SQL, less pager duty; a cron-driven batch server becomes a containerized job on ECS with managed scheduling; an FTP-based file exchange becomes S3 with presigned URLs. The workload's code mostly survives; its ops model does not.
- Failure modes: re-platforming without re-testing failure modes (managed DB failovers behave differently than manual ones); keeping on-prem config habits (IP-based connections, fixed capacity) that fight managed services; licensing traps (BYOL software that does not fit the new shape); and treating re-platforming as one big cutover instead of per-component with rollback.
- Operational tradeoffs: re-platforming captures most cloud benefits at moderate effort; the trade is dependency on managed services and their pricing/limits. Sequence components by risk, keep each swap reversible, and measure cost/operability before and after.
- RSIS3/mykb relevance: the wiki's migration roadmap sequences re-platforming per service with before/after metrics, so the loop's recommendations stay evidence-based.
- Data migration: re-platforming databases needs cutover tooling (logical replication, dual-writes) and rollback snapshots; test the cutover repeatedly until it is boring.
- Contract review: managed services change SLAs, backup semantics, and support paths; review these per component before committing the migration budget.

## Related
- [[wiki/infrastructure/containerization|Containerization]] — replatforming destination for VM apps
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]] — the strategy family it belongs to
- [[wiki/cloud-infra/lift-and-shift|Lift-and-Shift]] — the minimal-change alternative
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local container replatforming
