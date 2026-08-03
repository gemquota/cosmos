---
type: "concept"
title: "Data Encryption at Rest"
description: "Protecting stored data with encryption keys and envelope encryption"
tags: ["encryption", "security", "kms", "at-rest"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Encryption at Rest

## Summary

Encryption at rest protects files, tables, and backups from physical or unauthorized access to storage. The threat model is specific: someone who obtains the storage medium (a stolen disk, an unauthorized copy of a database file, a misconfigured bucket) must not be able to read the data. Encryption at rest is the control that makes stored data useless without the key — and its hard problem is key management, not cipher choice.

## Details

- Encryption at rest protects files, tables, and backups from physical or unauthorized access to storage. It defends against the storage-level threat model: media theft, discarded drives, cloud provider misconfiguration, and copies that escape the application's access control. It does not defend the application layer — if an application bug leaks data through a query, encryption at rest does not help — so it is one layer in a stack that includes application-level access control and encryption in transit.
- Envelope encryption wraps data keys with a master key held in a KMS, enabling rotation without re-encrypting data. The mechanism: each data object gets a unique data key (DEK); the DEK encrypts the data; and the DEK itself is encrypted with a master key (KEK) held in a hardware-backed key management service. To decrypt, the application fetches the wrapped DEK from storage, asks the KMS to unwrap it, and uses it briefly. The design payoff: rotating the master key (or revoking one) does not require re-encrypting any data — you re-wrap DEKs instead — and the KMS can enforce usage policies and audit every unwrap, making key access observable.
- Layers: storage-level (S3/disk), table-level (TDE), column-level, and client-side encryption for high-sensitivity data. Each layer sits at a different trust boundary: storage-level encryption (S3 SSE, disk encryption) protects against media theft but the provider can decrypt; TDE (transparent data encryption) protects database files and backups, decrypting in the DB engine's memory; column-level encryption protects specific columns (the data is encrypted in the database, decrypted in the application); client-side encryption keeps the plaintext in the application's trust domain entirely — the storage layer never sees unencrypted data. The rule: the more sensitive the data, the closer encryption should sit to the client.
- Key management, rotation, and access logging matter more than the cipher choice; escrow and compliance affect key custody. AES-256 is settled; the operational questions are who holds keys (cloud KMS vs self-managed vs HSM), how rotation works (automated, with old keys retained for old data), whether keys are escrowed (recovery vs losing the keys = losing the data), and how compliance requirements (data residency, key separation for multi-tenant systems) constrain custody.
- For mykb: the node is the at-rest counterpart to TLS (in transit), with tokenization/masking as the usable-data alternatives and audit trails proving the controls.

## Related

- [[wiki/security-auth/tls-encryption|TLS Encryption]] — encryption in transit, the counterpart
- [[wiki/security-auth/data-classification|Data Classification]] — deciding what needs encryption
- [[wiki/infrastructure/tokenization-and-masking|Tokenization And Masking]] — alternatives for usable-but-protected data
- [[wiki/infrastructure/compliance-and-audit-trails|Compliance and Audit Trails]] — proving controls to auditors
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — key lifecycle management
