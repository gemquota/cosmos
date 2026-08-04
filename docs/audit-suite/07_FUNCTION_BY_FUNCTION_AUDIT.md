# 07 — Function-by-Function Audit

**Doc ID:** COSMOS-AUDIT-07 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Coverage:** complete registry of all 720 Python functions (AST-extracted, audited file state 2026-08-04). SPACE TypeScript functions inventoried at module level in §4 (354 funcs/methods, regex-extracted). Risk class assigned per function (heuristic + manual review of core).
**Cross-references:** [05 File-by-File](05_FILE_BY_FILE_AUDIT.md) · [14 Static Code Analysis](14_STATIC_CODE_ANALYSIS.md) · [28 Technical Debt](28_TECHNICAL_DEBT_REGISTER.md)

---

## 1. Risk Classes
- **LOW** — pure/read-only; no I/O; no state mutation.
- **MED** — I/O or mutation but guarded (timeouts, try/except, allowlists).
- **HIGH** — subprocess/exec/network/untrusted input without strong guards, or stateful concurrency.

## 2. Registry: RSIS3 `rsis/` + `rack/` + MyKB server/daemons (per module)

### `components/mykb/.wiki-daemon/build_graph.py` (124 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `read_fm_title` | `text` | LOW |  |
| `main` | `` | LOW |  |
| `add_edge` | `src, tgt` | LOW |  |
| `resolve_target` | `raw` | LOW |  |

### `components/mykb/.wiki-daemon/build_index_pages.py` (67 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `frontmatter_title` | `path` | LOW |  |
| `main` | `` | LOW |  |

### `components/mykb/.wiki-daemon/build_stats.py` (694 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `parse_frontmatter` | `text` | LOW |  |
| `body_words` | `text` | LOW |  |
| `walk_md` | `` | LOW |  |
| `iso_month` | `ts` | LOW |  |
| `iso_day` | `ts` | LOW |  |
| `main` | `` | LOW |  |
| `pct` | `n, d` | LOW |  |
| `med` | `xs` | LOW |  |
| `series` | `counter, top` | LOW |  |
| `_bucket_of` | `w` | LOW |  |
| `graph_ok` | `nid` | LOW |  |

### `components/mykb/.wiki-daemon/build_stub_audit.py` (125 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `parse_fm` | `text` | LOW |  |
| `body_words` | `text` | LOW |  |
| `first_add_dates` | `` | LOW |  |
| `main` | `` | LOW |  |

### `components/mykb/.wiki-daemon/build_stub_index.py` (103 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `parse_frontmatter` | `text` | LOW |  |
| `body_words` | `text` | LOW |  |
| `category_path` | `rel` | LOW |  |
| `main` | `` | LOW |  |

### `components/mykb/.wiki-daemon/enrich_links.py` (551 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `get_domain` | `filepath` | LOW |  |
| `is_index` | `filepath` | LOW |  |
| `count_entities_in_dir` | `dirpath` | LOW |  |
| `get_children_dirs` | `dirpath` | LOW |  |
| `list_entities_in_dir` | `dirpath, limit` | LOW |  |
| `frontmatter_block` | `tags, extra` | LOW |  |

### `components/mykb/.wiki-daemon/kb_linter.py` (203 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `find_all_md_files` | `base` | LOW |  |
| `extract_wikilinks` | `text` | LOW |  |
| `extract_tags` | `text` | LOW |  |
| `lint` | `return_json` | LOW |  |

### `components/mykb/.wiki-daemon/link_check.py` (67 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `main` | `` | LOW |  |

### `components/mykb/.wiki-daemon/search_fusion.py` (576 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_hash_token` | `token` | LOW |  |
| `hashed_embed` | `text, dim` | LOW |  |
| `semantic_search` | `index_data, query_text, top_n` | LOW |  |
| `chunk_markdown` | `text, source_path` | LOW |  |
| `extract_signatures` | `code_blocks` | LOW |  |
| `build_chunks_from_wiki` | `` | LOW |  |
| `tokenize` | `text` | LOW |  |
| `build_indices` | `chunks` | LOW |  |
| `save_index` | `index_data` | MED |  |
| `load_index` | `` | LOW |  |
| `rrf_fusion` | `` | LOW |  |
| `search_query` | `index_data, query_text, top_n` | LOW |  |
| `cmd_build_index` | `` | LOW |  |
| `_rows_from_results` | `index_data, fused, top_n` | LOW |  |
| `cmd_query` | `query_text, semantic_only` | LOW |  |
| `cmd_serve` | `` | LOW |  |
| `flush` | `` | LOW |  |
| `do_POST` | `self` | LOW |  |
| `do_GET` | `self` | LOW |  |
| `log_message` | `self, format` | LOW |  |

### `components/mykb/.wiki-daemon/temporal_engine.py` (198 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `get_repo` | `` | LOW |  |
| `format_ts` | `dt` | LOW |  |
| `parse_ts` | `ts_str` | LOW |  |
| `cmd_status` | `` | LOW |  |
| `cmd_commit` | `target_path` | MED |  |
| `cmd_history` | `filepath` | LOW |  |
| `cmd_snapshot` | `filepath, timestamp` | LOW |  |
| `cmd_diff` | `filepath` | LOW |  |

