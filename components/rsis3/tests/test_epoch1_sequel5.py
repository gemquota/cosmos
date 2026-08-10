"""Epoch 1, Sequel V (Phases 21–25) — Federated Intelligence."""
import tempfile
import unittest
from pathlib import Path

from rsis.epoch1 import load_json, read_jsonl
from rsis.exchange import (
    adopt, canonical_key, confidence, corroborate, find_canonical,
    provenance_intact, record_hop,
)
from rsis.identity import (
    ensure_keypair, import_peer_key, register_peer, rotate_key, sign, trusted,
    verify,
)
from rsis.popgov import (
    adopt_rules, cast_vote, publish_rules, require_quorum,
    resolve_rule_divergence,
)
from rsis.resilience import (
    enter_partition, merge_fork, peer_join, reconcile_partition, survival_drill,
)
from rsis.swarm import dispatch, fail_peer, report_verdict, status as swarm_status


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


class IdentityTests(unittest.TestCase):
    def test_sign_verify_tamper(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            key = ensure_keypair(ws)
            sig = sign(ws, {"a": 1, "b": "x"})
            self.assertEqual(sig["by"], key["id"])
            self.assertTrue(verify(ws, {"a": 1, "b": "x"}, sig))
            self.assertFalse(verify(ws, {"a": 2, "b": "x"}, sig))

    def test_peer_key_must_match_fingerprint(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            other = make_ws(Path(tmp) / "other")
            ok = ensure_keypair(other)
            self.assertTrue(import_peer_key(ws, ok["fingerprint"], ok["public_key"]))
            self.assertFalse(import_peer_key(ws, "0" * 32, ok["public_key"]))

    def test_rotate_keeps_old_key_verify_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            old = ensure_keypair(ws)
            sig = sign(ws, {"n": 1})
            new = rotate_key(ws)
            self.assertNotEqual(old["fingerprint"], new["fingerprint"])
            # retired keys verify but the new key signs
            self.assertTrue(verify(ws, {"n": 1}, sig))
            fresh = sign(ws, {"n": 2})
            self.assertEqual(fresh["fingerprint"], new["fingerprint"])

    def test_trust_filtering(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            register_peer(ws, "p1", "a" * 32, trust="peer")
            register_peer(ws, "p2", "b" * 32, trust="quarantined")
            self.assertEqual(len(trusted(ws)), 1)
            self.assertEqual(len(trusted(ws, min_trust="quarantined")), 2)
            with self.assertRaises(ValueError):
                register_peer(ws, "p3", "c" * 32, trust="boss")


class ExchangeTests(unittest.TestCase):
    def test_confidence_moves_with_corroboration(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            sha = "abc123"
            self.assertEqual(confidence(ws, sha), 0.5)
            corroborate(ws, sha, True, provider="peer-a")
            corroborate(ws, sha, True, provider="peer-b")
            self.assertEqual(confidence(ws, sha), 0.7)
            corroborate(ws, sha, False, provider="peer-c")
            self.assertEqual(confidence(ws, sha), 0.6)

    def test_canonical_dedup(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            title, content = "Durable rule", "always verify before applying changes"
            r1 = adopt(ws, title, content, origin="inst-a")
            self.assertFalse(r1["deduped"])
            r2 = adopt(ws, title, content + " (near-identical)", origin="inst-b")
            self.assertTrue(r2["deduped"])
            self.assertEqual(r2["canonical"], canonical_key(title, content))
            self.assertIsNotNone(find_canonical(ws, title, content))

    def test_provenance_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            env = {"origin": {"instance": "a", "fingerprint": "f1"},
                   "content_sha": "x" * 40,
                   "provenance": {"federation_history": [
                       {"from": "a", "to": "b"}, {"from": "b", "to": "c"}]}}
            ok, issues = provenance_intact(env, min_hops=3)
            self.assertTrue(ok)
            hop = record_hop(ws, env, "d")
            self.assertEqual(hop["provenance"]["federation_history"][-1]["to"], "d")


class SwarmTests(unittest.TestCase):
    def test_corroboration_resolves_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            rec = dispatch(ws, {"candidate_sha": "c1"}, peers=["p1", "p2", "p3"])
            report_verdict(ws, rec["id"], "p1", "c1", "pass")
            report_verdict(ws, rec["id"], "p2", "c1", "pass")
            final = report_verdict(ws, rec["id"], "p3", "c1", "fail")
            self.assertEqual(final["status"], "verified")
            self.assertIn("corroborated_by", final)
            # corroboration raised confidence in the exchange ledger
            self.assertEqual(confidence(ws, "c1"), 0.7)

    def test_reconcile_divergence(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            rec = dispatch(ws, {"candidate_sha": "c2"}, peers=["p1", "p2"])
            report_verdict(ws, rec["id"], "p1", "c2", "pass")
            final = report_verdict(ws, rec["id"], "p2", "c2", "fail")
            self.assertEqual(final["status"], "verified")
            self.assertIn("reconciled", final)

    def test_fail_peer_redistributes(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            rec = dispatch(ws, {"x": 1}, peers=["p1", "p2"])
            rec = fail_peer(ws, rec["id"], "p1")
            self.assertEqual(rec["status"], "redistributed")
            rec = fail_peer(ws, rec["id"], "p2")
            self.assertEqual(rec["status"], "failed")
            self.assertEqual(swarm_status(ws)["dispatches"], 1)


class PopgovTests(unittest.TestCase):
    def test_local_policy_wins(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            (ws / "rack" / "policy.json").write_text(
                '{"version": 1, "ceiling_usd": 0.10}')
            rec = publish_rules(ws, {"ceiling_usd": 5.0}, origin="foreign")
            result = adopt_rules(ws, rec["rule_sha"])
            self.assertTrue(result["adopted"])
            self.assertIn("ceiling_usd", result["conflicts"])
            self.assertEqual(result["resolution"], "local-policy-wins")

    def test_quorum_resolves(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            require_quorum(ws, "approval-1", quorum=2)
            cast_vote(ws, "approval-1", "peer-a", "approve")
            r = cast_vote(ws, "approval-1", "peer-b", "approve")
            self.assertTrue(r["resolved"])
            self.assertTrue(r["decision"])
            self.assertEqual(r["approves"], 2)

    def test_divergence_deterministic(self):
        a = {"rule_sha": "aaa", "adopted": "2026-01-02T00:00:00Z",
             "ratification_history": [1]}
        b = {"rule_sha": "bbb", "adopted": "2026-01-03T00:00:00Z",
             "ratification_history": [1]}
        self.assertEqual(resolve_rule_divergence(a, b), b)


class ResilienceTests(unittest.TestCase):
    def test_churn_and_partition(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            peer_join(ws, "p1")
            peer_join(ws, "p2")
            enter_partition(ws, ["p2"])
            reconcile_partition(ws, ["p2"])
            kinds = read_jsonl(Path(ws) / "rack" / "resilience" / "events.jsonl")
            self.assertEqual(len(kinds), 4)

    def test_fork_merge_preserves_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            a = {"rule_sha": "a" * 64, "adopted": "2026-01-01T00:00:00Z",
                 "ratification_history": [{"by": "x"}]}
            b = {"rule_sha": "b" * 64, "adopted": "2026-02-01T00:00:00Z",
                 "ratification_history": [{"by": "y"}]}
            result = merge_fork(ws, a, b, forked_from="orig")
            self.assertEqual(result["merged"]["rule_sha"], "b" * 64)
            self.assertEqual(result["preserved"], ["a", "b"])

    def test_survival_drill_empty_consistent(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            ok, info = survival_drill(ws, leader="p1", kill_peers=["p2"])
            self.assertTrue(ok)
            self.assertEqual(info["stuck_dispatches"], [])


if __name__ == "__main__":
    unittest.main()
