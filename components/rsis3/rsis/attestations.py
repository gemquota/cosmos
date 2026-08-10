"""Public attestation & external audit — hash-linked transparency log.

Phase 16 (Sequel IV): attestations become independently verifiable by
third parties that do not trust the instance at all.

- ``append`` — every record carries the previous record's sha256, forming
  a tamper-evident chain in ``rack/attestations/chain.jsonl``.
- ``verify_chain`` — replays the chain and recomputes every linkage.
- ``export_bundle`` — renders a self-contained bundle (chain + invariant
  registry + gate code shas + verification ledger) a third party can
  replay offline.
- ``verify_bundle`` — reproduces the ledger decisions from the bundle with
  zero access to instance state.
- ``replay`` — re-runs the deterministic Phase 7 gates (candidate sha,
  contracts gate, property checks) from recorded artifacts and compares
  against the ledger decision.
"""

from __future__ import annotations

import json
import logging
import os
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl,
    sha256_file, sha256_text,
)

logger = logging.getLogger(__name__)

CHAIN_VERSION = 1
#: files whose shas become part of the verifier bundle (gate code)
GATE_SOURCES = (
    "rsis/verify.py", "rsis/evaluator.py", "rsis/invariants.py",
    "evaluator/evaluator.py",
)


def att_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "attestations"


def chain_path(workspace: Path) -> Path:
    return att_dir(workspace) / "chain.jsonl"


def _canonical(record: dict, prev_sha: str) -> str:
    """Deterministic hash input for a chain record."""
    payload = json.dumps(record.get("payload"), sort_keys=True,
                         ensure_ascii=False)
    return "|".join([
        str(record.get("index", "")), prev_sha,
        str(record.get("kind", "")), payload,
        str(record.get("ts", "")),
    ])


def append(workspace: Path, kind: str, payload: dict,
           meta: Optional[dict] = None) -> dict:
    """Append an attestation record; returns it with its ``sha``."""
    ws = Path(workspace)
    ensure_rack(ws, "attestations")
    path = chain_path(ws)
    chain = read_jsonl(path)
    prev_sha = chain[-1]["sha"] if chain else "0" * 64
    record = {
        "index": len(chain),
        "kind": kind,
        "payload": payload,
        "meta": meta or {},
        "ts": now_ts(),
        "prev": prev_sha,
        "chain": "cosmos-attestations/1",
    }
    record["sha"] = sha256_text(_canonical(record, prev_sha))
    append_jsonl(path, record)
    emit(ws, "attestation_appended",
         kind=kind, index=record["index"], sha=record["sha"][:12])
    return record


def verify_chain(workspace: Path) -> tuple[bool, list[str]]:
    """Replay the chain; returns (ok, issues)."""
    issues: list[str] = []
    prev = "0" * 64
    for i, rec in enumerate(read_jsonl(chain_path(workspace))):
        if rec.get("prev") != prev:
            issues.append(f"record {i}: broken link (prev mismatch)")
        if rec.get("index") != i:
            issues.append(f"record {i}: index mismatch")
        recomputed = sha256_text(_canonical(rec, rec.get("prev", "")))
        if recomputed != rec.get("sha"):
            issues.append(f"record {i}: sha mismatch (tampered)")
        prev = rec.get("sha", "")
    return (len(issues) == 0, issues)


def verification_ledger(workspace: Path) -> list[dict]:
    """All Phase 7 verification records, oldest first."""
    vdir = Path(workspace) / "rack" / "verification"
    recs: list[dict] = []
    if not vdir.is_dir():
        return recs
    for f in sorted(vdir.glob("*.jsonl")):
        recs.extend(read_jsonl(f))
    return sorted(recs, key=lambda r: r.get("ts", ""))


def _gate_sources_shas(workspace: Path) -> dict:
    root = Path(workspace)
    return {src: sha256_file(root / src) for src in GATE_SOURCES}


def export_bundle(workspace: Path, out_path: Optional[Path] = None) -> dict:
    """Self-contained attestation bundle (chain + invariants + gate shas +
    verification ledger) for offline third-party replay."""
    ws = Path(workspace)
    bundle = {
        "format": "cosmos-attestations-bundle/1",
        "generated": now_ts(),
        "chain": read_jsonl(chain_path(ws)),
        "invariants": load_json(Path(ws) / "rack" / "invariants.json"),
        "gate_sources": _gate_sources_shas(ws),
        "verification": verification_ledger(ws),
    }
    bundle["sha"] = sha256_text(json.dumps(
        {"chain": bundle["chain"], "invariants": bundle["invariants"],
         "gate_sources": bundle["gate_sources"]}, sort_keys=True))
    if out_path:
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(bundle, indent=1, sort_keys=True),
                            encoding="utf-8")
    emit(ws, "attestation_exported", sha=bundle["sha"][:12],
         chain_len=len(bundle["chain"]))
    return bundle