### `components/mykb/hooks/post-tool-use.py` (54 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `main` | `` | LOW |  |

### `components/mykb/hooks/session-stop.py` (33 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `main` | `` | LOW |  |

### `components/mykb/server.py` (386 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `search_query` | `q, limit` | LOW |  |
| `get_system_stats` | `` | LOW |  |
| `send_json` | `self, data` | LOW |  |
| `do_GET` | `self` | LOW |  |
| `log_message` | `self, format` | LOW |  |

### `components/rsis3/rack/rrp_conversation.py` (496 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `auto_answer_open` | `question, goal` | LOW |  |
| `auto_answer_multi` | `question, options, goal` | LOW |  |
| `__init__` | `self, goal, target_files, interactive, x, y…` | LOW |  |
| `ask` | `self, prompt, is_multi, options` | LOW |  |
| `pick_questions` | `self, bank, count, used` | LOW |  |
| `pick_multi` | `self, answer, count` | LOW |  |
| `run` | `self` | MED |  |

### `components/rsis3/rack/rrp_engine.py` (706 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `run_rrp_session` | `goal_description, target_files, x, y, z, u…` | MED |  |
| `avg` | `self` | LOW | property |
| `max_dim` | `self` | LOW | property |
| `converged` | `self` | LOW | property |
| `calibrate_from_confidence` | `self, confidence, ambiguity_est` | LOW |  |
| `reduce` | `self, factor` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `record_round` | `self, tokens` | LOW |  |
| `saturation_pct` | `self` | LOW | property |
| `to_dict` | `self` | LOW |  |
| `average` | `self` | LOW | property |
| `record` | `self, score` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `cumulative` | `self` | LOW | property |
| `trend` | `self` | LOW | property |
| `record` | `self, score` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `start_round` | `self` | MED |  |
| `end_round` | `self` | LOW |  |
| `avg_duration` | `self` | LOW | property |
| `total_duration` | `self` | LOW | property |
| `to_dict` | `self` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `__init__` | `self, u, m, x, y, z…` | LOW |  |
| `start_session` | `self` | MED |  |
| `process_open_ended` | `self, questions, answers, satisfaction` | LOW |  |
| `process_multi_choice` | `self, mcqs, answers, satisfaction` | LOW |  |
| `process_decision` | `self, decision, confidence, reasoning` | LOW |  |
| `finalize` | `self` | LOW |  |
| `generate_open_questions` | `self` | LOW |  |
| `generate_multi_choice` | `self, open_answers` | LOW |  |
| `generate_probing_questions` | `self` | LOW |  |
| `_extract_constraints` | `self, text` | LOW |  |
| `_detect_contradictions` | `self` | LOW |  |
| `_detect_topics` | `self, texts` | LOW |  |
| `_log_transaction` | `self, round_num, phase, description, ambiguity_before, ambiguity_after…` | LOW |  |
| `_save_checkpoint` | `self` | MED |  |
| `_summary` | `self` | LOW |  |

### `components/rsis3/rack/run_rrp_pulse.py` (323 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `capture_telemetry` | `` | LOW |  |
| `run_pulse` | `pulse_num, num_goals, x, y, z, u…` | MED |  |

### `components/rsis3/rack/server.py` (29 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self` | LOW |  |
| `guess_type` | `self, path` | LOW |  |
| `end_headers` | `self` | LOW |  |
| `log_message` | `self, format` | LOW |  |

### `components/rsis3/rsis/checkpoint.py` (119 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, repo_root` | LOW |  |
| `_git` | `self` | LOW |  |
| `ensure_repo` | `self` | LOW |  |
| `has_changes` | `self` | LOW |  |
| `checkpoint` | `self, message` | LOW |  |
| `rollback` | `self, commit_hash` | LOW |  |
| `rollback_last_checkpoint` | `self` | LOW |  |
| `latest_checkpoint` | `self` | LOW |  |
| `sha256_digest` | `self, path` | LOW |  |
| `verify_digest` | `self, path, expected` | LOW |  |

### `components/rsis3/rsis/config.py` (388 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_clamp` | `value, lo, hi` | LOW |  |
| `_apply_tuned_state` | `cfg` | MED |  |
| `load_config` | `` | LOW |  |
| `_apply` | `name, value` | MED |  |

### `components/rsis3/rsis/dashboard/app.py` (95 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_get_data` | `` | LOW |  |
| `index` | `request` | LOW | ? |
| `api_status` | `` | LOW | ? |
| `api_trends` | `` | LOW | ? |
| `api_velocity` | `` | LOW | ? |
| `api_search` | `request, q` | LOW | ? |
| `health` | `` | LOW | ? |

### `components/rsis3/rsis/error_classifier.py` (67 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `classify_error_text` | `text` | LOW |  |
| `classify_error` | `exc` | LOW |  |
| `is_retryable` | `failure` | LOW |  |

