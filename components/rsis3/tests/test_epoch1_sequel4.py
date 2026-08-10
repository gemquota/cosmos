"""Epoch 1, Sequel IV (Phases 16–20) — Open Autonomy."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.attestations import (
    append, chain_summary, export_bundle, replay, verify_bundle, verify_chain,
)
from rsis.identity import ensure_keypair
from rsis.portable import continuity_check, export_instance, import_instance
from rsis.protocol import negotiate


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


class AttestationTests(unittest.TestCase):
    def test_chain_tamper_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            a0 = append(ws, "test", {"x": 1})
            append(ws, "test", {"x": 2})
            self.assertTrue(verify_chain(ws)[0])
            path = ws / "rack" / "attestations" / "chain.jsonl"
            text = path.read_text()
            path.write_text(text.replace(a0["sha"], "0" * 64, 1))
            ok, issues = verify_chain(ws)
            self.assertFalse(ok)
            self.assertTrue(any("link" in i or "sha" in i for i in issues))

    def test_bundle_standalone_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            append(ws, "test", {"x": 1})
            bundle = export_bundle(ws)
            self.assertTrue(verify_bundle(bundle)[0])
            bundle["chain"][-1]["sha"] = "0" * 64
            self.assertFalse(verify_bundle(bundle)[0])

    def test_replay_unknown_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            self.assertIsNone(replay(ws, "deadbeef" * 8))


class ProtocolTests(unittest.TestCase):
    def test_negotiation_fail_closed(self):
        self.assertTrue(negotiate("cosmos-protocol/1"))
        self.assertTrue(negotiate("cosmos-protocol/1.2"))
        self.assertFalse(negotiate("cosmos-protocol/2"))
        self.assertFalse(negotiate("other-protocol/1"))
        self.assertFalse(negotiate("garbage"))
        self.assertFalse(negotiate(None))


class PortableTests(unittest.TestCase):
    def test_export_import_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            (ws / "rsis").mkdir(parents=True)
            (ws / "rsis" / "epoch1.py").write_text("# hello\n")
            (ws / "rack" / "policy.json").write_text(
                json.dumps({"version": 1, "approval_required": {"paths": []}}))
            bundle = export_instance(ws)
            target = Path(tmp) / "ws2"
            result = import_instance(target, bundle)
            self.assertEqual(result["checksums_verified"], True)
            self.assertTrue((target / "rsis" / "epoch1.py").is_file())

    def test_continuity_check_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            ok, state = continuity_check(ws)
            self.assertIn("invariants_ok", state)


if __name__ == "__main__":
    unittest.main()


class RedteamTests(unittest.TestCase):
    def test_probes_and_triage(self):
        from rsis.redteam import findings_path, run_probes, triage
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            findings = run_probes(ws)
            self.assertIsInstance(findings, list)
            # every finding is open until triaged
            self.assertTrue(all(f["status"] == "open" for f in findings))
            with findings_path(ws).open("a") as fh:
                for f in findings:
                    fh.write(json.dumps(f) + "\n")
            self.assertTrue(triage(ws, 0, "triaged", resolution="accepted risk"))
            recs = [json.loads(l) for l in
                    findings_path(ws).read_text().splitlines()]
            self.assertEqual(recs[0]["status"], "triaged")
            self.assertFalse(triage(ws, 0, "bogus"))


class AppsTests(unittest.TestCase):
    def test_app_identity_and_quota(self):
        from rsis.apps import (
            add_app, authenticate, issue_token, quota_ok,
        )
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            app = add_app(ws, "third-party", capabilities=["read", "propose"])
            self.assertIn("secret", app)
            token = issue_token(ws, "third-party", app["secret"])
            self.assertIsNotNone(token)
            auth = authenticate(ws, token)
            self.assertEqual(auth["id"], "third-party")
            self.assertIsNone(authenticate(ws, "garbage.token"))
            ok, usage = quota_ok(ws, auth)
            self.assertTrue(ok)
            self.assertEqual(usage["rate"], 0)

    def test_app_secret_must_match(self):
        from rsis.apps import add_app, issue_token
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            app = add_app(ws, "bad-app")
            self.assertIsNone(issue_token(ws, "bad-app", "wrong-secret"))

    def test_duplicate_app_rejected(self):
        from rsis.apps import add_app
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            add_app(ws, "dup")
            with self.assertRaises(ValueError):
                add_app(ws, "dup")
