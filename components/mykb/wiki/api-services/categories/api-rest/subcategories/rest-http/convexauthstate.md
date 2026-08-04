---
type: "entity"
title: "ConvexAuthState"
description: "Authentication state managed by the Convex reactive backend"
tags: ["entity", "authentication", "convex", "state", "frontend"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# ConvexAuthState

## Summary

ConvexAuthState is the authentication state in applications built on Convex, the reactive backend platform where server functions and client state sync automatically. Auth state — who is signed in and what they may do — must be trusted data, so its handling is a security-critical part of the app. The pattern generalizes: auth state should be derived from verifiable tokens, never from client assertions alone.

## Details

- **Definition** — Auth state records the current identity and permissions; in reactive backends it is a queryable value that clients observe and re-render on change.
- **Trust boundary** — Clients display auth state, but servers must re-derive identity from tokens and enforce authorization on every operation.
- **Session lifecycle** — Sign-in, token refresh, sign-out, and expiry transitions update state; races in these transitions cause flicker and permission bugs.
- **Worked example** — A Convex app stores auth state from a provider, gates queries on the session, and redirects unauthenticated users at the router.
- **Common failure modes** — Storing tokens in insecure locations, trusting client-side role flags, and missing handling of expiry that leaves stale UI.
- **Practical relevance** — Reactive auth state improves UX but inherits all the usual identity pitfalls, so token validation remains server-side.
- **Variants** — Provider-managed sessions, JWTs, and server sessions differ in where the source of truth lives.
- **Telemetry note** — Recorded in API and cloud sessions with an authentication tag, matching auth-integration work.
- **Reactivity** — Because clients re-render on state change, auth transitions must be atomic: a half-updated state can briefly show privileged UI to the wrong user.
- **Testing** — Auth flows deserve tests for signed-out, signed-in, expired, and denied states, with fake providers to keep runs deterministic.
- **Worked example** — A route guard subscribes to auth state, shows a spinner during refresh, and redirects after the state settles to a definitive signed-in or signed-out value.

## Related

- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — the token flows
- [[wiki/api-protocols/json-web-tokens|JSON Web Tokens]] — verifiable identity claims
- [[wiki/compositions/identity-management|Identity Management]] — managing identities
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/identitysnapshot|IdentitySnapshot]] — capturing auth state
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — client-side auth rendering
- [[wiki/testing/authentication-testing|Authentication Testing]] — verifying auth behavior
