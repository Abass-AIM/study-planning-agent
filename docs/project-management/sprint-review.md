# Sprint Review Week 8 (Simulated)
## Sprint Goal
Make the Study Planning Agent easier to trust and review by improving visibility of saved plans, handling missing deadline information explicitly, and providing a shareable plan output[cite: 122].

## Evidence inspected
- **Current executable baseline:** existing SQLite-enabled agent still runs (`python run.py --reset-db` and `python inspect_database.py`)[cite: 122].
- **Exercise artifacts:** planned saved-request display, missing-deadline acceptance conditions, Markdown export outline[cite: 122].
- **Final simulated board:** 6 Done, 1 In Review, 1 In Progress[cite: 122].

## Selected work at review
| PBI | Simulated task progress | Real product feature delivered? | Review decision |
|---|---|---|---|
| PB-01 | T-01, T-02, T-03 all Done | **No**[cite: 123] | Design exercise complete; implementation future work[cite: 122] |
| PB-02 | T-04, T-05 both Done | **No**[cite: 123] | Rules clarified; implementation future work[cite: 122] |
| PB-03 | T-06 Done; T-07 In Progress; T-08 In Review | **No**[cite: 123] | Open; review priority in backlog refinement[cite: 122] |

## Stakeholder feedback (classroom role-play)
1. Show a request identifier and final state beside each saved planning request[cite: 123].
2. When an assignment lacks a deadline, ask for clarification rather than generate a guessed date[cite: 123].
3. Markdown export must remain legible and include enough context to explain the plan[cite: 123].

## Sprint Goal assessment
**Partially achieved in the classroom simulation:** PB-01 and PB-02 planning/design tasks reached simulated Done; PB-03 remains unfinished. **No new functioning production Increment was delivered in Week 8.** The working software baseline is unchanged[cite: 123].

## Product Backlog adaptation
- Return PB-03's unfinished design/integration work to backlog refinement (not automatically into the next Sprint)[cite: 123].
- Add "show request ID and final state" to PB-01's acceptance notes[cite: 123].
- Keep all product feature implementation work visible for a later coding Sprint[cite: 123].
- Review PB-03 priority based on stakeholder feedback and current team capacity[cite: 123].