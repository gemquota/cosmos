---
type: "concept"
title: "Dynamic Data Masking"
description: "Masking sensitive values at query time"
tags: ["masking", "dynamic-masking", "security", "pii"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dynamic Data Masking

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- DDM applies masking rules when queries return sensitive columns.
- Rules can vary by role: full value for admins, masked for support.
- Masking functions: partial, hash, null, or format-preserving.
- It is defense-in-depth, not a substitute for access control.

## Related

- [[wiki/security-auth/data-classification|Data Classification]] — classification
- [[wiki/infrastructure/column-level-security|Column-Level Security]] — column security
- [[wiki/infrastructure/tokenization-and-masking|Tokenization And Masking]] — masking family
- [[wiki/infrastructure/data-classification-labels|Data Classification Labels]] — labels
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
