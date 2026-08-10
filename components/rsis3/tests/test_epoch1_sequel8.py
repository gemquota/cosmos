"""Epoch 1, Sequel VIII (Phases 36–40) — Collaborative Governance."""
import json
import tempfile
import time
import unittest
from pathlib import Path

from rsis.codesign import (
    add_artifact, create_canvas, goal_from_merge, merge,
    status as codesign_status,
)
from rsis.delegation import check, execute, issue, revoke, status as dlg_status
from rsis.explain import (
    counterfactual, load_latest, record_rationale, render,
)
from rsis.nlpolicy import apply, compile_rule, compile_rules, roundtrip
from rsis.policy import load_policy
from rsis.trust import metrics, recalibrate, record_outcome


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


def seed_verification_ledger(ws: Path, candidate_sha: str) -> None:
    vdir = ws / "rack" / "verification"
    vdir.mkdir(parents=True, exist_ok=True)
    rec = {
        "candidate_sha": candidate_sha,
        "gates": [
            {"name": "path_safety", "passed": True},
            {"name": "compilation", "passed": True},
            {"name": "contracts", "passed": False, "notes": "contracts: 1 fail"},
        ],
        "scores": {"fitness": 0.7},
        "artifacts": ["diff.patch"],
        "pre_digests": {"rack/policy.json": "abc"},
    }
    with (vdir / "ledger.jsonl").open("a") as fh:
        fh.write(json.dumps(rec) + "\n")


class ExplainTests(unittest.TestCase):
    def test_rationale_three_depths(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            sha = "c" * 64
            seed_verification_ledger(ws, sha)
            rationale = record_rationale(ws, sha, decision="pass")
            self.assertIn("Applied after 2/3 gates passed", rationale["one_line"])
            self.assertIn("2/3 gates passed", rationale["paragraph"])
            self.assertIsNotNone(load_latest(ws))
            self.assertEqual(render(ws, "one_line"), rationale["one_line"])
            self.assertEqual(render(ws, "full"), json.dumps(
                rationale["trace"], indent=1, sort_keys=True))

    def test_counterfactual(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            sha = "d" * 64
            seed_verification_ledger(ws, sha)
            cf = counterfactual(ws, sha, "no approval gate")
            self.assertIn("passed gates", cf["would_have"])


class NlPolicyTests(unittest.TestCase):
    def test_compile_apply_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            rule = compile_rule("never spend more than $0.05 per day on evaluator")
            self.assertTrue(rule["compiled"])
            self.assertEqual(rule["policy_key"], "per_loop")
            back = roundtrip([rule])
            self.assertIn("Limit evaluator to $0.05 per day", back[0])
            n = apply(ws, [rule])
            self.assertEqual(n, 1)
            per_loop = load_policy(ws)["per_loop"]
            self.assertEqual(per_loop["evaluator"]["daily_usd"], 0.05)

    def test_conflict_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            apply(ws, [compile_rule("spend at most $2 per day")])
            res = compile_rules(ws, ["spend at most $5 per day"])
            self.assertEqual(len(res["conflicts"]), 1)
            self.assertEqual(res["conflicts"][0]["existing"], 2)

    def test_approval_path_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            rule = compile_rule("always ask before touching rack/policy.json")
            self.assertTrue(rule["compiled"])
            self.assertEqual(rule["policy_key"], "approval_required.paths")
            self.assertEqual(rule["value"], "rack/policy.json")
            apply(ws, [rule])
            paths = load_policy(ws)["approval_required"]["paths"]
            self.assertIn("rack/policy.json", paths)


class DelegationTests(unittest.TestCase):
    def test_bounds_and_revocation(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            expiry = int(time.time()) + 3600
            d = issue(ws, "agent-x", actions=["propose"], projects=["cosmos"],
                      budget=1.0, expiry_ts=expiry)
            ok, reason = check(ws, d["id"], "propose", "cosmos", cost=0.1)
            self.assertTrue(ok)
            r = execute(ws, d["id"], "propose", "cosmos", cost=0.1)
            self.assertTrue(r["executed"])
            # out-of-scope action fails closed
            r2 = execute(ws, d["id"], "approve", "cosmos")
            self.assertFalse(r2["executed"])
            self.assertEqual(r2["reason"], "action out of scope")
            # budget breach fails closed
            r3 = execute(ws, d["id"], "propose", "cosmos", cost=5.0)
            self.assertFalse(r3["executed"])
            self.assertEqual(r3["reason"], "budget exceeded")
            # revocation takes effect immediately
            self.assertTrue(revoke(ws, d["id"]))
            ok, reason = check(ws, d["id"], "propose", "cosmos")
            self.assertFalse(ok)
            self.assertEqual(reason, "revoked")
            self.assertEqual(dlg_status(ws)["revoked"], 1)

    def test_expired_delegation(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            d = issue(ws, "agent-y", actions=["read"], projects=["cosmos"],
                      budget=1.0, expiry_ts=int(time.time()) - 10)
            ok, reason = check(ws, d["id"], "read", "cosmos")
            self.assertFalse(ok)
            self.assertEqual(reason, "expired")


class TrustTests(unittest.TestCase):
    def test_over_trust_recalibrates(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            # acted when the human wanted to be asked -> over-trust
            for _ in range(3):
                record_outcome(ws, "alice", "apply", "cosmos",
                               asked=False, wanted_ask=True)
            m = metrics(ws)
            self.assertGreater(m["per_human"]["alice"]["over_trust"], 0.10)
            thresholds = recalibrate(ws)
            self.assertGreater(thresholds["by_human"]["alice"], 0.5)


class CodesignTests(unittest.TestCase):
    def test_merge_authorship_and_goal(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            create_canvas(ws, "engine", "Engine hardening")
            add_artifact(ws, "engine", "line one", author="human")
            add_artifact(ws, "engine", "line two", author="system")
            m = merge(ws, "engine", ["a0", "a1"], title="Joint plan")
            self.assertTrue(m["merged"])
            self.assertEqual(m["authorship"], {"human": 1, "system": 1})
            g = goal_from_merge(ws, "engine", m["id"])
            self.assertEqual(g["status"], "proposed")
            self.assertEqual(g["source"], "codesign:engine")
            s = codesign_status(ws, project="engine")
            self.assertEqual(s["artifacts"], 2)
            self.assertEqual(s["merged"], 1)


if __name__ == "__main__":
    unittest.main()
