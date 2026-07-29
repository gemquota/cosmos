import { useStore } from '../store'
import { allSeries } from '../data/loader'

export default function Summary() {
  const { state, dispatch } = useStore()
  const answers = state.answers
  const totalRounds = allSeries.reduce((a, s) => a + s.x_rounds, 0)
  const completed = allSeries.reduce((acc, s) =>
    acc + [...Array(s.x_rounds).keys()].filter(r =>
      state.completedRounds.has(`${s.id}-${r + 1}`)
    ).length, 0
  )

  const completionPct = Math.round((completed / totalRounds) * 100)

  const allData = allSeries.map(series => ({
    ...series,
    rounds: series.rounds.map(round => ({
      ...round,
      open_ended: round.open_ended.map(oe => ({
        ...oe,
        answer: answers[`${series.id}.${round.round}.${oe.id}`] || null
      }))
    }))
  }))

  const handleExportJSON = () => {
    const exportData = allSeries.map(series => ({
      id: series.id,
      name: series.name,
      rounds: series.rounds.map(round => ({
        round: round.round,
        focus: round.focus,
        open_ended: round.open_ended.map(oe => {
          const key = `${series.id}.${round.round}.${oe.id}`
          const ans = answers[key]
          return {
            id: oe.id,
            question: oe.text,
            answer: ans?.openEnded || '',
            selectedChoice: ans?.selectedChoice
              ? oe.follow_up_choices.find(c => c.id === ans.selectedChoice)?.text
              : '',
            selectedChoiceId: ans?.selectedChoice || '',
          }
        })
      }))
    }))

    const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'prompt-framework-specification.json'
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <div className="summary-view">
      <div className="summary-header">
        <h2>Specification Summary</h2>
        <p className="summary-subtitle">
          {completed} of {totalRounds} rounds completed ({completionPct}%)
        </p>
        <div className="summary-progress-bar">
          <div className="summary-progress-fill" style={{ width: `${completionPct}%` }} />
        </div>
      </div>

      <div className="summary-actions">
        <button className="btn btn-primary" onClick={handleExportJSON}>
          Export as JSON
        </button>
        <button className="btn btn-secondary" onClick={() => dispatch({ type: 'RESET' })}>
          Reset All Answers
        </button>
      </div>

      <div className="summary-series">
        {allData.map(series => {
          const roundsDone = [...Array(series.x_rounds).keys()]
            .filter(r => state.completedRounds.has(`${series.id}-${r + 1}`)).length

          return (
            <details key={series.id} className="summary-series-block" open={roundsDone === series.x_rounds}>
              <summary className="summary-series-header">
                <span className="ss-num">{series.id}</span>
                <span className="ss-name">{series.name}</span>
                <span className="ss-status">
                  {roundsDone === series.x_rounds ? '✓ Complete' : `${roundsDone}/${series.x_rounds} rounds`}
                </span>
              </summary>

              <div className="summary-rounds">
                {series.rounds.map(round => (
                  <div key={round.round} className="summary-round">
                    <h4 className="sr-title">Round {round.round}: {round.focus}</h4>
                    {round.open_ended.map(oe => (
                      <div key={oe.id} className="summary-answer">
                        <div className="sa-question">
                          <span className="sa-id">{oe.id}</span>
                          {oe.text}
                        </div>
                        {oe.answer ? (
                          <>
                            <div className="sa-text">
                              <span className="sa-label">Open-ended:</span>
                              <p>{oe.answer.openEnded || <em>Not answered</em>}</p>
                            </div>
                            <div className="sa-choice">
                              <span className="sa-label">Selected:</span>
                              <span className="sa-choice-badge">
                                {oe.answer.selectedChoice
                                  ? oe.follow_up_choices.find(c => c.id === oe.answer.selectedChoice)?.text || oe.answer.selectedChoice
                                  : <em>Not selected</em>}
                              </span>
                            </div>
                          </>
                        ) : (
                          <p className="sa-unanswered"><em>Not yet answered</em></p>
                        )}
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            </details>
          )
        })}
      </div>
    </div>
  )
}
