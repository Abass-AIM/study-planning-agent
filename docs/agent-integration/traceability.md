\# Week 11 Traceability



| Requirement or design concern | Implementation | Verification | Evidence |

|---|---|---|---|

| Generate a plan from valid assignments | `agent/planning\_agent.py`, `agent/orchestrator.py` | `python run.py --reset-db` | `Completed`; two `PLAN` lines |

| Do not invent missing input | `agent/orchestrator.py`, `agent/coordinator.py` | `python run.py --reset-db --no-assignments` | `WaitingForInput`; reflection skipped |

| Handle calendar failures safely | `ports/calendar\_port.py`, `agent/coordinator.py` | `python run.py --reset-db --calendar-fail` | `Failed`; reflection skipped |

| Enforce at most two hours per session | `agent/planning\_policy.py`, `agent/reflection\_agent.py` | `tests/test\_planning\_policy.py`, `tests/test\_reflection\_agent.py` | Policy tests and review verdict |

| Preserve reflection evidence | `adapters/sqlite\_memory.py`, `agent/coordinator.py` | `python inspect\_database.py` | Seven memory events on clean success |

| Detect incomplete candidate plan | `agent/reflection\_agent.py` | `python -m agent.reflection\_demo` | Missing ID `202`; rejected |

| Keep calendar provider replaceable | `factories/calendar\_factory.py`, `adapters/logging\_calendar.py` | `tests/test\_calendar\_integration.py` | Factory/Decorator traces |

| Keep regression confidence | `tests/` | `python -m unittest discover -s tests -v` | 13 tests; `OK` |



\## Trace interpretation

A terminal trace proves that an event was printed. An SQLite row gives persistent evidence. A passing unit test proves the asserted rule for its inputs, not that every real calendar provider or every scheduling case is correct.

