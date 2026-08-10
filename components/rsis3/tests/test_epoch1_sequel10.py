"""Epoch 1, Sequel X (Phases 46–50) — Epoch-Scale Intelligence."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.epoch import capstone_check, decade_program, registry as epoch_registry
from rsis.experiments import assign, complete, start, status as exp_status
from rsis.failures import archive, cluster, record_nearmiss, status as fail_status
from rsis.longitudinal import define_study, snapshot, status as lng_status, trend_report
from rsis.metainvariant import attest_proof, check_reachable, properties


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


class LongitudinalTests(unittest.TestCase):
    def test_snapshot_study_trend(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            snapshot(ws, {"fitness": 0.5, "cost": 0.01})
            snapshot(ws, {"fitness": 0.7, "cost": 0.02})
            define_study(ws, "s1", "fitness rises", ["fitness"], window_days=90)
            report = trend_report(ws, "fitness")
            self.assertEqual(report["samples"], 2)
            self.assertGreater(report["trend_slope"], 0)
            self.assertEqual(lng_status(ws)["snapshots"], 2)


class ExperimentsTests(unittest.TestCase):
    def test_completed_with_guardrails(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            x = start(ws, "tuning-a", "l2_attempts", control=3, treatment=5,
                      min_sample=1, seed=7)
            for i in range(20):
                assign(ws, x["id"], f"unit-{i}")
            done = complete(ws, x["id"], {"result": 0.12})
            self.assertEqual(done["status"], "completed")
            self.assertTrue(done["guardrails"]["sample_ok"])
            self.assertTrue(done["significant"])
            self.assertEqual(exp_status(ws)["completed"], 1)

    def test_terminated_when_undersized(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            x = start(ws, "tuning-b", "budget", control=1, treatment=2,
                      min_sample=10)
            for i in range(3):
                assign(ws, x["id"], f"u{i}")
            done = complete(ws, x["id"], {"result": 0.01})
            self.assertEqual(done["status"], "terminated")
            self.assertFalse(done["guardrails"]["sample_ok"])
            self.assertEqual(exp_status(ws)["terminated"], 1)


class FailuresTests(unittest.TestCase):
    def test_corpus_cluster_nearmiss(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            archive(ws, "inc-1", "budget file lock contention", "flock",
                    "parallel writes", "use atomic replace")
            archive(ws, "inc-2", "budget file lock contention", "flock",
                    "daemon overlap", "serialize writers")
            cl = cluster(ws)
            self.assertEqual(cl["recurring"], 1)
            record_nearmiss(ws, "budgets", "lock acquired just in time")
            self.assertEqual(fail_status(ws)["nearmisses"], 1)


class MetainvariantTests(unittest.TestCase):
    def test_properties_exist(self):
        props = properties()
        self.assertIn("P1", props)
        self.assertIn("assumptions", props)

    def test_reachable_ok_when_no_relaxation(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            result = check_reachable(ws, [
                {"from": {"ceiling_usd": 1.0}, "to": {"ceiling_usd": 1.0},
                 "label": "noop"},
                {"from": {"ceiling_usd": 1.0}, "to": {"ceiling_usd": 2.0},
                 "label": "tighten"},
            ])
            self.assertTrue(result["ok"])
            self.assertEqual(result["violations"], [])

    def test_reachable_detects_relaxation(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            result = check_reachable(ws, [
                {"from": {"ceiling_usd": 1.0}, "to": {"ceiling_usd": 0.5},
                 "label": "relax"},
            ])
            self.assertFalse(result["ok"])
            self.assertTrue(any("P1" in v for v in result["violations"]))

    def test_attest_proof(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            check_reachable(ws, [{"from": {"ceiling_usd": 1.0},
                                  "to": {"ceiling_usd": 1.0}, "label": "noop"}])
            out = attest_proof(ws)
            self.assertTrue(out["attested"])
            self.assertTrue(out["commons_sha"])


class EpochTests(unittest.TestCase):
    def test_decade_program_and_registry(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            program = decade_program(ws, ratified_by="approver")
            self.assertEqual(program["years"], 10)
            self.assertEqual(program["status"], "active")
            reg = epoch_registry(ws, phases=[
                {"n": 1, "status": "delivered"},
            ], arcs=[{"sequel": "I", "phases": "1–5"}])
            self.assertEqual(len(reg["epochs"]), 2)
            self.assertEqual(reg["phases"][0]["n"], 1)
            saved = json.loads((ws / "rack" / "epochs.json").read_text())
            self.assertEqual(saved["invariant"],
                             "autonomy is cumulative but never unconditional")

    def test_capstone_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            decade_program(ws)
            result = capstone_check(ws)
            self.assertIn("guardrails_ok", result)
            self.assertIn("attestation_chain", result)
            self.assertIn("decade_program", result)


if __name__ == "__main__":
    unittest.main()
