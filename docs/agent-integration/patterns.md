\# Week 11 Agent Design Patterns



| Pattern | Implementing component | Visible evidence | Boundary |

|---|---|---|---|

| Planning | `PlanningAgent` delegating to `StudyPlanningOrchestrator` | `PLANNING AGENT -> goal received` | The specialist does not reimplement scheduling |

| Tool use | `CalendarPort`, `CalendarAdapterFactory`, `LoggingCalendarDecorator` | `FACTORY -> ...`, `DECORATOR -> ...` | The orchestrator never creates a concrete adapter |

| Memory | `SQLiteMemoryStore` | `memory\_events: 7` after a clean success | Events survive after Python exits |

| Reflection | `ReflectionAgent` and `ReflectionResult` | Three `REFLECTION CHECK` lines | No review before `Completed` |

| Coordination | `AgentCoordinator` | `COORDINATOR -> planning phase started` | Reflection is conditional on state |



\## Why these roles are not just renamed functions

Their responsibilities are distinct: planning produces a candidate, reflection checks it, and coordination controls when each role may run. The project still uses deterministic rules and fake calendar availability; it is \*\*not\*\* an LLM-backed agent.



\## Limitations

The current reflection criteria are intentionally narrow. For example, a unique string label for a calendar slot does not prove there is no real-world time overlap. Rejection is recorded as a verdict, but `AgentCoordinator.run()` returns the candidate `StudyPlan` for compatibility with existing callers; downstream callers must not treat that return value as proof of review acceptance.

