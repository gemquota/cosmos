---
type: "concept"
title: "LDAP"
description: "Directory access protocol for reading and searching identity, user, and group records"
tags: ["ldap", "directory", "identity", "authentication", "enterprise"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# LDAP

## Summary
LDAP (Lightweight Directory Access Protocol) reads and searches hierarchical directories — users, groups, org units. It underpins enterprise identity (Active Directory, OpenLDAP).

## Details
- Tree structure with DNs; binds authenticate users; searches filter by attributes.
- Often the source of truth that SSO/SAML layers federate.
- Modern stacks expose it via connectors; direct LDAP auth is legacy.

## Directory Model

An LDAP directory is a tree of entries. Each entry has a distinguished name (DN) built from relative names (RDNs), a set of attributes with defined syntaxes, and one or more object classes that dictate which attributes are allowed or required. Common object classes cover people, groups, organizational units, and devices, which is why directories map naturally to identity stores.

## Authentication and Search

- A bind operation authenticates a client with a DN and credentials; password policies, locking, and SASL mechanisms (GSSAPI, PLAIN, SCRAM) extend the basic flow.
- Searches start at a base DN and filter entries by attribute expressions with a scope (base, one level, or subtree).
- Results are limited by size and time limits, and access control determines which attributes a caller can read.

## Integration Notes

- SSO layers and connectors read from the directory as the identity source; write paths should go through governed processes.
- LDAP queries embedded in strings must be parameterized or filtered to avoid injection.
- TLS configuration matters: binds sent in plaintext expose credentials on the wire.

## Related

- [[wiki/security/sso|Single Sign-On]] — federates LDAP directories
- [[wiki/security/saml|SAML]] — assertion layer above LDAP
- [[wiki/security/rbac|RBAC]] — groups from directories
- [[wiki/security/zero-trust|Zero Trust Architecture]] — directory as identity source
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — query injection risks

## Related
- [[wiki/security/sso|Single Sign-On]] — federates LDAP directories
- [[wiki/security/saml|SAML]] — assertion layer above LDAP
- [[wiki/security/rbac|RBAC]] — groups from directories
- [[wiki/security/zero-trust|Zero Trust Architecture]] — directory as identity source
