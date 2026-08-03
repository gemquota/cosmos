---
type: "concept"
title: "Allowlist Validation"
description: "Accepting only explicitly permitted values and formats"
tags: ["validation", "input", "security", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Allowlist Validation

## Summary

Allowlist validation accepts only explicitly permitted values, types, and formats, rejecting everything else by default. It inverts the denylist mindset: instead of enumerating what is bad, it enumerates what is good and treats all unlisted input as suspicious.

## Details
- Mechanism: define the set of legal values at the boundary — an enum for categories, a regex for codes, a range for numbers, a maximum length for strings — and fail closed when input does not match. In HTML forms this pairs with pattern, min, max, and the select/option structure, but server-side validation must re-check whatever the client accepted.
- Concrete example: an API accepting a sort order field accepts only "asc" or "desc"; anything else returns 400 before touching the query builder. The same principle applies to content types, language tags, and redirect targets — every free-form field is a candidate for an allowlist.
- Failure modes: allowlists rot when legitimate values change (new ISO codes, new locales) and block valid traffic until updated; over-strict patterns reject legitimate inputs with confusing errors; and allowlists written against raw strings break when input arrives with different Unicode normalization or case, so normalize before comparing.
- Operational tradeoffs: allowlists are safer but more maintenance-heavy than denylists; they force explicit decisions about what the product supports, which is usually a feature, not a bug. Document the source of truth for each list and version it so audits can trace why a value is permitted.
- Distinguish validation from sanitization: validation rejects, sanitization rewrites. Rejecting is preferable for structured fields because rewriting hides the original input; use sanitization only where rejection is impractical, such as rich text.
- RSIS3/mykb relevance: the wiki's acquisition pipeline applies the same rule when ingesting notes — frontmatter types and tags are checked against known vocabularies before a synthesis is committed, and unknown tags are flagged rather than silently created.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/denylist-validation|Denylist Validation]]
- [[wiki/web-platforms/input-normalization|Input Normalization]]
- [[wiki/web-platforms/unicode-normalization|Unicode Normalization]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
