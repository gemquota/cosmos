---
type: "concept"
title: "API Deprecation"
description: "Deprecation policy, Sunset header, and migration windows"
tags: ["api-design", "deprecation", "lifecycle", "sunset", "versioning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc8594", "https://stripe.com/blog/deprecation-api"]
---

# API Deprecation

## Summary
Deprecation is the managed retirement of API behavior: mark it, announce it, keep it working for a migration window, then remove it. The Sunset header (RFC 8594) tells clients when a response is slated for removal, turning an operational decision into a machine-readable signal.

## Details
- Policy: define deprecation up front — minimum notice period, removal criteria, and who is notified (usually: announce, mark deprecated, keep N months, then remove).
- Signals: OpenAPI deprecated: true on fields/operations, a Deprecation header or response header, documentation banners, and changelog entries.
- Sunset header: Sunset: Sat, 31 Jan 2027 23:59:59 GMT declares the removal date; RFC 8594 also defines the Link header to a deprecation policy or replacement endpoint.
- Grace and migration: keep deprecated endpoints serving during the window, log usage of deprecated paths, and share migration guides with high-traffic consumers.
- Measuring: track deprecation header hits in analytics; only remove when usage drops below a threshold, not on a calendar alone.
- Hard removal: 410 Gone (or 404) with a clear error body and a link to the replacement; keep the error shape documented for years.
- Anti-pattern: silent removal — clients break in production with no notice, eroding trust in the platform.

## Related
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — deprecation is the exit from compatibility
- [[wiki/api-protocols/semver-for-apis|SemVer for APIs]] — deprecation windows precede breaking majors
- [[wiki/api-protocols/api-analytics|API Analytics]] — usage metrics decide when to remove
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 410 Gone signals intentional removal
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — deprecation errors stay structured
