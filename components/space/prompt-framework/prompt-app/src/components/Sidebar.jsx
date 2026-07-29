import { useStore } from '../store'
import { allSeries } from '../data/loader'

export default function Sidebar() {
  const { state, dispatch } = useStore()

  const isLocked = (seriesId) => {
    const series = allSeries.find(s => s.id === seriesId)
    if (!series) return true
    return (series.depends_on || []).some(depId => {
      const dep = allSeries.find(s => s.id === depId)
      return dep ? !state.completedRounds.has(`${dep.id}-${dep.x_rounds}`) : true
    })
  }

  return (
    <aside className="sidebar">
      <div className="sidebar-header" onClick={() => dispatch({ type: 'SET_VIEW', view: 'welcome' })}>
        <h1 className="sidebar-title">Prompt Framework</h1>
        <span className="sidebar-subtitle">v1.0.0</span>
      </div>

      <nav className="series-nav">
        {allSeries.map((series) => {
          const locked = isLocked(series.id)
          const active = state.activeSeries === series.id
          const roundsCompleted = [...Array(series.x_rounds).keys()]
            .filter(r => state.completedRounds.has(`${series.id}-${r + 1}`)).length
          const isFinished = roundsCompleted === series.x_rounds

          return (
            <div
              key={series.id}
              className={`series-nav-item ${isFinished ? 'status-done' : active ? 'status-active' : locked ? 'status-locked' : 'status-ready'} ${active ? 'active' : ''}`}
              onClick={() => {
                if (!locked) {
                  dispatch({ type: 'SELECT_SERIES', seriesId: series.id })
                  dispatch({ type: 'SET_ROUND', round: 1 })
                }
              }}
            >
              <div className="nav-item-header">
                <span className="nav-step-number">{isFinished ? '✓' : series.id}</span>
                <span className="nav-step-name">{series.name}</span>
              </div>
              <div className="nav-progress">
                <div className="nav-progress-bar">
                  <div className="nav-progress-fill" style={{ width: `${(roundsCompleted / series.x_rounds) * 100}%` }} />
                </div>
                <span className="nav-progress-text">{roundsCompleted}/{series.x_rounds}</span>
              </div>
              {locked && <div className="nav-lock-hint">Complete Series {series.depends_on?.[0] || series.id - 1} first</div>}
            </div>
          )
        })}
      </nav>

      <div className="sidebar-footer">
        <div className="sidebar-summary">
          {allSeries.reduce((acc, s) => acc + [...Array(s.x_rounds).keys()]
            .filter(r => state.completedRounds.has(`${s.id}-${r + 1}`)).length, 0)} / {allSeries.reduce((a, s) => a + s.x_rounds, 0)} rounds
        </div>
        <button className="summary-btn" onClick={() => dispatch({ type: 'GO_TO_SUMMARY' })}>
          View Summary
        </button>
      </div>
    </aside>
  )
}
