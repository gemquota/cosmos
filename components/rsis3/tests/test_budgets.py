"""Phase 8 — cost budgets: per-loop daily limits, budget_hit events."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.budgets import (
    budget_status, check_budget, daily_limit, ensure_budgets,
    load_budgets, save_budgets, spend_by_agent,
)


def ws_with_costs(tmp: str, costs=((1786291200, "evaluator", 0.01),
                                   (1786291200, "identity", 0.005))):
    """1786291200 = 2026-08-09 UTC day boundary."""
    root = Path(tmp)
    rsis = root / ".rsis"
    rsis.mkdir(parents=True)
    with (rsis / "costs.jsonl").open("w") as fh:
        for ts, agent, cost in costs:
            fh.write(json.dumps({"kind": "llm", "agent": agent, "cost": cost,
                                 "ts": ts}) + "\n")
    return root


class BudgetTests(unittest.TestCase):
    def test_defaults_and_persist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp)
            data = ensure_budgets(root)
            self.assertEqual(data["version"], 1)
            self.assertTrue((root / ".rsis" / "budgets.json").is_file())
            self.assertEqual(load_budgets(root)["ceiling_usd"], 0.50)

    def test_spend_by_agent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp)
            spend = spend_by_agent(root, day="2026-08-09")
            self.assertAlmostEqual(spend["evaluator"], 0.01)
            self.assertAlmostEqual(spend["identity"], 0.005)

    def test_daily_limit_per_loop_and_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp)
            save_budgets(root, {"per_loop": {"evaluator": {"daily_usd": 0.05}},
                                "default_daily_usd": 0.02,
                                "ceiling_usd": 0.5})
            self.assertEqual(daily_limit(load_budgets(root), "evaluator"), 0.05)
            self.assertEqual(daily_limit(load_budgets(root), "identity"), 0.02)

    def test_check_budget_blocks_when_over(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp, costs=((1786291200, "evaluator", 0.03),))
            save_budgets(root, {"per_loop": {"evaluator": {"daily_usd": 0.02}},
                                "default_daily_usd": 0.02,
                                "ceiling_usd": 0.5})
            res = check_budget(root, "evaluator")
            self.assertFalse(res["allowed"])
            self.assertAlmostEqual(res["spend"], 0.03)
            # budget_hit event was recorded
            hits = json.loads(
                (root / ".rsis" / "budget_hits.jsonl")
                .read_text().splitlines()[0])
            self.assertEqual(hits["kind"], "cost.budget_hit")

    def test_check_budget_allows_under_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp, costs=((1786291200, "evaluator", 0.005),))
            save_budgets(root, {"per_loop": {}, "default_daily_usd": 0.02,
                                "ceiling_usd": 0.5})
            self.assertTrue(check_budget(root, "evaluator")["allowed"])

    def test_budget_status_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_costs(tmp)
            save_budgets(root, {"per_loop": {"evaluator": {"daily_usd": 0.05}},
                                "default_daily_usd": 0.02,
                                "ceiling_usd": 0.5})
            st = budget_status(root)
            self.assertIn("per_loop", st)
            self.assertIn("evaluator", st["per_loop"])
            self.assertIn("remaining", st)


if __name__ == "__main__":
    unittest.main()
