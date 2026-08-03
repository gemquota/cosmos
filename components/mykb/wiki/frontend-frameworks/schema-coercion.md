---
type: "concept"
title: "Schema Coercion"
description: "Casting raw input to typed values during validation"
tags: ["validation", "schemas", "types", "coercion"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Schema Coercion

## Summary
Schema coercion is the casting of raw input — almost always strings from forms, query parameters, or JSON — into typed values during validation: `"42"` to `42`, `"true"` to `true`, `"2026-08-03"` to a `Date`. Zod, Yup, and similar libraries do this inside their schemas, and the practice question is how aggressive to be: coercion that is too eager masks client bugs, while no coercion at all makes every form a type-error minefield.

## Details
- Mechanism: schema libraries chain a type check with a transformation: Zod's `z.coerce.number()` (or `z.number({ coerce: true })` in older versions) parses the string and produces a number, Yup casts during validation, and TypeScript types are inferred from the same schema so the parsed value's type is known statically. Coercion runs after the raw value passes shape checks and before strict type validation, so `" 42 "` may trim and parse, `"42abc"` fails, and `""` has configurable behavior (often becoming `NaN` or failing). Because coercion is lossy and order-dependent, the schema's declared types become the contract for what the app actually receives.
- Concrete examples: a search form submits `?limit=20&page=2` as strings; coercing to numbers prevents `"20" + 1 === "201"` bugs downstream. A checkbox payload `"on"`/`"true"`/`"false"` coerced to a boolean; a date input `"2026-08-03"` coerced to a `Date` (with timezone pitfalls — date-only strings parse as UTC, timestamps as local); an API gateway that coerces header strings (`X-Retry-After: "120"`) before passing to a retry scheduler.
- Failure modes: the classic failure is over-eager coercion masking real bugs — `z.coerce.number()` turning a `null`-or-empty string into `0` silently corrupts data; locale-dependent parsing (`"1,5"` in some locales) produces surprises; and date coercion's timezone handling is a permanent source of off-by-one-day bugs. Coercing before validation can also bypass type checks that were the point of the schema, and schemas that coerce by default make strict-mode audits impossible.
- Operational tradeoffs: the safe pattern is explicit coercion: declare input types strictly (reject mismatches), then transform at a named boundary (`z.string().transform(Number)` or `z.coerce.number()` used deliberately), so coercion is visible in the schema rather than implicit. Trimming, defaults, and number parsing should be written down, not assumed. The tradeoff is ergonomics versus strictness: permissive coercion makes forms and query strings painless but hides errors; strict schemas surface every mismatch but demand discipline from callers. For API boundaries, strict is safer; for user-facing forms, targeted coercion with defaults is pragmatic.
- RSIS3/mykb relevance: the daemon's search and filter parameters arrive as strings; coercing them through explicit schemas at the API boundary (with types inferred for the UI) prevents the class of bugs where "page 2" becomes "201", mirroring RSIS3's rule that input validation is explicit and typed at every trust boundary.

## Related
- [[wiki/web-platforms/forms-practice|Forms in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/form-libraries|Form Libraries]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/react-hook-form|React Hook Form]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/yup-schemas|Yup Schemas]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
