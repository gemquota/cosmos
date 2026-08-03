---
type: "concept"
title: "Data Residency & Locality"
description: "Where data physically lives and the laws that follow it"
tags: ["residency", "locality", "compliance", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Data Residency & Locality

## Summary

Data residency means keeping data in specific jurisdictions to satisfy law, compliance, or latency; locality means keeping it near compute. They overlap but answer different questions — where it may be, vs where it should be — and both shape architecture more than most features.

## Details
- Mechanism: residency constraints come from regulations (GDPR, Schrems II, country-specific data localization), contract, or policy; providers answer with region selection, data-classification controls, and residency commitments (which regions keep data in-country, where support/telemetry flows). Locality is an engineering trade: compute near data minimizes latency and transfer costs; regions far apart add RTT and egress bills.
- Concrete example: a European health app keeps PII in eu-central with backups in eu-west, disables cross-border replication, and routes support tooling through region-scoped access; a global analytics pipeline replicates only aggregates across regions while raw data stays in the region of origin; latency-critical auth caches replicate keys, not the whole dataset.
- Failure modes: assuming "region" equals residency (support access, logs, and metadata may leave the region); accidentally replicating data to other regions via misconfigured backups or CDNs; and latency designs that ignore residency, forcing round-trips to a far region. Residency and latency can conflict — a distributed team serving one region with mandatory local storage needs a real strategy.
- Operational tradeoffs: residency compliance costs redundancy options and speed; locality buys latency at data-architecture complexity. Document data classification per dataset, map it to region/residency commitments, and test that flows (logs, telemetry, vendor integrations) stay within the allowed boundaries.
- RSIS3/mykb relevance: the wiki's deployment is single-region with residency notes per dataset; this node is the checklist the loop consults before adding replication or third-party processing.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/infrastructure/data-plane-versus-control-plane|Data Plane vs Control Plane]]
- [[wiki/cloud-infra/data-archiving|Data Archiving]]
- [[wiki/infrastructure/data-deduplication-in-storage|Data Deduplication in Storage]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
