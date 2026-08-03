---
type: "concept"
title: "Coldline & Archive Storage Classes"
description: "Low-cost access patterns for rarely read data"
tags: ["coldline", "archive", "storage", "gcp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Coldline & Archive Storage Classes

## Summary

Coldline (GCP), Archive (GCP), and the equivalent cold classes on AWS/Azure are storage tiers for data accessed rarely: low storage cost, retrieval fees, and latency. They are for compliance archives, backups, and media masters — not for data someone will page you about.

## Details
- Mechanism: GCP coldline targets data accessed less than once a quarter, archive less than once a year; both charge per-GB storage with retrieval fees (per GB and per operation) and minimum storage durations (30/90/365 days); objects are synchronously retrievable (unlike some glacier classes) but reads cost more than hot/coldline. AWS Glacier Instant vs Flexible vs Deep Archive and Azure archive tier map to the same trade.
- Concrete example: 5TB of legal holds in Archive at ~$0.004/GB-month vs ~$0.02 hot — a 5x saving on the dominant cost — with a documented restore procedure for e-discovery; database backups move to coldline after 30 days via lifecycle rules, keeping the last week hot for DR drills.
- Failure modes: restoring frequently from archive (retrieval fees dwarf the storage savings); lifecycle rules moving objects before the minimum duration (early-deletion charges); access patterns changing (a "cold" bucket that analytics reads weekly is over-tiered); and applications assuming instant access to archived objects.
- Operational tradeoffs: tier by measured access frequency and restore RTO requirements; coldline is a safe default for quarterly-recovery data, archive for yearly; automation (lifecycle policies) beats manual tiering, and restore-time/cost should be tested annually, not assumed.
- RSIS3/mykb relevance: the wiki's backup tiers would be documented with access telemetry, so the loop's retention reviews move tiers based on real restore patterns.
- Restore rehearsal: test archive restore end-to-end annually with a representative object; the retrieval path is the part of the design nobody verifies until it is urgent. Include the e-discovery workflow in the rehearsal so legal deadlines are not the first test.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
