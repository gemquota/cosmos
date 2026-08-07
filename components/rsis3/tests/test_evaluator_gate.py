"""Deterministic evaluator gate: path safety, compile, AST scan, regression.

The gate runs in the immutable evaluator subprocess
(``evaluator/evaluator.py``), which is loaded here by path so tests exercise
the exact artifact CI ships, never the ``rsis.evaluator`` client.
"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

EVALUATOR_PATH = (
    Path(__file__).resolve().parent.parent / "evaluator" / "evaluator.py"
)

_spec = importlib.util.spec_from_file_location(
    "rsis_evaluator_gate", EVALUATOR_PATH)
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)


@pytest.fixture(autouse=True)
def _no_llm_key(monkeypatch):
    """Never touch the network from gate tests."""
    monkeypatch.delenv("RSIS_EVALUATOR_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)


def candidate(code, target=("rsis/foo.py",), **extra):
    return {
        "description": "test candidate",
        "target_files": list(target),
        "diff": code,
        **extra,
    }


# ── PASS paths ──────────────────────────────────────────────────────── #

def test_clean_module_passes():
    result = ev.evaluate(candidate("def helper():\n    return 42\n"))
    assert result["decision"] == "PASS"
    assert all(result["scores"][k] == 1.0 for k in ev.SCORE_KEYS)


def test_clean_unified_diff_passes():
    diff = (
        "--- a/rsis/foo.py\n"
        "+++ b/rsis/foo.py\n"
        "@@ -0,0 +1,3 @@\n"
        "+def helper():\n"
        "+    return 42\n"
    )
    assert ev.evaluate(candidate(diff))["decision"] == "PASS"


def test_indented_diff_fragment_passes():
    """Added lines inside an enclosing block must not false-fail."""
    diff = (
        "--- a/rsis/foo.py\n"
        "+++ b/rsis/foo.py\n"
        "@@ -5,6 +5,7 @@\n"
        "     def bar(self):\n"
        "         x = 1\n"
        "+        y = 2\n"
        "         return x\n"
    )
    assert ev.evaluate(candidate(diff))["decision"] == "PASS"


def test_json_data_candidate_passes():
    """L8/L9 tuning deltas are JSON documents, not Python code."""
    result = ev.evaluate(candidate(
        json.dumps({"l5.mutation_rate": 0.05}, indent=2),
        target=(".rsis/metameta_state.json",)))
    assert result["decision"] == "PASS"
    assert result["scores"]["correctness"] == 1.0


def test_diff_or_code_fallback_used():
    result = ev.evaluate({
        "description": "d",
        "target_files": ["rsis/foo.py"],
        "diff_or_code": "def helper():\n    return 42\n",
    })
    assert result["decision"] == "PASS"


# ── safety hard gates ───────────────────────────────────────────────── #

@pytest.mark.parametrize("code", [
    "import os\nos.system('rm -rf /')\n",
    "import os\nos.remove('/etc/passwd')\n",
    "import shutil\nshutil.rmtree('/tmp/x')\n",
    "eval('1+1')\n",
    "exec('x = 1')\n",
    "compile('x', '<s>', 'exec')\n",
    "import subprocess\nsubprocess.run('ls', shell=True)\n",
    "import subprocess\nsubprocess.Popen(['rm', '-rf', '/'])\n",
    "import pickle\npickle.loads(b'x')\n",
    "open('/etc/passwd', 'w')\n",
    "open('../escape.txt', 'a')\n",
    "open('~/x', 'w')\n",
])
def test_unsafe_code_fails(code):
    result = ev.evaluate(candidate(code))
    assert result["decision"] == "FAIL"
    assert result["scores"]["safety"] == 0.0


def test_unsafe_indented_diff_fragment_fails():
    diff = (
        "--- a/rsis/foo.py\n"
        "+++ b/rsis/foo.py\n"
        "@@ -5,6 +5,7 @@\n"
        "     def bar(self):\n"
        "+        os.system('rm -rf /')\n"
        "         return x\n"
    )
    result = ev.evaluate(candidate(diff))
    assert result["decision"] == "FAIL"
    assert result["scores"]["safety"] == 0.0


def test_json_data_with_destructive_string_fails():
    result = ev.evaluate(candidate(
        json.dumps({"cmd": "rm -rf /"}), target=(".rsis/x.json",)))
    assert result["decision"] == "FAIL"
    assert result["scores"]["safety"] == 0.0


def test_benign_subprocess_allowed():
    result = ev.evaluate(candidate(
        "import subprocess\n"
        "subprocess.run(['git', 'status'], shell=False)\n"))
    assert result["decision"] == "PASS"


def test_relative_write_allowed():
    result = ev.evaluate(candidate(
        "with open('data/out.txt', 'w') as f:\n    f.write('x')\n"))
    assert result["decision"] == "PASS"


# ── correctness hard gate ───────────────────────────────────────────── #

def test_syntax_error_fails():
    result = ev.evaluate(candidate("def broken(:\n"))
    assert result["decision"] == "FAIL"
    assert result["scores"]["correctness"] == 0.0


def test_missing_code_fails():
    result = ev.evaluate({"description": "d", "target_files": ["rsis/foo.py"]})
    assert result["decision"] == "FAIL"


def test_diff_with_no_added_lines_fails():
    diff = (
        "--- a/rsis/foo.py\n"
        "+++ b/rsis/foo.py\n"
        "@@ -1,1 +1,1 @@\n"
        "-x = 1\n"
    )
    assert ev.evaluate(candidate(diff))["decision"] == "FAIL"


# ── path safety ─────────────────────────────────────────────────────── #

@pytest.mark.parametrize("bad", [
    "/etc/passwd",
    "../escape.py",
    "rsis/../../etc/x.py",
    "C:\\evil.py",
    "C:/evil.py",
    "a\\b.py",
])
def test_bad_target_paths_fail(bad):
    assert ev.evaluate(candidate("x = 1\n", target=(bad,)))["decision"] == "FAIL"


def test_missing_or_empty_target_files_fails():
    assert ev.evaluate({"description": "d", "diff": "x = 1\n"})["decision"] == "FAIL"
    assert ev.evaluate(candidate("x = 1\n", target=()))["decision"] == "FAIL"


def test_non_string_target_entry_fails():
    result = ev.evaluate(candidate("x = 1\n", target=(123,)))
    assert result["decision"] == "FAIL"


def test_non_dict_candidate_fails():
    result = ev.evaluate("not a dict")
    assert result["decision"] == "FAIL"


# ── regression hard gate ────────────────────────────────────────────── #

def test_removed_definition_fails():
    diff = (
        "--- a/rsis/foo.py\n"
        "+++ b/rsis/foo.py\n"
        "@@ -1,4 +1,3 @@\n"
        "-def helper():\n"
        "-    return 42\n"
        "+def helper():\n"
        "+    return 43\n"
    )
    result = ev.evaluate(candidate(diff))
    assert result["decision"] == "FAIL"
    assert result["scores"]["regression"] == 0.0


def test_diff_touching_undeclared_file_notes_and_scores():
    diff = (
        "--- a/rsis/other.py\n"
        "+++ b/rsis/other.py\n"
        "@@ -0,0 +1,1 @@\n"
        "+x = 1\n"
    )
    result = ev.evaluate(candidate(diff, target=("rsis/foo.py",)))
    assert result["decision"] == "PASS"
    assert result["scores"]["regression"] == 0.9
    assert any("outside target_files" in n for n in result["suggestions"])


# ── style / efficiency heuristics ───────────────────────────────────── #

def test_style_heuristics_lower_score_and_suggest():
    code = (
        "def ok():  # TODO: finish later\n"
        "    raise NotImplementedError\n"
    )
    result = ev.evaluate(candidate(code))
    assert result["decision"] == "PASS"
    assert result["scores"]["style"] < 1.0
    assert result["suggestions"]


def test_efficiency_flags_noop_function():
    result = ev.evaluate(candidate("def f():\n    return None\n"))
    assert result["scores"]["efficiency"] < 1.0


# ── LLM refinement (fail-closed) ────────────────────────────────────── #

def test_llm_cannot_overturn_hard_fail(monkeypatch):
    result = ev.evaluate(candidate("eval('x')\n"))
    assert result["decision"] == "FAIL"
    merged = ev._merge_llm("FAIL", dict(result["scores"]), "PASS",
                           {k: 1.0 for k in ev.SCORE_KEYS})
    assert merged[0] == "FAIL"
    assert merged[1]["safety"] == 0.0


def test_llm_can_downgrade_pass_to_fail():
    decision, scores = ev._merge_llm(
        "PASS", {k: 1.0 for k in ev.SCORE_KEYS}, "FAIL", {})
    assert decision == "FAIL"


def test_llm_scores_merged_when_pass():
    decision, scores = ev._merge_llm(
        "PASS", {k: 1.0 for k in ev.SCORE_KEYS}, "PASS",
        {"style": 0.7, "bogus": 0.0, "safety": 1.7})
    assert decision == "PASS"
    assert scores["style"] == 0.7
    assert scores["safety"] == 1.0  # out-of-range ignored


def test_llm_evaluate_disabled_without_key(monkeypatch):
    monkeypatch.delenv("RSIS_EVALUATOR_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert ev._llm_evaluate({"description": "d"}) is None


# ── CLI surface ─────────────────────────────────────────────────────── #

def run_evaluator(args, stdin_text, env_extra=None):
    env = dict(os.environ)
    env.update({"RSIS_EVALUATOR_API_KEY": "", "OPENAI_API_KEY": ""})
    if env_extra:
        env.update(env_extra)
    return subprocess.run(
        [sys.executable, str(EVALUATOR_PATH), *args],
        input=stdin_text, capture_output=True, text=True, timeout=60, env=env,
    )


def test_main_roundtrip_passes():
    r = run_evaluator([], json.dumps(candidate("def helper():\n    return 42\n")))
    assert r.returncode == 0
    assert json.loads(r.stdout)["decision"] == "PASS"


def test_main_roundtrip_rejects_unsafe():
    r = run_evaluator([], json.dumps(candidate("import os\nos.system('x')\n")))
    assert r.returncode == 0
    assert json.loads(r.stdout)["decision"] == "FAIL"


def test_main_invalid_json_exits_nonzero():
    r = run_evaluator([], "not json")
    assert r.returncode == 1
    assert "INVALID_INPUT" in r.stderr


def test_main_verify_digest():
    digest = hashlib.sha256(EVALUATOR_PATH.read_bytes()).hexdigest()
    ok = run_evaluator(["--verify", digest], "{}")
    assert ok.returncode == 0
    bad = run_evaluator(["--verify", "0" * 64], "{}")
    assert bad.returncode == 1
    assert "DIGEST_MISMATCH" in bad.stderr
