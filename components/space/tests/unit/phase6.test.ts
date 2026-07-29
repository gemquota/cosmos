import { describe, it, expect } from 'vitest';
import { createSpace } from '../../src/engine/core.js';
import { scoreCompleteness } from '../../src/intelligence/completeness-scorer.js';
import { detectContradictions } from '../../src/intelligence/contradiction-detector.js';
import { computeSessionMetrics } from '../../src/intelligence/analytics.js';
import { generateRecommendations } from '../../src/intelligence/recommendations.js';
import { analyzeRouting, shouldSkipQuestion } from '../../src/intelligence/adaptive-router.js';
import { getIntelligenceReport } from '../../src/intelligence/index.js';
import type { SessionState, ArtifactDictionary } from '../../src/types/index.js';

describe('Phase 6: Intelligence Layer', () => {
  const space = createSpace();

  describe('Completeness Scorer', () => {
    it('scores empty session as draft', () => {
      const session = space.startSession('intel_test');
      const report = scoreCompleteness(session, {});
      expect(report.overall_score).toBe(0);
      expect(report.readiness_level).toBe('draft');
      expect(report.per_dimension.length).toBe(7);
    });

    it('scores session with some artifacts', () => {
      const session = space.startSession('intel_test2');
      const artifacts: ArtifactDictionary = {
        domain: { value: 'ML', source_question_id: '1.1.1', source_series_id: 1, confidence: 0.9, last_updated: '' },
        audience_level: {
          value: 'Practitioners',
          source_question_id: '1.1.2',
          source_series_id: 1,
          confidence: 0.8,
          last_updated: '',
        },
      };
      const report = scoreCompleteness(session, artifacts);
      expect(report.overall_score).toBeGreaterThan(0);
      expect(report.overall_score).toBeLessThan(100);
    });
  });

  describe('Contradiction Detector', () => {
    it('detects no contradictions in empty session', () => {
      const session = space.startSession('contra_test');
      const contradictions = detectContradictions(session, {});
      expect(contradictions).toHaveLength(0);
    });

    it('detects solo-vs-scrum contradiction', () => {
      const session = space.startSession('contra_test2');
      const artifacts: ArtifactDictionary = {
        team_composition: {
          value: 'Solo or pair',
          source_question_id: '6.1.2',
          source_series_id: 6,
          confidence: 0.9,
          last_updated: '',
        },
        development_cadence: {
          value: 'Sprint-based agile (Scrum)',
          source_question_id: '6.1.1',
          source_series_id: 6,
          confidence: 0.9,
          last_updated: '',
        },
      };
      const contradictions = detectContradictions(session, artifacts);
      expect(contradictions.length).toBeGreaterThanOrEqual(1);
      expect(contradictions[0].type).toBe('direct');
    });
  });

  describe('Analytics', () => {
    it('computes session metrics', () => {
      const session = space.startSession('analytics_test');
      space.submitAnswer(
        session.session.id,
        '1.1.1',
        'Machine learning recommendation systems with focus on collaborative filtering',
        '1.1.1.a',
      );

      const metrics = computeSessionMetrics(session);
      expect(metrics.session_id).toBe(session.session.id);
      expect(metrics.quality.total_answers).toBe(1);
      expect(metrics.quality.avg_answer_length).toBeGreaterThan(0);
    });
  });

  describe('Recommendations', () => {
    it('generates gap recommendations for empty session', () => {
      const session = space.startSession('rec_test');
      const recs = generateRecommendations(session, {});
      expect(recs.length).toBeGreaterThan(0);
      expect(recs.some((r) => r.category === 'gap')).toBe(true);
    });

    it('generates tip when nearly complete', () => {
      const session = space.startSession('rec_test2');
      // Complete most rounds
      for (let i = 1; i <= 24; i++) {
        session.progress.completed_rounds.push(`1-${i}`);
      }
      const recs = generateRecommendations(session, {});
      expect(recs.some((r) => r.category === 'tip' && r.title.includes('Almost there'))).toBe(true);
    });
  });

  describe('Adaptive Router', () => {
    it('returns decisions for a fresh session', () => {
      const session = space.startSession('route_test');
      const decisions = analyzeRouting(session, space.framework);
      expect(Array.isArray(decisions)).toBe(true);
    });

    it('detects high edit counts', () => {
      const session = space.startSession('route_test2');
      session.answers['1.1.1'] = {
        question_id: '1.1.1',
        series_id: 1,
        round: 1,
        open_ended_text: 'ML',
        answered_at: '',
        edit_count: 5,
      };
      const decisions = analyzeRouting(session, space.framework);
      expect(decisions.some((d) => d.action === 'recommend_review')).toBe(true);
    });

    it('returns null for unanswered question that has deps met', () => {
      // All deps are met for series 1 (no deps) and question not yet answered
      const session = space.startSession('route_test3');
      session.progress.completed_series = [1]; // Simulate series 1 completed
      session.progress.current_series = 2;
      const result = shouldSkipQuestion('2.1.1', session, space.framework);
      expect(result).toBeNull();
    });
  });

  describe('Intelligence Report', () => {
    it('generates complete intelligence report', () => {
      const session = space.startSession('report_test');
      space.submitAnswer(session.session.id, '1.1.1', 'Machine learning systems', '1.1.1.a');
      const artifacts = space.getArtifacts(session.session.id);

      const report = getIntelligenceReport(session, artifacts);
      expect(report.metrics).toBeDefined();
      expect(report.completeness).toBeDefined();
      expect(report.contradictions).toBeDefined();
      expect(report.recommendations).toBeDefined();
      expect(report.recommendations.length).toBeGreaterThan(0);
    });
  });
});
