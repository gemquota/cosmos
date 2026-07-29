import type { State, Action } from '../App.tsx';
interface Props { state: State; dispatch: React.Dispatch<Action> }
export default function SummaryView({state,dispatch}:Props) {
  const done=state.completed.size; const pct=Math.round((done/25)*100);
  return (
    <div className="summary-view">
      <h1>Specification Summary</h1>
      <p className="summary-subtitle">{done}/25 rounds ({pct}%)</p>
      <div className="summary-progress"><div className="summary-progress-fill" style={{width:`${pct}%`}}/></div>
      <div className="summary-actions">
        <button className="btn btn-primary" onClick={()=>{const data=JSON.stringify({answers:state.answers,completed:[...state.completed]},null,2);
          const b=new Blob([data],{type:'application/json'});const u=URL.createObjectURL(b);
          const a=document.createElement('a');a.href=u;a.download='space-export.json';a.click();}}>Export JSON</button>
        <button className="btn btn-danger" onClick={()=>{if(confirm('Reset all?'))dispatch({t:'RESET'})}}>Reset</button>
      </div>
    </div>);
}
