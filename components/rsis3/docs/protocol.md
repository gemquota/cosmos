# cosmos-protocol/1 — Open Interop Protocol

Adopted: 2026-08-10 · Phase 17 (Sequel IV) · Status: active
Supersedes: private interfaces of Phases 6, 7, 13 and 16.

`cosmos-protocol/1` is the versioned, implementation-independent surface
of the loop stack. Any client — Python, JS, curl, or a foreign ecosystem —
may implement it from this document alone and interoperate with a live
instance. Unknown or unsupported protocol versions fail closed.

## 1. Version & capability handshake

- `GET /version` → `{"protocol": "cosmos-protocol/1", "name": "cosmos-protocol",
  "version": "1", "endpoints": {...}, "fail_closed": true}`
- Client sends its protocol id in every request header `X-Protocol:
  cosmos-protocol/1`. Responses with `409` mean the version is
  unsupported; the client must not retry with degraded semantics.

## 2. Memory API (extends Phase 6 MyKB surface)

| Endpoint | Method | Semantics |
|----------|--------|-----------|
| `/api/search?q=...` | GET | TF-IDF/vector search over the knowledge base; returns note paths + scores |
| `/api/notes/<rel>` | GET | Read a note body + frontmatter |
| `/api/notes` | POST | Create a note; create-only unless the session is the owner |

Notes are identified by repo-relative paths (`wiki/syntheses/<name>.md`).
Writes are advisory-lock protected; concurrent writers never clobber.

## 3. Verification API (extends Phase 7)

| Endpoint | Method | Semantics |
|----------|--------|-----------|
| `/health` | GET | liveness; 200 `{"ok": true}` |
| `/version` | GET | capability handshake (above) |
| `/verify` | POST | run the full gate pass on a candidate `{description, target_files, diff_or_code, rationale, goal}`; returns the ledger record |
| `/ledger?date=YYYY-MM-DD` | GET | replay a day's verification records |

A candidate's `candidate_sha` is `sha256(diff_or_code)`. The ledger
records gates (evaluator, contracts, property checks), `decision`, scores
and pre-apply digests. Consumers must treat the `evaluator` gate as
recorded evidence — deterministic replay is provided by the attestation
bundle (below).

## 4. Federation envelope (extends Phase 13)

Published syntheses travel as envelopes:

```json
{"format": "cosmos-federation-envelope/1", "origin": {"instance": "...", "fingerprint": "..."},
 "note_rel": "...", "content_sha": "...", "confidence": 0.8,
 "provenance": {"source": "...", "project": "...", "session": "...",
                "producer": "...", "verification": "...",
                "transformations": [], "federation_history": []},
 "signed": {"by": "...", "sig": "..."}}
```

Recipients verify `signed.sig` against the origin fingerprint before
adoption (Phase 21). Unknown origins are quarantined, never adopted.

## 5. Attestation bundle (extends Phase 16)

`GET /attestations/bundle` (or `rsis attestations export`) yields:

```json
{"format": "cosmos-attestations-bundle/1", "chain": [...], "invariants": {...},
 "gate_sources": {"rsis/verify.py": "sha256...", ...}, "verification": [...],
 "sha": "sha256(...)"}
```

An independent verifier replays the chain (hash links), the invariant
registry and the recorded verification decisions with zero access to
instance state.

## 6. Conformance

The conformance suite (`tests/test_protocol.py`) runs against any
implementation: it boots a live verify-server, drives the read path and
candidate verification with a plain HTTP client, and asserts the
handshake, ledger and attestation shapes. A conformant implementation
must pass the suite without modifications to its own code.

## 7. Versioning & deprecation

- Protocol versions coexist; clients negotiate per request.
- Deprecation: `X-Protocol` versions older than `cosmos-protocol/1` are
  rejected (`409`). Future majors publish a sunset calendar in this file.
- Any change that breaks an existing endpoint bumps the major version and
  requires a conformance-suite update.
