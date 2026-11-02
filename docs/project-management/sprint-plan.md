# Sprint Plan Week 8 Classroom Simulation
## Sprint Goal
Make the Study Planning Agent easier to trust and review by improving visibility of saved plans, handling missing deadline information explicitly, and providing a shareable plan output[cite: 117].

## Scope and assumptions
- Existing SQLite-enabled agent application is a **read-only technical baseline** for this lab[cite: 117].
- This is a **simulated iteration for learning Scrum**; writing these documents does not deliver the three production features[cite: 117, 118].
- Simulated Sprint capacity: **13 story points**[cite: 118].
- Story points measure relative effort/complexity/uncertainty; **not a fixed number of hours**[cite: 118].

## Selected Sprint Backlog
| PBI | Intended outcome | SP | Why selected |
|---|---|---|---|
| PB-01 | Review saved planning requests | 5 | Reuses current SQLite persistence[cite: 118] |
| PB-02 | Make missing deadlines explicit | 3 | Protects an agent boundary requirement[cite: 118] |
| PB-03 | Share a plan as Markdown | 5 | Visible reviewable output[cite: 118] |
| **TOTAL** | | **13** | Fits the classroom capacity[cite: 118] |

## Scrum accountabilities for the exercise
| Accountability | Example person / responsibility |
|---|---|
| Product Owner | Student acting as PO: orders PBIs and clarifies value[cite: 118] |
| Scrum Master | Student facilitator: helps remove impediments and protect events[cite: 118] |
| Developers | Developer A, B, C: estimate, plan and coordinate work collectively[cite: 118] |

## Task-level plan (hours are coordination estimates only)
| Task | Parent PBI | Owner | Estimate | Intended evidence |
|---|---|---|---|---|
| T-01 | Saved-request query design | PB-01 | Developer A | 2h | Query sketch / sample fields[cite: 118] |
| T-02 | History display design | PB-01 | Developer B | 1h | Display layout sketch[cite: 118] |
| T-03 | History acceptance checks | PB-01 | Developer C | 1h | Test scenarios written[cite: 118] |
| T-04 | Missing-deadline rule | PB-02 | Developer A | 1h | Explicit validation rule[cite: 118] |
| T-05 | Clarification response | PB-02 | Developer B | 1h | Response scenarios written[cite: 118] |
| T-06 | Markdown export format | PB-03 | Developer C | 1h | Markdown outline[cite: 118] |
| T-07 | Export integration point | PB-03 | Developer A | 1h | Proposed dependency boundary[cite: 118] |
| T-08 | Demo/review preparation | PB-03 | Developer B | 1h | Demo notes for review[cite: 118] |

## Risks and decisions
1. **Ambiguous deadline handling:** clarify PB-02 acceptance before treating it as complete[cite: 118].
2. **Architectural coupling:** put Markdown export at an application edge, not the domain model[cite: 118].
3. **Insufficient review time:** keep unfinished work visible instead of marking all tasks Done[cite: 118].
4. **Scope change:** do not edit production Python code in this lab; capture ideas for later sprints[cite: 118].