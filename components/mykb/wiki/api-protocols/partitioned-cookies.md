---
type: "concept"
title: "Partitioned Cookies"
description: "CHIPS: cookies scoped to a top-level site to block cross-site tracking"
tags: ["http", "cookies", "privacy", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Partitioned Cookies

## Summary
Partitioned cookies (CHIPS — Cookies Having Independent Partitioned State) scope a cookie to the top-level site that set it, so the same third-party cookie from the same embed behaves differently on different top-level sites. The goal is to preserve embedded-site functionality while blocking cross-site tracking.

## Details
A partitioned cookie is set with the Partitioned attribute (plus Secure). The browser keys the cookie's storage by (top-level site, cookie origin): the same cookie domain gets separate jars per top-level site. A widget at widget.example reading cookie user_pref on site-a.example gets a different value than on site-b.example — and neither site's jar leaks to the other.

The mechanism: partitioning changes the cookie jar from a single per-domain store to a per-(site,domain) store. Requests from an embed include the partition's cookies; the embed cannot read another partition's. This preserves legitimate state (theme, session, embed preferences) without letting a third party join a user's identity across sites — the tracking use that third-party-cookie blocking targets. Partitioned cookies are the middle path between fully blocked third-party cookies and fully shared ones.

Concrete example: a chat widget embedded on many wikis sets a theme cookie. Without Partitioned, the widget's cookie follows the user across every site, enabling cross-site profiling; with Partitioned, each wiki sees only the cookie jar for its own top-level site, and the widget must re-learn the theme per site. Functionality survives; tracking does not.

Failure modes: Partitioned without Secure is rejected; cookies that legitimately need cross-site state (SSO iframes, federated auth) break when partitioned, so those flows need redesign; and mixing partitioned and non-partitioned cookies for the same name causes confusing jar selection. Legacy browsers ignore the attribute, silently returning to shared third-party cookies — a privacy regression users won't notice.

Operational tradeoffs: partitioning trades cross-site functionality for privacy; the migration cost is per-embed: audit which cookies genuinely need cross-site state and keep those (if acceptable) or move them into the top-level site's own domain. The baseline for new third-party embeds: Partitioned plus Secure, and never rely on third-party cookies for identity. Monitoring should detect jar-mismatch bugs (users seeing wrong state) after rollout.

RSIS3/mykb relevance: the dashboard embeds third-party widgets; documenting which cookies are partitioned and which are first-party keeps the privacy posture auditable in RSIS3's checks.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-site-requests|Cross-Site Requests]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-flags|Cookie Flags]] — related coverage in the same cluster
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
