# Product Backlog Study Planning Agent
**Context:** Week 8 classroom planning simulation. Estimates are relative story points, not hours. The Product Owner owns ordering; the Developers provide estimates and technical input[cite: 115].

## Product goal
Help students create trustworthy, reviewable study plans using explicit inputs, transparent scheduling decisions and persistent information[cite: 115, 116].

## Ordered candidate backlog (at Sprint Planning)
| Rank | ID | Product Backlog Item | Value / user benefit | SP | Sprint 8? |
|---|---|---|---|---|---|
| 1 | PB-01 | View saved planning requests | Students can inspect prior requests | 5 | Yes[cite: 116] |
| 2 | PB-02 | Detect missing assignment deadlines | Avoids silently invented data | 3 | Yes[cite: 116] |
| 3 | PB-03 | Export a study plan to Markdown | Allows sharing/review | 5 | Yes[cite: 116] |
| 4 | PB-04 | Configure weekly study-hour limits | Respects capacity constraints | 8 | No[cite: 116] |
| 5 | PB-05 | Improve tool-call failure messages | Clarifies unsuccessful tool calls | 3 | No[cite: 116] |
| 6 | PB-06 | Add tests for planning rules | Reduces regression risk | 5 | No[cite: 116] |
| 7 | PB-07 | Use assignment priority in scheduling | Better allocation of limited time | 8 | No[cite: 116] |
| 8 | PB-08 | Add a cleanup command for demo data | Easier repeatable demonstrations | 2 | No[cite: 116] |

**Selected Sprint 8 capacity:** $PB-01 + PB-02 + PB-03 = 5 + 3 + 5 = 13 \text{ SP}$[cite: 116].

## Refinement detail: selected items
### PB-01 View saved planning requests (5 SP)[cite: 116]
- **User story:** As a student, I want to inspect previously saved planning requests so that I can review what was requested[cite: 116].
- **Illustrative acceptance conditions:** persisted request IDs can be listed; visible output identifies the student and final state; no database modification is required to view history[cite: 116].
- **Dependencies/uncertainty:** depends on SQLite `planning_requests`; display format and privacy need review[cite: 116].

### PB-02 Detect missing assignment deadlines (3 SP)[cite: 116]
- **User story:** As a student, I want the system to request a missing deadline so that it does not invent information[cite: 116].
- **Illustrative acceptance conditions:** missing deadline is detected before planning; the agent asks for input; no fake date is generated or stored[cite: 116].
- **Dependencies/uncertainty:** exact validation boundary and user-facing wording need clarification[cite: 116].

### PB-03 Export a study plan to Markdown (5 SP)[cite: 116]
- **User story:** As a student, I want a Markdown export so that I can share and review my study plan[cite: 116].
- **Illustrative acceptance conditions:** the export includes student name and study items; Markdown headings/lists render; domain logic does not depend on Markdown formatting[cite: 116].
- **Dependencies/uncertainty:** export interface placement and demo preparation; work remains unfinished in the simulation[cite: 116].

## Why this order?
PB-01 reuses existing persistence, PB-02 improves trust at the agent boundary, and PB-03 offers visible output value. PB-04 and PB-07 have greater uncertainty (8 SP); PB-05 to PB-08 remain candidates for later selection[cite: 116].

## After the simulated Sprint Review
- PB-01 and PB-02: **simulated exercise tasks complete**, not implemented production features[cite: 116].
- PB-03: **open**; T-07 and T-08 require further work. Review its priority at the next Product Backlog refinement; it does **not** automatically enter the next Sprint[cite: 116].
- Production implementation: **none performed in Week 8**; all eight PBIs remain potential future software work unless independently completed and verified later[cite: 116].