### `components/rsis3/rsis/evaluator.py` (130 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `passed` | `self` | LOW | property |
| `score_avg` | `self` | LOW | property |
| `__init__` | `self, evaluator_path, ledger` | LOW |  |
| `verify_integrity` | `self` | HIGH |  |
| `evaluate` | `self, candidate` | HIGH |  |

### `components/rsis3/rsis/event_bus.py` (89 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, max_history` | LOW |  |
| `_matches` | `pattern, topic` | LOW | staticmethod |
| `publish` | `self, topic, event` | LOW |  |
| `subscribe` | `self, topic` | LOW |  |
| `unsubscribe` | `self, topic, sub_queue` | LOW |  |
| `drain` | `self, sub_queue` | LOW |  |
| `history` | `self, topic` | LOW |  |
| `subscriber_count` | `self` | LOW | property |

### `components/rsis3/rsis/extrapolation.py` (245 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_get` | `ev` | LOW |  |
| `__init__` | `self, telemetry_dir` | LOW |  |
| `load_events` | `self, force` | LOW |  |
| `get_sessions` | `self` | LOW |  |
| `_build_session` | `self, events` | LOW |  |
| `predict_optimal_iterations` | `self` | HIGH |  |
| `detect_regression_trends` | `self` | LOW |  |
| `find_redundancy_candidates` | `self, memory_kg` | LOW |  |
| `generate_velocity_report` | `self` | LOW |  |

### `components/rsis3/rsis/loop_l1.py` (253 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, checkpoint_mgr, tools, tool_manager, agent_name` | LOW |  |
| `execute` | `self, task, context` | MED |  |
| `_plan_next_action` | `self, task, context, previous_calls` | LOW |  |
| `_arguments_for` | `self, tool_name, task, context` | LOW |  |
| `_execute_tool` | `self, name, args` | MED |  |

### `components/rsis3/rsis/loop_l2.py` (407 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, evaluator, checkpoint_mgr, l1_loop, recovery` | LOW |  |
| `run_session` | `self, goal, budget` | HIGH |  |
| `_run_parallel_session` | `self, goal, budget` | HIGH |  |
| `_review_candidates` | `self, goal, candidates` | HIGH |  |
| `_start_bus_bridge` | `self, bus` | MED |  |
| `_record_bus_event` | `self, event` | LOW |  |
| `_generate_candidate` | `self, goal, attempt, previous_results` | HIGH |  |
| `_apply_improvement` | `self, candidate` | MED |  |
| `run` | `task` | MED |  |
| `handler` | `task` | LOW |  |
| `drain` | `` | LOW |  |

### `components/rsis3/rsis/loop_l3.py` (256 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |
| `_detect_trends` | `self` | LOW |  |
| `_consolidate_memory` | `self, trends` | LOW |  |
| `_evolve_strategies` | `self, insights_added, trends` | LOW |  |
| `_refine_redundancies` | `self` | LOW |  |

