import { useStore } from '../store'

export default function RoundView({ series, round }) {
  const { state, dispatch } = useStore()

  const allComplete = round.open_ended.every(oe => {
    const key = `${series.id}.${round.round}.${oe.id}`
    const ans = state.answers[key]
    return ans && ans.openEnded && ans.openEnded.trim() && ans.selectedChoice
  })

  const goNext = () => {
    if (round.round < series.x_rounds) {
      dispatch({ type: 'SET_ROUND', round: round.round + 1 })
    } else {
      dispatch({ type: 'SET_VIEW', view: 'welcome' })
    }
  }

  return (
    <div className="round-view">
      <div className="round-header">
        <h3 className="round-focus">
          {round.focus}
          <span className="round-badge">Round {round.round} of {series.x_rounds}</span>
        </h3>
      </div>

      <div className="questions-list">
        {round.open_ended.map((oe, idx) => (
          <QuestionCard
            key={oe.id}
            oe={oe}
            index={idx + 1}
            seriesId={series.id}
            round={round.round}
          />
        ))}
      </div>

      <div className="round-actions">
        {round.round > 1 && (
          <button
            className="btn btn-secondary"
            onClick={() => dispatch({ type: 'SET_ROUND', round: round.round - 1 })}
          >
            ← Previous Round
          </button>
        )}
        <button
          className={`btn btn-primary ${allComplete ? '' : 'disabled'}`}
          disabled={!allComplete}
          onClick={() => {
            dispatch({ type: 'COMPLETE_ROUND', seriesId: series.id, round: round.round })
            if (allComplete) goNext()
          }}
        >
          {allComplete ? (
            round.round < series.x_rounds ? 'Complete & Next Round →' : 'Complete Series ✓'
          ) : 'Answer all questions to continue'}
        </button>
      </div>
    </div>
  )
}

function QuestionCard({ oe, index, seriesId, round }) {
  const { state, dispatch } = useStore()
  const key = `${seriesId}.${round}.${oe.id}`
  const answer = state.answers[key] || {}

  return (
    <div className="question-card">
      <div className="q-header">
        <span className="q-number">Q{index}</span>
        <span className="q-id">{oe.id}</span>
      </div>
      <p className="q-text">{oe.text}</p>
      <textarea
        className="q-textarea"
        placeholder="Write your answer freely here..."
        value={answer.openEnded || ''}
        onChange={e => dispatch({
          type: 'ANSWER_OE', seriesId, round, oeId: oe.id, text: e.target.value
        })}
        rows={4}
      />
      <div className="q-choices">
        <p className="q-choices-label">After answering, choose one:</p>
        <div className="choices-grid">
          {oe.follow_up_choices.map(choice => (
            <label
              key={choice.id}
              className={`choice-item ${answer.selectedChoice === choice.id ? 'selected' : ''}`}
            >
              <input
                type="radio"
                name={oe.id}
                checked={answer.selectedChoice === choice.id}
                onChange={() => dispatch({
                  type: 'ANSWER_MC', seriesId, round, oeId: oe.id, choiceId: choice.id
                })}
              />
              <span className="choice-label">{choice.id.slice(-1)}</span>
              <span className="choice-text">{choice.text}</span>
            </label>
          ))}
        </div>
      </div>
    </div>
  )
}
