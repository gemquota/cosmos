"""Epoch 1, Sequel IX (Phases 41–45) — Global Commons."""
import tempfile
import unittest
from pathlib import Path

from rsis.archival import register as archival_register
from rsis.commons import adopt, attribution_report, publish
from rsis.crisis import drill, enter, exit_crisis, status as crisis_status
from rsis.diplomacy import (
    dispute, resolve, sign_treaty, status as diplomacy_status, trust_level,
)
from rsis.planetary import health, resource_plan
from rsis.standards import (
    conformance_status, deprecate, register_version,
)


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


class StandardsTests(unittest.TestCase):
    def test_register_and_deprecate(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            register_version(ws, "cosmos-protocol", "2", status="current")
            cs = conformance_status(ws)
            entry = next(s for s in cs["standards"]
                         if s["id"] == "cosmos-protocol")
            self.assertIn("2", entry["versions"])
            self.assertTrue(deprecate(ws, "cosmos-protocol", "1",
                                      sunset="2030-01-01"))
            self.assertEqual(len(conformance_status(ws)["sunset_calendar"]), 1)
            self.assertFalse(deprecate(ws, "nope", "9", "2030-01-01"))


class CommonsTests(unittest.TestCase):
    def test_publish_adopt_attribution(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            item = publish(ws, "Synthesis A", "durable rule", origin="inst-1",
                           contributor="producer")
            self.assertFalse(item.get("duplicate"))
            self.assertEqual(item["license"], "cc-by-4.0")
            dup = publish(ws, "Synthesis A", "durable rule", origin="inst-2")
            self.assertTrue(dup["duplicate"])
            res = adopt(ws, item["sha"], adopter="inst-3")
            self.assertTrue(res["adopted"])
            report = attribution_report(ws)
            self.assertTrue(report["attribution_ok"])
            self.assertEqual(report["ledger_records"], 2)


class DiplomacyTests(unittest.TestCase):
    def test_treaty_levels_and_disputes(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            sign_treaty(ws, "pop-b", terms={"read": True}, level="allies")
            tl = trust_level(ws, "pop-b")
            self.assertEqual(tl["level"], "allies")
            self.assertIn("approve", tl["capabilities"])
            # no treaty -> quarantined with zero capabilities
            self.assertEqual(trust_level(ws, "unknown")["level"], "quarantined")
            dispute(ws, "pop-b", "0" * 64, "rule conflict")
            self.assertTrue(resolve(ws, "pop-b", "0" * 64, "quorum won"))
            self.assertEqual(diplomacy_status(ws)["open_disputes"], 0)

    def test_bad_level_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            with self.assertRaises(ValueError):
                sign_treaty(ws, "pop-c", {}, level="overlord")


class CrisisTests(unittest.TestCase):
    def test_enter_exit_and_drill(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            state = enter(ws, profile="default")
            self.assertTrue(state["active"])
            self.assertEqual(state["mode"]["writes"], "fail-closed")
            exited = exit_crisis(ws)
            self.assertFalse(exited["active"])
            ok, rec = drill(ws, scenario="default")
            self.assertTrue(ok)
            self.assertTrue(rec["policy_critical_kept"])
            self.assertEqual(crisis_status(ws)["drills"], 1)
            self.assertTrue(crisis_status(ws)["last_drill_ok"])

    def test_double_exit_noop(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            self.assertFalse(exit_crisis(ws)["ok"])


class PlanetaryTests(unittest.TestCase):
    def test_resource_plan_sovereign(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            p = resource_plan(ws, {"pop-a": 0.4, "pop-b": 0.6})
            self.assertTrue(p["local_policy_sovereign"])

    def test_health_ok_when_all_checks_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            (ws / "wiki" / "syntheses").mkdir(parents=True)
            (ws / "wiki" / "syntheses" / "n.md").write_text("x")
            archival_register(ws)
            publish(ws, "T", "content", origin="inst-1", contributor="c")
            sign_treaty(ws, "pop-b", {}, level="peers")
            h = health(ws)
            self.assertTrue(h["health_ok"])
            self.assertTrue(h["checks"]["attribution"])


if __name__ == "__main__":
    unittest.main()
