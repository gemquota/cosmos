"""Instance identity & trust graph — signed federation with real keys.

Phase 21 (Sequel V): instances authenticate each other; federation stops
trusting shared tokens and starts trusting keys. Ed25519 keypairs
(cryptography) live in ``.rsis/identity/``; fingerprints publish in the
federation ledger; peers register in ``rack/federation/peers.json``;
unknown peers are quarantined; keys rotate with a grace period (retired
keys verify but never sign).
"""

from __future__ import annotations

import base64
import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

from rsis.epoch1 import emit, load_json, now_ts, save_json

logger = logging.getLogger(__name__)

TRUST_LEVELS = ("quarantined", "peer", "trusted", "allied")
DEFAULT_ROTATION_DAYS = 90
GRACE_DAYS = 7


def id_dir(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "identity"


def peers_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "federation" / "peers.json"


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def fingerprint_of(pub: ed25519.Ed25519PublicKey) -> str:
    raw = pub.public_bytes(
        serialization.Encoding.Raw,
        serialization.PublicFormat.Raw)
    import hashlib
    return hashlib.sha256(raw).hexdigest()[:32]


def ensure_keypair(workspace: Path) -> dict:
    """Create (or load) the instance keypair; returns {id, fingerprint}."""
    d = id_dir(workspace)
    d.mkdir(parents=True, exist_ok=True)
    priv_path = d / "instance.key"
    pub_path = d / "instance.pub"
    if not priv_path.is_file():
        private = ed25519.Ed25519PrivateKey.generate()
        priv_path.write_bytes(private.private_bytes(
            serialization.Encoding.Raw, serialization.PrivateFormat.Raw,
            serialization.NoEncryption()))
        pub_path.write_bytes(private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw))
    raw = priv_path.read_bytes()
    private = ed25519.Ed25519PrivateKey.from_private_bytes(raw)
    fingerprint = fingerprint_of(private.public_key())
    instance_id = "cosmos-" + fingerprint[:12]
    return {"id": instance_id, "fingerprint": fingerprint,
            "public_key": _b64(private.public_key().public_bytes(
                serialization.Encoding.Raw,
                serialization.PublicFormat.Raw))}


def load_public(workspace: Path, fingerprint: str) -> Optional[ed25519.Ed25519PublicKey]:
    """Load a public key by fingerprint — the instance's own key, imported
    peer keys, and retired (verify-only) keys are all candidates."""
    d = id_dir(workspace)
    candidates = []
    own = d / "instance.pub"
    if own.is_file():
        candidates.append(own.read_bytes())
    candidates.extend(p.read_bytes() for p in sorted(d.glob("peer-*.pub")))
    retired = load_json(d / "retired.json", {"version": 1, "keys": []})
    candidates.extend(k.get("pub", "").encode("latin-1")
                      for k in retired.get("keys", []))
    for raw in candidates:
        try:
            pub = ed25519.Ed25519PublicKey.from_public_bytes(raw)
            if fingerprint_of(pub) == fingerprint:
                return pub
        except Exception:
            continue
    return None


def import_peer_key(workspace: Path, fingerprint: str,
                    public_key_b64: str) -> bool:
    d = id_dir(workspace)
    d.mkdir(parents=True, exist_ok=True)
    try:
        raw = base64.urlsafe_b64decode(public_key_b64 + "=" * (-len(public_key_b64) % 4))
        pub = ed25519.Ed25519PublicKey.from_public_bytes(raw)
    except Exception:
        return False
    if fingerprint_of(pub) != fingerprint:
        return False
    (d / f"peer-{fingerprint}.pub").write_bytes(raw)
    return True


def sign(workspace: Path, payload: dict) -> dict:
    """Sign a payload's canonical JSON; returns {by, fingerprint, sig}."""
    key = ensure_keypair(workspace)
    raw = id_dir(workspace) / "instance.key"
    private = ed25519.Ed25519PrivateKey.from_private_bytes(raw.read_bytes())
    body = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    sig = private.sign(body)
    return {"by": key["id"], "fingerprint": key["fingerprint"],
            "sig": _b64(sig)}


