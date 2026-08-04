---
type: "entity"
title: "Zod Validation"
description: "TypeScript-first runtime schema parsing and validation"
tags: ["zod", "validation", "typescript", "schemas"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Zod Validation

## Summary
Zod is a TypeScript-first schema library: you declare a schema once — `z.object({ id: z.string().uuid(), count: z.number().int() })` — and Zod both validates at runtime and infers the static type (`z.infer<typeof schema>`), so the TypeScript type and the runtime check can never drift. Parsing produces detailed, path-annotated errors, making it the default choice for API boundaries and form validation in modern TypeScript stacks.

## Details
- Mechanism: `schema.parse(value)` returns the typed value or throws a `ZodError` with issues like `[{ path: ['user', 'email'], message: 'Invalid email' }]`; `safeParse` returns a discriminated result (`{ success: true, data }` | `{ success: false, error }`) without throwing. Schemas compose: `z.object`, `z.array`, `z.union`, `z.discriminatedUnion`, `z.record`, and transformations via `z.string().transform(...)` or `z.coerce.number()` for coercion. `z.infer` and `z.input` derive static types, and `.extend()`, `.pick()`, `.partial()` derive variants — a patch schema is `UpdateSchema.partial()` without new definitions. `superRefine` and `.refine()` express cross-field rules.
- Concrete examples: an API client parses every response with `schema.safeParse(json)` so malformed server data is caught at the boundary with typed errors; a form uses `zodResolver` (React Hook Form) mapping `ZodError` paths onto field errors; an env-var loader parses `process.env` into typed config, failing fast at boot; an OpenAPI-adjacent workflow generates Zod schemas from specs so server and client validate identically.
- Failure modes: the classic failures are over-nesting (gigantic monolithic schemas that are hard to read — compose small ones), transform misuse (transforms run after validation, so a transform that throws produces confusing errors unless wrapped in `z.pipe` or `superRefine`), and schema explosion from hand-writing every variant when `.pick`/`.partial` would do. Coercion pitfalls (`z.coerce.number()` turning `""` into `0`) mask bugs, and teams that parse in only one place (say the form) forget the API boundary still needs validation.
- Operational tradeoffs: Zod's type inference is its killer feature — one definition, compile-time and runtime guarantees — at the cost of schema size (it ships as a real dependency), some API-surface learning, and the discipline that every trust boundary parses. It compares favorably with Yup (stronger types) and JSON Schema (Zod is code-first, while JSON Schema is data-first and tooling-rich); the practical synthesis is JSON Schema/OpenAPI for the wire contract and Zod for the TypeScript boundary, kept in sync by generators.
- RSIS3/mykb relevance: the daemon's search and telemetry payloads are exactly Zod's target: parse at the boundary with inferred types flowing into the UI and loop code, so a malformed pulse or query is rejected with a structured error instead of corrupting the knowledge graph — mirroring RSIS3's typed-input invariants.

## Related
- [[wiki/web-platforms/forms-practice|Forms in Practice]]
- [[wiki/frontend-frameworks/schema-coercion|Schema Coercion]]
- [[wiki/frontend-frameworks/form-libraries|Form Libraries]]
- [[wiki/frontend-frameworks/react-hook-form|React Hook Form]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
