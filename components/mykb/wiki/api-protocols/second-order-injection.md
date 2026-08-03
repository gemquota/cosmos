---
type: "concept"
title: "Second-Order Injection"
description: "Payloads stored safely at write time but executed later at a different sink"
tags: ["security", "injection", "attacks", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Second-Order Injection

## Summary
Second-order injection is an attack where a payload is stored harmlessly at write time and only becomes dangerous later, when a different code path reads the stored value and uses it in an unsafe sink. Because the input looks benign at the moment it is accepted, the attack slips past input validation and is notoriously hard to find with naive scanners.

## Details
- Mechanism: the attack has two phases. Phase one is storage: an attacker submits a value that is safe in its original context, such as a username containing `'); DROP TABLE users;--` or a profile field containing `<img src=x onerror=alert(1)>`. The application parameterizes the first query correctly, so nothing breaks and the row is saved. Phase two is consumption: later, a different feature reads that stored value and interpolates it into a second query, an HTML template, a log line, or a shell command without context-appropriate escaping, and the payload executes.
- Concrete examples: a classic is the "poisoned username" bug where account creation is injection-proof but the admin audit page builds a query like `SELECT * FROM logs WHERE actor = '${name}'`, executing the stored payload. Others include stored XSS via comment bodies rendered inside an admin dashboard, CSV injection where exported cells beginning with `=` run formulas in Excel, and log injection where a username containing newlines forges fake log entries. The common thread is that the sink, not the source, is where the damage occurs.
- Failure modes: the worst failure is escaping at the first sink and assuming the data is then "clean" forever, which is exactly wrong: escaping is sink-specific, so a value that is safe in SQL is still dangerous in HTML, shell, or JSON. Whitelist-only validation at the boundary helps but cannot cover every future consumer, and the second consumer often has no knowledge that the data is attacker-influenced at all.
- Operational tradeoffs: the robust defense is output encoding at every sink (parameterized queries, HTML escaping, shell quoting) combined with treating all stored data as untrusted, plus data-flow awareness so teams can trace which fields flow into which sinks. Tools like static analysis and taint tracking help, but a practical discipline is: never concatenate stored values into queries, never render stored values into HTML without escaping, and validate the shape (not just the safety) of values at write time so consumers can rely on types.
- RSIS3/mykb relevance: MyKB stores arbitrary article content and metadata, and RSIS3 loops read that state back; the second-order principle says the memory layer must sanitize on read, at each render and export path, not just at ingest, so knowledge artifacts cannot turn into executable payloads downstream.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/blind-injection|Blind Injection]]
- [[wiki/api-protocols/header-injection|Header Injection]]
- [[wiki/api-protocols/crlf-injection|CRLF Injection]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
