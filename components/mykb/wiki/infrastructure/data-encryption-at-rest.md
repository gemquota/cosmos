---
type: "concept"
title: "Data Encryption at Rest"
description: "Protecting stored data with encryption keys and envelope encryption"
tags: ["encryption", "security", "kms", "at-rest"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Encryption at Rest

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Encryption at rest protects files, tables, and backups from physical or unauthorized access to storage.
- Envelope encryption wraps data keys with a master key held in a KMS, enabling rotation without re-encrypting data.
- Layers: storage-level (S3/disk), table-level (TDE), column-level, and client-side encryption for high-sensitivity data.
- Key management, rotation, and access logging matter more than the cipher choice; escrow and compliance affect key custody.

## Related

- [[wiki/security-auth/tls-encryption|TLS Encryption]] — encryption in transit, the counterpart
- [[wiki/security-auth/data-classification|Data Classification]] — deciding what needs encryption
- [[wiki/infrastructure/tokenization-and-masking|Tokenization And Masking]] — alternatives for usable-but-protected data
- [[wiki/infrastructure/compliance-and-audit-trails|Compliance and Audit Trails]] — proving controls to auditors
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — key lifecycle management
