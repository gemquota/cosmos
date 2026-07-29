import { createSpace } from './src/engine/core.js';
const space = createSpace();
const session = space.startSession('debug');

for (let i = 0; i < 8; i++) {
  const q = space.getCurrentQuestion(session.session.id);
  if (!q) { console.log('No question at step', i); break; }
  console.log('Q:', q.question.id, 'Series:', q.series_id, 'Round:', q.round);
  const choiceId = q.question.follow_up_choices[0]?.id || '';
  const result = space.submitAnswer(session.session.id, q.question.id, 'Test answer for ' + q.question.id, choiceId);
  console.log('  -> accepted:', result.accepted, 'round_done:', result.round_completed, 'series_done:', result.series_completed);
  console.log('  -> progress:', JSON.stringify(session.progress));
}
