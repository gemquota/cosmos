"""Phase 9 — policy-controlled governance: policy, approvals, audit, rollback."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from rsis.audit import append, replay
from rsis.policy import (
    approve, check_unauthorized_writes, ensure_policy, list_staged,
    load_policy, reject, requires_approval, stage_candidate,
)
from rsis.rollback import rollback


def make_ws(tmp: str) -> Path:
    root = Path(tmp)
    (root / "rack").mkdir(parents=True)
    (root / "wiki" / "syntheses").mkdir(parents=True)
    return root


def staged_candidate(target=("rack/policy.json",)):
    return {
        "description": "touches a gated path",
        "target_files": list(target),
        "diff_or_code": "# gated content",
        "goal": "test goal",
        "rationale": "test",
    }


class PolicyTests(unittest.TestCase):
    def test_ensure_policy_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            policy = ensure_policy(root)
            self.assertEqual(policy["version"], 1)
            self.assertIn("rack/policy.json",
                          policy["approval_required"]["paths"])
            self.assertTrue((root / "rack" / "policy.json").is_file())

    def test_requires_approval(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            policy = ensure_policy(root)
            self.assertTrue(requires_approval(staged_candidate(), policy=policy))
            self.assertFalse(requires_approval(
                staged_candidate(target=("rsis/ok.py",)), policy=policy))

    def test_stage_approve_flow(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            rec = stage_candidate(root, staged_candidate(),
                                  reason="policy gate", actor="system")
            self.assertEqual(rec["status"], "staged")
            self.assertEqual(len(list_staged(root)), 1)
            self.assertTrue(approve(root, rec["id"], actor="alice"))
            self.assertEqual(
                (root / "rack" / "policy.json").read_text(), "# gated content")
            entries = replay(root)
            self.assertEqual(entries[0]["kind"], "approval.applied")
            self.assertEqual(entries[0]["actor"], "alice")
            self.assertEqual(len(list_staged(root)), 0)

    def test_reject(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            rec = stage_candidate(root, staged_candidate(),
                                  reason="policy gate")
            self.assertTrue(reject(root, rec["id"], actor="bob"))
            self.assertEqual(len(list_staged(root)), 0)
            self.assertEqual(replay(root)[0]["kind"], "approval.rejected")

    def test_rollback_restores_pre_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            (root / "rack" / "policy.json").write_text("original")
            rec = stage_candidate(root, staged_candidate(),
                                  reason="policy gate")
            approve(root, rec["id"])
            self.assertEqual(
                (root / "rack" / "policy.json").read_text(), "# gated content")
            mykb = root / "mykb"
            (mykb / "wiki" / "backlog").mkdir(parents=True)
            self.assertTrue(rollback(root, rec["id"], mykb=mykb))
            self.assertEqual(
                (root / "rack" / "policy.json").read_text(), "original")
            self.assertEqual(replay(root)[0]["kind"], "rollback")
            self.assertTrue(list((mykb / "wiki" / "backlog")
                                 .glob("rollback-*.md")))

    def test_unauthorized_writes_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            ensure_policy(root)
            subprocess.run(["git", "init", "-q"], cwd=str(root), check=True)
            # untracked gated file shows up in git status
            (root / "rack" / "policy.json").write_text("modified directly")
            violations = check_unauthorized_writes(root)
            self.assertTrue(any("rack" in v for v in violations))

    def test_audit_replay_since(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_ws(tmp)
            append(root, {"kind": "a", "ts": "2026-08-09T00:00:00Z"})
            append(root, {"kind": "b", "ts": "2026-08-09T12:00:00Z"})
            entries = replay(root, since="2026-08-09T06:00:00Z")
            self.assertEqual([e["kind"] for e in entries], ["b"])


if __name__ == "__main__":
    unittest.main()
