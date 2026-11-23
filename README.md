# Study Planning Agent 
 
**Course:** Software Engineering and AI Agent Fundamentals 
**Course code:** GAINBAN-SZOFMEIN-1 
**Project type:** Semester laboratory project 
 
## About This Repository 
 
This repository contains the semester project and laboratory artefacts for the Software Engineering and AI Agent Fundamentals course. 
 
The project is developed incrementally. Each laboratory adds software engineering documentation, models, source code, tests, or AI-agent-related components. 
 
 
## Current Repository Structure 
 
```text 
study-planning-agent/ 

├── adapters/ 

│   ├── __init__.py 

│   ├── fake_calendar.py 

│   ├── logging_calendar.py 

│   ├── sqlite_database.py 

│   ├── sqlite_memory.py 

│   └── sqlite_repository.py 

├── agent/ 

│   ├── __init__.py 

│   ├── orchestrator.py 

│   ├── planner.py 

│   ├── planning_policy.py 

│   └── states.py 

├── db/ 

│   └── schema.sql 

├── docs/ 

│   ├── architecture/ 

│   │   ├── agent-architecture.md 

│   │   ├── architecture-decisions.md 

│   │   ├── interfaces.md 

│   │   ├── README.md 

│   │   └── system-architecture.md 

│   ├── behavior/ 

│   │   ├── activity-diagram.md 

│   │   ├── README.md 

│   │   ├── sequence-diagram.md 

│   │   └── state-machine-diagram.md 

│   ├── data-model/ 

│   │   ├── conceptual-model.md 

│   │   ├── mapping.md 

│   │   ├── normalization.md 

│   │   ├── queries.md 

│   │   ├── README.md 

│   │   └── relational-schema.md 

│   ├── design-patterns/ 

│   │   ├── code-review-checklist.md 

│   │   ├── patterns.md 

│   │   ├── README.md 

│   │   ├── solid-review.md 

│   │   └── traceability.md 

│   ├── models/ 

│   │   ├── class-diagram.md 

│   │   ├── database-diagram.md 

│   │   ├── object-diagram.md 

│   │   ├── package-diagram.md 

│   │   ├── README.md 

│   │   └── use-case-diagram.md 

│   ├── project-management/ 

│   │   ├── daily-scrum-log.md 

│   │   ├── definition-of-done.md 

│   │   ├── product-backlog.md 

│   │   ├── README.md 

│   │   ├── retrospective.md 

│   │   ├── sprint-board.md 

│   │   ├── sprint-plan.md 

│   │   ├── sprint-review.md 

│   │   └── xp-tdd-notes.md 

│   ├── testing/ 

│   │   ├── acceptance-scenarios.md 

│   │   ├── agent-evaluation.md 

│   │   ├── README.md 

│   │   ├── tdd-cycle.md 

│   │   └── test-strategy.md 

│   ├── requirements.md 

│   ├── stakeholdres.md 

│   ├── use-cases.md 

│   └── user-stories.md 

├── domain/ 

│   ├── __init__.py 

│   └── models.py 

├── factories/ 

│   ├── __init__.py 

│   └── calendar_factory.py 

├── notes/ 

│   └── week1.md 

├── ports/ 

│   ├── __init__.py 

│   ├── calendar_port.py 

│   ├── memory_store.py 

│   └── study_repository.py 

├── tests/ 

│   ├── __init__.py 

│   ├── test_acceptance_workflows.py 

│   ├── test_calendar_integration.py 

│   ├── test_planning_policy.py 

│   └── test_system_planning.py 

├── .gitignore 

├── __init__.py 

├── agent_memory.json 

├── agent_output.txt 

├── evaluate_agent.py 

├── inspect_database.py 

├── lab_agent.py 

├── README.md 

└── run.py 
``` 
 
The tree summarizes the key source and Week 10 deliverables; earlier files in 
`docs/` and the Week 1 outputs remain in the repository. 
 
 
## Week 2 - Requirements Engineering 
 
Week 2 adds stakeholder analysis, functional and non-functional requirements, AI-agent boundaries, user stories, acceptance criteria, traceability, and a Mermaid use-case-style model. The artefacts are stored in `docs/`. 
 
## Week 3 – UML Structural Modeling 
 
Week 3 adds structural models and a small Python domain-model application. Mermaid sources are stored in `docs/models/`, and `app.py` implements the same Student, Assignment, StudyPlan, and PlanItem concepts shown in the diagrams. 
 
## Week 4 - Behavioral Modeling 
 
