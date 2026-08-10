"""Phase 15 — long-horizon autonomy tests (seasons, energy, repair, review)."""
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

# Midday UTC of the current day — energy_mode reads today's budget spend.
_TODAY_TS = int(datetime.now(timezone.utc).replace(
    hour=12, minute=0, second=0, microsecond=0).timestamp())

from rsis.seasons import (
    adaptive_sleep, current_season, energy_mode, ensure_seasons, incident,
    quarterly_review, rotate, season_goals, self_repair,
)


def make_workspace(tmp: Path, improving=True):
    ws = tmp / "ws"
    ws.mkdir(parents=True)
    (ws / ".rsis").mkdir()
    (ws / "rack").mkdir()
    history = []
    for i in range(6):
        best = round(0.1 * (i + 1), 3) if improving else round(0.6 - 0.1 * i, 3)
        history.append({"generation": i, "best_fitness": best})
    (ws / ".rsis" / "strategies.json").write_text(json.dumps({
        "generation": 6, "history": history,
        "population": [{"id": "s1", "fitness": history[-1]["best_fitness"]}],
    }))
    return ws


class SeasonsTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.ws = make_workspace(self.tmp, improving=True)
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "syntheses").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def test_ensure_and_current_season(self):
        s = ensure_seasons(self.ws)
        self.assertEqual(s["name"], "output")
        self.assertEqual(s["season_id"], 0)
        self.assertTrue((self.ws / "rack" / "seasons.json").is_file())
        self.assertEqual(current_season(self.ws)["name"], "output")

    def test_rotate_force_cycles_domains(self):
        s = rotate(self.ws, force=True)
        self.assertEqual(s["season_id"], 1)
        self.assertEqual(s["name"], "communication")
        self.assertEqual(s["rotations"], 1)
        # cadence not met: no rotation
        s2 = rotate(self.ws)
        self.assertEqual(s2["season_id"], 1)
        # wraps around
        for _ in range(8):
            s = rotate(self.ws, force=True)
        self.assertEqual(s["season_id"], 2)
        self.assertTrue((self.ws / "rack" / "incidents.jsonl").is_file())

    def test_season_goals(self):
        goals = season_goals(self.ws)
        self.assertEqual(len(goals), 3)
        self.assertTrue(any("output" in g for g in goals))

    def test_energy_mode_improving(self):
        self.assertEqual(energy_mode(self.ws), "sprint")

    def test_energy_mode_budget_pause(self):
        # spend past the ceiling → fail-close pause
        (self.ws / ".rsis" / "budgets.json").write_text(json.dumps({
            "version": 1, "default_daily_usd": 0.10, "ceiling_usd": 0.05,
            "per_loop": {}}))
        with (self.ws / ".rsis" / "costs.jsonl").open("w") as fh:
            fh.write(json.dumps({"kind": "llm", "agent": "evaluator",
                                 "cost": 0.04, "ts": _TODAY_TS}) + "\n")
            fh.write(json.dumps({"kind": "llm", "agent": "evaluator",
                                 "cost": 0.04, "ts": _TODAY_TS}) + "\n")
        self.assertEqual(energy_mode(self.ws), "pause")

    def test_adaptive_sleep_factors(self):
        # record an improving forecast → Phase 10 shrinks cadence (0.7x),
        # sprint mode keeps the factor at 1.0
        from rsis.forecast import predict, record
        record(self.ws, predict(self.ws))
        base = adaptive_sleep(self.ws, 180)
        self.assertLessEqual(base, 126)
        # declining workspace → idle
        ws2 = make_workspace(self.tmp / "ws2", improving=False)
        self.assertEqual(energy_mode(ws2), "idle")

    def test_self_repair_reports_incidents(self):
        # stale lock + kg dupes → repairable; incidents logged
        (self.ws / "rack" / "cycle-daemon.lock").write_text("999999")
        (self.ws / ".rsis" / "knowledge_graph.json").write_text(
            json.dumps({"nodes": [{"id": "n1"}, {"id": "n1"}]}))
        incidents = self_repair(self.ws, self.mykb)
        kinds = {i["kind"] for i in incidents}
        self.assertIn("self-repair", kinds)
        self.assertFalse((self.ws / "rack" / "cycle-daemon.lock").exists())

    def test_incident_log(self):
        rec = incident(self.ws, "test", "boom")
        self.assertEqual(rec["kind"], "test")
        log = (self.ws / "rack" / "incidents.jsonl").read_text()
        self.assertIn("boom", log)

    def test_quarterly_review_stages_proposal(self):
        r = quarterly_review(self.ws, self.mykb)
        self.assertIn("proposal_id", r)
        self.assertEqual(r["nightlies"], 0)
        approvals = self.ws / "rack" / "approvals"
        self.assertTrue(list(approvals.glob("*.json")))
        rec = json.loads(next(approvals.glob("*.json")).read_text())
        self.assertEqual(rec["status"], "staged")
        self.assertIn("rack/policy.json", rec["target_files"])


if __name__ == "__main__":
    unittest.main()
