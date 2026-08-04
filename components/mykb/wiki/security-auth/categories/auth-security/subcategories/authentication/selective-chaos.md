---
type: "entity"
title: "Selective Chaos"
description: "Referenced in session 75202bac"
tags: ["entity", "angular", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Selective Chaos

## Summary

Selective chaos is a testing and reliability practice in which controlled, targeted disruptions are injected into a system — deliberately failing specific components — to expose weaknesses before they cause real incidents. It is a restrained form of chaos engineering: instead of random broad disruption, the failures are chosen to probe known risk areas such as authentication dependencies. The practice matters because it turns reliability from an assumption into a tested property.

## Details

- **Entity record** — this page indexes "Selective Chaos" as an entity from an analyzed session whose tags point to authentication, Angular, API, and AST topics.
- **Definition** — selective chaos chooses the failure injection points deliberately, focusing on critical paths like login, token validation, or upstream APIs.
- **Contrast with full chaos** — full chaos engineering randomizes failures across the fleet; selective chaos limits blast radius for safer, more targeted learning.
- **Auth-focused probes** — failing an identity provider, revoking a signing key, or throttling a token endpoint tests whether fallbacks and error paths behave.
- **Game days** — teams run scheduled exercises that inject the selected failures while observers verify detection, recovery, and user impact.
- **Worked example** — a team selectively fails the session-validation service for a minute and confirms that users are re-authenticated cleanly instead of receiving broken sessions.
- **Failure modes** — injecting chaos into systems without monitoring or rollback plans, and running exercises without follow-up, wastes the value.
- **Practical relevance** — selective chaos complements unit and integration testing by validating runtime behavior under real conditions.
- **Relation to resilience** — the practice feeds incident response and reliability engineering, making recovery paths known before emergencies.
- **Best practice** — start with low-risk, high-value targets, measure everything, and document each experiment's outcome.

## Related

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/login|Login]] — a likely probe target
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/redirect|Redirect]] — sibling entity
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/memoryconfig|MemoryConfig]] — sibling entity
- [[wiki/security/tls|TLS]] — resilience of secure channels
- [[wiki/security/zero-trust|Zero Trust]] — architecture that survives failures
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detection during exercises

