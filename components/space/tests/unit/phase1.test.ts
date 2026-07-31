import { describe, it, expect } from 'vitest';
import { createSpace } from '../../src/engine/core.js';
import {
  createSession,
  setAnswer,
  completeRound,
  completeSeries,
  computeCompletionPct,
} from '../../src/engine/session-manager.js';
import { getSeriesStatus, getAllSeriesStatuses, getNextAvailableSeries } from '../../src/engine/dependency-resolver.js';
import { validateAnswer } from '../../src/engine/validator.js';
import { computeProgressMetrics } from '../../src/engine/progress.js';
import type { OpenEndedQuestion, FrameworkDefinition } from '../../src/types/index.js';

const space = createSpace();

describe('Phase 1: Execution Engine', () => {
  describe('Session Manager', () => {
    it('creates a new session with correct defaults', () => {
      const session = createSession('proj_test');
      expect(session.session.id).toMatch(/^sess_/);
      expect(session.session.project_id).toBe('proj_test');
      expect(session.session.status).toBe('created');
      expect(session.answers).toEqual({});
      expect(session.progress.completed_rounds).toEqual([]);
    });

    it('sets answers correctly', () => {
      const session = createSession('proj_test');
      setAnswer(session, '1.1.1', 1, 1, 'Machine learning', '1.1.1.a', 'A single domain');
      expect(session.answers['1.1.1']).toBeDefined();
      expect(session.answers['1.1.1'].open_ended_text).toBe('Machine learning');
      expect(session.answers['1.1.1'].multi_choice_id).toBe('1.1.1.a');
    });

    it('computes completion percentage', () => {
      const session = createSession('proj_test');
      expect(computeCompletionPct(session, 25)).toBe(0);
      completeRound(session, 1, 1);
      expect(computeCompletionPct(session, 25)).toBe(4);
    });
  });

  describe('Dependency Resolver', () => {
    it('marks series 1 as available (no deps)', () => {
      const fw = space.framework;
      const status = getSeriesStatus(fw.series[0], [], [], fw.series);
      expect(status).toBe('available');
    });

    it('marks series 2 as locked when series 1 incomplete', () => {
      const fw = space.framework;
      const status = getSeriesStatus(fw.series[1], [], [], fw.series);
      expect(status).toBe('locked');
    });

    it('marks series 2 as available when series 1 complete', () => {
      const fw = space.framework;
      const completed = ['1-1', '1-2', '1-3'];
      const status = getSeriesStatus(fw.series[1], completed, [1], fw.series);
      expect(status).toBe('available');
    });

    it('gets all series statuses', () => {
      const fw = space.framework;
      const statuses = getAllSeriesStatuses(fw, [], []);
      expect(statuses).toHaveLength(7);
      expect(statuses[0].status).toBe('available');
      expect(statuses[1].status).toBe('locked');
    });

    it('finds next available series', () => {
      const fw = space.framework;
      const next = getNextAvailableSeries(fw, [], []);
      expect(next).not.toBeNull();
      expect(next!.id).toBe(1);
    });
  });

  describe('Question Router', () => {
    it('returns first question for new session', () => {
      const session = space.startSession('proj_test');
      const q = space.getCurrentQuestion(session.session.id);
      expect(q).not.toBeNull();
      expect(q!.question.id).toBe('1.1.1');
      expect(q!.series_id).toBe(1);
      expect(q!.round).toBe(1);
    });
  });

  describe('Answer Submission', () => {
    it('accepts valid answer', () => {
      const session = space.startSession('proj_answer_test');
      const result = space.submitAnswer(session.session.id, '1.1.1', 'Machine learning systems', '1.1.1.a');
      expect(result.accepted).toBe(true);
      expect(result.artifacts_updated.length).toBeGreaterThan(0);
    });

    it('rejects empty answer', () => {
      const session = space.startSession('proj_reject_test');
      const result = space.submitAnswer(session.session.id, '1.1.1', '', '1.1.1.a');
      expect(result.accepted).toBe(false);
    });

    it('rejects invalid choice', () => {
      const session = space.startSession('proj_reject_test2');
      const result = space.submitAnswer(session.session.id, '1.1.1', 'ML', 'invalid_choice');
      expect(result.accepted).toBe(false);
    });
  });

  describe('Full Session Flow', () => {
    it('completes a full session through all 25 rounds', () => {
      const session = space.startSession('proj_full_test');
      let questionCount = 0;
      let maxQuestions = 500; // safety limit

      while (questionCount < maxQuestions) {
        const q = space.getCurrentQuestion(session.session.id);
        if (!q) break;

        const choiceId = q.question.follow_up_choices[0]?.id || '';
        const result = space.submitAnswer(
          session.session.id,
          q.question.id,
          `Test answer for ${q.question.id} — detailed enough to pass validation`,
          choiceId,
        );

        if (!result.accepted) break;
        questionCount++;

        if (result.session_completed) break;
      }

      expect(questionCount).toBeGreaterThan(0);
      expect(questionCount).toBeLessThanOrEqual(326);

      const progress = space.getProgress(session.session.id);
      expect(progress).not.toBeNull();
      expect(progress!.overall.answered).toBeGreaterThan(0);
    });
  });

  describe('Progress Metrics', () => {
    it('computes metrics for partial session', () => {
      const session = space.startSession('proj_metrics_test');
      space.submitAnswer(session.session.id, '1.1.1', 'Test domain', '1.1.1.a');
      space.submitAnswer(session.session.id, '1.1.2', 'Test audience', '1.1.2.b');

      const metrics = space.getProgress(session.session.id);
      expect(metrics).not.toBeNull();
      expect(metrics!.overall.total_questions).toBe(67); // 67 open-ended questions
      expect(metrics!.overall.answered).toBe(2);
      expect(metrics!.by_series).toHaveLength(7);
    });
  });

  describe('Artifacts', () => {
    it('accumulates artifacts from answers', () => {
      const session = space.startSession('proj_artifacts_test');
      space.submitAnswer(session.session.id, '1.1.1', 'Machine learning', '1.1.1.a');
      space.submitAnswer(session.session.id, '1.1.2', 'ML practitioners', '1.1.2.b');

      const artifacts = space.getArtifacts(session.session.id);
      expect(artifacts.domain).toBeDefined();
      expect(artifacts.domain.value).toBe('Machine learning');
      expect(artifacts.audience_level).toBeDefined();
    });
  });

  describe('Serialization', () => {
    it('saves and loads session', () => {
      const session = space.startSession('proj_serial_test');
      space.submitAnswer(session.session.id, '1.1.1', 'Test', '1.1.1.a');

      const json = space.saveSession(session.session.id);
      expect(json).toBeTruthy();

      const loaded = space.loadSession(json);
      expect(loaded.session.id).toBe(session.session.id);
      expect(loaded.answers['1.1.1']).toBeDefined();
    });
  });

  describe('Validator', () => {
    const question: OpenEndedQuestion = {
      id: '1.1.1',
      text: 'What is the domain?',
      follow_up_choices: [
        { id: '1.1.1.a', text: 'Single domain' },
        { id: '1.1.1.b', text: 'Interdisciplinary' },
      ],
    };

    it('validates correct answer', () => {
      const result = validateAnswer({ open_ended: 'Machine learning', choice_id: '1.1.1.a' }, question);
      expect(result.valid).toBe(true);
    });

    it('rejects empty open-ended', () => {
      const result = validateAnswer({ open_ended: '', choice_id: '1.1.1.a' }, question);
      expect(result.valid).toBe(false);
      expect(result.errors).toContain('Open-ended answer cannot be empty');
    });

    it('rejects missing choice', () => {
      const result = validateAnswer({ open_ended: 'ML' }, question);
      expect(result.valid).toBe(false);
      expect(result.errors).toContain('Must select a multiple-choice option');
    });

    it('warns on short answer', () => {
      const result = validateAnswer({ open_ended: 'ML', choice_id: '1.1.1.a' }, question);
      expect(result.warnings.length).toBeGreaterThan(0);
    });
  });
});
