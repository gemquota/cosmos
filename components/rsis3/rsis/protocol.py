"""Open interop protocol — versioned surface + capability negotiation.

Phase 17 (Sequel IV): the loop stack's interfaces become a versioned
protocol any client can implement. ``docs/protocol.md`` is the spec;
this module implements the capability handshake (``/api/version``) and
fail-closed version negotiation. The conformance suite lives in
``tests/test_protocol.py`` and drives a live verify-server with a plain
HTTP reference client (stdlib only).
"""

from __future__ import annotations

import json
from pathlib import Path

PROTOCOL_NAME = "cosmos-protocol"
PROTOCOL_VERSION = "1"
PROTOCOL_ID = f"{PROTOCOL_NAME}/{PROTOCOL_VERSION}"

#: endpoints the protocol promises; unknown/unsupported versions fail closed
ENDPOINTS = {
    "memory": ["GET /api/search", "GET /api/notes", "POST /api/notes"],
    "verification": ["GET /health", "GET /version", "POST /verify",
                     "GET /ledger"],
    "federation": ["envelope publish", "envelope pull", "ledger status"],
    "attestation": ["chain verify", "bundle export", "bundle verify"],
}


def capabilities() -> dict:
    """Capability handshake payload served at ``/version``."""
    return {
        "protocol": PROTOCOL_ID,
        "name": PROTOCOL_NAME,
        "version": PROTOCOL_VERSION,
        "endpoints": ENDPOINTS,
        "fail_closed": True,
        "generated": __import__("rsis.epoch1", fromlist=["now_ts"]).now_ts(),
    }


def negotiate(client_protocol: str, supported: str = PROTOCOL_ID) -> bool:
    """Fail-closed version negotiation.

    Accepts ``cosmos-protocol/1`` exactly, or a same-name newer minor.
    Anything else — unknown names, newer majors, garbage — is rejected.
    """
    if not isinstance(client_protocol, str):
        return False
    name, _, ver = client_protocol.partition("/")
    if name != PROTOCOL_NAME:
        return False
    major = ver.split(".", 1)[0]
    try:
        return int(major) == int(PROTOCOL_VERSION)
    except ValueError:
        return False


def spec_path(workspace: Path) -> Path:
    return Path(workspace) / "docs" / "protocol.md"


def status(workspace: Path) -> dict:
    p = spec_path(workspace)
    return {
        "protocol": PROTOCOL_ID,
        "spec_exists": p.is_file(),
        "endpoints": ENDPOINTS,
        "version_negotiation": "fail-closed",
    }
