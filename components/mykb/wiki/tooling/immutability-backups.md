---
type: "concept"
title: "Immutability Backups"
description: "Backups that cannot be altered or deleted, even by attackers or accidents"
tags: ["immutability", "backups", "security", "ransomware"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Immutability Backups

## Summary
Immutable backups enforce write-once semantics — object lock, WORM storage, air-gapped copies — so data cannot be encrypted or deleted by ransomware or a rogue process. They are the recovery guarantee for hostile environments.

## Details
- Object lock (S3/Object Lock, GCS bucket lock) enforces immutability for a fixed window.
- Immutability must survive admin compromise: separate credentials and air gaps matter.
- Plan the unlock path: truly immutable means you cannot free storage early either.
- mykb relevance: the wiki archive's immutable copies survive even a compromised sync host.

## Related
- [[wiki/cloud-infra/object-lock-and-worm|Object Lock and WORM]]
- [[wiki/tooling/backup-verification|Backup Verification]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/communities/checksums|Checksums]]
