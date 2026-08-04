---
type: "entity"
title: "Yup Schemas"
description: "Declarative object schema validation for forms and payloads"
tags: ["yup", "validation", "schemas", "forms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Yup Schemas

## Summary
Yup is a JavaScript schema validation library that describes object shapes and their rules declaratively: `yup.object({ email: yup.string().email().required() })` declares what valid data looks like, and `validate`/`validateSync` enforce it. It became the standard companion to Formik and React Hook Form for form validation, and its `cast` method also coerces raw input into typed values.

## Details
- Mechanism: schemas chain validators: `yup.string().min(2).max(50).matches(regex)`, `yup.number().positive().integer()`, `yup.boolean()`, `yup.date()`, and `yup.array().of(...)` / `yup.object().shape({...})`. `validate(value)` returns a promise that rejects with a `ValidationError` carrying the failing path and message; `validateSync` does the same synchronously; `cast(value)` coerces — strings to numbers, dates, and booleans, with `stripUnknown`/`abortEarly` options controlling behavior. Cross-field constraints use `.test()` with access to the whole object (`(value, ctx) => ctx.parent.otherField...`), and `when()` makes rules conditional on sibling fields.
- Concrete examples: a signup schema validating email format, password strength, and password confirmation via `.test()` comparing to `ctx.parent.password`; a checkout schema with arrays of line items validated by `yup.array().of(itemSchema)`; a query-param parser that `cast`s `"page=2&limit=20"` into numbers; a React Hook Form resolver `yupResolver(schema)` that maps Yup errors onto form fields.
- Failure modes: the classic failures are async validation pitfalls (un-cancelled validations racing — an older slow check overwriting a newer result), schema drift between Yup and TypeScript types (Yup predates first-class type inference, so types are maintained separately and go stale), and cross-field tests that run out of order or reference fields that may be undefined. `cast`'s aggressive coercion (empty strings to `undefined` or `NaN`, `"0"` to `false` for booleans) surprises teams that expect strict behavior.
- Operational tradeoffs: Yup's strengths are maturity, Formik-era ecosystem integration, and a familiar chainable API; its weaknesses are weaker TypeScript inference than Zod and a historically loose type/schema relationship. The modern guidance is to prefer Zod for new TypeScript projects and reach for Yup when maintaining existing forms or when the team's stack (Formik, older RHF versions) already uses it. The practice rule: keep schemas in one place, export the types from them, validate at the boundary (form and API), and treat `cast` as explicit coercion, not magic.
- RSIS3/mykb relevance: MyKB's form-like surfaces (filters, settings) benefit from a single schema that drives both UI validation and daemon request validation, so the client and server agree on shape — the same single-source-of-truth rule RSIS3 applies to registry schemas.

## Related
- [[wiki/web-platforms/forms-practice|Forms in Practice]]
- [[wiki/frontend-frameworks/zod-validation|Zod Validation]]
- [[wiki/frontend-frameworks/schema-coercion|Schema Coercion]]
- [[wiki/frontend-frameworks/form-libraries|Form Libraries]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
