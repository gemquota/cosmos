---
type: "concept"
title: "SQL Injection Prevention"
description: "Preventing attacker-controlled input from altering SQL queries"
tags: ["sqli", "injection", "databases", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"]
---

# SQL Injection Prevention

- SQL injection occurs when input is concatenated into queries, letting attackers read, modify, or drop data.
- Primary defense: parameterized queries / prepared statements; secondary: allowlists for identifiers and strict input validation.
- Stored procedures and ORMs reduce risk but are not automatic protection — dynamic queries still concatenate.
- For mykb: every query layer touching memory stores must use parameter binding, with SAST scanning for concatenation patterns.

## Related

- [[wiki/security-auth/command-injection|Command Injection]] — sibling injection into the OS
- [[wiki/api-services/sast|Static Application Security Testing]] — automated detection of injection patterns
- [[wiki/security-auth/audit-logging|Audit Logging]] — logging query failures for detection
- [[wiki/devops-infra/postgresql|PostgreSQL]] — parameterized access to the store
