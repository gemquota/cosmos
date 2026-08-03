---
type: "concept"
title: "SQL Injection"
description: "Injection of SQL through unsanitized input into dynamically built queries"
tags: ["security", "injection", "sql", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SQL Injection

## Summary
SQL injection is the injection of SQL syntax through unsanitized input into dynamically built queries, letting an attacker read, modify, or destroy data the application never intended to expose. It is the most studied web vulnerability in existence, and the defense is now mechanical: never concatenate user input into SQL, always bind parameters.

## Details
- Mechanism: when a query is built by string interpolation such as `SELECT * FROM users WHERE name = '" + name + "'`, an input like `' OR '1'='1` changes the query's logic, and stacked or union payloads can read other tables, write rows, or call functions. Prepared statements and parameterized queries send the SQL skeleton and the data as separate channels, so the database engine can never confuse a value with syntax, closing the vulnerability at the API boundary regardless of the input's content.
- Concrete examples: a login form bypassed with `' OR 1=1 --`; a search box exfiltrating the whole users table via `UNION SELECT`; an order-by parameter that becomes `ORDER BY (SELECT ...)` for blind time-based extraction; an ORM whose `.order_by()` or `.raw()` accepts a string built from a request parameter, which is exactly how injection sneaks back past otherwise-safe frameworks.
- Failure modes: the most common reintroduction paths are raw query fragments, dynamic identifiers (table names, column names, sort keys) that cannot be parameterized, and stored procedures that build SQL internally from parameters. ORMs protect the common cases but are not a magic shield: raw SQL, `LIKE` escaping done by hand, and JSON/array operators all bypass the safe path. Blind injection (boolean- or time-based) is slower but just as damaging, and it often survives scanners because no error text is returned.
- Operational tradeoffs: parameterized queries cost nothing measurable at modern database scales, so there is no performance excuse; the real cost is in identifier handling, where you must validate against an allowlist instead of interpolating, and in legacy code where refactoring every concatenation is a slow, risky migration. Layered defenses help: least-privilege database roles, query timeouts, WAF rules for known payload shapes, and alerting on unusual query patterns.
- RSIS3/mykb relevance: MyKB's TF-IDF search and knowledge graph queries are built from user search text; keeping those queries parameterized is a standing invariant, and RSIS3 loop hygiene should treat any dynamic SQL construction as a review flag, since memory-layer compromise corrupts everything that reads it.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/xml-injection|XML Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/nosql-injection|NoSQL Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/second-order-injection|Second-Order Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
