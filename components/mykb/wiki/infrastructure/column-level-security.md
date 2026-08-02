---
type: "concept"
title: "Column-Level Security"
description: "Restricting which columns users can see"
tags: ["column-level-security", "masking", "access-control", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Column-Level Security

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Column security hides or restricts sensitive columns per role.
- Options: drop column, mask values, or deny access outright.
- Dynamic masking pairs naturally with column-level grants.
- Consistent policy across SQL, BI, and APIs is the hard part.

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — RBAC
- [[wiki/infrastructure/row-level-security|Row Level Security]] — row analog
- [[wiki/infrastructure/dynamic-data-masking|Dynamic Data Masking]] — masking
- [[wiki/infrastructure/data-classification-labels|Data Classification Labels]] — classification
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
