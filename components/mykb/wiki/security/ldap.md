---
type: "concept"
title: "LDAP"
description: "Directory access protocol for reading and searching identity, user, and group records"
tags: ["ldap", "directory", "identity", "authentication", "enterprise"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# LDAP

## Summary
LDAP (Lightweight Directory Access Protocol) reads and searches hierarchical directories — users, groups, org units. It underpins enterprise identity (Active Directory, OpenLDAP).

## Details
- Tree structure with DNs; binds authenticate users; searches filter by attributes.
- Often the source of truth that SSO/SAML layers federate.
- Modern stacks expose it via connectors; direct LDAP auth is legacy.

## Related
- [[wiki/security/sso|Single Sign-On]] — federates LDAP directories
- [[wiki/security/saml|SAML]] — assertion layer above LDAP
- [[wiki/security/rbac|RBAC]] — groups from directories
- [[wiki/security/zero-trust|Zero Trust Architecture]] — directory as identity source
