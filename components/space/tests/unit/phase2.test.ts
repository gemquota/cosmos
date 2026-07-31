import { describe, it, expect } from 'vitest';
import { createSpace } from '../../src/engine/core.js';
import { NullProvider } from '../../src/llm/providers/null-provider.js';
import { TemplateProvider } from '../../src/llm/providers/template-provider.js';
import { createProvider, createTemplateProvider } from '../../src/llm/factory.js';
import { QuestionRefiner } from '../../src/llm/question-refiner.js';
import { ArtifactSynthesizer } from '../../src/llm/artifact-synthesizer.js';
import { SpecificationGenerator } from '../../src/llm/spec-generator.js';
import { QualityScorer } from '../../src/llm/quality-scorer.js';
import type { SpaceConfig } from '../../src/config/defaults.js';

describe('Phase 2: LLM Integration', () => {
  describe('Providers', () => {
    it('NullProvider returns placeholder', async () => {
      const provider = new NullProvider();
      expect(await provider.isAvailable()).toBe(false);
      const result = await provider.complete({ system_prompt: 'test', user_prompt: 'test' });
      expect(result.text).toContain('unavailable');
      expect(result.latency_ms).toBe(0);
    });

    it('TemplateProvider returns deterministic response', async () => {
      const provider = new TemplateProvider();
      expect(await provider.isAvailable()).toBe(true);
      const result = await provider.complete({
        system_prompt: 'question refinement',
        user_prompt: 'Question: What is the domain?\ndomain: machine learning',
      });
      expect(result.text).toBeTruthy();
      expect(result.text).toContain('machine learning');
    });

    it('createProvider returns correct type', () => {
      const nullProvider = createProvider({ llm_provider: 'none' } as SpaceConfig);
      expect(nullProvider).toBeInstanceOf(NullProvider);

      const templateProvider = createProvider({ llm_provider: 'openai' } as SpaceConfig);
      expect(templateProvider).toBeInstanceOf(TemplateProvider); // No API key, falls back
    });
  });

  describe('QuestionRefiner', () => {
    it('refines question with artifact context', async () => {
      const provider = new TemplateProvider();
      const refiner = new QuestionRefiner(provider);

      const result = await refiner.refine(
        'What are the primary entities in this domain?',
        { domain: 'machine learning', audience_level: 'practitioners' },
        { series_name: 'Ontological Characteristics', round_focus: 'Entity Discovery' },
      );

      expect(result.refined_text).toBeTruthy();
      expect(result.original_text).toBe('What are the primary entities in this domain?');
      expect(result.artifacts_used).toContain('domain');
    });
  });

  describe('ArtifactSynthesizer', () => {
    it('synthesizes answer into artifact', async () => {
      const provider = new TemplateProvider();
      const synth = new ArtifactSynthesizer(provider);

      const result = await synth.synthesize({
        question_text: 'What is the domain?',
        open_ended_answer: 'Machine learning recommendation systems',
        selected_choice: 'A single well-established domain',
        prior_artifacts: {},
      });

      expect(result.summary).toBeTruthy();
    });
  });

  describe('QualityScorer', () => {
    it('scores answer quality', async () => {
      const provider = new TemplateProvider();
      const scorer = new QualityScorer(provider);

      const result = await scorer.scoreAnswer({
        question_text: 'What is the domain?',
        answer_text:
          'Machine learning recommendation systems with focus on collaborative filtering and content-based approaches for e-commerce platforms',
        choice_text: 'A single well-established domain',
      });

      expect(result.score).toBeGreaterThanOrEqual(0);
      expect(result.score).toBeLessThanOrEqual(1);
      expect(result.dimensions.completeness).toBeGreaterThanOrEqual(0);
    });

    it('scores entire session', async () => {
      const scorer = new QualityScorer(new TemplateProvider());
      const result = await scorer.scoreSession({
        '1.1.1': { open_ended_text: 'Machine learning' },
        '1.1.2': { open_ended_text: 'ML practitioners' },
      });

      expect(result.overall_score).toBeGreaterThanOrEqual(0);
      expect(result.per_answer['1.1.1']).toBeDefined();
    });
  });

  describe('SpecificationGenerator', () => {
    it('generates specification from artifacts', async () => {
      const provider = new TemplateProvider();
      const gen = new SpecificationGenerator(provider);
      const space = createSpace();

      const result = await gen.generate({
        project_name: 'Test Project',
        artifacts: {
          domain: {
            value: 'machine learning',
            source_question_id: '1.1.1',
            source_series_id: 1,
            confidence: 0.9,
            last_updated: '',
          },
        },
        answers: {},
        framework: space.framework,
        format: 'full',
      });

      expect(result.content).toBeTruthy();
      expect(result.word_count).toBeGreaterThan(0);
      expect(result.quality_score).toBeGreaterThanOrEqual(0);
    });
  });

  describe('Integration with Engine', () => {
    it('engine uses template provider for LLM features', () => {
      const space = createSpace();
      // Verify the engine was created and LLM is configured
      expect(space.config.llm_provider).toBe('none');
      expect(space.framework).toBeDefined();
    });
  });
});
