# Week 9 SOLID Refactoring and Design Patterns
## Purpose
This folder documents the Week 9 refactoring of the existing Study Planning Agent. The aim is to improve dependency boundaries and observability without changing the planning goal, SQLite schema, or controlled-failure behavior[cite: 74].
Week 9 starts from the integrated Week 8 main branch. We implement a Factory for calendar-provider construction and a Decorator for calendar-call logging. The existing FakeCalendarAdapter still acts as an Adapter for CalendarPort[cite: 74].

## Implemented design and exact source locations
| Role | Source file | Responsibility |
|---|---|---|
| Application composition | `run.py` | Reads configuration and assembles the system[cite: 74] |
| Factory | `factories/calendar_factory.py` | Creates a provider satisfying CalendarPort[cite: 74] |
| Abstract contract | `ports/calendar_port.py` | Declares `get_availability()` and `CalendarUnavailableError`[cite: 74] |
| Adapter | `adapters/fake_calendar.py` | Returns deterministic slots or raises a controlled error[cite: 74] |
| Decorator | `adapters/logging_calendar.py` | Logs before/after a calendar call and re-raises errors[cite: 74] |
| Core orchestration | `agent/orchestrator.py` | Coordinates input, tool calls, task states, and persistence[cite: 74] |
| Planning rules | `agent/planner.py` | Orders assignments and creates plan items[cite: 74] |
| Persistence | `adapters/sqlite_repository.py` and `adapters/sqlite_memory.py` | Stores plans, request states, tool calls, and memory events[cite: 74] |

## Design documentation index
- [solid-review.md](solid-review.md): concrete SRP, OCP, LSP, ISP, and DIP evidence[cite: 74].
- [patterns.md](patterns.md): Factory, Adapter, and Decorator roles and interaction[cite: 74].
- [traceability.md](traceability.md): requirements, code, and runtime verification links[cite: 74].
- [code-review-checklist.md](code-review-checklist.md): checks to perform before the Pull Request[cite: 74].

## Behavior that must remain unchanged
1. Valid assignments and working calendar produce a non-empty plan, persist it in SQLite, and reach `Completed`[cite: 74].
2. An unavailable calendar produces a controlled message and reaches `Failed`; the Decorator does not hide the error[cite: 74, 75].
3. Missing assignments reach `WaitingForInput` without calling the calendar provider[cite: 75].
4. An unknown provider name produces a configuration error and a non-zero exit code[cite: 75].