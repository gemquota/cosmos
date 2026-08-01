---
type: "concept"
title: "LDAP Injection"
description: "Injection into LDAP queries that alters directory lookups and access decisions"
tags: ["ldap", "injection", "directories", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/attacks/LDAP_Injection"]
---

# LDAP Injection

- LDAP injection modifies LDAP filter strings built from user input, potentially bypassing authentication or extracting directory data.
- Prevention: escape LDAP special characters (RFC 4515), use parameterized bind/search APIs, and validate input strictly.
- The risk is highest in login forms that build filters like (uid=<input>) or (cn=<input>).
- For mykb: any directory integration should use SDK query builders and never string-concatenate filters.

## Related

- [[wiki/security/ldap|LDAP]] — the directory protocol being injected
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — same class of injection flaw
- [[wiki/identity/identity-providers|Identity Providers]] — IdPs often bind to directories
- [[wiki/security-auth/xml-external-entities|XML External Entities]] — related parser-injection family
