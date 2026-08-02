---
type: "concept"
title: "Client-Side Timeouts"
description: "Timeouts enforced by the client so a slow server cannot hang it"
tags: ["timeouts", "clients", "reliability", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Client-Side Timeouts

## Summary
Client-side timeouts bound how long a client waits for a response, protecting the client from server hangs and stalled connections. They are the first line of defense against cascading slowness.

## Details
- Set connect, request, and total timeouts separately — they fail differently.
- Timeout values should reflect the dependency's SLO, not a guess.
- On timeout, cancel the underlying request so the server can stop working on it.
- mykb relevance: the source fetcher's client timeouts keep one slow site from stalling curation.

## Related
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/tooling/client-side-retries|Client-Side Retries]]
- [[wiki/tooling/keepalives|Keepalives]]
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
