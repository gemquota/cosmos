---
type: "concept"
title: "SQL Injection"
description: "Injection of SQL through unsanitized input into dynamically built queries"
tags: ["security", "injection", "sql", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# SQL Injection

## Summary
Injection of SQL through unsanitized input into dynamically built queries. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Parameterized queries and prepared statements eliminate SQL injection at the API boundary
- ORM raw queries and dynamic identifiers reintroduce it
- Open question — how do query builders keep identifiers safe?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/xml-injection|XML Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/nosql-injection|NoSQL Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/second-order-injection|Second-Order Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
