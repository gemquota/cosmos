---
type: "entity"
title: "curl & HTTP Clients"
description: "Request flags, headers, and scripting"
tags: ["curl", "http", "cli", "rest"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://curl.se/docs/manpage.html", "https://everything.curl.dev/"]
---

# curl & HTTP Clients

## Summary
curl transfers data with URLs, supporting HTTP(S), FTP, and many more protocols, and it is the de facto HTTP client for scripts and APIs. One -d, -H, and -X away from any request, it also powers automation via its exit codes and --fail behavior.

## Details
- Basic: curl https://api.example.com/v1/items prints the body; -o file saves it, -i shows response headers, -I does a HEAD request.
- Methods and data: -X POST with -d '{"k":"v"}' (form-encoded by default, use -H 'Content-Type: application/json' for JSON).
- Headers and auth: -H 'Authorization: Bearer TOKEN', -u user:pass for basic auth, -b/-c for cookies.
- Follow redirects with -L; verify certificates by default and use -k only for testing; --cacert pins a CA bundle.
- Exit codes matter: 0 success, 22 HTTP >= 400, 6 DNS failure, 7 connection refused; --fail makes >=400 an error by default in scripts.
- Multipart uploads: -F 'file=@photo.jpg' for form file fields; --data-urlencode for tricky values.
- Advanced: --retry/--retry-all-errors for flaky APIs, --max-time timeouts, and piping to jq: curl -s ... | jq '.'.

## Related
- [[wiki/os-shell/http-basics|HTTP Basics]] — the protocol curl speaks
- [[wiki/os-shell/jq-json-processing|jq]] — parsing the JSON responses
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]] — certificate verification in transit
- [[wiki/dev-tools/curl-patterns|Curl Patterns]] — battle-tested request recipes
- [[wiki/api-protocols/rest-apis|REST APIs]] — what curl is usually called against
