import { describe, it, expect } from 'vitest';
import { createSpace } from '../../src/engine/core.js';
import { exportSession, exportDiff } from '../../src/export/index.js';
import type { SessionState, ArtifactDictionary } from '../../src/types/index.js';

const space = createSpace();

function makeSession(): { session: SessionState; artifacts: ArtifactDictionary } {
  const s = space.startSession('export_test');
  space.submitAnswer(s.session.id, '1.1.1', 'Machine learning recommendation systems', '1.1.1.a');
  space.submitAnswer(s.session.id, '1.1.2', 'ML practitioners', '1.1.2.b');
  space.submitAnswer(s.session.id, '1.2.1', 'Core ML fundamentals assumed', '1.2.1.b');
  return { session: s, artifacts: space.getArtifacts(s.session.id) };
}

describe('Phase 3: Export Pipeline', () => {
  const fw = space.framework;

  describe('JSON Export', () => {
    it('exports valid JSON with metadata', () => {
      const { session, artifacts } = makeSession();
      const result = exportSession(session, artifacts, fw, 'json', 'Test Project');

      expect(result.mime_type).toBe('application/json');
      expect(result.filename).toContain('.json');

      const parsed = JSON.parse(result.content);
      expect(parsed.meta.framework_version).toBe('2.0.0');
      expect(parsed.meta.project_name).toBe('Test Project');
      expect(parsed.session.project_id).toBe('export_test');
      expect(parsed.summary.total_questions).toBe(67);
    });
  });

  describe('Markdown Export', () => {
    it('exports markdown with sections', () => {
      const { session, artifacts } = makeSession();
      const result = exportSession(session, artifacts, fw, 'markdown', 'Test Project');

      expect(result.mime_type).toBe('text/markdown');
      expect(result.content).toContain('# Test Project — Specification Document');
      expect(result.content).toContain('## Series Progress');
      expect(result.content).toContain('Conceptual Depth');
    });
  });

  describe('YAML Export', () => {
    it('exports valid YAML', () => {
      const { session, artifacts } = makeSession();
      const result = exportSession(session, artifacts, fw, 'yaml', 'Test Project');

      expect(result.mime_type).toBe('text/yaml');
      expect(result.content).toContain('framework_version:');
      expect(result.content).toContain('project_name: Test Project');
    });
  });

  describe('Prompt Export', () => {
    it('exports prompt format', () => {
      const { session, artifacts } = makeSession();
      const result = exportSession(session, artifacts, fw, 'prompt', 'Test Project');

      expect(result.mime_type).toBe('text/plain');
      expect(result.content).toContain('generating a specification for: Test Project');
      expect(result.content).toContain('Machine learning');
    });
  });

  describe('HTML Export', () => {
    it('exports styled HTML', () => {
      const { session, artifacts } = makeSession();
      const result = exportSession(session, artifacts, fw, 'html', 'Test Project');

      expect(result.mime_type).toBe('text/html');
      expect(result.content).toContain('<!DOCTYPE html>');
      expect(result.content).toContain('Test Project');
    });
  });

  describe('Diff Export', () => {
    it('detects differences between sessions', () => {
      const s1 = space.startSession('diff_test_1');
      space.submitAnswer(s1.session.id, '1.1.1', 'ML systems', '1.1.1.a');

      const s2 = space.startSession('diff_test_2');
      space.submitAnswer(s2.session.id, '1.1.1', 'NLP systems', '1.1.1.b');
      space.submitAnswer(s2.session.id, '1.1.2', 'Researchers', '1.1.2.a');

      const result = exportDiff(s1, s2, fw, 'Original', 'Revised');

      expect(result.content).toContain('## Changed Answers');
      expect(result.content).toContain('## Added');
      expect(result.content).toContain('1.1.2');
    });
  });

  describe('All Formats Handle Partial Sessions', () => {
    it('handles empty session gracefully', () => {
      const s = space.startSession('empty_test');
      const artifacts = space.getArtifacts(s.session.id);

      const formats = ['json', 'markdown', 'yaml', 'prompt', 'html'] as const;
      for (const fmt of formats) {
        const result = exportSession(s, artifacts, fw, fmt, 'Empty Project');
        expect(result.content).toBeTruthy();
        expect(result.content.length).toBeGreaterThan(0);
      }
    });
  });
});
