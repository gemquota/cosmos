---
type: "concept"
title: "Privacy by Design"
description: "Engineering privacy protections into systems from the start rather than retrofitting them"
tags: ["privacy", "gdpr", "design", "data-protection"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://gdpr-info.eu/art-25-gdpr/"]
---

# Privacy by Design

## Summary

Privacy by design means building data-protection measures into systems at the architecture stage instead of bolting them on later. GDPR Article 25 makes it a legal duty: data protection by design and by default. The principles — data minimization, purpose limitation, transparency, user control, and default privacy — matter because retrofitting privacy after a breach is expensive and often impossible. For RSIS3, whose memory contains personal and sensitive knowledge, privacy-by-design is a load-bearing requirement of the memory system itself.

## Details

- GDPR Article 25: controllers must implement data-protection measures at design time and ensure that, by default, only necessary personal data is processed.
- Data minimization: collect and retain only what is needed; for a knowledge system this means pruning, expiry, and deletion pipelines are first-class features.
- Default privacy: privacy-friendly settings are the default (e.g. private by default, minimal disclosure), with opt-in for expansion.
- Mechanisms: pseudonymization, encryption, access controls, DPIA (data protection impact assessment) for high-risk processing, and documented records of processing.
- Transparency: users should be able to see what is stored about them and how it is used — provenance and audit trails serve this.
- For mykb, the memory layer's retention policy, classification labels, and access decisions are privacy-by-design artifacts, not add-ons.

## Related

- [[wiki/security-auth/data-classification|Data Classification]] — labels that drive minimization and access
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — GDPR and others codify privacy duties
- [[wiki/security-auth/zero-knowledge-proofs|Zero-Knowledge Proofs]] — proving facts without revealing data
- [[wiki/security-auth/audit-logging|Audit Logging]] — transparency about data access
- [[wiki/identity/breach-notification|Breach Notification]] — the failure-path duty under GDPR
- [[wiki/identity/device-fingerprinting|Device Fingerprinting]] — privacy impact of persistent device identifiers
- [[wiki/memory/provenance|Provenance]] — recording where knowledge came from
- [[wiki/concepts/triad-architecture|Triad Architecture]] — privacy controls across memory components
