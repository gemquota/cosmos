"""Exit-criterion validation windows — P4 24h -> P5 7-day tracking."""
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from rsis.validation import (
    WINDOWS, checkin, evidence, main, start, status, windows_path,
)


def make_ws(tmp: str) -> Path:
    root = Path(tmp) / "ws"
    (root / "rack").mkdir(parents=True)
    (root / ".rsis").mkdir(parents=True)
    (root.parent / "mykb" / "wiki" / "syntheses").mkdir(parents=True)
    return root


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def seed_evidence(ws: Path, started_at: datetime, cards: int = 400,
                  summary_days=("yesterday", "today")):
    """Fabricate passable evidence since started_at."""
    cycles = ws / "rack" / "bridge" / "cycles"
    cycles.mkdir(parents=True, exist_ok=True)
    day = started_at.strftime("%Y-%m-%d")
    with (cycles / f"{day}.jsonl").open("w") as fh:
        for i in range(cards):
            fh.write(json.dumps({
                "id": f"c{i}", "ts": iso(started_at + timedelta(minutes=i)),
                "cycle": i, "status": "complete", "rc": 0}) + "\n")
    with (ws / ".rsis" / "costs.jsonl").open("w") as fh:
        fh.write(json.dumps({"kind": "llm", "agent": "evaluator",
                             "cost": 0.01, "ts": iso(started_at)}) + "\n")
    mykb = ws.parent / "mykb" / "wiki" / "syntheses"
    dates = {"yesterday": started_at, "today": started_at + timedelta(days=1)}
    for key in summary_days:
        d = dates[key].strftime("%Y-%m-%d")
        (mykb / f"rsis3-daily-summary-{d}.md").write_text("# summary\n")
    (ws / "rack" / "cycle-daemon.lock").write_text("999999999\n")


class ValidationTests(unittest.TestCase):
    def test_start_creates_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            win = start(ws, "p4-24h")
            self.assertEqual(win["kind"], "p4-24h")
            self.assertEqual(win["status"], "running")
            self.assertEqual(win["hours"], WINDOWS["p4-24h"]["hours"])
            self.assertTrue(windows_path(ws).is_file())
            self.assertIn("ends_at", win)
            # idempotent: starting the same kind returns the same window
            self.assertEqual(start(ws, "p4-24h")["id"], win["id"])

    def test_checkin_no_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            res = checkin(ws)
            self.assertIsNone(res["checkin"])
            self.assertIn("no running window", res["note"])

    def test_checkin_baseline_records_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            win = start(ws, "p4-24h")
            res = checkin(ws)
            rec = res["checkin"]
            self.assertIsNotNone(rec)
            self.assertIn("evidence", rec)
            self.assertIn("criteria", rec)
            self.assertEqual(len(rec["criteria"]), 7)
            self.assertIn("lockfile", {r["id"]: r for r in rec["criteria"]})
            self.assertIn("id", win)

    def test_p4_completes_and_advances_to_p5(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            win = start(ws, "p4-24h")
            # backdate the window so it has ended (25h ago)
            started = (datetime.now(timezone.utc) -
           timedelta(hours=25)).replace(microsecond=0)
            recs = json.loads(windows_path(ws).read_text())
            w = recs["windows"][0]
            w["started_at"] = iso(started)
            w["ends_at"] = iso(started + timedelta(hours=24))
            windows_path(ws).write_text(json.dumps(recs))
            seed_evidence(ws, started)
            res = checkin(ws)
            self.assertTrue(res["checkin"]["all_pass"])
            self.assertTrue(res["checkin"]["window_ended"])
            data = json.loads(windows_path(ws).read_text())
            p4 = [x for x in data["windows"] if x["kind"] == "p4-24h"][-1]
            p5 = [x for x in data["windows"] if x["kind"] == "p5-7d"][-1]
            self.assertEqual(p4["status"], "completed")
            self.assertIsNotNone(p4["completed_at"])
            # P5 starts cleanly at P4's completion timestamp
            self.assertEqual(p5["status"], "running")
            self.assertEqual(p5["started_at"], p4["completed_at"])

    def test_status_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            start(ws, "p4-24h")
            rows = status(ws)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["kind"], "p4-24h")
            self.assertIn("remaining_h", rows[0])
            self.assertIn("elapsed_h", rows[0])

    def test_main_json_start(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            self.assertEqual(main(ws, action="start", json_out=True), 0)
            self.assertTrue(windows_path(ws).is_file())


if __name__ == "__main__":
    unittest.main()
