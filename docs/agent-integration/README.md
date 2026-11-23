\# Week 11 AI-Agent Integration



\## Purpose

This folder documents the new \*\*PlanningAgent\*\*, \*\*ReflectionAgent\*\*, and \*\*AgentCoordinator\*\* roles around the tested Study Planning Agent. No LLM or external account is required: the agents are deterministic teaching components.



\## Files

\- \[architecture.md](architecture.md) — Mermaid component-and-dependency view.

\- \[sequence.md](sequence.md) — Mermaid success and controlled-failure interaction sequence.

\- \[patterns.md](patterns.md) — Concrete mapping of planning, tool use, memory, reflection and coordination.

\- \[traceability.md](traceability.md) — Requirements, implementation files, observable output and test evidence.

\- \[testing.md](testing.md) — Commands, scenario evidence, regression tests and limits.



\## Runtime verification

From the repository root, use `python run.py --reset-db` for the successful path, `python inspect\_database.py` to inspect persisted evidence, and `python -m unittest discover -s tests -v` to run all 13 tests.



\## Important boundary

The coordinator only reflects a plan after the original orchestrator reaches `Completed`. For `WaitingForInput` and `Failed`, it skips reflection rather than pretending the goal succeeded.

