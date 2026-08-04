---
type: "entity"
title: "Access Denied"
status: "growing"
description: "Access Denied"
tags: ["entity", "android", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---


## Access Denied

Access Denied appears in 1 session(s) categorized as API, Mobile, Security. Related topics: android, api, auth, authentication.

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/00-index|Auth Security › Access Denied

## Overview

Access Denied is the outcome when a request fails authorization: the identity was established, but the action is not permitted. In HTTP terms this is typically a 403 Forbidden, distinct from 401 Unauthorized, which signals missing or invalid credentials. Sessions categorized the term under API, Mobile, and Security, reflecting client-side handling of denied requests and the server-side rules that produce them.

## Implementation Notes

- Enforce authorization at the API boundary with role or attribute checks; never rely on hiding the UI alone.
- Return 403 for authenticated-but-forbidden requests and 401 when credentials are absent or invalid.
- Log denied attempts with enough context to investigate abuse without leaking sensitive details.
- Frontend UX should distinguish "sign in to continue" from "you lack permission" so users know the correct next step.

## Related Concepts

- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 401 vs 403 semantics
- [[wiki/security/rbac|RBAC]] — role-based permission rules
- [[wiki/security/abac|ABAC]] — attribute-based authorization for finer control
- [[wiki/security/zero-trust|Zero Trust]] — verifying authorization on every request


## Example

A mobile app requests a user's profile; the server returns 403 because the account lacks the clinician role. The client shows "Access denied — contact an administrator," refreshes permissions on next launch, and logs the attempt server-side for audit. This keeps the failure honest and actionable rather than a generic error.


## Related Concepts

- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — the credential checks preceding authorization
- [[wiki/security/password-hashing|Password Hashing]] — protecting credentials at rest


Consistent 403 handling across the API and client keeps authorization failures predictable for users and developers alike.


## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/abuseipdb-2|Abuseipdb 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ac-2|Ac 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ach-2|Ach 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/actionnode-2|Actionnode 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/addressfamily|Addressfamily
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/aec-2|Aec 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/agentconfig|Agentconfig
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/agentswitchrecord|Agentswitchrecord
