# Week 10 - Testing and AI-Agent Evaluation
This folder documents the Week 10 verification of the integrated Study Planning Agent. The project uses standard-library `unittest`, disposable SQLite databases, and four deterministic agent-evaluation scenarios.

## Documents
- [Test strategy](test-strategy.md) - scope, isolation, and the nine automated tests[cite: 79].
- [TDD cycle](tdd-cycle.md) - RED, GREEN, and REFACTOR using `PlanningPolicy`[cite: 79].
- [Acceptance scenarios](acceptance-scenarios.md) - Given/When/Then outcomes[cite: 79].
- [Agent evaluation](agent-evaluation.md) - metrics, traces, and interpretation[cite: 79].

## Run from repository root
```powershell
python -m unittest discover -s tests -v
python evaluate_agent.py
python run.py --reset-db
python inspect_database.py