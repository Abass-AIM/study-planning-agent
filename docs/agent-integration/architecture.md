\# Week 11 Integrated Agent Architecture



The diagram keeps the existing Week 5-10 application core while adding two specialist roles and coordination. Dependencies are supplied at the outer composition root (`run.py`).



```mermaid

flowchart LR

&#x20;   Student\["Student / CLI"] --> Coordinator\["AgentCoordinator"]

&#x20;   Coordinator --> PlanningAgent\["PlanningAgent"]

&#x20;   PlanningAgent --> Orchestrator\["StudyPlanningOrchestrator"]

&#x20;   Orchestrator --> Planner\["Planner"]

&#x20;   Planner --> Policy\["PlanningPolicy"]

&#x20;   Orchestrator --> CalendarPort\["CalendarPort"]

&#x20;   CalendarPort --> Decorator\["LoggingCalendarDecorator"]

&#x20;   Decorator --> Adapter\["FakeCalendarAdapter"]

&#x20;   Orchestrator --> Repo\["StudyRepository"]

&#x20;   Orchestrator --> Memory\["MemoryStore"]

&#x20;   Coordinator --> ReflectionAgent\["ReflectionAgent"]

&#x20;   ReflectionAgent --> Policy

&#x20;   Coordinator --> Memory

&#x20;   Repo --> SQLite\[("SQLite")]

&#x20;   Memory --> SQLite