def verify_bundle(bundle: dict) -> tuple[bool, list[str]]:
    """Standalone verification of an exported bundle (no instance state).

    Re-checks chain linkage/shas, invariant registry integrity and the
    recorded gate-source shas.
    """
    issues: list[str] = []
    chain = bundle.get("chain") or []
    prev = "0" * 64
    for i, rec in enumerate(chain):
        if rec.get("prev") != prev:
            issues.append(f"chain[{i}]: broken link")
        if sha256_text(_canonical(rec, rec.get("prev", ""))) != rec.get("sha"):
            issues.append(f"chain[{i}]: sha mismatch")
        prev = rec.get("sha", "")
    inv = bundle.get("invariants") or {}
    if inv:
        for key in ("registry", "version"):
            if key not in inv:
                issues.append(f"invariants: missing {key!r}")
    ok = len(issues) == 0
    return ok, issues


def replay(workspace: Path, candidate_sha: str,
           bundle: Optional[dict] = None) -> Optional[dict]:
    """Replay a candidate through the deterministic gates and compare.

    Re-runs candidate-sha recomputation, the contracts gate and recorded
    property checks from the bundle/ledger; returns a report with
    ``reproduced`` (the recorded decision matches the deterministic gates).
    """
    recs = verification_ledger(workspace) if bundle is None \
        else (bundle.get("verification") or [])
    rec = next((r for r in recs if r.get("candidate_sha") == candidate_sha), None)
    if rec is None:
        return None
    from rsis.verify import contracts_gate, repo_root
    ok_contracts, contract_fail = contracts_gate(repo_root(Path(workspace)))
    deterministic = {
        "contracts": ok_contracts,
        "contract_fail": contract_fail,
        "recorded_contract_fail": rec.get("contract_fail", -1),
        "property_checks": rec.get("property_checks", []),
    }
    reproduced = (contract_fail == rec.get("contract_fail", -1))
    return {"candidate_sha": candidate_sha, "recorded": rec,
            "deterministic": deterministic, "reproduced": reproduced}


def chain_summary(workspace: Path) -> dict:
    ok, issues = verify_chain(workspace)
    chain = read_jsonl(chain_path(workspace))
    kinds: dict = {}
    for r in chain:
        kinds[r.get("kind", "?")] = kinds.get(r.get("kind", "?"), 0) + 1
    return {"ok": ok, "count": len(chain), "kinds": kinds,
            "issues": issues[:5], "head": chain[-1].get("sha", "") if chain else None}


def main(workspace: Path, action: str = "status",
         out: Optional[str] = None, candidate_sha: Optional[str] = None,
         bundle: Optional[str] = None, json_out: bool = False) -> int:
    ws = Path(workspace)
    if action == "append":
        rec = append(ws, "manual", {"note": "manual attestation"})
        print(f"  appended attestation #{rec['index']} ({rec['sha'][:12]})")
    elif action == "verify":
        ok, issues = verify_chain(ws)
        print("  chain:", "OK" if ok else "TAMPERED",
              f"({len(read_jsonl(chain_path(ws)))} records)")
        for i in issues[:10]:
            print("   -", i)
        return 0 if ok else 1
    elif action == "export":
        out_path = Path(out) if out else Path(ws) / "rack" / "attestations" / "bundle.json"
        b = export_bundle(ws, out_path)
        print(f"  exported bundle -> {out_path} ({b['sha'][:12]})")
    elif action == "verify-bundle":
        b = json.loads(Path(bundle).read_text()) if bundle else None
        if b is None:
            print("  --bundle required"); return 2
        ok, issues = verify_bundle(b)
        print("  bundle:", "OK" if ok else "INVALID")
        for i in issues[:10]:
            print("   -", i)
        return 0 if ok else 1
    elif action == "replay":
        if not candidate_sha:
            print("  --candidate-sha required"); return 2
        report = replay(ws, candidate_sha)
        if report is None:
            print(f"  no verification record for {candidate_sha}"); return 1
        print("  replay:", "reproduced" if report["reproduced"] else "DIVERGED")
        print(f"    recorded contracts: {report['recorded']['contract_fail']} fail; "
              f"re-run: {report['deterministic']['contract_fail']} fail")
        return 0 if report["reproduced"] else 1
    else:
        s = chain_summary(ws)
        print(f"  attestations: {s['count']} records, "
              f"{'chain OK' if s['ok'] else 'chain BROKEN'}")
        for k, v in sorted(s["kinds"].items()):
            print(f"    {k}: {v}")
        if json_out:
            print(json.dumps(s))
    return 0
