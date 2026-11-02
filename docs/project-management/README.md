# Week 8 Scrum Planning and Project Governance
**Project:** Study Planning Agent[cite: 114]
**Branch:** week8-scrum-planning[cite: 114]
**Learning mode:** classroom simulation; no production Python feature is implemented in Week 8[cite: 114].

## Purpose
This directory records a simulated Scrum iteration built on the existing SQLite-enabled Study Planning Agent. It documents decisions, relative estimates, roles, task movement, inspection and adaptation. **Simulated board completion is not proof that a product feature has been implemented.**[cite: 114]

## Artifact index
| File | What it records |
|---|---|
| [product-backlog.md](product-backlog.md) | Ordered PB-01 to PB-08, story points, value and risks[cite: 114] |
| [sprint-plan.md](sprint-plan.md) | Sprint Goal, 13 SP capacity, selected work and roles[cite: 114] |
| [sprint-board.md](sprint-board.md) | T-01 to T-08 and simulated status changes[cite: 114] |
| [daily-scrum-log.md](daily-scrum-log.md) | Three daily inspection/adaptation rounds[cite: 114] |
| [definition-of-done.md](definition-of-done.md) | Quality agreement and simulation boundaries[cite: 114, 115] |
| [sprint-review.md](sprint-review.md) | Goal inspection, feedback, open work and backlog adaptation |
| [retrospective.md](retrospective.md) | Team-process learning and measurable improvement |
| [xp-tdd-notes.md](xp-tdd-notes.md) | XP practices and a planned Red-Green-Refactor example |

## Sprint at a glance
- **Product direction:** make the study-planning process trustworthy and reviewable.
- **Selected PBIs:** PB-01 (5 SP), PB-02 (3 SP), PB-03 (5 SP) = **13 SP**.
- **Exercise owners:** Developer A, Developer B and Developer C.
- **Final simulated board:** **6 Done, 1 In Review, 1 In Progress**.
- **Simulated planning outcome:** PB-01 and PB-02 complete in the exercise; PB-03 remains open.
- **Real product state:** Week 6 SQLite application remains the executable baseline; no new feature is claimed[cite: 115].

## Verification and working agreements
1. Read the eight documents in the order shown above[cite: 115].
2. Check that sprint-plan.md and product-backlog.md both total 13 selected story points[cite: 115].
3. Check that the final board contains exactly eight tasks and that daily notes explain the movements[cite: 115].
4. Verify the existing application with `python run.py --reset-db` and `python inspect_database.py`[cite: 115].
5. Do not commit `.db`, `.db-shm` or `.db-wal` runtime files[cite: 115].
6. Review and merge documentation through a Pull Request into main[cite: 115].