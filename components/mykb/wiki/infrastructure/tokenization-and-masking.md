---
type: "concept"
title: "Tokenization and Masking"
description: "Replacing sensitive values with tokens or masked forms that preserve usability"
tags: ["tokenization", "masking", "pii", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tokenization and Masking

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Tokenization substitutes a sensitive value with a random token stored in a secure vault; only the vault maps back.
- Masking (static or dynamic) obscures values for non-privileged users while keeping format and queryability.
- Dynamic data masking can apply at query time in warehouses, so raw data stays in one place.
- Both reduce PII exposure in dev/test environments and support privacy-by-design without breaking joins or analytics.

## Related

- [[wiki/security-auth/data-classification|Data Classification]] — classifying what must be tokenized
- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — privacy baked into data flows
- [[wiki/infrastructure/data-anonymization-techniques|Data Anonymization Techniques]] — irreversible de-identification
- [[wiki/infrastructure/data-encryption-at-rest|Data Encryption At Rest]] — encryption vs tokenization tradeoffs
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
