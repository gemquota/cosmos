import { describe, it, expect } from 'vitest';
import { createSpace } from '../../src/engine/core.js';

describe('Phase 4: Interactive UI', () => {
  describe('TUI module', () => {
    it('TUI has runTUI function', async () => {
      // Dynamic import to avoid CLI side effects
      const tui = await import('../../src/cli/tui.js');
      expect(tui.runTUI).toBeDefined();
      expect(typeof tui.runTUI).toBe('function');
    });
  });

  describe('Engine integration for UI', () => {
    it('engine provides all data needed by UI components', () => {
      const space = createSpace();

      expect(space.framework.series).toHaveLength(7);

      for (const s of space.framework.series) {
        expect(s.rounds.length).toBeGreaterThan(0);
        for (const r of s.rounds) {
          expect(r.open_ended.length).toBeGreaterThan(0);
          for (const q of r.open_ended) {
            expect(q.id).toBeTruthy();
            expect(q.text).toBeTruthy();
            expect(q.follow_up_choices.length).toBeGreaterThan(0);
          }
        }
      }

      const session = space.startSession('ui-test');
      const q = space.getCurrentQuestion(session.session.id);
      expect(q).not.toBeNull();

      const result = space.submitAnswer(
        session.session.id,
        q!.question.id,
        'Test',
        q!.question.follow_up_choices[0].id,
      );
      expect(result.accepted).toBe(true);
    });

    it('UI state transitions work correctly', () => {
      const space = createSpace();
      const session = space.startSession('ui-state-test');

      // Simulate UI flow: dashboard -> question -> answer -> next
      let q = space.getCurrentQuestion(session.session.id);
      expect(q!.series_id).toBe(1);
      expect(q!.round).toBe(1);

      // Answer first question
      space.submitAnswer(session.session.id, q!.question.id, 'ML domain', q!.question.follow_up_choices[0].id);

      // Get next question (should still be in round 1)
      q = space.getCurrentQuestion(session.session.id);
      expect(q!.question.id).toBe('1.1.2');

      // Answer second question to complete round
      space.submitAnswer(session.session.id, q!.question.id, 'Practitioners', q!.question.follow_up_choices[1].id);

      // Progress should show round completed
      const progress = space.getProgress(session.session.id);
      expect(progress!.overall.answered).toBe(2);
    });
  });
});
