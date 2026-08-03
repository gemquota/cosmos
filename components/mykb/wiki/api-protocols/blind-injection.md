---
type: "concept"
title: "Blind Injection"
description: "Injection attacks that infer success without visible output"
tags: ["security", "injection", "attacks", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Blind Injection

## Summary
Blind injection is an injection attack where the response doesn't echo the injected data, so the attacker infers success from timing, error differences, or out-of-band callbacks instead of visible output.

## Details
In classic SQL injection, the attacker sees the injected data reflected in the response — error messages or query results. In blind injection, the application suppresses output: the query result only affects control flow ("record found" versus "not found") or nothing visible at all. The attacker then recovers information bit by bit through boolean probes (true/false differences), time delays (SLEEP), or out-of-band exfiltration (DNS or HTTP callbacks to an attacker-controlled server).

The mechanism: boolean-based blind injection uses a probe like id=1 AND (SELECT SUBSTRING(secret,1,1))='a' — the page behaves differently for true versus false, so the attacker iterates characters. Time-based injection uses id=1; SELECT SLEEP(5) to confirm a predicate by delay. Out-of-band uses database functions that make the server resolve a hostname (LOAD_FILE, UTL_HTTP, xp_dirtree) containing the exfiltrated value: secret.a1b2.attacker.example.

Concrete example: a login endpoint does SELECT * FROM users WHERE name='<input>' and only reveals "invalid credentials" either way. An attacker probes ' OR '1'='1 — behavior differs, confirming injection — then uses boolean probes to dump the password hash one character at a time. Even "safe-looking" endpoints that return generic errors can be blind-injectable if the query is string-built.

Failure modes: blind injection is slower but fully general — any injectable query can be drained given enough requests, and automation (sqlmap) makes it cheap; time-based probes amplify into denial of service on shared databases; out-of-band probes require egress filtering that many networks lack; and generic error messages give false confidence, since they protect error-based but not blind extraction.

Operational tradeoffs: the durable fix is parameterized queries — input can never become SQL structure — plus strict input validation as defense in depth. Egress filtering, WAF rules on sleep and union patterns, and rate limits slow automated blind extraction but are not fixes. Detection focuses on query-shape anomalies and repeated predicate patterns in database logs.

RSIS3/mykb relevance: blind injection is a good worked example for RSIS3's security synthesis notes: the lesson is that hiding output is not a control, only parameterization is, and that principle transfers to all query-building code.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/header-injection|Header Injection]]
- [[wiki/api-protocols/crlf-injection|CRLF Injection]]
- [[wiki/api-protocols/response-splitting|Response Splitting]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
