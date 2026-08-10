"""Phase 4 — convergence monitor tests (plateaus, bound no-ops, proposals)."""
import json
import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from rsis.convergence import (
    detect, file_backlog_note, last_applied, main, _mark_applied,
    write_proposal,
)

RSIS3 = Path(__file__).resolve().parent.parent


def make_workspace(tmp: Path, plateau=True, noops=None):
    ws = tmp / "ws"
    ws.mkdir()
    (ws / ".rsis").mkdir()
    history = []
    for i in range(6):
        best = 0.064 if plateau else 0.1 * (i + 1)
        entry = {"generation": i, "avg_fitness": 0.05, "best_fitness": best,
                 "population": 2, "accepted": True}
        history.append(entry)
    (ws / ".rsis" / "strategies.json").write_text(json.dumps({
        "generation": 6, "history": history,
        "population": [{"id": "s1", "fitness": best}],
    }))
    if noops:
        tel = ws / ".rsis" / "telemetry"
        tel.mkdir()
        lines = []
        for loop, count in noops.items():
            for _ in range(count):
                lines.append(json.dumps({
                    "type": f"{loop}_complete", "changed": False,
                    "timestamp": "2026-08-08T12:00:00+00:00"}))
        (tel / "000.jsonl").write_text("\n".join(lines) + "\n")
    return ws


class ConvergenceTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "syntheses").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def test_plateau_detected(self):
        ws = make_workspace(self.tmp, plateau=True)
        rep = detect(ws, plateau_window=5)
        self.assertTrue(rep["detected"])
        self.assertEqual(rep["plateau"]["best_fitness"], 0.064)
        self.assertEqual(rep["proposed_loop"], "identity")
        self.assertEqual(rep["command"], "python -m rsis identity")

    def test_no_plateau_when_moving(self):
        ws = make_workspace(self.tmp, plateau=False)
        rep = detect(ws, plateau_window=5)
        self.assertIsNone(rep["plateau"])

    def test_bound_noops_propose_retune(self):
        ws = make_workspace(self.tmp, plateau=False, noops={"l7": 8})
        rep = detect(ws, noop_window=10, noop_threshold=8)
        self.assertTrue(rep["detected"])
        self.assertEqual(rep["proposed_loop"], "metacog")
        self.assertEqual(rep["noops"]["l7"], 8)

    def test_noop_below_threshold_ignored(self):
        ws = make_workspace(self.tmp, plateau=False, noops={"l6": 2})
        rep = detect(ws, noop_threshold=8)
        self.assertFalse(rep["detected"])

    def test_proposal_and_backlog_written_once(self):
        ws = make_workspace(self.tmp, plateau=True)
        code = main(ws, self.mykb, RSIS3, apply=False, json_out=True)
        self.assertEqual(code, 0)
        props = list((ws / "rack" / "proposals").glob("convergence-*.json"))
        self.assertEqual(len(props), 1)
        payload = json.loads(props[0].read_text())
        self.assertEqual(payload["type"], "convergence-proposal")
        self.assertFalse(payload["applied"])
        backlogs = list((self.mykb / "wiki" / "backlog").glob("convergence-*.md"))
        self.assertEqual(len(backlogs), 1)
        self.assertIn('type: "backlog"', backlogs[0].read_text())
        # create-only: second run writes nothing new
        main(ws, self.mykb, RSIS3, apply=False)
        self.assertEqual(len(list((ws / "rack" / "proposals").glob("*.json"))), 1)
        self.assertEqual(len(list((self.mykb / "wiki" / "backlog").glob("*.md"))), 1)

    def test_mark_and_last_applied(self):
        ws = make_workspace(self.tmp, plateau=True)
        self.assertIsNone(last_applied(ws))
        _mark_applied(ws, {"proposed_loop": "identity", "generation": 6})
        rec = last_applied(ws)
        self.assertEqual(rec["loop"], "identity")
        self.assertEqual(rec["generation"], 6)


if __name__ == "__main__":
    unittest.main()
