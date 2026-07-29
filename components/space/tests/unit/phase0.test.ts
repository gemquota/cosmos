import { describe, it, expect } from 'vitest';
import { loadFrameworkFromV1, validateFramework, topologicalSort } from '../../src/data/framework-loader.js';
import { accumulateArtifacts, ARTIFACT_MAPPINGS } from '../../src/data/artifact-mapping.js';
import { DEFAULT_CONFIG } from '../../src/config/defaults.js';
import type { SessionState } from '../../src/types/index.js';

const FRAMEWORK_DIR = '/data/data/com.termux/files/home/dev/space/prompt-framework';

describe('Phase 0: Foundation', () => {
  describe('Framework Loader', () => {
    it('loads v1 framework and converts to v2', () => {
      const fw = loadFrameworkFromV1(FRAMEWORK_DIR);
      expect(fw.meta.total_series).toBe(7);
      expect(fw.meta.total_rounds).toBe(25);
      expect(fw.meta.total_open_ended).toBe(67);
      expect(fw.meta.total_multi_choice).toBe(259);
      expect(fw.series).toHaveLength(7);
      expect(fw.dependency_graph.edges.length).toBeGreaterThan(0);
    });

    it('validates framework (R1-R8)', () => {
      const fw = loadFrameworkFromV1(FRAMEWORK_DIR);
      const result = validateFramework(fw);
      expect(result.valid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });

    it('produces valid topological sort', () => {
      const fw = loadFrameworkFromV1(FRAMEWORK_DIR);
      const order = topologicalSort(fw);
      expect(order).toHaveLength(7);
      expect(order[0]).toBe(1); // Series 1 has no deps
      expect(order[6]).toBe(7); // Series 7 has most deps
    });
  });

  describe('Artifact Mapping', () => {
    it('has mappings for all 7 series', () => {
      const seriesIds = new Set(ARTIFACT_MAPPINGS.map((m) => m.source_series_id));
      expect(seriesIds.size).toBe(7);
    });

    it('accumulates artifacts from answers', () => {
      const session: SessionState = {
        session: {
          id: 'test',
          project_id: 'p1',
          framework_version: '2.0.0',
          created_at: '',
          updated_at: '',
          status: 'in_progress',
          estimated_completion_pct: 0,
          total_time_ms: 0,
        },
        answers: {
          '1.1.1': {
            question_id: '1.1.1',
            series_id: 1,
            round: 1,
            open_ended_text: 'Machine learning',
            multi_choice_id: '1.1.1.a',
            multi_choice_text: 'A single well-established domain',
            answered_at: '',
            edit_count: 0,
          },
          '1.1.2': {
            question_id: '1.1.2',
            series_id: 1,
            round: 1,
            open_ended_text: 'ML practitioners',
            multi_choice_id: '1.1.2.b',
            multi_choice_text: 'Practitioners / professionals',
            answered_at: '',
            edit_count: 0,
          },
        },
        progress: { completed_rounds: [], completed_series: [], current_series: 1, current_round: 1 },
        artifacts: {},
      };
      const artifacts = accumulateArtifacts(session);
      expect(artifacts.domain).toBeDefined();
      expect(artifacts.domain.value).toBe('Machine learning');
      expect(artifacts.audience_level).toBeDefined();
      expect(artifacts.audience_level.value).toBe('Practitioners / professionals');
    });
  });

  describe('Config', () => {
    it('has sensible defaults', () => {
      expect(DEFAULT_CONFIG.llm_provider).toBe('none');
      expect(DEFAULT_CONFIG.enable_adaptive_questions).toBe(true);
      expect(DEFAULT_CONFIG.default_export_format).toBe('markdown');
    });
  });
});
