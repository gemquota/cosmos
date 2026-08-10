"""Phase 13 — federated memory tests (publish gate, provenance, consensus)."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.federation import (
    backlog_path, ledger_path, outbox_dir, publish, pull, status,
)


def make_note(mykb: Path, name: str, title: str, tags, ts="2026-08-09T00:00:00Z"):
    d = mykb / "wiki" / "syntheses"
    d.mkdir(parents=True, exist_ok=True)
    front = (f"---\ntype: \"synthesis\"\ntitle: \"{title}\"\n"
             f"tags: \"{', '.join(tags)}\"\ntimestamp: \"{ts}\"\n"
             "status: \"stable\"\n---\n\nDurable rule body.\n")
    (d / f"{name}.md").write_text(front)
    return f"wiki/syntheses/{name}.md"


class FederationTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.ws = self.tmp / "ws"
        self.ws.mkdir()
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "syntheses").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def test_private_note_never_publishes(self):
        rel = make_note(self.mykb, "private", "Private", ["internal"])
        env = publish(self.ws, self.mykb, rel)
        self.assertIsNone(env)
        self.assertFalse(outbox_dir(self.ws).exists())

    def test_publish_envelope_provenance(self):
        rel = make_note(self.mykb, "pub", "Shared rule",
                        ["publishable", "project:alpha"])
        env = publish(self.ws, self.mykb, rel, producer="alice",
                      confidence=0.9)
        self.assertIsNotNone(env)
        self.assertEqual(env["provenance"]["project"], "alpha")
        self.assertEqual(env["provenance"]["producer"], "alice")
        self.assertEqual(env["provenance"]["confidence"], 0.9)
        self.assertEqual(env["provenance"]["verification_state"],
                         "unverified")
        self.assertEqual(len(env["provenance"]["federation_history"]), 1)
        out = outbox_dir(self.ws) / f"{env['id']}.json"
        self.assertTrue(out.is_file())
        ledger = [json.loads(l) for l in
                  ledger_path(self.ws).read_text().splitlines() if l.strip()]
        self.assertEqual(ledger[-1]["op"], "publish")

    def test_pull_adopts_create_only(self):
        rel = make_note(self.mykb, "src", "Foreign idea",
                        ["publishable", "project:beta"])
        env = publish(self.ws, self.mykb, rel)
        # second instance
        ws2 = self.tmp / "ws2"
        ws2.mkdir()
        mykb2 = self.tmp / "mykb2"
        (mykb2 / "wiki" / "syntheses").mkdir(parents=True)
        result = pull(ws2, mykb2, env)
        self.assertEqual(result["outcome"], "adopted")
        self.assertTrue(Path(result["rel"]).is_file())
        # name collision: adopt as federated copy, never overwrite
        make_note(mykb2, "foreign-idea", "Foreign idea", ["publishable"],
                  ts="2026-08-01T00:00:00Z")
        result2 = pull(ws2, mykb2, env)
        self.assertEqual(result2["outcome"], "adopted")
        self.assertIn("federated", result2["rel"])
        ledger = [json.loads(l) for l in
                  ledger_path(ws2).read_text().splitlines() if l.strip()]
        self.assertEqual(ledger[-1]["op"], "pull")

    def test_consensus_newest_fact_wins(self):
        make_note(self.mykb, "local", "Fact X", ["publishable"],
                  ts="2026-08-08T00:00:00Z")
        rel = make_note(self.mykb, "foreign", "Fact X", ["publishable"],
                        ts="2026-08-10T00:00:00Z")
        env = publish(self.ws, self.mykb, rel)
        result = pull(self.ws, self.mykb, env)
        self.assertEqual(result["outcome"], "adopted")  # newer wins

    def test_consensus_local_policy_wins(self):
        rel = make_note(self.mykb, "foreign-policy", "Budget rule",
                        ["publishable", "policy"],
                        ts="2026-08-10T00:00:00Z")
        env = publish(self.ws, self.mykb, rel)
        make_note(self.mykb, "budget-rule", "Budget rule",
                  ["policy"], ts="2026-08-08T00:00:00Z")
        result = pull(self.ws, self.mykb, env)
        self.assertEqual(result["outcome"], "local-policy-wins")
        backlog = backlog_path(self.ws).read_text().splitlines()
        self.assertTrue(any("local-policy-wins" in l for l in backlog))

    def test_older_fact_skipped_and_backlogged(self):
        make_note(self.mykb, "fact-y", "Fact Y", ["publishable"],
                  ts="2026-08-10T00:00:00Z")
        rel = make_note(self.mykb, "foreign", "Fact Y", ["publishable"],
                        ts="2026-08-08T00:00:00Z")
        env = publish(self.ws, self.mykb, rel)
        result = pull(self.ws, self.mykb, env)
        self.assertEqual(result["outcome"], "older-fact-skipped")
        self.assertTrue(backlog_path(self.ws).is_file())

    def test_status(self):
        rel = make_note(self.mykb, "pub", "Shared", ["publishable"])
        publish(self.ws, self.mykb, rel)
        self.assertEqual(status(self.ws, json_out=True), 0)


if __name__ == "__main__":
    unittest.main()
