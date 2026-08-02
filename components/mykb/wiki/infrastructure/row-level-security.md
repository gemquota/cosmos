---
type: "concept"
title: "Row-Level Security"
description: "Restricting which rows users can see"
tags: ["row-level-security", "security", "access-control", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Row-Level Security

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- RLS filters rows by the requesting user's attributes (region, team, tenant).
- Implementations: Postgres policies, warehouse dynamic filters, BI row security.
- Centralize policy in the semantic layer to avoid drift.
- Test RLS with simulated users; misconfig leaks data.

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — RBAC
- [[wiki/security-auth/least-privilege|Least Privilege]] — principle
- [[wiki/infrastructure/column-level-security|Column Level Security]] — column analog
- [[wiki/infrastructure/data-access-requests|Data Access Requests]] — access process
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
