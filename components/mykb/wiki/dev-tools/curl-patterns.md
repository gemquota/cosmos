---
type: "concept"
title: "Curl Patterns"
description: "Recurring command-line idioms for transferring data with curl during development and debugging"
tags: ["curl", "http", "cli", "debugging"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Curl Patterns

## Summary
Curl is the universal command-line HTTP client; its patterns — -i for headers, -d for POST bodies, -u for auth, -w for timing — form a vocabulary every developer and agent uses to probe APIs. Mastery of these idioms turns curl from a tool into a debugging instrument.

## Details
- Common idioms: `curl -sS -i` shows status and headers; `-X POST -H 'Content-Type: application/json' -d '{...}'` exercises JSON APIs; `-u user:pass` or `-H 'Authorization: Bearer ...'` handles auth; `-k` skips TLS verification for test servers (never in production scripts); `--data @file.json` reads bodies from files.
- Timing and scripting: `--max-time` bounds hangs; `-w '%{http_code} %{time_total}'` emits machine-readable timing; `-o /dev/null` discards bodies for health checks; `--retry` and `--retry-delay` add basic resilience; `-L` follows redirects; `-v` or `--trace` reveals the full exchange including TLS.
- Concrete example: a health check script runs `curl -sS -o /dev/null -w '%{http_code}' --max-time 5 https://api.example/health` and fails when the output is not 200; a debugging session reproduces a bug by replaying the exact request with `-i -X POST`.
- Failure modes: `-s` hiding errors (add `-S`); piping binary output into text tools; hardcoding secrets into commands that end up in shell history; `-X POST` used where `-d` already implies POST, causing double-method surprises with redirects; timeout defaults that hang scripts forever.
- Tradeoffs: curl is ubiquitous and scriptable but raw — response validation, retries, and JSON handling are left to the caller; the alternative, HTTP client libraries or tools like httpie, trade universality for sugar; the pattern is curl for probing and scripting, libraries for real integrations.
- Operational notes: keep a collection of request templates, and use `curl --compressed` to verify cache and compression behavior.
- RSIS3 relevance: the mykb daemon uses curl-style requests for the dashboard API — these patterns are the debugging vocabulary for RSIS3's own HTTP integrations.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — curl is the REST developer's first client
- [[wiki/dev-tools/jq-querying|Jq Querying]] — curl pipes into jq to inspect responses
- [[wiki/api-protocols/http-caching|HTTP Caching]] — curl headers reveal cache behavior
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — curl timing shows rate-limit backoff
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — curl is a canonical CLI
