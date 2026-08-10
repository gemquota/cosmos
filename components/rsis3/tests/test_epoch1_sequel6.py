"""Epoch 1, Sequel VI (Phases 26–30) — Governed Evolution."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.capacity import degradation_ladder, plan, sustainability
from rsis.endurance import continuity, guardrails
from rsis.goals import propose, ratify, record_fitness, status as goals_status
from rsis.metagov import (
    meta_invariant_check, propose as propose_policy, ratify as ratify_policy,
    score,
)
from rsis.policy import load_policy, save_policy
from rsis.steward import custody_action, handoff, monitor, onboard


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


class MetagovTests(unittest.TestCase):
    def test_score_blocks_relaxation(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            p = propose_policy(ws, {"ceiling_usd": -1},
                               "raise ceiling", ["incident-1"])
            s = score(ws, p["id"])
            self.assertEqual(s["verdict"], "block")
            self.assertIn("ceiling_usd", s["violations"])
            self.assertFalse(ratify_policy(ws, p["id"]))

    def test_ratify_applies_and_enforces(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            p = propose_policy(ws, {"ceiling_usd": 0.25},
                               "tighten ceiling", ["forecast"])
            s = score(ws, p["id"])
            self.assertEqual(s["verdict"], "ok")
            self.assertTrue(ratify_policy(ws, p["id"], actor="approver"))
            self.assertEqual(load_policy(ws)["ceiling_usd"], 0.25)
            # silently relaxing the ratified control is detected
            policy = load_policy(ws)
            policy["ceiling_usd"] = 0.10
            save_policy(ws, policy)
            ok, issues = meta_invariant_check(ws)
            self.assertFalse(ok)
            self.assertTrue(any("ceiling_usd" in i for i in issues))


class CapacityTests(unittest.TestCase):
    def test_plan_and_sustainability(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            p = plan(ws)
            self.assertEqual(p["horizon_days"], 90)
            self.assertEqual(p["daily_avg"], 0.0)
            s = sustainability(ws)
            self.assertEqual(s["total_spend"], 0.0)

    def test_degradation_ladder_keeps_policy_critical(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            for pressure in (1, 2, 3, 4):
                d = degradation_ladder(ws, pressure=pressure)
                self.assertIn("policy-critical", d["always_on"])
            # verification survives until the highest pressure band
            self.assertIn("verification",
                          degradation_ladder(ws, pressure=1)["always_on"])


class GoalsTests(unittest.TestCase):
    def test_ratify_merges_into_stack(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            g = propose(ws, "Harden bridge", "red-team gap",
                        expected_value="gate strength", source="redteam")
            self.assertTrue(ratify(ws, g["id"], actor="approver"))
            self.assertTrue(record_fitness(ws, g["id"], 0.8, cost=0.01))
            stack = json.loads((ws / "rack" / "goals_stack.json").read_text())
            self.assertEqual(len(stack["system_proposed"]), 1)
            self.assertEqual(goals_status(ws)["ratified"], 1)

    def test_unratified_never_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            propose(ws, "Skipped goal", "no approval")
            self.assertEqual(goals_status(ws)["ratified"], 0)


class StewardTests(unittest.TestCase):
    def test_monitor_and_custody(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            self.assertEqual(monitor(ws, ["nope"]), [])
            rec = custody_action(ws, "peer-x", "retune", "l2 params")
            self.assertTrue(rec["attested"])
            self.assertEqual(rec["action"], "retune")

    def test_onboard_and_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            ob = onboard(ws, repo="example/engine", name="engine")
            self.assertEqual(ob["kind"], "onboard")
            self.assertEqual(ob["repo"], "example/engine")
            h = handoff(ws, successor="heir-1", peer="peer-x")
            self.assertEqual(h["kind"], "handoff")


class EnduranceTests(unittest.TestCase):
    def test_guardrail_battery(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            g = guardrails(ws)
            self.assertIn("meta_invariant", g["checks"])
            self.assertIn("energy_ladder", g["checks"])
            self.assertIsInstance(g["ok"], bool)

    def test_continuity(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            c = continuity(ws)
            self.assertIn("identity", c)
            self.assertIn("attestations", c)


if __name__ == "__main__":
    unittest.main()
