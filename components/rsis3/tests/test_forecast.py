"""Phase 10 — self-model forecasting tests (predict, verify, quality, cadence)."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.forecast import (
    adaptive_interval, main, predict, quality, record, verify,
)


def make_workspace(tmp: Path, improving=True, telemetry=True):
    """Workspace with strategy history; optionally improving fitness."""
    ws = tmp / "ws"
    ws.mkdir()
    (ws / ".rsis").mkdir()
    history = []
    for i in range(6):
        best = round(0.1 * (i + 1), 3) if improving else 0.05
        history.append({"generation": i, "avg_fitness": 0.05,
                        "best_fitness": best, "population": 2,
                        "accepted": True})
    (ws / ".rsis" / "strategies.json").write_text(json.dumps({
        "generation": 6, "history": history,
        "population": [{"id": "s1", "fitness": history[-1]["best_fitness"]}],
    }))
    if telemetry:
        tel = ws / ".rsis" / "telemetry"
        tel.mkdir()
        lines = [json.dumps({"type": f"{loop}_{kind}",
                             "timestamp": "2026-08-09T12:00:00+00:00"})
                 for loop in ("l1", "l2", "l3")
                 for kind in ("start", "complete")]
        (tel / "000.jsonl").write_text("\n".join(lines) + "\n")
    return ws


class ForecastTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_predict_improving_trend_and_band(self):
        ws = make_workspace(self.tmp, improving=True)
        fc = predict(ws)
        self.assertTrue(fc["available"])
        self.assertEqual(fc["trend"], "improving")
        self.assertGreater(fc["fitness"]["predicted"], 0.6)
        self.assertLess(fc["fitness"]["low"], fc["fitness"]["predicted"])
        self.assertGreater(fc["fitness"]["high"], fc["fitness"]["predicted"])
        self.assertGreater(fc["fitness"]["band"], 0)
        self.assertEqual(fc["success_rate"], 1.0)

    def test_predict_no_history(self):
        ws = self.tmp / "empty"
        ws.mkdir()
        (ws / ".rsis").mkdir()
        (ws / ".rsis" / "strategies.json").write_text("{}")
        fc = predict(ws)
        self.assertFalse(fc["available"])

    def test_record_verify_and_quality(self):
        ws = make_workspace(self.tmp, improving=True)
        fc = predict(ws)
        record(ws, fc)
        v = verify(ws)
        self.assertEqual(v["verified"], 1)
        self.assertEqual(v["hits"], 1)
        self.assertEqual(v["coverage"], 1.0)
        q = quality(ws)
        self.assertEqual(q["verified"], 1)
        self.assertIn("calibration", q)
        self.assertIn("bias", q)
        self.assertIn("degradation", q)

    def test_verify_miss(self):
        ws = make_workspace(self.tmp, improving=False)
        fc = predict(ws)
        fc["fitness"] = {"predicted": 99.0, "band": 0.1,
                         "low": 98.9, "high": 99.1}
        record(ws, fc)
        v = verify(ws)
        self.assertEqual(v["misses"], 1)
        self.assertEqual(v["coverage"], 0.0)

    def test_adaptive_interval(self):
        ws = make_workspace(self.tmp, improving=True)
        fc = predict(ws)
        record(ws, fc)
        self.assertEqual(adaptive_interval(ws, 180), 125)
        fc["trend"] = "declining"
        record(ws, fc)
        self.assertEqual(adaptive_interval(ws, 180), 234)
        fc["trend"] = "plateau"
        record(ws, fc)
        self.assertEqual(adaptive_interval(ws, 180), 198)
        # base is clamped to [120, 300] before the cadence factor applies
        self.assertEqual(adaptive_interval(ws, 50), 132)
        self.assertEqual(adaptive_interval(ws, 1000), 300)

    def test_adaptive_interval_no_forecast(self):
        ws = self.tmp / "bare"
        ws.mkdir()
        self.assertEqual(adaptive_interval(ws, 180), 180)

    def test_main_smoke(self):
        ws = make_workspace(self.tmp, improving=True)
        self.assertEqual(main(ws, do_verify=True), 0)
        ledger = ws / "rack" / "forecasts" / "forecasts.jsonl"
        self.assertTrue(ledger.is_file())
        self.assertEqual(len(ledger.read_text().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
