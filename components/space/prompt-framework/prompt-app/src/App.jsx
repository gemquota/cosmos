import { useStore } from './store'
import Sidebar from './components/Sidebar'
import Welcome from './components/Welcome'
import SeriesView from './components/SeriesView'
import Summary from './components/Summary'

export default function App() {
  const { state } = useStore()

  return (
    <div className="app-layout">
      <Sidebar />
      <main className="main-content">
        {state.view === 'welcome' && <Welcome />}
        {state.view === 'series' && state.activeSeries && <SeriesView />}
        {state.view === 'summary' && <Summary />}
      </main>
    </div>
  )
}
