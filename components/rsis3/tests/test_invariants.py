"""Phase 14 — invariant registry + attestation + self-repair tests."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.invariants import (
    attest, ensure_invariants, load_invariants, main, repair, run_invariants,
)


class InvariantsTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.ws = self.tmp / "ws"
        self.ws.mkdir()
        (self.ws / ".rsis" / "telemetry").mkdir(parents=True)
        (self.ws / "rack").mkdir()
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "backlog").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def test_registry_defaults_and_persist(self):
        reg = ensure_invariants(self.ws)
        self.assertTrue((self.ws / "rack" / "invariants.json").is_file())
        self.assertEqual(len(reg), 7)
        self.assertEqual(load_invariants(self.ws), reg)

    def test_run_all_checks(self):
        rows = run_invariants(self.ws)
        by_id = {r["id"]: r for r in rows}
        self.assertEqual(len(by_id), 7)
        # empty workspace: schemas pass trivially, ast passes (no pkg yet)
        self.assertTrue(by_id["state_files_disjoint"]["ok"])
        self.assertTrue(by_id["telemetry_coverage"]["ok"])
        self.assertTrue(by_id["kg_idempotency"]["ok"])
        self.assertTrue(by_id["state_schemas"]["ok"])
        self.assertTrue(by_id["ast_invariants"]["ok"])
        self.assertTrue(by_id["stale_locks"]["ok"])

    def test_kg_duplicate_detected_and_repaired(self):
        kg = {"nodes": [{"id": "n1"}, {"id": "n1"}, {"id": "n2"}],
              "edges": [{"id": "e1"}, {"id": "e1"}]}
        (self.ws / ".rsis" / "knowledge_graph.json").write_text(
            json.dumps(kg))
        rows = run_invariants(self.ws)
        kg_row = [r for r in rows if r["id"] == "kg_idempotency"][0]
        self.assertFalse(kg_row["ok"])
        self.assertTrue(kg_row["repairable"])
        repaired = repair(self.ws, rows, mykb=self.mykb)
        self.assertIn("kg_idempotency", repaired)
        fixed = json.loads((self.ws / ".rsis" / "knowledge_graph.json")
                           .read_text())
        self.assertEqual(len(fixed["nodes"]), 2)
        self.assertEqual(len(fixed["edges"]), 1)

    def test_stale_lock_repaired(self):
        lock = self.ws / "rack" / "cycle-daemon.lock"
        lock.write_text("999999")
        rows = run_invariants(self.ws)
        lock_row = [r for r in rows if r["id"] == "stale_locks"][0]
        self.assertFalse(lock_row["ok"])
        repaired = repair(self.ws, rows, mykb=self.mykb)
        self.assertIn("stale_locks", repaired)
        self.assertFalse(lock.exists())

    def test_attestation_record(self):
        rows = run_invariants(self.ws)
        rec = attest(self.ws, "candidate:abc123", rows, actor="l2")
        self.assertEqual(rec["actor"], "l2")
        self.assertEqual(len(rec["sha256"]), 64)
        self.assertEqual(rec["invariant_count"], 7)
        ledger = (self.ws / "rack" / "attestations" /
                  f"{rec['ts'][:10]}.jsonl")
        self.assertTrue(ledger.is_file())
        self.assertIn("candidate:abc123", ledger.read_text())

    def test_main_exit_codes(self):
        self.assertEqual(main(self.ws, json_out=True), 0)
        # break a repairable invariant, fail without repair, pass with
        (self.ws / ".rsis" / "knowledge_graph.json").write_text(
            json.dumps({"nodes": [{"id": "n1"}, {"id": "n1"}]}))
        self.assertEqual(main(self.ws, json_out=True), 1)
        self.assertEqual(main(self.ws, do_repair=True, json_out=True), 0)


if __name__ == "__main__":
    unittest.main()
