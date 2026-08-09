"""Phase 5 — nightly summary tests (daily MyKB note)."""
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from rsis.nightly import summarize_day, write_nightly_note

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def make_workspace(tmp: Path):
    ws = tmp / "ws"
    (ws / ".rsis" / "telemetry").mkdir(parents=True)
    now = datetime.now(timezone.utc)
    events = []
    for cycle in range(3):
        for loop in ("l1", "l2", "l3", "l5"):
            events.append({
                "type": f"{loop}_start", "cycle": cycle,
                "timestamp": (now - timedelta(hours=1)).isoformat()})
            events.append({
                "type": f"{loop}_complete", "cycle": cycle, "changed": True,
                "timestamp": (now - timedelta(minutes=59)).isoformat()})
    events.append({"type": "l7_complete", "changed": False,
                   "timestamp": (now - timedelta(minutes=30)).isoformat()})
    (ws / ".rsis" / "telemetry" / "000.jsonl").write_text(
        "\n".join(json.dumps(e) for e in events) + "\n")
    (ws / ".rsis" / "strategies.json").write_text(json.dumps({
        "generation": 12,
        "population": [{"id": "s1", "fitness": 0.244}],
    }))
    (ws / ".rsis" / "knowledge_graph.json").write_text(json.dumps({
        "nodes": [{"id": "n1"}, {"id": "n2"}], "edges": [{"s": "n1", "t": "n2"}],
    }))
    (ws / ".rsis" / "costs.jsonl").write_text(json.dumps({
        "kind": "llm", "cost": 0.0005, "tokens_in": 100, "tokens_out": 50,
        "ts": now.timestamp(),
    }) + "\n")
    return ws


class NightlyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.ws = make_workspace(self.tmp)
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "syntheses").mkdir(parents=True)
        (self.mykb / "log.md").write_text("# Bundle Log\n")

    def tearDown(self):
        self._tmp.cleanup()

    def test_summarize_day_counts(self):
        summary = summarize_day(self.ws, self.mykb, day=TODAY)
        self.assertEqual(summary["cycles"], 3)
        self.assertEqual(summary["events"], 25)
        self.assertEqual(summary["noops"], 1)
        self.assertEqual(summary["strategies"]["best_fitness"], 0.244)
        self.assertEqual(summary["kg"], {"nodes": 2, "edges": 1})
        self.assertEqual(summary["costs"]["traces"], 1)
        self.assertEqual(summary["costs"]["cost"], 0.0005)

    def test_note_written_once_and_log_appended(self):
        summary = summarize_day(self.ws, self.mykb, day=TODAY)
        p1 = write_nightly_note(self.mykb, summary)
        self.assertTrue(p1.is_file())
        text = p1.read_text()
        self.assertIn('type: "synthesis"', text)
        self.assertIn("daily summary", text.lower())
        self.assertIn("## " + TODAY, (self.mykb / "log.md").read_text())
        # create-only: second write returns the same path, no duplication
        p2 = write_nightly_note(self.mykb, summary)
        self.assertEqual(p1, p2)
        self.assertEqual(p1.read_text(), text)
        self.assertEqual(
            (self.mykb / "log.md").read_text().count("## " + TODAY), 1)


if __name__ == "__main__":
    unittest.main()