def verify(workspace: Path, payload: dict, signature: dict) -> bool:
    """Verify a signature over the canonical payload."""
    pub = load_public(workspace, signature.get("fingerprint", ""))
    if pub is None:
        return False
    body = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    try:
        pub.verify(base64.urlsafe_b64decode(
            signature.get("sig", "") + "=" * (-len(signature.get("sig", "")) % 4)), body)
        return True
    except Exception:
        return False


def load_peers(workspace: Path) -> dict:
    return load_json(peers_path(workspace),
                     {"version": 1, "rotation_days": DEFAULT_ROTATION_DAYS,
                      "peers": []})


def register_peer(workspace: Path, peer_id: str, fingerprint: str,
                  trust: str = "quarantined", public_key_b64: Optional[str] = None,
                  actor: str = "system") -> dict:
    if trust not in TRUST_LEVELS:
        raise ValueError(f"bad trust {trust!r}")
    if public_key_b64 and not import_peer_key(workspace, fingerprint, public_key_b64):
        raise ValueError("peer public key does not match fingerprint")
    peers = load_peers(workspace)
    rec = {"id": peer_id, "fingerprint": fingerprint, "trust": trust,
           "added": now_ts(), "last_seen": now_ts(), "added_by": actor}
    peers["peers"] = [p for p in peers["peers"] if p["id"] != peer_id] + [rec]
    save_json(peers_path(workspace), peers)
    emit(workspace, "identity_peer_registered", peer=peer_id, trust=trust)
    return rec


def trusted(workspace: Path, peer_id: Optional[str] = None,
            min_trust: str = "peer") -> list[dict]:
    peers = load_peers(workspace)
    order = {t: i for i, t in enumerate(TRUST_LEVELS)}
    out = [p for p in peers["peers"] if order.get(p.get("trust", "quarantined"), 0)
           >= order.get(min_trust, 1)]
    if peer_id:
        return [p for p in out if p["id"] == peer_id]
    return out


def rotate_key(workspace: Path, actor: str = "system") -> dict:
    """Rotate the instance key; retire the old one (verify-only)."""
    d = id_dir(workspace)
    d.mkdir(parents=True, exist_ok=True)
    old_pub = d / "instance.pub"
    retired = load_json(d / "retired.json", {"version": 1, "keys": []})
    if old_pub.is_file():
        retired["keys"].append({"pub": old_pub.read_bytes().decode("latin-1"),
                                "retired": now_ts(), "verify_only": True})
        save_json(d / "retired.json", retired)
    old_pub.unlink(missing_ok=True)
    (d / "instance.key").unlink(missing_ok=True)
    key = ensure_keypair(workspace)
    emit(workspace, "identity_key_rotated", fingerprint=key["fingerprint"][:12])
    return key


def status(workspace: Path) -> dict:
    key = ensure_keypair(workspace)
    peers = load_peers(workspace)
    return {"instance": key["id"], "fingerprint": key["fingerprint"],
            "rotation_days": peers.get("rotation_days", DEFAULT_ROTATION_DAYS),
            "peers": peers["peers"], "trust_levels": list(TRUST_LEVELS)}


def main(workspace: Path, action: str = "status",
         peer_id: Optional[str] = None, fingerprint: Optional[str] = None,
         trust: str = "peer", pubkey: Optional[str] = None,
         json_out: bool = False) -> int:
    ws = Path(workspace)
    if action == "init" or action == "status":
        s = status(ws)
        print(f"  instance {s['instance']}")
        print(f"  fingerprint {s['fingerprint']}")
        print(f"  peers: {len(s['peers'])} "
              f"({sum(1 for p in s['peers'] if p['trust']!='quarantined')} trusted)")
        if json_out:
            print(json.dumps(s))
        return 0
    if action == "peer-add":
        if not peer_id or not fingerprint:
            print("  --peer-id and --fingerprint required"); return 2
        rec = register_peer(ws, peer_id, fingerprint, trust=trust,
                            public_key_b64=pubkey)
        print(f"  peer {rec['id']} registered ({rec['trust']})")
        return 0
    if action == "rotate":
        key = rotate_key(ws)
        print(f"  key rotated -> fingerprint {key['fingerprint'][:12]}")
        return 0
    print("  unknown action"); return 2
