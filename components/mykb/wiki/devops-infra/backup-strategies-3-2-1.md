---
type: "concept"
title: "Backup Strategies: 3-2-1"
description: "Three copies on two media with one offsite for resilience"
tags: ["backup", "3-2-1", "resilience", "recovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Backup Strategies: 3-2-1

## Summary
The 3-2-1 rule: keep at least three copies of the data, on two different media types, with one copy offsite. It defends against the independent failure classes that destroy single copies: hardware loss, media corruption, and site-level disasters such as fire, flood, or ransomware that encrypts every local copy.

## Details
- The three copies are the live data plus two backups (counting the working copy); the two media classes mean, for example, local disk plus object storage or tape, so a controller failure or filesystem bug does not take out both; the offsite copy survives loss of the whole building or region.
- Concrete example: a production Postgres cluster writes daily full backups to local disk and to S3-compatible object storage in another region, with WAL archiving streamed continuously; restoring to a fresh VM pulls from the offsite copy so a data-center outage does not block recovery.
- Failure modes: the rule is a minimum, not a guarantee — backups that are never restored are suspect (silent corruption, missing files, wrong retention); a backup on the same SAN as the primary defeats the two-media intent; an offsite copy in the same cloud account can be deleted by the same compromised credentials, which is why ransomware guidance adds immutable or air-gapped copies and the 3-2-1-1 variant with an offline copy.
- Tradeoffs: more copies cost storage, bandwidth, and restore-testing time; the real measures are RTO and RPO, so tune frequency (RPO) and restore speed (RTO) per data tier rather than giving everything three hourly copies.
- Operational notes: automate restores — a periodic restore drill is worth more than an extra copy — monitor backup success and staleness, and treat the backup catalog itself as critical data.
- RSIS3/mykb relevance: the wiki is git-versioned markdown, so repo plus remote mirror plus periodic export archive would be a natural 3-2-1; RSIS3's own state files should follow the same rule because loop evolution is worthless if the state that produced it is unrecoverable.

## Related
- [[wiki/devops-infra/cache-invalidation-strategies|Cache Invalidation Strategies]]
- [[wiki/devops-infra/backup-tools-restic-borg|Backup Tools: restic & Borg]]
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]]
- [[wiki/devops-infra/progressive-sync-strategies|Progressive Sync Strategies]]
