import type { State, Action } from '../App.tsx';
import { QDATA } from '../App.tsx';
interface Props { state: State; dispatch: React.Dispatch<Action> }

export default function QuestionView({state,dispatch}:Props) {
  const sd=QDATA[state.series];
  if(!sd) return <div>Series not found</div>;
  const rd=sd.rounds[state.round-1];
  if(!rd) return <div>Round not found</div>;

  const allAnswered=rd.questions.every(q=>state.answers[q.id]?.oe?.trim()&&state.answers[q.id]?.mc);
  const isSeriesDone = state.series > 7 ? false : false;

  return (
    <div className="question-view">
      <div className="breadcrumb">
        <span onClick={()=>dispatch({t:'VIEW',v:'dashboard'})} role="button" tabIndex={0} onKeyDown={(e)=>e.key==='Enter'&&dispatch({t:'VIEW',v:'dashboard'})}>Dashboard</span>
        <span className="sep">/</span>
        <span onClick={()=>dispatch({t:'SERIES',id:state.series})} role="button" tabIndex={0} onKeyDown={(e)=>e.key==='Enter'&&dispatch({t:'SERIES',id:state.series})}>{sd.name}</span>
        <span className="sep">/</span>
        <span>Round {state.round}</span>
      </div>

      <h1>{sd.name} — Round {state.round}</h1>
      <p className="round-focus">{rd.focus}</p>

      <div className="round-tabs" role="tablist" aria-label="Round navigation">
        {sd.rounds.map((r,i)=>{
          const roundNum=i+1;
          const done=state.completed.has(`${state.series}-${roundNum}`);
          const active=roundNum===state.round;
          return(
            <button
              key={roundNum}
              className={`round-tab${active?' active':''}${done?' done':''}`}
              onClick={()=>dispatch({t:'ROUND',r:roundNum})}
              aria-label={`Round ${roundNum}${done?' completed':''}${active?' (current)':''}`}
              aria-current={active?'true':undefined}
            >{roundNum}</button>);
        })}
      </div>

      {rd.questions.map((q,i)=>{
        const ans=state.answers[q.id];
        return(
          <div key={q.id} className="question-card" role="region" aria-label={`Question ${q.id}`}>
            <div className="q-header">
              <span className="q-num">{i+1}</span>
              <span className="q-id">{q.id}</span>
            </div>
            <div className="q-text">{q.text}</div>
            <textarea
              className="q-textarea"
              placeholder="Write your answer freely..."
              value={ans?.oe||''}
              onChange={e=>dispatch({t:'OE',qid:q.id,text:e.target.value})}
              aria-label={`Answer for question ${q.id}`}
            />
            <div className="choices-label">Select one:</div>
            <div className="choices-grid" role="radiogroup" aria-label={`Choices for question ${q.id}`}>
              {q.choices.map((c,ci)=>(
                <label
                  key={c.id}
                  className={`choice-item${ans?.mc===c.id?' selected':''}`}
                  role="radio"
                  aria-checked={ans?.mc===c.id}
                  tabIndex={0}
                  onKeyDown={(e)=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();dispatch({t:'MC',qid:q.id,cid:c.id})}}}
                >
                  <input type="radio" name={q.id} checked={ans?.mc===c.id} onChange={()=>dispatch({t:'MC',qid:q.id,cid:c.id})} />
                  <span className="choice-letter">{String.fromCharCode(97+ci)}</span>
                  <span className="choice-text">{c.text}</span>
                </label>
              ))}
            </div>
          </div>);
      })}

      <div className="question-actions">
        <button className="btn" onClick={()=>{
          const prev=state.round-1;
          if(prev>=1) dispatch({t:'ROUND',r:prev});
        }} disabled={state.round<=1}>← Previous Round</button>
        {allAnswered && (
          <button
            className="btn btn-primary"
            onClick={()=>{dispatch({t:'DONE',series:state.series,round:state.round}); const next=state.round+1; if(next<=sd.rounds.length) dispatch({t:'ROUND',r:next}); else dispatch({t:'VIEW',v:'summary'});}}
            aria-label={state.round<sd.rounds.length?'Complete round and continue':'Complete final round'}
          >
            {state.round<sd.rounds.length?'Complete Round →':'Finish Series →'}
          </button>
        )}
      </div>
    </div>);
}

