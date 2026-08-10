"""Phase 8 — anomaly policy: telemetry regression scan + retention prune."""
import json
import tempfile
import time
import unittest
from pathlib import Path

from rsis.anomalies import file_backlog, prune, scan


def ws_with_telemetry(tmp: str, events=None):
    root = Path(tmp)
    tel = root / ".rsis" / "telemetry"
    tel.mkdir(parents=True)
    if events is None:
        events = [
            {"type": "l2_start", "metadata": {}},
            {"type": "l2_complete", "metadata": {"duration_s": 1.0}},
        ]
    with (tel / "000.jsonl").open("w") as fh:
        for e in events:
            fh.write(json.dumps(e) + "\n")
    return root


class AnomalyScanTests(unittest.TestCase):
    def test_missing_completion_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_telemetry(tmp, [
                {"type": "l1_start", "metadata": {}},
                {"type": "l1_start", "metadata": {}},
            ])
            anomalies = scan(root)
            kinds = {a["kind"] for a in anomalies}
            self.assertIn("missing_telemetry", kinds)

    def test_success_drop_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_telemetry(tmp, [
                {"type": "l1_start", "metadata": {}},
                {"type": "l1_start", "metadata": {}},
                {"type": "l1_complete", "metadata": {}},
            ])
            kinds = {a["kind"] for a in scan(root)}
            self.assertIn("success_drop", kinds)

    def test_empty_window_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = ws_with_telemetry(tmp, [])
            anomalies = scan(root)
            self.assertEqual(anomalies[0]["kind"], "missing_telemetry")

    def test_duration_spike(self):
        with tempfile.TemporaryDirectory() as tmp:
            events = [{"type": "l3_start", "metadata": {}}]
            for i in range(6):
                events.append({"type": "l3_complete",
                               "metadata": {"duration_s": 1.0}})
            events.append({"type": "l3_complete",
                           "metadata": {"duration_s": 99.0}})
            root = ws_with_telemetry(tmp, events)
            kinds = {a["kind"] for a in scan(root)}
            self.assertIn("duration_spike", kinds)

    def test_backlog_note_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            mykb = root / "mykb"
            (mykb / "wiki" / "backlog").mkdir(parents=True)
            path = file_backlog(mykb, [{"loop": "l2", "kind": "success_drop",
                                        "severity": "medium", "detail": "x"}])
            self.assertIsNotNone(path)
            self.assertIn("anomalies", path.read_text())


class PruneTests(unittest.TestCase):
    def test_prune_archives_old_telemetry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tel = root / ".rsis" / "telemetry"
            tel.mkdir(parents=True)
            old = tel / "old.jsonl"
            old.write_text("{}")
            # backdate the file beyond the retention window
            old_ts = time.time() - 20 * 86400
            import os
            os.utime(old, (old_ts, old_ts))
            res = prune(root, retention_days=7)
            self.assertEqual(res["archived"], 1)
            self.assertFalse(old.exists())
            self.assertTrue(list((root / "rack" / "archive").glob("*.tar.gz")))


if __name__ == "__main__":
    unittest.main()
