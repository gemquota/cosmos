---
type: "entity"
title: "Deposits Error"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "Handling failures in deposit and payment flows with retries and clear errors"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "payments", "errors"]

# Deposits Error

## Summary
A deposits error is any failure in the flow that moves money into an account: declined cards, failed bank transfers, timeouts, or duplicate submissions. It matters because money flows demand idempotency, clear status, and honest communication with users. Mishandled deposit errors cause double charges, lost funds, and support escalations, so the error path deserves the same design attention as the happy path.

## Details
- **Definition** — deposit failures span authorization declines, processing timeouts, settlement errors, and invalid account details.
- **Idempotency** — retries must carry idempotency keys so a resubmitted request cannot create a second charge.
- **Distinct states** — a payment can be pending, succeeded, failed, or needs action; each state needs explicit representation and transitions.
- **Decline handling** — declines carry codes that map to user guidance, such as insufficient funds or card expired, without exposing sensitive details.
- **Retry policy** — transient failures warrant bounded retries with backoff; permanent declines should not be retried automatically.
- **Reconciliation** — external payment state must be reconciled with local records to catch discrepancies between the two sources of truth.
- **Common failure modes** — double charges from missing idempotency, stale statuses after callbacks, and generic errors that leave users guessing.
- **Worked example** — a user's deposit times out; the client retries with the same idempotency key, the gateway returns the original pending result, and the UI shows a clear retry state.
- **Practical relevance** — disciplined deposit error handling protects revenue and user trust in financial features.

- **User messaging** — deposit failures need honest, actionable messages that distinguish decline, timeout, and needs-action states.
- **Compliance** — error handling must preserve audit trails and not expose card data or processor internals to users.
## Related
- [[wiki/api-protocols/idempotency-keys|Idempotency Keys]] — safe retries
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — structured failures
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — stable codes
- [[wiki/testing/error-guessing|Error Guessing]] — finding edge cases
- [[wiki/api-protocols/timeouts|Timeouts]] — bounding payments
- [[wiki/tooling/client-side-retries|Client-Side Retries]] — retry behavior
