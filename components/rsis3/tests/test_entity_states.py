"""SPACE series 2 — entity lifecycle & constraint registry tests.

Covers the executable form of the series-2 spec artifacts
``entity_lifecycles`` (defined states + transition rules) and
``entity_constraints`` (required fields + validity rules).
"""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.convergence import _mark_applied, write_proposal
from rsis.entity_states import (
    EntityStateError, can_transition, states, transition, validate_record,
)


class EntityLifecycleTests(unittest.TestCase):
    """Lifecycle registry: states, transitions, transition enforcement."""

    def test_all_entities_defined(self):
        for etype in ("session", "proposal", "candidate", "checkpoint",
                      "strategy"):
            st = states(etype)
            self.assertTrue(st)
            spec = __import__("rsis.entity_states", fromlist=["LIFECYCLES"]).LIFECYCLES[etype]
            # every transition references defined states
            for cur, nxt in spec["transitions"]:
                self.assertIn(cur, st)
                self.assertIn(nxt, st)
            # required fields are non-empty
            self.assertTrue(spec["required"])

    def test_valid_transitions(self):
        self.assertEqual(transition("proposal", "proposed", "applied"),
                         "applied")
        self.assertEqual(transition("candidate", "generated", "evaluated"),
                         "evaluated")
        self.assertEqual(transition("session", "active", "completed"),
                         "completed")
        self.assertEqual(transition("checkpoint", "created", "restored"),
                         "restored")
        self.assertEqual(transition("strategy", "evolved", "active"),
                         "active")

    def test_invalid_transition_raises(self):
        with self.assertRaises(EntityStateError):
            transition("proposal", "applied", "proposed")  # backwards
        with self.assertRaises(EntityStateError):
            transition("candidate", "generated", "applied")  # skips evaluated
        with self.assertRaises(EntityStateError):
            transition("session", "completed", "abandoned")

    def test_unknown_entity_raises(self):
        with self.assertRaises(EntityStateError):
            states("widget")
        with self.assertRaises(EntityStateError):
            can_transition("widget", "a", "b")

    def test_undefined_state_raises(self):
        with self.assertRaises(EntityStateError):
            transition("proposal", "draft", "applied")
        with self.assertRaises(EntityStateError):
            transition("proposal", "proposed", "done")


class EntityConstraintTests(unittest.TestCase):
    """Record validation: required fields + validity rules."""

    def test_valid_records_pass(self):
        validate_record("proposal", {"ts": "2026-08-09T00:00:00Z",
                                     "generation": 95, "loop": "identity"})
        validate_record("candidate", {"description": "x", "target_files": []})
        validate_record("session", {"session_id": "s1", "status": "active"})
        validate_record("checkpoint", {"message": "pre-mutation"})
        validate_record("strategy", {"generation": 6, "population": []})

    def test_missing_required_raises(self):
        with self.assertRaises(EntityStateError):
            validate_record("proposal", {"ts": "2026-08-09T00:00:00Z"})
        with self.assertRaises(EntityStateError):
            validate_record("candidate", {"description": "x"})

    def test_extra_rules(self):
        # proposal needs loop or proposed_loop
        with self.assertRaises(EntityStateError):
            validate_record("proposal", {"ts": "t", "generation": 1})
        validate_record("proposal", {"ts": "t", "generation": 1,
                                     "proposed_loop": "identity"})
        # candidate target_files must be a list
        with self.assertRaises(EntityStateError):
            validate_record("candidate", {"description": "x",
                                          "target_files": "rsis/x.py"})
        # strategy population must be a list
        with self.assertRaises(EntityStateError):
            validate_record("strategy", {"generation": 1, "population": {}})

    def test_non_dict_record_raises(self):
        with self.assertRaises(EntityStateError):
            validate_record("proposal", ["ts"])


class ProposalIntegrationTests(unittest.TestCase):
    """Lifecycle/constraint wiring in the convergence proposal path."""

    def _ws(self, tmp):
        ws = Path(tmp) / "ws"
        (ws / "rack" / "proposals").mkdir(parents=True)
        return ws

    def test_write_proposal_validates_and_marks_proposed(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = self._ws(tmp)
            report = {"ts": "2026-08-09T14:00:00Z", "generation": 95,
                      "detected": True, "plateau": True,
                      "proposed_loop": "identity", "command": "python -m rsis identity"}
            path = write_proposal(ws, report)
            payload = json.loads(path.read_text())
            self.assertIs(payload["applied"], False)
            self.assertEqual(payload["type"], "convergence-proposal")

    def test_mark_applied_writes_valid_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = self._ws(tmp)
            report = {"ts": "2026-08-09T14:00:00Z", "generation": 95,
                      "proposed_loop": "identity"}
            _mark_applied(ws, report)
            recs = (ws / "rack" / "proposals" / "applied.jsonl").read_text().splitlines()
            self.assertEqual(len(recs), 1)
            rec = json.loads(recs[0])
            self.assertEqual(rec["loop"], "identity")
            validate_record("proposal", rec)  # shape check


if __name__ == "__main__":
    unittest.main()
