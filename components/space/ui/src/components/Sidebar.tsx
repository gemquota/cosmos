import type { State, Action } from '../App.tsx';
import { SERIES } from '../App.tsx';
import { areDepsMet } from '../data/framework-data.ts';

interface Props { state: State; dispatch: React.Dispatch<Action> }

export default function Sidebar({state,dispatch}:Props) {
  const done=state.completed.size;
  const totalRounds=SERIES.reduce((a,s)=>a+s.rounds,0);

  return (
    <aside className="sidebar" role="navigation" aria-label="Series navigation">
      <div
        className="sidebar-header"
        onClick={()=>dispatch({t:'VIEW',v:'dashboard'})}
        onKeyDown={(e)=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();dispatch({t:'VIEW',v:'dashboard'})}}}
        tabIndex={0}
        role="button"
        aria-label="Go to dashboard"
      >
        <h1 className="sidebar-title">🚀 SPACE</h1>
        <span className="sidebar-version">v2.1.0</span>
      </div>

      <nav className="series-nav" aria-label="Series list">
        {SERIES.map(s=>{
          const roundsDone=[...Array(s.rounds).keys()].filter(r=>state.completed.has(`${s.id}-${r+1}`)).length;
          const isDone=roundsDone===s.rounds;
          const depsOk=areDepsMet(s.id, state.completed);
          const isActive=state.series===s.id&&state.view==='question';
          return(
            <div
              key={s.id}
              className={`series-nav-item ${isActive?'active':''} ${isDone?'done':''}`}
              onClick={()=>{if(isDone||depsOk)dispatch({t:'SERIES',id:s.id})}}
              onKeyDown={(e)=>{
                if((e.key==='Enter'||e.key===' ')&&(isDone||depsOk)){
                  e.preventDefault();
                  dispatch({t:'SERIES',id:s.id});
                }
              }}
              tabIndex={isDone||depsOk?0:-1}
              role="button"
              aria-label={`Series ${s.id}: ${s.name}, ${roundsDone} of ${s.rounds} rounds complete${isDone?' (completed)':''}`}
              aria-current={isActive?'page':undefined}
            >
              <span className="nav-num" aria-hidden="true">{isDone?'✓':s.id}</span>
              <div className="nav-info">
                <span className="nav-name">{s.name}</span>
                <div
                  className="nav-progress"
                  role="progressbar"
                  aria-valuenow={roundsDone}
                  aria-valuemin={0}
                  aria-valuemax={s.rounds}
                  aria-label={`${s.name} progress: ${roundsDone} of ${s.rounds}`}
                >
                  <div className="nav-progress-fill" style={{width:`${(roundsDone/s.rounds)*100}%`}}/>
                </div>
                <span className="nav-rounds" aria-hidden="true">{roundsDone}/{s.rounds}</span>
              </div>
            </div>);
        })}
      </nav>

      <div className="sidebar-footer" role="status" aria-label="Session progress">
        <span className="rounds-count">{done} of {totalRounds} rounds</span>
        <button
          className="btn btn-sm"
          onClick={()=>dispatch({t:'VIEW',v:'summary'})}
          aria-label="View summary"
        >
          Summary
        </button>
      </div>
    </aside>);
}
