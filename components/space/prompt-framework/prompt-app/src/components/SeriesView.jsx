import { useStore } from '../store'
import { allSeries } from '../data/loader'
import RoundView from './RoundView'

export default function SeriesView() {
  const { state, dispatch } = useStore()
  const series = allSeries.find(s => s.id === state.activeSeries)
  if (!series) return <div className="empty-state">Select a series to begin.</div>

  const roundsComplete = [...Array(series.x_rounds).keys()]
    .filter(r => state.completedRounds.has(`${series.id}-${r + 1}`)).length

  const currentRoundData = series.rounds.find(r => r.round === state.activeRound)

  return (
    <div className="series-view">
      <div className="series-header">
        <div className="series-breadcrumb">
          <span
            className="breadcrumb-link"
            onClick={() => dispatch({ type: 'SET_VIEW', view: 'welcome' })}
          >
            All Series
          </span>
          <span className="breadcrumb-sep">/</span>
          <span className="breadcrumb-current">Series {series.id}</span>
        </div>
        <h2 className="series-title">{series.name}</h2>
        <p className="series-desc">{series.description}</p>

        {/* Round tabs */}
        <div className="round-tabs">
          {[...Array(series.x_rounds).keys()].map(i => {
            const rNum = i + 1
            const isComplete = state.completedRounds.has(`${series.id}-${rNum}`)
            const isActive = state.activeRound === rNum
            return (
              <button
                key={rNum}
                className={`round-tab ${isActive ? 'active' : ''} ${isComplete ? 'complete' : ''}`}
                onClick={() => dispatch({ type: 'SET_ROUND', round: rNum })}
              >
                <span className="round-tab-num">
                  {isComplete ? '✓' : rNum}
                </span>
                <span className="round-tab-label">Round {rNum}</span>
              </button>
            )
          })}
        </div>

        <div className="series-progress-compact">
          <div className="series-progress-bar">
            <div className="series-progress-fill" style={{ width: `${(roundsComplete / series.x_rounds) * 100}%` }} />
          </div>
          <span className="series-progress-text">{roundsComplete} / {series.x_rounds} rounds complete</span>
        </div>
      </div>

      {currentRoundData && (
        <RoundView
          key={`${series.id}-${state.activeRound}`}
          series={series}
          round={currentRoundData}
        />
      )}

      {!currentRoundData && (
        <div className="empty-state">Select a round to begin.</div>
      )}
    </div>
  )
}
