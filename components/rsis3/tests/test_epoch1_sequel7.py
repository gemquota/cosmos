"""Epoch 1, Sequel VII (Phases 31–35) — Intergenerational Continuity."""
import json
import os
import tempfile
import unittest
from pathlib import Path

from rsis.archival import (
    make_replica, migrate, patrol, register, status as archival_status,
)
from rsis.generations import (
    baseline, drift_check, scan_dependencies, scan_staleness,
)
from rsis.inheritance import adopt, export_bundle, parity_check
from rsis.identity import register_peer
from rsis.missions import checkpoint, create, handoff
from rsis.succession import plan, transfer


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / ".rsis").mkdir(parents=True)
    (root / "rack").mkdir(parents=True)
    return root


def make_mykb(tmp: str) -> Path:
    mykb = Path(tmp) / "mykb"
    (mykb / "wiki" / "syntheses").mkdir(parents=True)
    return mykb


class InheritanceTests(unittest.TestCase):
    def test_export_adopt_parity(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            mykb = make_mykb(tmp)
            note = mykb / "wiki" / "syntheses" / "epoch-1.md"
            note.write_text("# Epoch 1 curriculum\nkeep invariants green\n")
            bundle = export_bundle(ws, mykb)
            self.assertEqual(bundle["format"], "cosmos-inheritance/1")
            self.assertEqual(len(bundle["curriculum"]), 1)
            adopt(ws, bundle, mykb)
            parity, info = parity_check(ws, mykb)
            self.assertGreaterEqual(parity, 0.98)
            self.assertTrue(info["ok"])


class ArchivalTests(unittest.TestCase):
    def _setup(self, ws: Path) -> Path:
        (ws / "wiki" / "syntheses").mkdir(parents=True)
        note = ws / "wiki" / "syntheses" / "note.md"
        note.write_text("durable knowledge\n")
        return note

    def test_patrol_detects_and_rebuilds(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            note = self._setup(ws)
            register(ws)
            self.assertTrue(make_replica(ws, "wiki/syntheses/note.md"))
            note.write_text("tampered knowledge\n")
            rec = patrol(ws)
            self.assertIn("wiki/syntheses/note.md", rec["corrupt"])
            self.assertIn("wiki/syntheses/note.md", rec["rebuilt"])
            self.assertEqual(note.read_text(), "durable knowledge\n")

    def test_migrate_renames_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            self._setup(ws)
            register(ws)
            rec = migrate(ws, ".md", ".txt")
            self.assertIn("wiki/syntheses/note.md", rec["migrated"])
            self.assertTrue((ws / "wiki" / "syntheses" / "note.txt").is_file())

    def test_status_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            s = archival_status(ws)
            self.assertIn("tracked", s)
            self.assertEqual(s["replication_min"], 2)


class SuccessionTests(unittest.TestCase):
    def test_plan_and_transfer(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            p0 = plan(ws)
            self.assertEqual(p0["heirs"], [])
            register_peer(ws, "heir-1", "1" * 32, trust="trusted")
            p1 = plan(ws)
            self.assertEqual(len(p1["heirs"]), 1)
            bad = transfer(ws, p1["id"], "stranger")
            self.assertFalse(bad["ok"])
            good = transfer(ws, p1["id"], "heir-1")
            self.assertTrue(good["ok"])
            self.assertEqual(good["transfer"]["status"], "dual-running")


class MissionTests(unittest.TestCase):
    def test_contiguous_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            create(ws, "m1", "keep the loop green", steward="a")
            checkpoint(ws, "m1", "checkpoint one", progress=0.5)
            h = handoff(ws, "m1", "b", resume_seq=1)
            self.assertEqual(h["resume_seq"], 1)
            self.assertTrue(h["contiguous"])
            with self.assertRaises(ValueError):
                handoff(ws, "m1", "c", resume_seq=0)


class GenerationsTests(unittest.TestCase):
    def test_dependency_scan(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            baseline(ws, ["python2", "legacy-format"])
            flags = scan_dependencies(ws)
            self.assertEqual(len(flags), 2)
            self.assertTrue(all(f["reason"] == "obsolete" for f in flags))

    def test_staleness_and_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = make_ws(tmp)
            mykb = make_mykb(tmp)
            old = mykb / "wiki" / "syntheses" / "old.md"
            old.write_text("ancient")
            os.utime(old, (1000000000, 1000000000))  # 2001
            res = scan_staleness(ws, mykb, stale_days=30)
            self.assertIn("old.md", res["stale"])
            # drift against a manifest that requires a missing file
            man = {"files": {"rack/missing.json": "0" * 64}}
            drift = drift_check(ws, manifest=man)
            self.assertIn("rack/missing.json: missing", drift["drift"])


if __name__ == "__main__":
    unittest.main()
