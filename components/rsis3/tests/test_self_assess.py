"""Self-assessment routine tests (hermetic: no API key, no real wiki)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import RSISConfig, SelfAssessConfig


def test_self_assess_config_defaults():
    cfg = SelfAssessConfig()
    assert cfg.window_days == 7
    assert cfg.assessments_dir == "wiki/assessments"
    assert cfg.reflections_dir == "wiki/reflections"
    assert cfg.backlog_dir == "wiki/backlog"
    assert cfg.daemon_timeout_s == 60
    assert cfg.llm_enabled is True
    assert RSISConfig().self_assess == cfg
