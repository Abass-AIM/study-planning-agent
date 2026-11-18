# Week 10 Test Strategy 
 
## Scope and purpose 
 
| Level | File | Tests | What is verified | 
|---|---|---:|---| 
| Unit | `tests/test_planning_policy.py` | 3 | Two-hour cap, short session, negative input | 
| Integration | `tests/test_calendar_integration.py` | 2 | Factory + Decorator success and error propagation | 
| System | `tests/test_system_planning.py` | 1 | Orchestrator + Planner + SQLite end-to-end | 
| Acceptance | `tests/test_acceptance_workflows.py` | 3 | Success, missing input, calendar outage | 
| **Total** | | **9** | | 
 
## Isolation and reproducibility 
 
- Unit tests do not use the calendar or database. 
- Integration tests use a deterministic fake calendar and captured log output. 
- System and acceptance tests create separate temporary SQLite databases. 
- Each test is repeatable and does not modify `study_planning_agent.db`. 
- Standard library only: `unittest`, `tempfile`, `io`, and `sqlite3`. 
 
## What counts as success? 
 
- All nine test methods pass. 
- `python run.py --reset-db` still generates a persisted nonempty plan. 
- `--no-assignments` stops in `WaitingForInput` without a calendar call. 
- `--calendar-fail` stops in `Failed` with a failed tool trace. 
- The two-hour session rule is enforced by the new policy. 
 
## Commands 
 
```powershell 
python -m unittest tests.test_planning_policy -v 
python -m unittest tests.test_calendar_integration -v 
python -m unittest tests.test_system_planning -v 
python -m unittest tests.test_acceptance_workflows -v 
python -m unittest discover -s tests -v 
``` 
 
## Limits 
 
These tests use a fake calendar and fixed data. They do not prove real API 
availability, probabilistic LLM quality, or performance at scale. 