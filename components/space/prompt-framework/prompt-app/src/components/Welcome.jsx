import { useStore } from '../store'
import { allSeries } from '../data/loader'

export default function Welcome() {
  const { state, dispatch } = useStore()
  const completedRounds = allSeries.reduce((acc, s) =>
    acc + [...Array(s.x_rounds).keys()].filter(r =>
      state.completedRounds.has(`${s.id}-${r + 1}`)
    ).length, 0)
  const totalRounds = allSeries.reduce((a, s) => a + s.x_rounds, 0)

  return (
    <div className="welcome">
      <div className="welcome-hero">
        <h1 className="welcome-title">Structured Prompt<br/>Creation Framework</h1>
        <p className="welcome-desc">
          A multi-series, multi-round elicitation framework that alternates open-ended
          and multi-choice questions to produce a complete development specification.
        </p>
      </div>

      <div className="welcome-stats">
        <div className="stat-card">
          <span className="stat-number">{allSeries.length}</span>
          <span className="stat-label">Series</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{totalRounds}</span>
          <span className="stat-label">Rounds</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{allSeries.reduce((a, s) => a + s.total_open_ended, 0)}</span>
          <span className="stat-label">Open-Ended</span>
        </div>
        <div className="stat-card">
          <span className="stat-number">{allSeries.reduce((a, s) => a + s.total_multi_choice, 0)}</span>
          <span className="stat-label">Multi-Choice</span>
        </div>
      </div>

      {completedRounds > 0 && (
        <div className="welcome-resume">
          <span className="resume-text">You have {completedRounds} of {totalRounds} rounds completed.</span>
        </div>
      )}

      <div className="chain-viz">
        <h2>Dependency Chain</h2>
        <div className="chain-flow">
          {allSeries.map((s, i) => (
            <div key={s.id} className="chain-node">
              <span className="chain-num">{s.id}</span>
              <span className="chain-name">{s.name}</span>
              {i < allSeries.length - 1 && (
                <svg className="chain-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M5 12h14M13 5l7 7-7 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              )}
            </div>
          ))}
        </div>
      </div>

      <div className="series-cards">
        {allSeries.map(s => (
          <div
            key={s.id}
            className="series-card"
            onClick={() => {
              dispatch({ type: 'SELECT_SERIES', seriesId: s.id })
              dispatch({ type: 'SET_ROUND', round: 1 })
            }}
          >
            <div className="series-card-num">{s.id}</div>
            <div className="series-card-body">
              <h3>{s.name}</h3>
              <p>{s.description}</p>
              <div className="series-card-meta">
                <span>{s.x_rounds} rounds</span>
                <span>{s.total_open_ended} open-ended</span>
                <span>{s.total_multi_choice} multi-choice</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      <button
        className="start-btn"
        onClick={() => {
          dispatch({ type: 'SELECT_SERIES', seriesId: 1 })
          dispatch({ type: 'SET_ROUND', round: 1 })
        }}
      >
        Start with Series 1: Conceptual Depth
      </button>
    </div>
  )
}
