---
type: "concept"
title: "Data Archiving"
description: "Retaining data long-term for compliance, audit, or historical value with retrieval-friendly organization"
tags: ["archiving", "data", "retention", "compliance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Data Archiving

## Summary
Data archiving moves data that is no longer active but must be kept — records, logs, old versions — into cheap, durable storage with a clear retention and retrieval plan.

## Details
- Define retention by regulation and value, then automate deletion or transition at expiry.
- Archives need indexes and manifests; an unsearchable archive is a liability, not an asset.
- Encryption and access control still apply — archived data is a juicy target.
- Open question: how to keep decade-scale archives readable as formats and tools change.

## Related
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — the typical archive tier
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]] — moving data into archives
- [[wiki/cloud-infra/object-storage|Object Storage]] — durable home for archives
