import type { Action } from '../App.tsx';
interface Props { dispatch: React.Dispatch<Action> }
export default function Dashboard({dispatch}:Props) {
  return (
    <div className="dashboard">
      <h1>Structured Prompt<br/>Creation Framework</h1>
      <p>A multi-series, multi-round elicitation framework that alternates open-ended and multi-choice questions to produce a complete development specification.</p>
      <div className="stats-grid">
        <div className="stat-card"><span className="stat-num">7</span><span className="stat-label">Series</span></div>
        <div className="stat-card"><span className="stat-num">25</span><span className="stat-label">Rounds</span></div>
        <div className="stat-card"><span className="stat-num">67</span><span className="stat-label">Open-Ended</span></div>
        <div className="stat-card"><span className="stat-num">259</span><span className="stat-label">Multi-Choice</span></div>
      </div>
      <button className="btn btn-primary btn-lg" onClick={()=>dispatch({t:'SERIES',id:1})}>
        Start with Series 1: Conceptual Depth
      </button>
    </div>);
}
