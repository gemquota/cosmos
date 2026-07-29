import s1 from './01-conceptual-depth.json'
import s2 from './02-ontological-characteristics.json'
import s3 from './03-semantic-relationships.json'
import s4 from './04-procedural-breadth.json'
import s5 from './05-technical-specifications.json'
import s6 from './06-development-methodologies.json'
import s7 from './07-operational-functional.json'

export const allSeries = [s1, s2, s3, s4, s5, s6, s7].map(s => ({
  ...s.series,
  rounds: s.rounds
}))
