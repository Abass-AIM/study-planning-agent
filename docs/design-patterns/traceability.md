# Week 9 Engineering Traceability
| ID | Engineering concern | Primary evidence | Verification |
|---|---|---|---|
| W9-01 | Calendar provider selection is centralized | `factories/calendar_factory.py`, `run.py` | Normal run prints `FACTORY -> created FakeCalendarAdapter`[cite: 78] |
| W9-02 | Core planning avoids concrete provider construction | `agent/orchestrator.py`, `ports/calendar_port.py` | Orchestrator has no direct `FakeCalendarAdapter` import[cite: 78] |
| W9-03 | Tool-call logging added without editing provider | `adapters/logging_calendar.py`, `adapters/fake_calendar.py` | Success run prints `DECORATOR` messages[cite: 78] |
| W9-04 | Independent tool failures remain controlled | `ports/calendar_port.py`, `agent/orchestrator.py` | Failure run reaches `Failed` safely[cite: 78] |
| W9-05 | Missing input prevents tool invocation | `agent/orchestrator.py` | No-assignments run reaches `WaitingForInput`[cite: 78] |
| W9-06 | Refactoring preserves persistence | `adapters/sqlite_repository.py`, `db/schema.sql` | `inspect_database.py` shows rows[cite: 78] |