Week 4 adds an executable planning workflow and three behavioral views of the same use case: an activity-style flowchart, a native Mermaid state machine, and a native Mermaid sequence diagram. The sequence model includes an AI-agent-style component calling a calendar tool and handling both success and failure. 
 
## Week 5 - Software Architecture 
 
Week 5 refactors the behavioral prototype into a small modular architecture. The project separates domain concepts, orchestration, planning, external ports, and concrete adapters. Mermaid diagrams document the decomposition and dependency direction. 
 
## Week 6 - Data Modeling and Persistence 
 
Week 6 maps the Study Planning Agent domain model to a normalized relational schema and adds an executable SQLite persistence adapter. Students, assignments, plans and plan items are stored as business data. Planning-request state, memory events and calendar tool calls demonstrate persistence for agent workflows. 
 
## Week 8 - Scrum Planning and Project Governance 
- Planning artefacts: `docs/project-management/README.md` (index plus eight detailed Markdown files). 
- Scope: Scrum planning and simulated iteration; no new production Python feature in Week 8. 
- Sprint Goal: improve transparency, missing-deadline handling, and shareability. 
- Selected: PB-01 (5 SP), PB-02 (3 SP), PB-03 (5 SP); 13 SP capacity. 
- Final simulated board: 6 Done, 1 In Review, 1 In Progress; PB-03 is unfinished. 
- Existing SQLite application remains the working technical baseline. 
 
## Week 9 - SOLID Refactoring and Design Patterns 
  
Week 9 refactors calendar-provider construction into `factories/calendar_factory.py` and adds tool-call logging through `adapters/logging_calendar.py`. `run.py` selects the configured provider, wraps it with `LoggingCalendarDecorator`, and injects the resulting `CalendarPort` into the existing orchestrator. The domain model, agent goal, and SQLite schema remain unchanged. 
  
Documentation and engineering evidence: [`docs/design-patterns/README.md`](docs/design-patterns/README.md). The Week 9 branch is `week9-solid-patterns`; merge it into `main` after verifying success, controlled failure, missing-input, and persistence scenarios. 
 
## Application Status 
 
The current integrated application starts with `python run.py --reset-db`. 
The original `lab_agent.py` remains as Week 1 historical material; it is not the 
current main application. The Week 9 Factory and Decorator remain active, 
and Week 10 adds an injected `PlanningPolicy` without changing SQLite schema. 
 
## Week 10 - Testing, TDD and AI-Agent Evaluation 
 
Week 10 adds a separately tested two-hour planning policy, nine automated tests 
across four test scopes, acceptance checks for safe failure, and a four-scenario 
agent-evaluation report. See `docs/testing/README.md`. 
 
Run from the project root: 
 
```powershell 
python -m unittest discover -s tests -v 
python evaluate_agent.py 
python run.py --reset-db 
``` 
 
 ## Week 11 - Integrated AI-Agent Roles and Reflection
Week 11 adds specialized `PlanningAgent` and `ReflectionAgent` roles controlled by `AgentCoordinator` while preserving the tested Week 10 orchestrator, calendar boundary, SQLite persistence and `PlanningPolicy`. Reflection only runs after `Completed`; missing-input and failed requests skip review.

- Python files: `agent/planning_agent.py`, `agent/reflection_agent.py`, `agent/coordinator.py`, `agent/reflection_demo.py`.
- Tests: `tests/test_reflection_agent.py`, `tests/test_agent_coordination.py`.
- Documentation: `docs/agent-integration/README.md`.
- Verification: `python -m unittest discover -s tests -v` (13 passing tests).
- Runtime: `python run.py --reset-db` and `python inspect_database.py`.

## Current Project Status 
 
- Week 1: completed - Git workflow and introductory agent simulator 
- Week 2: completed - requirements engineering and use-case modeling 
- Week 3: completed - structural models and Python domain model 
- Week 4: completed - behavioral models and executable agent workflow 
- Week 5: completed - architectural decomposition and interfaces 
- Week 6: completed - conceptual data model, relational design, normalization and SQLite persistence 
- Week 7: completed - coding standards, code review, branching and traceability 
- Week 8: completed - Scrum sprint planning, Product Backlog, Sprint Board, simulated Daily Scrum, Sprint Review, Retrospective, and XP/TDD overview 
- Week 9: completed - SOLID refactoring, Factory/Adapter/Decorator design patterns, and regression verification 
- Week 10: completed - automated testing, TDD, acceptance checks and agent evaluation 
- Week 11: completed - planning, reflection, coordination, memory evidence and Mermaid documentation