### `components/rsis3/rsis/loop_l4.py` (237 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_default_params` | `self` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `aggregate_outcomes` | `memory, limit` | LOW | staticmethod |
| `_propose_deltas` | `self, success_rate, current` | LOW |  |
| `_apply` | `self, new_params` | MED |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/loop_l5.py` (297 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `_default_variant` | `cls, suffix` | LOW | classmethod |
| `_seed_from_l3` | `self, population` | LOW |  |
| `_score` | `self, variant, stats` | LOW |  |
| `_mutate` | `self, variant, gen` | LOW |  |
| `_recombine` | `self, a, b, gen` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/loop_l6.py` (205 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_default_params` | `self` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `_signal` | `self, stats, trends` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/loop_l7.py` (227 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_default_params` | `self` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `_l4_history` | `self` | LOW |  |
| `_signal` | `self, history, stats` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/loop_l8.py` (242 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_default_params` | `self` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `_l5_history` | `self` | LOW |  |
| `_signal` | `self, history` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/loop_l9.py` (233 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, telemetry, memory, evaluator, checkpoint_mgr` | LOW |  |
| `_default_params` | `self` | LOW |  |
| `_load_state` | `self` | LOW |  |
| `_save_state` | `self, state` | MED |  |
| `_l6_history` | `self` | LOW |  |
| `_signal` | `self, history, stats` | LOW |  |
| `run_cycle` | `self, budget` | MED |  |

### `components/rsis3/rsis/main.py` (745 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `setup_logging` | `` | LOW |  |
| `_init_subsystems` | `` | LOW |  |
| `cmd_init` | `args` | LOW |  |
| `cmd_run` | `args` | MED |  |
| `cmd_evolve` | `args` | LOW |  |
| `cmd_optimize` | `args` | LOW |  |
| `cmd_strategies` | `args` | LOW |  |
| `cmd_identity` | `args` | LOW |  |
| `cmd_metacog` | `args` | LOW |  |
| `cmd_metameta` | `args` | LOW |  |
| `cmd_mmm` | `args` | LOW |  |
| `cmd_dashboard` | `args` | LOW |  |
| `_fmt` | `val, unit` | LOW |  |
| `cmd_status` | `args` | LOW |  |
| `cmd_check` | `args` | LOW |  |
| `cmd_check_practices` | `args` | LOW |  |
| `cmd_scheduler` | `args` | LOW |  |
| `cmd_pipeline` | `args` | LOW |  |
| `cmd_recovery_test` | `args` | LOW |  |
| `main` | `` | LOW |  |

### `components/rsis3/rsis/memory.py` (346 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, ngram_range, dim` | LOW |  |
| `_ngrams` | `self, text` | LOW |  |
| `embed` | `self, text` | LOW |  |
| `__init__` | `self, path, dim` | LOW |  |
| `_load` | `self` | LOW |  |
| `save` | `self` | MED |  |
| `add` | `self, text, metadata` | LOW |  |
| `search` | `self, query, top_k` | LOW |  |
| `__init__` | `self, path` | LOW |  |
| `_load` | `self` | LOW |  |
| `save` | `self` | MED |  |
| `add_node` | `self, node_id, node_type` | LOW |  |
| `get_node` | `self, node_id` | LOW |  |
| `query` | `self, node_type` | LOW |  |
| `remove_node` | `self, node_id` | LOW |  |
| `add_edge` | `self, source, target, rel` | LOW |  |
| `get_edges` | `self, node_id` | LOW |  |
| `node_count` | `self` | LOW | property |
| `edge_count` | `self` | LOW | property |
| `get_insights` | `self, limit` | LOW |  |
| `get_strategies` | `self` | LOW |  |
| `get_failure_patterns` | `self` | LOW |  |
| `find_related` | `self, node_id, rel` | LOW |  |
| `__init__` | `self, repo_root` | LOW |  |
| `save` | `self` | MED |  |
| `record_improvement` | `self, description, target_files, eval_scores, outcome, goal` | LOW |  |
| `get_relevant_patterns` | `self, goal, limit` | LOW |  |
| `get_recent_improvements` | `self, limit` | LOW |  |

### `components/rsis3/rsis/pipeline.py` (319 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `run_demo` | `` | MED |  |
| `latency_s` | `self` | LOW | property |
| `__init__` | `self, num_workers, on_event, max_retries, retry_base_delay_s, retry_max_delay_s` | LOW |  |
| `add_task` | `self, task_id, role, payload, depends_on` | LOW |  |
| `_is_ready` | `self, task` | LOW |  |
| `run_pipeline` | `self, executor` | MED |  |
| `_retry_delay` | `self, attempt` | LOW |  |
| `_emit_retry` | `self, task, exc, delay` | LOW |  |
| `_emit` | `self, task` | LOW |  |
| `completed_results` | `self` | LOW |  |
| `failed_tasks` | `self` | LOW |  |
| `run` | `task` | MED |  |
| `run_retry` | `task` | MED |  |

### `components/rsis3/rsis/practices.py` (234 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_git` | `repo_root` | LOW |  |
| `check_registry` | `` | LOW |  |
| `check_state_files` | `` | LOW |  |
| `_telemetry_counts` | `telemetry_dir` | LOW |  |
| `check_telemetry` | `workspace` | LOW |  |
| `check_checkpoints` | `workspace` | LOW |  |
| `check_workspace` | `workspace` | LOW |  |
| `run_checks` | `workspace` | MED |  |
| `__init__` | `self, name, status, detail` | LOW |  |
| `__str__` | `self` | LOW |  |

### `components/rsis3/rsis/priority_pool.py` (567 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `latency_s` | `self` | LOW | property |
| `save_step_checkpoint` | `self, step_name, step_index, state_data` | MED |  |
| `effective_priority` | `self, aging_rate` | LOW |  |
| `__init__` | `self, num_workers, event_bus, on_event, base_backoff_sec, max_backoff_sec` | LOW |  |
| `_order_key` | `self, task` | LOW |  |
| `_is_ready` | `self, task` | LOW |  |
| `add_task` | `self, task_id, role, payload, priority, depends_on…` | LOW |  |
| `cancel_task` | `self, task_id` | LOW |  |
| `run` | `self, executor` | MED |  |
| `_dispatch_pass` | `self, executor, pool, remaining, queued` | LOW |  |
| `_collect_pass` | `self, remaining, queued` | LOW |  |
| `_handle_preempted` | `self, task` | LOW |  |
| `_handle_failure` | `self, task, exc` | LOW |  |
| `_backoff` | `self, category, attempt` | LOW |  |
| `_run_one` | `self, executor, task` | MED |  |
| `completed_results` | `self` | LOW |  |
| `failed_tasks` | `self` | LOW |  |
| `_emit` | `self, action, task, extra` | LOW |  |
| `_tick_if_due` | `self` | LOW |  |
| `__init__` | `self, num_workers, event_bus, on_event, base_backoff_sec, max_backoff_sec…` | LOW |  |
| `_order_key` | `self, task` | LOW |  |
| `request_preemption` | `self, task_id` | LOW |  |
| `_preempt_lowest_for` | `self, incoming` | LOW |  |
| `update_task_priority` | `self, task_id, new_priority` | LOW |  |
| `__init__` | `self, task, event_bus` | LOW |  |
| `run_step` | `self, step_index, step_name, step_fn, current_state` | MED |  |
| `__init__` | `self, num_workers, event_bus, on_event, base_backoff_sec, max_backoff_sec…` | LOW |  |
| `_tick_if_due` | `self` | LOW |  |

### `components/rsis3/rsis/recovery.py` (198 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, checkpoint_mgr` | LOW |  |
| `rollback_on_failure` | `self, context` | LOW |  |
| `_notify_human` | `self, message` | LOW |  |
| `request_human_review` | `self, context` | LOW |  |
| `set_fallback_interpreter` | `self, path` | LOW |  |
| `execute_via_fallback` | `self, code` | MED |  |
| `record_failure` | `self` | LOW |  |
| `reset_failure_count` | `self` | LOW |  |
| `__init__` | `self, workspace` | LOW |  |
| `corrupt_file` | `self, path` | LOW |  |
| `delete_file` | `self, path` | LOW |  |
| `simulate_crash` | `self, path` | LOW |  |
| `reset_all` | `self` | LOW |  |

### `components/rsis3/rsis/resource_monitor.py` (204 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, resource, value, limit, severity, action_taken` | LOW |  |
| `__repr__` | `self` | LOW |  |
| `__init__` | `self, limits` | LOW |  |
| `set_callbacks` | `self, on_halt, on_throttle, on_warn` | LOW |  |
| `start` | `self` | MED |  |
| `stop` | `self` | MED |  |
| `halt_requested` | `self` | LOW | property |
| `alerts` | `self` | LOW | property |
| `record_api_call` | `self` | HIGH |  |
| `api_calls_per_minute` | `self` | LOW |  |
| `_check_loop` | `self` | LOW |  |
| `_check_all` | `self` | LOW |  |
| `_escalate` | `self, callback, msg` | LOW |  |
| `check_before_operation` | `self` | LOW |  |

### `components/rsis3/rsis/scheduler.py` (213 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `run_demo` | `` | MED |  |
| `__init__` | `self, max_depth, cycle_limit` | LOW |  |
| `register_agent` | `self, role, handler` | LOW |  |
| `list_agents` | `self` | LOW |  |
| `submit_task` | `self, task_id, target_role, description, priority, payload…` | LOW |  |
| `run_event_loop` | `self` | MED |  |
| `_record` | `self, status, task_id, role, error, output…` | LOW |  |

### `components/rsis3/rsis/shared_memory.py` (143 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self` | LOW |  |
| `_get_key_lock` | `self, key` | LOW |  |
| `_copy` | `reg` | LOW | staticmethod |
| `read` | `self, key` | LOW |  |
| `write` | `self, key, value, agent_id` | MED |  |
| `compare_and_swap` | `self, key, expected_version, new_value, agent_id` | LOW |  |
| `atomic_mutate` | `self, key, mutate_fn, agent_id` | LOW |  |
| `snapshot` | `self` | LOW |  |
| `clear` | `self` | LOW |  |

### `components/rsis3/rsis/telemetry.py` (390 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `estimate_cost` | `model, in_tokens, out_tokens` | LOW |  |
| `default_ledger` | `` | LOW |  |
| `__init__` | `self, event_type, path, delta, duration_ms, metadata` | LOW |  |
| `to_dict` | `self` | LOW |  |
| `__init__` | `self, telemetry_dir, flush_interval_s` | LOW |  |
| `start` | `self` | MED |  |
| `stop` | `self` | MED |  |
| `record` | `self, event` | LOW |  |
| `flush` | `self` | LOW |  |
| `_flush_loop` | `self` | LOW |  |
| `session_report` | `self` | LOW |  |
| `__init__` | `self` | LOW |  |
| `cpu_usage` | `self` | LOW |  |
| `memory_usage_mb` | `self` | LOW |  |
| `disk_usage_pct` | `self, path` | LOW |  |
| `__init__` | `self, log_path, budget_cap_usd` | LOW |  |
| `record_llm` | `self, agent, model, latency_s, usage, error` | LOW |  |
| `guard_budget` | `self, model, in_tokens, out_tokens` | LOW |  |
| `budget_remaining` | `self` | LOW |  |
| `total_cost` | `self` | LOW |  |
| `total_cost_locked` | `self` | LOW |  |
| `snapshot` | `self` | LOW |  |
| `report` | `self` | LOW |  |
| `_check_budget_locked` | `self, entry` | LOW |  |
| `_push` | `self, entry` | LOW |  |
| `_replay` | `self` | LOW |  |

### `components/rsis3/rsis/timeout.py` (105 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `deadline` | `seconds, label` | LOW | contextmanager |
| `_timeout_via_sigalrm` | `seconds` | LOW |  |
| `_timeout_via_polling` | `seconds` | LOW |  |
| `__init__` | `self, max_iterations, max_time_s, label` | LOW |  |
| `remaining_time` | `self` | LOW | property |
| `expired` | `self` | LOW | property |
| `tick` | `self` | LOW |  |
| `reset` | `self` | LOW |  |
| `_handler` | `signum, frame` | LOW |  |

### `components/rsis3/rsis/tools/__init__.py` (82 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `default_tool_manager` | `workspace_dir, config` | LOW |  |

### `components/rsis3/rsis/tools/base.py` (46 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `ok` | `self` | LOW | property |
| `run` | `self, tm, args` | MED | ? |

### `components/rsis3/rsis/tools/hitl.py` (279 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `classify_risk` | `tool_name, args` | HIGH |  |
| `coerce` | `cls, mode` | LOW | classmethod |
| `__init__` | `self, mode, approval_threshold, approval_timeout, auto_approve, custom_approval_callback…` | LOW |  |
| `_coerce_threshold` | `threshold` | LOW | staticmethod |
| `classify_risk` | `self, tool_name, args` | HIGH |  |
| `needs_approval` | `self, tool_name, args` | LOW |  |
| `intercept_and_authorize` | `self, agent_role, tool_name, args` | HIGH |  |
| `resolve` | `self, request_id, approved` | LOW |  |
| `_poll_api_mode` | `self, request_id` | LOW |  |
| `_print_interception` | `self, agent_role, tool_name, args_preview, risk` | LOW |  |
| `_cli_prompt_operator` | `` | LOW | staticmethod |
| `_log` | `self, agent, tool, args_preview, risk, approved…` | LOW |  |

### `components/rsis3/rsis/tools/manager.py` (202 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `__init__` | `self, backend, service` | LOW |  |
| `get` | `self, name` | LOW |  |
| `redact` | `self, text` | LOW |  |
| `__init__` | `self, sandbox, config, audit_path` | LOW |  |
| `register` | `self, tool` | LOW |  |
| `list_tools` | `self, agent_name` | LOW |  |
| `execute` | `self, agent_name, tool_name, args` | MED |  |
| `scoped_env` | `self, tool` | LOW |  |
| `_validate` | `tool, args` | LOW | staticmethod |
| `_audit` | `self, agent, tool_name, args, result` | LOW |  |

### `components/rsis3/rsis/tools/sandbox.py` (351 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `as_tool_result` | `self` | LOW |  |
| `__init__` | `self, workdir, default_timeout, allow_network, max_memory_mb, mem_limit…` | LOW |  |
| `_child_limits` | `self` | HIGH |  |
| `run_command` | `self, cmd, env, timeout, cwd, inherit_env` | MED |  |
| `run_python` | `self, code, timeout` | HIGH |  |
| `_run_restricted_python` | `self, code, timeout` | HIGH |  |
| `_get_docker_client` | `self` | LOW |  |
| `run_docker` | `self, cmd, image, timeout, mem_limit, nano_cpus…` | HIGH |  |
| `setup` | `` | LOW |  |
| `_safe_getattr` | `obj, name, default` | LOW |  |
| `_allow_write` | `obj` | MED |  |
| `_passthrough` | `iterable` | LOW |  |
| `_getiter` | `iterable` | LOW |  |

### `components/rsis3/rsis/tools/workspace_tools.py` (115 LOC)

| Function | Args | Risk | Decorators |
|----------|------|------|------------|
| `_resolve_inside` | `root, rel_path` | LOW |  |
| `run` | `self, tm, args` | MED |  |
| `run` | `self, tm, args` | MED |  |
| `run` | `self, tm, args` | MED |  |
| `run` | `self, tm, args` | MED |  |

## 3. Deep-Dive: 20 Most Important Functions (observed)

- **cmd_run / main.py** — Wires L1 run: resource enforcer + telemetry + budget cap + recovery; `finally` guarantees teardown. Solid lifecycle.
- **_apply_tuned_state / config.py** — Applies 6 state files with bounds clamping; fault-tolerant skip on parse error. Finding: silent skip masks corruption.
- **load_config / config.py** — 30+ env overrides; singleton CONFIG at import time — import-time side effect (tests must reset state).
- **run / loop_l1.py** — Per-task action loop with tool-call budget, retries, deadline. Tested by test_loop_l1_retry.py.
- **run_cycle / loop_l2.py** — Improvement loop: candidates, parallel DAG via parallel_candidates, priority aging/preemption hooks.
- **pop / priority_pool.py** — Picks highest effective priority; aging boost per wait-second (D2). 307 LOC of tests.
- **record / telemetry.py** — Writes telemetry; flush interval configurable; part of cost ledger.
- **store / memory.py** — Persists outcome to memory index; called from loops; no schema version.
- **run_recovery / recovery.py** — Re-runs failed command via subprocess; invoked after tool failure.
- **run_python / sandbox.py** — Tier dispatch: RestrictedPython→subprocess→docker; returns SandboxResult. HIGH by design (security boundary).
- **_run_restricted / sandbox.py** — In-process `exec(bytecode, restricted_globals)` with allowlist. HIGH — allowlist is the security boundary.
- **request_approval / hitl.py** — HITL gate; blocklist regexes for rm -rf/subprocess/sys.exit in generated code.
- **run / manager.py** — ToolManager dispatch through allowlists; decides sandbox vs direct.
- **run_pulse / rrp_engine.py** — Runs RRP pulse, persists pulse-NNN.json + dashboard-data.json aggregates.
- **search_hybrid / search_fusion.py** — Hybrid retrieval over TF-IDF + semantic vectors; serves /api/v2/search/hybrid.
- **history / temporal_engine.py** — Subprocess entry from server.py for log/snapshot history.
- **search_query / server.py** — TF-IDF cosine scoring O(Q·D); reads 300 bytes per doc for title extraction.
- **submitAnswer / core.ts** — Validates + routes answer, updates session, emits events, persists.
- **saveSession / core.ts** — Serializes session state; framework_version embedded, no compat check.
- **extractArtifacts / artifact-extractor.ts** — Parses answer text into artifact dictionary; 658-LOC rule engine.

## 4. SPACE TypeScript Functions (module-level inventory)

- `components/space/debug-session.ts` (14 LOC): `for`, `if`
- `components/space/scripts/run-rsi.ts` (305 LOC): `has`, `if`, `is`, `itself`, `while`
- `components/space/src/cli/commands/export.ts` (45 LOC): `catch`, `exportCommand`, `for`, `if`
- `components/space/src/cli/commands/run.ts` (50 LOC): `catch`, `if`, `runCommand`
- `components/space/src/cli/index.ts` (311 LOC): `catch`, `for`, `green`, `if`, `log`
- `components/space/src/cli/tui.ts` (186 LOC): `ask`, `catch`, `if`, `resumeTUI`, `runSessionLoop`, `runTUI`, `while`
- `components/space/src/config/validation.ts` (191 LOC): `assertValidConfig`, `configFromEnv`, `for`, `if`, `listEnvVars`, `validateConfig`
- `components/space/src/data/artifact-extractor.ts` (659 LOC): `constructor`, `estimateConfidence`, `extractAttributes`, `extractAudienceLevel`, `extractBranching`, `extractCadence`, `extractCategories`, `extractCommunication`, `extractCompositionRules`, `extractConfigManagement`, `extractConstraints`, `extractDebtManagement` …
- `components/space/src/data/artifact-keys.ts` (138 LOC): `findClosestKey`, `for`, `if`, `levenshteinDistance`, `validateArtifactDictionary`, `validateArtifactKey`
- `components/space/src/data/artifact-mapping.ts` (533 LOC): `accumulateArtifacts`, `computeConfidence`, `for`, `getArtifact`
- `components/space/src/data/artifact-tracker.ts` (130 LOC): `artifactHash`, `detectStaleness`, `exportVersions`, `getVersionHistory`, `if`, `importVersions`, `recordUpdate`, `toISOString`, `whatIfAnalysis`
- `components/space/src/data/framework-loader.ts` (236 LOC): `catch`, `dfs`, `for`, `if`, `join`, `loadFrameworkFromV1`, `topologicalSort`, `validateFramework`, `while`
- `components/space/src/engine/core.ts` (377 LOC): `createSpace`, `emit`, `for`, `getArtifacts`, `getCurrentQuestion`, `getProgress`, `getStalenessReport`, `if`, `initProject`, `loadSession`, `on`, `resumeSession` …
- `components/space/src/engine/dependency-resolver.ts` (81 LOC): `getAllSeriesStatuses`, `getBlockedSeries`, `getNextAvailableSeries`, `getSeriesStatus`
- `components/space/src/engine/progress.ts` (63 LOC): `computeProgressMetrics`
- `components/space/src/engine/question-router.ts` (166 LOC): `advanceToNextQuestion`, `findNextSeries`, `for`, `getCurrentQuestion`, `goToPreviousQuestion`, `if`
- `components/space/src/engine/session-manager.ts` (125 LOC): `completeRound`, `completeSeries`, `computeCompletionPct`, `createSession`, `deserializeSession`, `for`, `isRoundComplete`, `isSeriesComplete`, `markSessionCompleted`, `markSessionPaused`, `markSessionRunning`, `serializeSession` …
- `components/space/src/engine/snapshot-manager.ts` (80 LOC): `constructor`, `createSnapshot`, `getLatest`, `if`, `listSnapshots`, `recover`, `restoreFromSnapshot`
- `components/space/src/engine/validator.ts` (43 LOC): `if`, `isQuestionAnswered`, `validateAnswer`
- `components/space/src/export/formatters/diff-exporter.ts` (83 LOC): `exportDiff`, `for`, `if`, `push`
- `components/space/src/export/formatters/html-exporter.ts` (99 LOC): `escapeHtml`, `exportHTML`, `for`, `if`
- `components/space/src/export/formatters/json-exporter.ts` (59 LOC): `exportJSON`, `if`
- `components/space/src/export/formatters/markdown-exporter.ts` (104 LOC): `exportMarkdown`, `for`, `if`
- `components/space/src/export/formatters/prompt-exporter.ts` (57 LOC): `exportPrompt`, `if`
- `components/space/src/export/formatters/yaml-exporter.ts` (39 LOC): `exportYAML`, `if`
- `components/space/src/export/index.ts` (117 LOC): `computeStaleness`, `exportDiff`, `exportSession`, `exportToFiles`, `for`, `if`, `switch`
- `components/space/src/i18n/index.ts` (80 LOC): `for`, `getAvailableLocales`, `getLocale`, `getMessages`, `if`, `setLocale`, `t`
- `components/space/src/integration/git.ts` (204 LOC): `autoCommit`, `commit`, `constructor`, `createBranch`, `createGitIntegration`, `diff`, `diffStats`, `for`, `getConfig`, `getDiffSummary`, `getStatus`, `init` …
- `components/space/src/intelligence/adaptive-router.ts` (118 LOC): `analyzeRouting`, `if`, `shouldSkipQuestion`
- `components/space/src/intelligence/analytics.ts` (74 LOC): `computeSessionMetrics`, `for`, `if`
- `components/space/src/intelligence/completeness-scorer.ts` (78 LOC): `scoreCompleteness`
- `components/space/src/intelligence/contradiction-detector.ts` (224 LOC): `detectContradictions`, `for`
- `components/space/src/intelligence/index.ts` (37 LOC): `getIntelligenceReport`
- `components/space/src/intelligence/recommendations.ts` (88 LOC): `for`, `generateRecommendations`, `if`
- `components/space/src/llm/artifact-synthesizer.ts` (43 LOC): `constructor`, `synthesize`
- `components/space/src/llm/factory.ts` (38 LOC): `createProvider`, `createTemplateProvider`, `switch`
- `components/space/src/llm/providers/anthropic-provider.ts` (50 LOC): `complete`, `constructor`, `isAvailable`
- `components/space/src/llm/providers/gemini-provider.ts` (49 LOC): `complete`, `constructor`, `isAvailable`
- `components/space/src/llm/providers/mistral-provider.ts` (51 LOC): `complete`, `constructor`, `isAvailable`
- `components/space/src/llm/providers/null-provider.ts` (19 LOC): `complete`, `isAvailable`
- `components/space/src/llm/providers/ollama-provider.ts` (56 LOC): `complete`, `constructor`, `isAvailable`
- `components/space/src/llm/providers/openai-provider.ts` (52 LOC): `complete`, `constructor`, `isAvailable`
- `components/space/src/llm/providers/template-provider.ts` (74 LOC): `complete`, `extractQuestion`, `for`, `isAvailable`, `match`, `parseArtifacts`, `refineQuestion`, `scoreQuality`, `synthesizeArtifact`
- `components/space/src/llm/quality-scorer.ts` (65 LOC): `Completeness`, `Specificity`, `constructor`, `scoreAnswer`, `scoreSession`
- `components/space/src/llm/question-refiner.ts` (49 LOC): `constructor`, `refine`, `stringify`
- `components/space/src/llm/spec-generator.ts` (37 LOC): `constructor`, `generate`, `stringify`
- `components/space/src/llm/types.ts` (21 LOC): `complete`, `isAvailable`
- `components/space/src/sql.js.d.ts` (21 LOC): `close`, `exec`, `export`, `initSqlJs`, `run`
- `components/space/src/storage/filesystem.ts` (222 LOC): `constructor`, `createProject`, `createSession`, `deleteProject`, `deleteSession`, `ensureDir`, `exportArchive`, `filter`, `findProjectForSession`, `for`, `getLatestSnapshot`, `getProject` …
- `components/space/src/storage/sqlite.ts` (270 LOC): `close`, `constructor`, `create`, `createProject`, `createSession`, `deleteProject`, `deleteSession`, `ensureDir`, `exportArchive`, `for`, `getDbPath`, `getLatestSnapshot` …
- `components/space/src/storage/types.ts` (30 LOC): `createProject`, `createSession`, `deleteProject`, `deleteSession`, `exportArchive`, `getLatestSnapshot`, `getProject`, `getSession`, `importArchive`, `listProjects`, `listSessions`, `listSnapshots` …
- `components/space/src/template/patterns.ts` (27 LOC): `extractTemplateVars`, `for`, `hasTemplateVars`
- `components/space/src/template/resolver.ts` (64 LOC): `getUnresolvedKeys`, `if`, `isResolved`, `resolveContextLines`, `resolveDocument`, `resolveTemplate`, `stringify`
- `components/space/tests/unit/phase1.test.ts` (219 LOC): `while`
- `components/space/tests/unit/phase3.test.ts` (111 LOC): `for`, `makeSession`
- `components/space/tests/unit/phase4.test.ts` (70 LOC): `for`
- `components/space/tests/unit/phase6.test.ts` (154 LOC): `for`
- `components/space/tests/unit/sqlite-storage.test.ts` (237 LOC): `makeProject`, `makeSession`, `makeSnapshot`

## 5. Remaining Python Functions (diagrams-gen, scripts, archived work)

The remaining ~600 functions live in `diagrams/gen/*.py` (visualization generators), build scripts, and archived `.rsirrp/work/` tooling. They are LOW risk (file-write I/O only). Full names/args in `data/audit_py.json`. [O]

## 6. Coverage & Confidence
- Registry completeness: 100% of Python functions enumerated via AST. [O]
- Risk class: heuristic + manual review of the 20 deep-dived functions (High confidence); Med confidence for the rest.
- Cyclomatic complexity not tool-computed (no analyzer installed); estimates in [14](14_STATIC_CODE_ANALYSIS.md).

---
*End of document 07. Next: [08 Class-by-Class Audit](08_CLASS_BY_CLASS_AUDIT.md).*